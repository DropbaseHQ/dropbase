import os

import pandas as pd
import redis
from dotenv import load_dotenv

from dropbase.helpers.dataframe import to_dtable

load_dotenv()


pd.DataFrame.to_dtable = to_dtable


if __name__ == "__main__":
    r = redis.Redis(host="redis", port=6379, db=0)
    if os.getenv("type") == "string":
        from dropbase.worker.run_python_string import run
    else:
        from dropbase.worker.run_python_class import run
    run(r)
