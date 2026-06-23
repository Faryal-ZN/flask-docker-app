<<<<<<< HEAD
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
=======
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker Flask App!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> d3596afba739d03af46a1c3546dae91d6c5976cf
