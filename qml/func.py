
from core.controller import Controller
controller = Controller()

def koe():
    #from core.controller import Controller

    #controller = Controller()
    controller.projects.current().title = "uusi"
    return controller.projects.current().title

def taas():
    return controller.projects.current().title
