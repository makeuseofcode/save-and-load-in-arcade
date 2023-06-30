import arcade
import json

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
blue = arcade.color.BLUE

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.player_x = width // 2
        self.high_score = 0
        self.load_game()

    def load_game(self):
        try:
            with open('save.json', 'r') as file:
                data = json.load(file)
                print(data)
                self.player_x = data.get('player_x', self.player_x)
                self.high_score = data.get('high_score', self.high_score)
        except FileNotFoundError:
            pass

    def save_game(self):
        data = {
            'player_x': self.player_x,
            'high_score': self.high_score
        }
        with open('save.json', 'w') as file:
            json.dump(data, file)
            print(data)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.player_x, 50, 50, 50, blue)

    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_x += PLAYER_SPEED
            self.high_score += 1
        elif key == arcade.key.S:
            self.save_game()
        elif key == arcade.key.L:
            self.load_game()

# Usage example
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
