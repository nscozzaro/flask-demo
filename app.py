from flask import Flask, render_template, request, redirect
import requests
import simplejson as json

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/graph', methods=["GET", "POST"])
def graph():
    form_dict = {}
    if request.method == 'POST':
        ticker = request.form['ticker']
        api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json?api_key=bhDkb5WTxo-gXcFN5mgq' % ticker
        response = requests.get(api_url)
        json_response = json.loads(response.content)
        return render_template('graph.html', response=json_response['id'])


if __name__ == '__main__':
  app.run(port=33507)
