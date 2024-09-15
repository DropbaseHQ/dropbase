from typing import Optional

from pydantic import BaseModel


class Store(BaseModel):
    """
    Please make sure to either user Optional or provide default values
    For example:
    ```
    name: str = "" # default value for name is an empty string
    # or
    name: Optional[str] # name is optional
    ```
    If no default value is provided and the field is not Optional,
    the system will assume the default value based on type.
    For example: int -> 0, str -> "", bool -> True
    """

    pass
