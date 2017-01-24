from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components


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
        # Extract form info
        ticker = request.form['ticker']
        features = request.form.getlist('features')

        # Call the Quandl API
        api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json?api_key=bhDkb5WTxo-gXcFN5mgq' % ticker
        response = requests.get(api_url)
        json_response = json.loads(response.content)

        # Put the data in a Pandas dataframe
        data = pd.DataFrame(json_response['data'], columns=json_response['column_names'])
        data['Date'] = pd.to_datetime(data['Date'])

        # Send the data to the Bokeh plot
        p = figure(x_axis_type="datetime", width=800, height=600)
        line_color=['red', 'green', 'blue', 'brown']
        for index, feature in enumerate(features):
            p.line(data['Date'], data[feature], legend=feature, line_color = line_color[index])
        script, div = components(p)
        return render_template('graph.html', script=script, div=div, company = ticker.upper())


if __name__ == '__main__':
    app.run(port=5000)
