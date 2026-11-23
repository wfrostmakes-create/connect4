from html import escape
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlencode, urlparse
import secrets
import socket
import threading

import winCheck


PORT = 8000
COLUMNS = "ABCDEFG"


class Game:
    def __init__(self):
        self.board = {column: [] for column in COLUMNS}
        self.names = ["Player 1", "Player 2"]
        self.started = False
        self.winner = None
        self.draw = False
        self.current_player = 0
        self.lock = threading.Lock()

    def reset(self):
        self.board = {column: [] for column in COLUMNS}
        self.started = False
        self.winner = None
        self.draw = False
        self.current_player = 0


class GameServer(ThreadingHTTPServer):
    def __init__(self, address, handler):
        super().__init__(address, handler)
        self.game = Game()
        self.token = secrets.token_urlsafe(18)


class GameHandler(BaseHTTPRequestHandler):
    def _authorized(self):
        query = parse_qs(urlparse(self.path).query)
        return secrets.compare_digest(query.get("token", [""])[0], self.server.token)

    def _send_html(self, page, status=200):
        body = page.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _redirect(self):
        location = "/?" + urlencode({"token": self.server.token})
        self.send_response(303)
        self.send_header("Location", location)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        if not self._authorized():
            self._send_html("<h1>Access denied</h1><p>Open the complete link printed by the game host.</p>", 403)
            return

        with self.server.game.lock:
            page = self._render_game()
        self._send_html(page)

    def do_POST(self):
        if not self._authorized():
            self._send_html("<h1>Access denied</h1>", 403)
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._send_html("<h1>Invalid request</h1>", 400)
            return
        if content_length < 0 or content_length > 4096:
            self._send_html("<h1>Invalid request</h1>", 400)
            return

        form = parse_qs(self.rfile.read(content_length).decode("utf-8", errors="replace"))
        action = form.get("action", [""])[0]
        game = self.server.game
        with game.lock:
            if action == "start" and not game.started:
                names = [form.get("player1", [""])[0].strip(),
                         form.get("player2", [""])[0].strip()]
                if all(names):
                    game.names = [name[:40] for name in names]
                    game.started = True
            elif action == "move" and game.started and game.winner is None and not game.draw:
                column = form.get("column", [""])[0]
                if column in COLUMNS and len(game.board[column]) < 7:
                    game.board[column].append("X" if game.current_player == 0 else "O")
                    if winCheck.check_win(game.board):
                        game.winner = game.current_player
                    elif all(len(pieces) == 7 for pieces in game.board.values()):
                        game.draw = True
                    else:
                        game.current_player = 1 - game.current_player
            elif action == "reset":
                game.reset()

        self._redirect()

    def _render_game(self):
        game = self.server.game
        token = escape(self.server.token, quote=True)
        if not game.started:
            return (
                "<!doctype html><html><head><meta name='viewport' content='width=device-width'>"
                "<title>Connect Four</title><style>" + self._styles() + "</style></head><body>"
                "<main><h1>Connect Four</h1><p>Enter both player names to start.</p>"
                f"<form method='post' action='/?token={token}'>"
                "<input type='hidden' name='action' value='start'>"
                "<label>Player 1 <input name='player1' maxlength='40' required></label>"
                "<label>Player 2 <input name='player2' maxlength='40' required></label>"
                "<button type='submit'>Start game</button></form></main></body></html>"
            )

        board_rows = []
        for row in range(6, -1, -1):
            cells = []
            for column in COLUMNS:
                pieces = game.board[column]
                piece = pieces[row] if row < len(pieces) else ""
                cells.append(f"<td class='{piece}'>{piece}</td>")
            board_rows.append("<tr>" + "".join(cells) + "</tr>")
        rows = "".join(board_rows)

        if game.winner is not None:
            status = f"{escape(game.names[game.winner])} wins!"
        elif game.draw:
            status = "It's a draw!"
        else:
            status = f"{escape(game.names[game.current_player])}'s turn"

        controls = ""
        if game.winner is None and not game.draw:
            buttons = "".join(
                f"<button name='column' value='{column}'"
                f"{' disabled' if len(game.board[column]) == 7 else ''}>{column}</button>"
                for column in COLUMNS
            )
            controls = (
                f"<form method='post' action='/?token={token}'>"
                "<input type='hidden' name='action' value='move'>" + buttons + "</form>"
            )

        return (
            "<!doctype html><html><head><meta name='viewport' content='width=device-width'>"
            "<meta http-equiv='refresh' content='5'><title>Connect Four</title>"
            "<style>" + self._styles() + "</style></head><body><main><h1>Connect Four</h1>"
            f"<p class='status'>{status}</p>{controls}<table aria-label='Game board'><tbody>{rows}"
            "</tbody></table><form method='post' action='/?token=" + token + "'>"
            "<input type='hidden' name='action' value='reset'>"
            "<button type='submit'>New game</button></form></main></body></html>"
        )

    @staticmethod
    def _styles():
        return (
            "body{font-family:system-ui,sans-serif;background:#f3f6fb;color:#17233b}"
            "main{max-width:560px;margin:2rem auto;padding:1rem;text-align:center}"
            "form{margin:1rem 0}label{display:block;margin:.7rem}input{padding:.5rem}"
            "button{padding:.6rem 1rem;margin:.2rem;cursor:pointer}button:disabled{opacity:.4}"
            "table{border-collapse:separate;border-spacing:5px;margin:1rem auto;background:#1769aa}"
            "td{width:48px;height:48px;border-radius:50%;background:white;color:transparent}"
            "td.X{background:#e44848}td.O{background:#ffd34e}.status{font-size:1.3rem;font-weight:bold}"
        )

    def log_message(self, format_string, *args):
        print(f"[web] {self.address_string()} - {format_string % args}")


def _lan_ip():
    probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        probe.connect(("192.0.2.1", 80))
        address = probe.getsockname()[0]
        if not address.startswith("127."):
            return address
    except OSError:
        pass
    finally:
        probe.close()
    return "127.0.0.1"


def start_server():
    server = GameServer(("0.0.0.0", PORT), GameHandler)
    local_ip = _lan_ip()
    print("Connect Four web mode is running.")
    print(f"On this computer: http://127.0.0.1:{PORT}/?token={server.token}")
    print(f"On your local network: http://{local_ip}:{PORT}/?token={server.token}")
    print("Share the complete local-network link only with people you trust.")
    print("Press Ctrl+C to stop the server.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping web server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    start_server()
