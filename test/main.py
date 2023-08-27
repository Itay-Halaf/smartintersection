import asyncio
import threading

from Subscriber import run_subscriber
from fastapi_app import app

def start_subscriber():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_subscriber())

if __name__ == "__main__":
    subscriber_thread = threading.Thread(target=start_subscriber)
    subscriber_thread.start()

    uvicorn_thread = threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 8000})
    uvicorn_thread.start()

    subscriber_thread.join()
    uvicorn_thread.join()
