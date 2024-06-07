from flask import Flask, render_template, request
import search

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    json_bing = {}
    json_google = {}
    if request.method == 'POST':
        query = request.form.get('query', '')
        json_bing = search.get_bing_results(query)
        json_google = search.get_google_results(query)

    return render_template('index.html', json_bing=json_bing, json_google=json_google)

if __name__ == '__main__':
    app.run(debug=True)
