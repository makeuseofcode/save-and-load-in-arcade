import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
blue = arcade.color.BLUE

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.player_x = width // 2

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.player_x, 50, 50, 50, blue )

    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_x += PLAYER_SPEED

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()
