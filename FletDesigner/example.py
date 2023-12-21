from Parser.LoadDesignFile import LoadDesignFile
import flet

ldf = LoadDesignFile(jsonfilepath="test.json")

then = None


def change_color(e):
    ldf.junaid.bgcolor = "blue"
    ldf.junaid.update()


ldf.junaid.ink = True
ldf.junaid.on_click = change_color
ldf.run()


# # # import the library
# from fletsb import LoadStoryBoard, StoryBoard
import flet as ft
