from workspace.demo.page1 import Context, State
from dropbase.database import connect


def delete_order(state: State, context: Context) -> Context:
    try:
        # parse value
        order_id = state.tables.table1.order_id

        # delete in db
        db = connect("demo")
        db.execute(f"DELETE FROM orders where order_id = {order_id};")

        # update user
        context.widgets.widget1.message = "Order has been deleted"
        context.tables.table1.reload = True
    except Exception:
        # handle exception
        context.widgets.widget1.message = "Failed to delete order"
        context.widgets.widget1.message_type = "error"
    return context
