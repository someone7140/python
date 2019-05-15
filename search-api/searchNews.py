import json
import requests
import constants
import flask
import tokenizeSentence

class NewsApi(object):
    @staticmethod
    def get_recent_news(input_word, input_page):
        data = {} 
        if input_word is not None:
            try:
                word = ' AND '.join(map(lambda x: '"' + x + '"', input_word.split(" ")))
                page = input_page if input_page is not None else 1
                url = constants.Api.newsApiUrl + "sortBy=publishedAt&apiKey=" + constants.Api.newsApiKey + "&page=" + page + "&q=" + word
                response = requests.get(url)
                if response.status_code == 200:
                    result = json.loads(response.content)
                    data["status_code"] = response.status_code
                    data["total_results"] = 100 if result["totalResults"] > 100 else result["totalResults"]
                    articleList =  list(map(
                        lambda x:
                            {
                                'title': x.get("title"),
                                'url': x.get("url"),
                                'image': x.get("urlToImage"),                           
                                'source': x["source"]["name"],
                                'date': x.get("publishedAt").replace("T", " ").replace("Z", ""),
                                'description':
                                    tokenizeSentence.TokenizerSentence.delete_tag(x.get("description")) if x.get("description") is not None else "",
                                'noun':
                                    tokenizeSentence.TokenizerSentence.extract_noun(tokenizeSentence.TokenizerSentence.delete_tag(x.get("description"))) if x.get("description") is not None and tokenizeSentence.TokenizerSentence.is_japanese(x.get("description")) else []
                            }
                        , result["articles"]
                    ))
                    data["articles"] = articleList
                else:
                    data = {'status_code': response.status_code}
            except json.JSONDecodeError :
                data = {'status_code': 500}
        else:
            data = {'status_code': 400}
        respToClient = flask.Response(json.dumps(data, ensure_ascii=False))
        respToClient.headers['Access-Control-Allow-Origin'] = constants.View.viewUrl
        respToClient.headers['Access-Control-Allow-Headers'] = "Content-Type"
        return respToClient
