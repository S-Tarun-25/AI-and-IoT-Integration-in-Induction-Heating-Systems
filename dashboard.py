from flask import Flask, request, render_template
import csv
import time

app = Flask(__name__)

# Endpoint to receive sensor data
@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json  # Get JSON data from the request
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Add a timestamp

    # Debug: Print received data
    print(f"Received data: {data}")

    # Save data to CSV file
    with open("sensor_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, data["temperature"], data["current"], data["voltage"]])

    # Debug: Print confirmation
    print("Data saved to CSV file.")
    return "Data received", 200  # Return a success response

# Endpoint to display the dashboard
@app.route("/")
def dashboard():
    try:
        # Read data from CSV file
        with open("sensor_data.csv", mode="r") as file:
            reader = csv.DictReader(file, fieldnames=["timestamp", "temperature", "current", "voltage"])
            data = list(reader)  # Convert CSV data to a list of dictionaries

        # Debug: Print keys of the first row
        if data:
            print(f"Keys in data: {data[0].keys()}")

        # Render the dashboard template with the data
        return render_template("dashboard.html", data=data)
    except Exception as e:
        # Debug: Print any errors
        print(f"Error reading CSV file: {e}")
        return "Error reading data", 500

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask server