import avatar
from avatar import Avatar
import core
from creep import Creep


def setup():
        print("Setup START---------")
        core.fps = 150
        core.WINDOW_SIZE = [1920,1080]
        core.memoryCentre=0

        core.memory("a",Avatar())

        core.memory("listcreep", [])
        core.memory("nbrcreep", 100)

        for c in range(0, core.memory("nbrcreep")):
            core.memory("listcreep").append(Creep(1920,1080))

        print("Setup END-----------")


def run():
    core.cleanScreen()
    for c in core.memory("listcreep"):
       c.show(core.screen)

    core.memory("a").deplacement(core.getMouseLeftClick())

    core.memory("a").show(core.screen)
    core.memory("a").bord(core.screen)


    for c in core.memory("listcreep"):
        core.memory("a").eat(c)

    if core.getKeyPressList("q"):
        quit()





core.main(setup, run)
