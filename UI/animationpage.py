from flet import Container, ElevatedButton, Page, Stack, colors, View, padding, colors
import flet
import random
from math import pi
import time


class __view__:
    # page.horizontal_alignment = "center"
    # page.vertical_alignment = "center"
    # page.spacing = 30

    # page = View(route="/welcome", controls=[])
    # page.bgcolor = colors.BLACK
    def __init__(self):
        self.size = 40
        self.gap = 2
        self.duration = 2000
        c1 = colors.PINK_500
        c2 = colors.AMBER_500
        c3 = colors.LIGHT_GREEN_500
        c4 = colors.DEEP_PURPLE_500

        self.all_colors = [
            colors.AMBER_400,
            colors.AMBER_ACCENT_400,
            colors.BLUE_400,
            colors.BROWN_400,
            colors.CYAN_700,
            colors.DEEP_ORANGE_500,
            colors.CYAN_500,
            colors.INDIGO_600,
            colors.ORANGE_ACCENT_100,
            colors.PINK,
            colors.RED_600,
            colors.GREEN_400,
            colors.GREEN_ACCENT_200,
            colors.TEAL_ACCENT_200,
            colors.LIGHT_BLUE_500,
        ]

        designer_top = 8
        designer_size = 17
        designer_gap = 3
        designer_leftmargin = 0
        self.parts = [
            # F
            [
                {"left": 0, "top": 0, "size": 20, "gap": 5},
                (0, 0, c1),
                (0, 1, c1),
                (0, 2, c1),
                (0, 3, c1),
                (0, 4, c1),
                (1, 0, c1),
                (1, 2, c1),
                (2, 0, c1),
            ],
            # L
            [
                {"left": 9.25, "top": 0, "size": 20, "gap": 5},
                (0, 0, c2),
                (0, 1, c2),
                (0, 2, c2),
                (0, 3, c2),
                (0, 4, c2),
                (1, 4, c2),
                (2, 4, c2),
            ],
            # E
            [
                {"left": 17.25, "top": 0, "size": 20, "gap": 5},
                (0, 0, c3),
                (1, 0, c3),
                (2, 0, c3),
                (0, 1, c3),
                (0, 2, c3),
                (1, 2, c3),
                (2, 2, c3),
                (0, 3, c3),
                (0, 4, c3),
                (1, 4, c3),
                (2, 4, c3),
            ],
            # T
            [
                {"left": 25.5, "top": 0, "size": 20, "gap": 5},
                (0, 0, c4),
                (1, 0, c4),
                (2, 0, c4),
                (1, 1, c4),
                (1, 2, c4),
                (1, 3, c4),
                (1, 4, c4),
            ],
            # D
            [
                {
                    "left": 0,
                    "top": designer_top,
                    "size": designer_size,
                    "gap": designer_gap,
                },
                (0, 0, c4),
                (0, 1, c4),
                (0, 2, c4),
                (0, 3, c4),
                (0, 4, c4),
                (1, 0, c4),
                (1, 4, c4),
                (2, 0, c4),
                (2, 4, c4),
                (3, 2, c4),
                (3, 1, c4),
                (3, 3, c4),
            ],
            # E
            [
                {
                    "left": 5 + designer_leftmargin,
                    "top": designer_top,
                    "size": designer_size,
                    "gap": designer_gap,
                },
                (0, 0, c3),
                (1, 0, c3),
                (2, 0, c3),
                (0, 1, c3),
                (0, 2, c3),
                (1, 2, c3),
                (2, 2, c3),
                (0, 3, c3),
                (0, 4, c3),
                (1, 4, c3),
                (2, 4, c3),
            ],
            # S
            [
                {
                    "left": 9 + designer_leftmargin,
                    "top": designer_top,
                    "size": designer_size,
                    "gap": designer_gap,
                },
                (0, 0, c3),
                (0, 1, c3),
                (0, 2, c3),
                (0, 4, c3),
                (1, 0, c3),
                (1, 2, c3),
                (1, 4, c3),
                (2, 0, c3),
                (2, 2, c3),
                (2, 3, c3),
                (2, 4, c3),
            ],
            # I
            [
                {
                    "left": 13 + designer_leftmargin,
                    "top": designer_top,
                    "size": designer_size,
                    "gap": designer_gap,
                },
                (0, 0, c3),
                (1, 0, c3),
                (2, 0, c3),
                (1, 1, c3),
                (1, 2, c3),
                (1, 3, c3),
                (0, 4, c3),
                (1, 4, c3),
                (2, 4, c3),
            ],
            # G
            [
                {
                    "left": 17 + designer_leftmargin,
                    "top": designer_top,
                    "size": designer_size,
                    "gap": designer_gap,
                },
                (0, 0, c3),
                (0, 1, c3),
                (0, 2, c3),
                (0, 3, c3),
                (0, 4, c3),
                (1, 0, c3),
                (1, 4, c3),
                (2, 0, c3),
                (2, 2, c3),
                (2, 4, c3),
                (3, 0, c3),
                (3, 2, c3),
                (3, 3, c3),
                (3, 4, c3),
            ],
            # N
            [
                {
                    "left": 22 + designer_leftmargin,
                    "top": designer_top,
                    "size": designer_size,
                    "gap": designer_gap,
                },
                (0, 0, c3),
                (0, 1, c3),
                (0, 2, c3),
                (0, 3, c3),
                (0, 4, c3),
                (1, 1, c3),
                (2, 2, c3),
                (3, 3, c3),
                (4, 4, c3),
                (4, 4, c3),
                (4, 0, c3),
                (4, 1, c3),
                (4, 2, c3),
                (4, 3, c3),
                (4, 4, c3),
            ],
            # E
            [
                {
                    "left": 28 + designer_leftmargin,
                    "top": designer_top,
                    "size": designer_size,
                    "gap": designer_gap,
                },
                (0, 0, c3),
                (1, 0, c3),
                (2, 0, c3),
                (0, 1, c3),
                (0, 2, c3),
                (1, 2, c3),
                (2, 2, c3),
                (0, 3, c3),
                (0, 4, c3),
                (1, 4, c3),
                (2, 4, c3),
            ],
            # R
            [
                {
                    "left": 32 + designer_leftmargin,
                    "top": designer_top,
                    "size": designer_size,
                    "gap": designer_gap,
                },
                (0, 0, c3),
                (1, 0, c3),
                (2, 0, c3),
                (0, 1, c3),
                (0, 2, c3),
                (0, 3, c3),
                (0, 4, c3),
                (0, 4, c3),
                (1, 2, c3),
                (1, 3, c3),
                (2, 1, c3),
                (2, 2, c3),
                (2, 4, c3),
            ],
        ]

    def recursive_len(self, item):
        if type(item) == list:
            return sum(self.recursive_len(subitem) for subitem in item)
        else:
            return 1

    def get_width(self):
        width = 0
        lastpart = self.parts[-1]
        left = lastpart[0]["left"]
        size = lastpart[0]["size"]
        gap = lastpart[0]["gap"]
        for square in lastpart[1::]:
            width += square[0] * (size + gap)
        return width

    def get_height(self):
        height = 0
        lastpart = self.parts[-1]
        top = lastpart[0]["top"]
        size = lastpart[0]["size"]
        gap = lastpart[0]["gap"]
        for square in lastpart[1::]:
            height += square[1] * (size + gap)
        return height

    def randomize(self, e):
        random.seed()
        for i in range(self.recursive_len(self.parts) - len(self.parts)):
            c = self.canvas.controls[i]
            part_size = random.randrange(int(self.size / 2), int(self.size * 3))
            c.left = random.randrange(0, self.width)
            c.top = random.randrange(0, self.height)
            c.bgcolor = self.all_colors[random.randrange(0, len(self.all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(self.size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        self.canvas.scale = 5
        self.canvas.opacity = 0.3
        self.view.update()

    def assemble(self, e):
        i = 0
        for container in self.parts:
            data = container[0]
            main_left = data["left"]
            main_top = data["top"]
            main_size = data["size"]
            main_gap = data["gap"]
            for partnum, (left, top, bgcolor) in enumerate(container[1::]):
                c = self.canvas.controls[i]
                c.left = (left + main_left) * (main_size + main_gap)
                c.top = (main_top + top) * (main_size + main_gap)
                c.bgcolor = bgcolor
                c.width = main_size
                c.height = main_size
                c.border_radius = 5
                c.rotate = 0
                i += 1
                self.canvas.scale = 1
                self.canvas.opacity = 1
                self.view.update()

    def build(self):
        self.width = 16 * (self.size + self.gap) + self.get_width()
        self.height = -3 * (self.size + self.gap) + self.get_height()

        self.view = View(route="/welcome")

        self.view.horizontal_alignment = "center"
        self.view.vertical_alignment = "center"
        # page.spacing = 30
        self.view.bgcolor = colors.BLACK

        self.canvas = Stack(
            width=self.width,
            height=self.height,
            animate_scale=self.duration,
            animate_opacity=self.duration,
        )

        # self.button=
        # self.view.padding = padding.only(left=200, right=200)

        for i in range(self.recursive_len(self.parts) - len(self.parts)):
            self.canvas.controls.append(
                Container(
                    animate=self.duration,
                    animate_position=self.duration,
                    animate_rotation=self.duration,
                )
            )
        self.view.padding = padding.only(left=50)
        self.view.controls.append(self.canvas)
        self.view.spacing = 30
        return self.view
