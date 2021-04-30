from datetime import datetime
import flask
from flask_cors import CORS
import json
from flask import Flask, render_template
from flask import request

from ogpInfo.ogpInfoController import getOgpInfo
from recentPost.recentPostController import getRecentPosts


app = Flask(__name__)
# staticのURLパスを指定
app = Flask(__name__, static_url_path='/')
CORS(app)


# デフォルトのパス
@app.route("/")
def index():
    return render_template("index.html")


# 最新投稿の取得
@app.route('/recentPosts')
def recentPosts():
    posts = getRecentPosts()
    respToClient = flask.Response(json.dumps(
        posts, default=json_serial, ensure_ascii=False))
    return respToClient


# Ogp情報の取得
@app.route("/ogpInfo", methods=["POST"])
def ogpInfo():
    ogpInfos = getOgpInfo(request.json)
    respToClient = flask.Response(json.dumps(
        ogpInfos, default=json_serial, ensure_ascii=False))
    return respToClient


def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError("Type %s not serializable" % type(obj))


if __name__ == '__main__':
    app.run()
