from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Fetched HTML</title></head>
<body>
<h2>Fetched HTML from {{ url }}</h2>
<textarea style="width:100%;height:600px;font-family:monospace;">{{ html }}</textarea>
</body>
</html>
"""

@app.route('/')
def index():
    url = request.args.get('url', 'https://linkz.mom/number/11926')
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/113.0.0.0 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        html = f"Error fetching URL: {e}"
    return render_template_string(HTML_TEMPLATE, url=url, html=html)

if __name__ == '__main__':
    app.run(debug=True)
