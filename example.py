from Parser.LoadDesignfile import LoadDesignFile
import flet


ldf = LoadDesignFile(jsonfilepath="request.json")


def update1(e):
    ldf.b1.text = "update"       
    ldf.b1.update()


ldf.b1.on_click = update1


def update12(e):
    ldf.b12.text = "update"
    ldf.b12.update()


ldf.b12.on_click = update12
ldf.run()
