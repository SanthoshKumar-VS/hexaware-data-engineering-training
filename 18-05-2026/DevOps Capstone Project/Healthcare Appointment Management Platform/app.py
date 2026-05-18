from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return render_template("health.html")

@app.route("/appointment-status")
def appointment_status():
    return render_template("appointment.html")

@app.route("/doctor-availability")
def doctor_availability():
    return render_template("doctor.html")

if __name__ == "__main__":
    app.run(debug=True)