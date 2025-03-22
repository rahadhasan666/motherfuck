from flask import Flask, render_template, request, jsonify
import threading
import asyncio
import attack

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_attack", methods=["POST"])
def start_attack():
    target_url = request.form["url"]
    total_requests = int(request.form["requests"])
    requests_per_second = int(request.form["rps"])

    thread = threading.Thread(target=asyncio.run, args=(attack.start_attack(target_url, requests_per_second, total_requests),))
    thread.start()

    return jsonify({"message": f"🔥 Attack Started on {target_url}!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
