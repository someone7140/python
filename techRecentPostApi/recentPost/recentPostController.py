import sys

sys.path.append("recentPost")
from externalApiService import getQiitaPostsFromApi, getZennPostsFromApi


# 最新の投稿を取得
def getRecentPosts():
    # qiitaとzennの投稿を取得
    postCount = 75
    qiitaPosts = sorted(getQiitaPostsFromApi(postCount),
                        key=lambda x: x['updated_at'], reverse=True)
    qiitaPostLength = len(qiitaPosts)
    zennPosts = sorted(getZennPostsFromApi(postCount),
                       key=lambda x: x['updated_at'], reverse=True)
    zennPostLength = len(zennPosts)
    # 結合
    recentPosts = []
    for i in range(postCount):
        if qiitaPostLength >= i + 1:
            recentPosts.append(qiitaPosts[i])
        if zennPostLength >= i + 1:
            recentPosts.append(zennPosts[i])
    return recentPosts
