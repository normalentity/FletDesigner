from Parser.LoadDesignfile import LoadDesignFile
import flet

ldf = LoadDesignFile(jsonfilepath="request.json")


def update1(e):
    print("kaboom")
    ldf.b1.text = "update"
    ldf.b1.update()


# print(ldf.b1)
ldf.b1.on_click = update1


def update12(e):
    print("kaboom")
    ldf.b12.text = "update"
    ldf.b12.update()


# print(ldf.b1)
ldf.b12.on_click = update12
ldf.run()
