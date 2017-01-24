from flask import Flask, render_template, request, redirect
import requests

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
        data = request.form['ticker']
        api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json?api_key=gVz7XbzeecyxHdkCn8yB' % 'ticker'
        response = requests.get(api_url)
        return render_template('graph.html', data = data, response=response.content)


if __name__ == '__main__':
  app.run(port=33507)
