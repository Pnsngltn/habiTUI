from textual.app import App
from textual.widgets import Static


class HabitTracker(App):
    def compose(self):
        yield Static("Hello, World!")


if __name__ == "__main__":
    app = HabitTracker()
    app.run()
