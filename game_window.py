import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class App:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("bowling_display.glade")

        self.main_window = builder.get_object("main_window")

    def run(self):
        self.main_window.connect("destroy", Gtk.main_quit)
        self.main_window.show_all()

        Gtk.main()


app = App()
app.run()
