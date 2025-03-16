from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static, Placeholder
from textual.containers import Vertical
from rich.panel import Panel
from rich.text import Text
import random

SHEEP_QUOTES = [
    "Baa~ Don't use 'password' as your password!",
    "Your security should be as fluffy as me, but stronger!",
    "Did you know? Reusing passwords is like walking into a wolf’s den.",
    "Encrypt your secrets like I hide in my wool!",
    "Baa careful! Hackers are always lurking!"
]

class VaultSheepApp(App):
    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        yield MainMenuScreen()

class MainMenuScreen(Static):
    def compose(self) -> ComposeResult:
        yield Static(self.get_sheep_art(), classes="sheep-art")
        yield Static("[bold cyan]Welcome to VaultSheep![/bold cyan]\n", classes="title")
        yield Static(f"[italic green]{random.choice(SHEEP_QUOTES)}[/italic green]", classes="sheep-quote")
        yield Vertical(
            Button("🔑 Password Manager", id="passwords"),
            Button("📖 Diary", id="diary"),
            Button("⚙️ Settings", id="settings"),
            Button("❌ Exit", id="exit"),
            classes="menu-buttons"
        )

    def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "exit":
            self.app.exit()
        elif button_id == "passwords":
            self.app.push_screen(Placeholder("Password Manager Coming Soon!"))
        elif button_id == "diary":
            self.app.push_screen(Placeholder("Diary Feature Coming Soon!"))
        elif button_id == "settings":
            self.app.push_screen(Placeholder("Settings Feature Coming Soon!"))

    def get_sheep_art(self) -> str:
        return Panel(
            Text(
                r"""
     ____________________________
    < Baa! Secure your passwords! >
     ----------------------------
            \   ,__,  
             \ (o.o)     
              (")(")      
                """,
                style="bold magenta"
            ),
            title="Sheepy the Security Sheep",
            border_style="bright_yellow"
        )

if __name__ == "__main__":
    app = VaultSheepApp()
    app.run()
