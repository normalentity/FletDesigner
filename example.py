from Parser.LoadDesignfile import LoadDesignFile
import flet

ldf = LoadDesignFile(jsonfilepath="request.json")


def update1(e):
    print("kaboom")
    ldf.b1.text = "update"
    ldf.b1.update()


# print(ldf.b1)
ldf.b1.on_click = update1
ldf.run()
