from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trace', methods=['POST'])
def trace_product():
    product_url = request.form.get("url")
    try:
        response = requests.get(product_url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("title").text.strip()
        ali_search_url = f"https://www.aliexpress.com/wholesale?SearchText={quote(title)}"
        return render_template("index.html", product_title=title, ali_url=ali_search_url)
    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

