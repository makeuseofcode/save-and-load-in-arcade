import arcade
import json

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
blue = arcade.color.BLUE

class GameState:
    def __init__(self):
        self.player_x = 0

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.game_state = GameState()
        self.load_game()

    def load_game(self):
        try:
            with open('save.json', 'r') as file:
                data = json.load(file)
                self.game_state.player_x = data['player_x']
        except FileNotFoundError:
            pass

    def save_game(self):
        data = {
            'player_x': self.game_state.player_x
        }
        with open('save.json', 'w') as file:
            json.dump(data, file)
            print(data)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.game_state.player_x, 50, 50, 50, blue)

    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.game_state.player_x -= PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.game_state.player_x += PLAYER_SPEED
        elif key == arcade.key.S:
            self.save_game()
        elif key == arcade.key.L:
            self.load_game()
            
def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()
