from datetime import datetime as dt
import json
import requests


# qiitaの最新投稿を取得
def getQiitaPostsFromApi(postCount):
    try:
        response = requests.get(
            "https://qiita.com//api/v2/items?page=1&per_page=" + str(postCount))
        if response.status_code == 200:
            results = json.loads(response.content)
            return list(map(
                lambda x:
                {
                    "id": "qiita_" + str(x[0]),
                    'url': x[1].get("url"),
                    "updated_at": dt.strptime(x[1].get("updated_at"), '%Y-%m-%dT%H:%M:%S+09:00')
                }, enumerate(results)
            ))
        else:
            return []
    except json.JSONDecodeError:
        return []


# zennの最新投稿を取得
def getZennPostsFromApi(postCount):
    try:
        response = requests.get(
            "https://zenn.dev/api/articles?page=1&order=latest&count=" + str(postCount))
        if response.status_code == 200:
            results = json.loads(response.content)
            articles = results["articles"]
            return list(map(
                lambda x:
                {
                    "id": "zenn_" + str(x[0]),
                    'url': "https://zenn.dev/" + x[1].get("user").get("username") + "/articles/" + x[1].get("slug"),
                    "updated_at": dt.strptime(x[1].get("updated_at"), '%Y-%m-%dT%H:%M:%S.%f+09:00')
                }, enumerate(articles)
            ))
        else:
            return []
    except json.JSONDecodeError:
        return []
