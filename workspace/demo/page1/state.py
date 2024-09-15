from dropbase.models.state import *
from pydantic import BaseModel
from .store import Store
class State(BaseModel):
    page: PageState
    store: Store
    table1: TableState
    button1: ButtonState
