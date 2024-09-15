from .state import State
from dropbase.database.connect import connect
import pandas as pd

# functions
def on_click(state: State) -> State:
    state.page.message = "Great!"
    state.page.message_status = "info"
    return state


def get_table_data(state: State) -> State:
    db = connect("demo")
    table_data = db.query("SELECT * FROM orders")
    table_df = pd.DataFrame(table_data)
    state.table1.data = table_df.to_dict(orient="records")
    return state
