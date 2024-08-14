from dropbase.classes.scriptABC import ScriptABC
from workspace.demo.page1.main import *  # noqa, here we're importing all user defined classes


class Script(ScriptABC):
    def __init__(self, app_name, page_name):
        super().__init__(app_name, page_name)
        for key, value in self.properties.blocks:
            if value.type == 'text':
                continue
            class_ = globals()[key.capitalize()]
            self.__dict__[key] = class_()
        # add page to script
        key = "page"
        class_ = globals()[key.capitalize()]
        self.__dict__[key] = class_()
