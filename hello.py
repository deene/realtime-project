from flask import Flask, render_template, request, json

app = Flask(__name__)

app.config.update(
    DEBUG=True
)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
