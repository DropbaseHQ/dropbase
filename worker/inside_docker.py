import redis
from dotenv import load_dotenv

from dropbase.worker.run_python import run

load_dotenv()


if __name__ == "__main__":
    # NOTE: we need to use host.docker.internal to connect to the host machine's redis. tested on mac
    r = redis.Redis(host="host.docker.internal", port=6379, db=0)
    run(r)
