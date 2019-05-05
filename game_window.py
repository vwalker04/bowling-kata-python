import gi

from game_scoring import Game

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class App:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("bowling_display.glade")

        self.game = Game()
        self.main_window = self.builder.get_object("main_window")
        self.score_display = self.builder.get_object("scr_display")

        self.score_button = self.builder.get_object("scr_button")
        self.score_button.connect("clicked", self.update_score)

        self.reset_button = self.builder.get_object("reset_button")
        self.reset_button.connect("clicked", self.reset_game)

        self.rolls_from_builder = self.__build_roll_objects()

    def run(self):
        self.main_window.connect("destroy", Gtk.main_quit)
        self.main_window.show_all()

        Gtk.main()

    def update_score(self, score_button):
        self.roll()
        self.score_display.set_text(str(self.game.score()))

    def roll(self):
        rolls_input = self.__get_roll_input()

        for pins_knocked_down in rolls_input:
            if pins_knocked_down == "":
                pins_knocked_down = 0
            self.game.roll(int(pins_knocked_down))

    def reset_game(self, reset_button):
        ''' Reset should clear out current inputs
            Reset should also zero out the current score
            on both the display and in bowling logic '''
        self.game.reset_game()

    def __build_roll_objects(self):
        rolls = []
        incremented_rolls = ["roll_%s" % roll for roll in range(0, 21)]
        for roll in incremented_rolls:
            rolls.append(self.builder.get_object(roll))
        return rolls

    def __get_roll_input(self):
        rolls = []
        for roll in self.rolls_from_builder:
            rolls.append(roll.get_text())
        return rolls


app = App()
app.run()
