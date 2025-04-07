import time
import os
from app.database import insert_data, create_table
from dotenv import load_dotenv

load_dotenv()
SIMULATION_MODE = os.getenv("SIMULATION_MODE", "False").lower() == "true"

if SIMULATION_MODE:
    class MockDHT:
        @staticmethod
        def read_retry(sensor, pin):
            import random
            temp = round(20 + (5 * random.random()), 2)
            humid = round(40 + (10 * random.random()), 2)
            return humid, temp


    class MockGPIO:
        BOARD = None
        OUT = IN = HIGH = LOW = None

        def setmode(self, mode): pass

        def setup(self, pin, mode): pass

        def output(self, pin, state): pass

        def cleanup(self): pass


    Adafruit_DHT = MockDHT
    GPIO = MockGPIO()
    DHT_SENSOR = None
else:
    import Adafruit_DHT
    import RPi.GPIO as GPIO

    DHT_SENSOR = Adafruit_DHT.DHT11
    GPIO.setmode(GPIO.BOARD)


def read_temp_and_humid():
    gpio = int(os.getenv("DHT_PIN", 4))
    humid, temp = Adafruit_DHT.read_retry(DHT_SENSOR, gpio)
    print(humid, temp)
    if humid is None or temp is None:
        raise Exception("Failed to read from DHT sensor")
    return {
        "temperature": round(temp, 2),
        "humidity": round(humid, 2)
    }


def loop_reading():
    try:
        while True:
            data = read_temp_and_humid()
            print(f"Temperature: {data['temperature']}°C | Humidity: {data['humidity']}%")
            insert_data(data["temperature"], data["humidity"])
            time.sleep(10)
    except Exception as e:
        GPIO.cleanup()
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    create_table()
    try:
        loop_reading()
    except KeyboardInterrupt:
        print("Stopping the program.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()
        print("GPIO cleanup done.")
