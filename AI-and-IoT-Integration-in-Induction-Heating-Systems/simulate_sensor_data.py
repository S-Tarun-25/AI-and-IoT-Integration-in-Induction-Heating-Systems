import requests
import random
import time

# Flask server URL
URL = "http://localhost:5000/data"

# Simulate sensor data
while True:
    temperature = random.uniform(20, 100)  # Simulated temperature in °C
    current = random.uniform(10, 50)       # Simulated current in A
    voltage = random.uniform(200, 400)     # Simulated voltage in V

    # Create payload
    payload = {
        "temperature": temperature,
        "current": current,
        "voltage": voltage
    }

    # Send data to Flask server
    try:
        response = requests.post(URL, json=payload)
        print(f"Published: {payload}, Status: {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {e}")

    time.sleep(5)  # Send data every 5 seconds