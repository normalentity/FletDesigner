from .Parser.LoadDesignFile import LoadDesignFile
import flet

ldf = LoadDesignFile(jsonfilepath="test.json")

then = None


def change_color(e):
    ldf.container1.bgcolor = "blue"
    ldf.container1.update()


ldf.container1.ink = True
ldf.container1.on_click = change_color
ldf.run()


# # # import the library
# from fletsb import LoadStoryBoard, StoryBoard
import flet as ft
