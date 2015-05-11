from flask import Flask, render_template, request, json
from pusher import Pusher

pusher = Pusher(
  app_id=u'119338',
  key=u'fb391863deb66c13d8c4',
  secret=u'c65b995116f79406534e'
)

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
    pusher.trigger(u'test_channel', u'my_event', {u'message': u'hello world'})
    #return abort(500)
    return json.dumps({'status': 'ok'})

if __name__ == "__main__":
    app.run(debug=True)
