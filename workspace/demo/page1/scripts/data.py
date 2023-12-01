from workspace.demo.page1 import State
import pandas as pd


def data(state: State) -> pd.DataFrame:
    data = {
        'CustomerID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 28, 35, 22],
        'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'david@email.com', 'eva@email.com'],
        'City': ['San Francisco', 'New York', 'Los Angeles', 'Toronto', 'Montreal']
    }
    df = pd.DataFrame(data)
    return df
