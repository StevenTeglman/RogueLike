import tcod
from tcod.tileset import CHARMAP_TCOD


def main():
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "tilemap.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=1, y=1, string="@")

            context.present(root_console)

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()
