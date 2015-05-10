from flask import Flask, render_template, request, json

app = Flask(__name__)

app.config.update(
    DEBUG=True
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/takeCode')
def takeCode():
    takeCode_request = {}
    takeCode_request['code'] = request.args.get('code','')
    #return abort(500)
    return json.dumps({'status': 'ok'})

if __name__ == "__main__":
    app.run(debug=True)
