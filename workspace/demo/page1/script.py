from dropbase.classes.scriptABC import ScriptABC
from workspace.demo.page1.main import *  # noqa, here we're importing all user defined classes


class Script(ScriptABC):
    def __init__(self, app_name, page_name):
        super().__init__(app_name, page_name)
        for key, _ in self.properties:
            class_name = key.capitalize()
            class_ = globals()[class_name]  # Get the actual class name from globals
            self.__dict__[key] = class_()
