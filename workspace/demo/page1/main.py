import pandas as pd
from typing import List
from dropbase.classes.tableABC import TableABC
from dropbase.classes.widgetABC import WidgetABC
from workspace.demo.page1.context import *
from workspace.demo.page1.state import *
from dropbase.database.connect import connect


class Table1(TableABC):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, state: State, context: Context):
        db = connect("demo")
        table_data = db.query("SELECT * FROM orders")
        table_df = pd.DataFrame(table_data)
        context.table1.data = table_df.to_dtable()
        return context

    def add(self, state: State, context: Context, row: Table1ColumnsState) -> Context:
        db = connect("demo")
        row_data = {
            "order_id": row.order_id,
            "user_id": row.user_id,
            "product_name": row.product_name,
            "quantity": row.quantity,
            "total_price": row.total_price,
            "order_date": row.order_date,
        }
        insert_query = """
            INSERT INTO orders (order_id, user_id, product_name, quantity, total_price, order_date)
            VALUES (:order_id, :user_id, :product_name, :quantity, :total_price, :order_date)
            ON CONFLICT(order_id) DO NOTHING
        """
        db.execute(insert_query, row_data)
        table_data = db.query("SELECT * FROM orders")
        table_df = pd.DataFrame(table_data)
        context.table1.data = table_df.to_dtable()
        context.page.message = "Row added successfully"
        context.page.message_type = "success"
        return context

    def update(
        self, state: State, context: Context, updates: List[Table1ColumnUpdate]
    ) -> Context:
        db = connect("demo")
        for update in updates:
            row_data = update.new.dict()
            if "order_id" in row_data:
                update_query = """
                    UPDATE orders
                    SET {}
                    WHERE order_id = :order_id
                """.format(
                    ", ".join(
                        [f"{k} = :{k}" for k in row_data.keys() if k != "order_id"]
                    )
                )
                db.execute(update_query, row_data)
            else:
                context.page.message = "Order ID is required for update"
                context.page.message_type = "error"
                continue
        table_data = db.query("SELECT * FROM orders")
        table_df = pd.DataFrame(table_data)
        context.table1.data = table_df.to_dtable()
        context.page.message = "Rows updated successfully"
        context.page.message_type = "success"
        return context

    def delete(self, state: State, context: Context) -> Context:
        if state.table1.columns.order_id is not None:
            db = connect("demo")
            delete_query = "DELETE FROM orders WHERE order_id = :order_id"
            db.execute(delete_query, {"order_id": state.table1.columns.order_id})
            table_data = db.query("SELECT * FROM orders")
            table_df = pd.DataFrame(table_data)
            context.table1.data = table_df.to_dtable()
            context.page.message = "Row deleted successfully"
            context.page.message_type = "success"
        else:
            context.page.message = "Order ID is required for delete"
            context.page.message_type = "error"
        return context

    def on_row_change(self, state: State, context: Context) -> Context:
        return context


class Widget1(WidgetABC):

    def components_button1_on_click(self, state: State, context: Context) -> Context:
        context.page.message = "Great!"
        context.page.message_type = "info"
        return context
