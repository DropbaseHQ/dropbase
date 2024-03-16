from workspace.demo.page1 import Context, State
from dropbase.database import connect


def create_order(state: State, context: Context) -> Context:
    try:
        # parse values
        values = {
            "user_id": state.widgets.widget1.input1,
            "product_name": state.widgets.widget1.input2,
            "quantity": state.widgets.widget1.input3,
            "total_price": state.widgets.widget1.input4,
            "order_date": state.widgets.widget1.input5,
        }

        # update db
        db = connect("demo")
        keys = list(values.keys())
        sql = f"""INSERT INTO orders ({', '.join(keys)})
        VALUES (:{', :'.join(keys)});"""
        db.execute(sql, values)

        # update user
        context.widgets.widget1.message = "good"
        context.tables.table1.reload = True
    except Exception:
        # handle exception
        context.widgets.widget1.message = "Failed to create an order"
        context.widgets.widget1.message_type = "error"
    return context
