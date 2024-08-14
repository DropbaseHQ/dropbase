import pandas as pd
import plotly.express as px
from typing import List
from dropbase.classes import *
from workspace.demo.page1 import Context, State, Store
from dropbase.helpers.decorators import clear_store_add, clear_store_update
from dropbase.database.connect import connect


class Page(PageABC):
    def load(
        self, state: State, context: Context, store: Store) -> tuple[Context, Store]:
        return context, store


class Table1(TableABC):

    def get(self, state: State, context: Context, store: Store) -> tuple[Context, Store]:
        db = connect("demo")
        table_data = db.query("SELECT * FROM orders")
        table_df = pd.DataFrame(table_data)
        context.table1.data = table_df.to_dtable()
        return context, store

    @clear_store_add
    def add(self, state: State, context: Context, store: Store) -> tuple[Context, Store]:
        return context, store

    @clear_store_update
    def update(self, state: State, context: Context, store: Store) -> tuple[Context, Store]:
        return context, store

    def delete(self, state: State, context: Context, store: Store) -> tuple[Context, Store]:
        return context, store

    def row_change(self, state: State, context: Context, store: Store) -> tuple[Context, Store]:
        return context, store
class Button1(ButtonABC):

    def click(self, state: State, context: Context, store: Store) -> tuple[Context, Store]:
        context.page.message = "Great!"
        context.page.message_type = "info"
        return context, store
