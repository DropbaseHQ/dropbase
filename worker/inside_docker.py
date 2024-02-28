import os

import redis
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    r = redis.Redis(host="host.docker.internal", port=6379, db=0)
    response = {"stdout": "", "traceback": "", "message": "", "type": "", "status_code": 202}

    if os.getenv("type") == "string":
        from dropbase.worker.run_python_string import run
    else:
        from dropbase.worker.run_python_file import run

    run(r, response)
