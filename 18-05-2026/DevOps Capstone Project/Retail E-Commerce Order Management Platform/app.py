from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return render_template("health.html")

@app.route("/order-status")
def order_status():
    return render_template("order.html")

@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

if __name__ == "__main__":
    app.run(debug=True)