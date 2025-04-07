import threading
import os
from app import api
from app import sensor_reader
from dotenv import load_dotenv
from app.database import create_table

load_dotenv()


def run_api():
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    api.app.run(host="0.0.0.0", port=port, debug=debug)


def run_sensor():
    sensor_reader.loop_reading()


if __name__ == "__main__":
    try:
        create_table()
        print("Initializing the Climate Station...")
        sensor_thread = threading.Thread(target=run_sensor)
        sensor_thread.start()
        run_api()
        sensor_thread.join()
    except KeyboardInterrupt:
        print("Stopping the Climate Station.")
