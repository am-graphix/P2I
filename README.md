# P2I
P2ǐ (Press To Identify) is a fingerprint-based attendance system I’m building for my school’s Robotics Club to mark attendance. Instead of passing papers around, members scan their fingerprints, then every detail is saved. It uses an optical fingerprint sensor connected to a PC via USB-to-TTL, with a website for interacting with it..

---

## 🧠 How it works (in plain terms)

The fingerprint sensor is connected to a computer through a TTL-to-USB converter. A Python backend communicates with the sensor using the PyFingerprint library.

When a fingerprint is scanned, the sensor returns an ID. The backend then checks a SQLite database to see who that ID belongs to. If a match is found, the system displays the user’s details and records their attendance with the current date and time.

Everything is controlled through a web interface built with Flask, HTML, CSS, and JavaScript.

---

## Admin side

The admin has access to a dashboard where they can:

* Enroll new students
* Enter student details (name, class, house)
* Capture and store fingerprints
* View registered users
* Check attendance records

During enrollment, the fingerprint is saved inside the sensor, and the returned ID is linked to the student’s details in the database.

---

## Student side

For attendance, the process is simple:

1. Open the website
2. Place a finger on the scanner
3. Click the **Scan** button

If the fingerprint matches a stored record:

* The student’s details are displayed
* Attendance is marked automatically

---

## Tech Stack

**Backend**

* Python
* Flask
* PyFingerprint
* SQLite3

**Frontend**

* HTML
* CSS
* JavaScript

**Hardware**

* ZA620 M5 Fingerprint Sensor
* TTL-to-USB Converter

---

## 🔌 Hardware setup

The wiring is pretty standard:

* VCC → 5V
* GND → GND
* TX → RX
* RX → TX

After connecting, plug the converter into your PC and note the serial port (e.g., `COM3` or `/dev/ttyUSB0`).

---

## Running the project

Clone the repo and install dependencies:

git clone https://github.com/am-graphix/P2I.git
cd fingerprint
pip install -r requirements.txt
```

Start the Flask app:

python app.py
```

Then open your browser and go to:
http://localhost:5000

---

## Data handling

* Fingerprints themselves are stored in the sensor
* The database only stores:

  * User details
  * Fingerprint ID (returned by the sensor)
  * Attendance timestamps

---

## Note

Since the system relies on the sensor’s internal storage for fingerprint IDs, clearing the sensor memory will break the mapping with the database. A future improvement would be adding a backup or sync mechanism.

---

## Project structure (simplified)

app.py              # Flask app
fingerprint.py      # Fingerprint logic
templates/          # HTML
static/             # CSS, Images & JS
database.db         # SQLite database


## Deployment

The web interface for this project is hosted on Vercel, making it accessible from a browser.

However, the fingerprint sensor requires direct hardware access, so the backend (Flask + PyFingerprint) must still run on a local machine connected to the sensor.

In short:

* **Frontend (UI)** → hosted on Vercel
* **Backend + Sensor Communication** → runs locally

This setup allows the system to have a clean, accessible interface while still interacting with physical hardware.

---

## How everything connects

* The user interacts with the website (hosted online)
* Actions like "Scan" are sent to the local backend
* The backend communicates with the fingerprint sensor via serial
* Results are returned and displayed on the web interface

---

## Note on Deployment

Because this project depends on physical hardware, it cannot be fully deployed as a cloud-only application. Any system using it must have:

* The fingerprint sensor connected
* The backend running on that machine

---

## Future ideas

Some things that could make this better:

* Add login/authentication for the admin
* Export attendance to CSV or Excel
* Improve the UI
* Add real-time feedback when scanning
* Deploy it online

## Quick  And Important Note
THis project is still under development.. An initial version was made and tested during club meeting... This is an improvised version, with more focus on a beffiting UI for a Robotics Club... So backend is not fully linked with frontend... And most of the data displayed are dummy values

## Author

Ayisi Michael Kwabena
