from screeninfo import get_monitors


def get_screen_dimensions():
    for m in get_monitors():
        m.width
        m.height


get_screen_dimensions()
