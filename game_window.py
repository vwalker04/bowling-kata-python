import gi

from game_scoring import Game

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class App:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("bowling_display.glade")

        self.game = Game()
        self.main_window = builder.get_object("main_window")
        self.score_display = builder.get_object("scr_display")

        self.score_button = builder.get_object("scr_button")
        self.score_button.connect("clicked", self.update_score)

    def run(self):
        self.main_window.connect("destroy", Gtk.main_quit)
        self.main_window.show_all()

        Gtk.main()

    def update_score(self, object):
        self.score_display.set_text(self.game.score())


app = App()
app.run()
