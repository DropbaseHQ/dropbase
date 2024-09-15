from dropbase.models.models import *
from .functions import *


page = Page(
    id="page1",
    name="Page 1",
    on_load=get_table_data,
    blocks=(
        Table(id="table1", label="Table1", w=10, h=4, x=0, y=0, visible=True, on_row_change=None, columns=[]),
        Button(id="button1", label="Button1", w=2, h=1, x=10, y=0, visible=True, on_click=on_click),
    ),
)
