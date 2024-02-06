
# Airline Reservation System

## Overview
This is a simple Airline Reservation System implemented in Python using MySQL as the database. The system provides functionalities such as searching for flight details, ticket reservation, cancellation, and checking PNR status. It also includes a feature to display all flight details and a popularity graph based on destination preferences.

## Requirements
- Python 3.x
- MySQL database
- Required Python packages: `mysql-connector`, `tabulate`, `matplotlib`

## Setup
1. **Install Python:** [Download Python](https://www.python.org/downloads/)
2. **Install MySQL:** [Download MySQL](https://dev.mysql.com/downloads/)
3. **Install required Python packages:**
   ```bash
   pip install mysql-connector tabulate matplotlib
   ```
4. **Set up MySQL database:**
   - Create a database named `myairport`.
   - Execute the SQL script provided in the repository (`database_setup.sql`) to create the necessary tables.

## Usage
1. **Run the main program:**
   ```bash
   python airline_reservation_system.py
   ```
2. **Follow the on-screen instructions to navigate through the Airline Reservation System.**

## Features
- **Search Flight Details:** Enter source and destination cities to view available flight details.
- **Reservation of Ticket:** Reserve a ticket by providing passenger details and selecting the class.
- **Cancellation of Ticket:** Cancel a ticket by entering the PNR number.
- **Display PNR Status:** Check the status of a reservation using the PNR number.
- **Display All Flight Details:** View details of all available flights.
- **Show Popularity Graph:** Display a bar graph showing the popularity of destinations.

## Note
- Make sure to update the database connection details in the program (`mydb=mysql.connector.connect(...)`) with your MySQL server information.

Feel free to explore, modify, and enhance the Airline Reservation System according to your needs!
