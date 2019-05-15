from flask import Flask
from flask import request
import searchNews

app = Flask(__name__)

@app.route('/search_news')
def search_news():
    word = request.args.get('word')
    page = request.args.get('page')
    return searchNews.NewsApi.get_recent_news(word, page)

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
