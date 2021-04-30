import requests
from bs4 import BeautifulSoup


# OGPの情報を取得して返す
def getOgpInfo(requestInfos):
    ogpResults = []
    for request in requestInfos:
        try:
            result = {
                "id": request["id"],
                "url": request["url"],
                "updated_at": request["updated_at"],
            }
            r = requests.get(request["url"])
            soup = BeautifulSoup(r.text, 'html.parser')
            for i in soup.find_all("meta"):
                if i.get("property", None) == "og:title":
                    result["title"] = i.get("content", None)
                if i.get("property", None) == "og:image":
                    result["image"] = i.get("content", None)
            ogpResults.append(result)
        except Exception:
            continue

    return ogpResults
