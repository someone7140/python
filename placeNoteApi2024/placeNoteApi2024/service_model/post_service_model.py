from dataclasses import dataclass
from enum import Enum
from urllib.parse import urlparse
import uuid

import bs4
import requests
import urllib


class UrlTypeEnum(Enum):
    X = "x"
    Instagram = "instagram"
    Threads = "threads"
    WebWithInfo = "webWithInfo"
    WebNoInfo = "webNoInfo"


@dataclass
class UrlInfoServiceModel:
    title: str
    image_url: str | None
    site_name: str | None


@dataclass
class UrlServiceModel:
    url_id: str
    url: str
    url_type: UrlTypeEnum
    url_info: UrlInfoServiceModel | None
    embed_html: str | None

    URL_DOMAIN_DICT = {
        "x.com": UrlTypeEnum.X,
        "twitter.com": UrlTypeEnum.X,
        "www.instagram.com": UrlTypeEnum.Instagram,
        "www.threads.net": UrlTypeEnum.Threads,
    }

    @classmethod
    def make_object_from_url(cls, url: str):
        # urlのホスト名から種別を判定
        parsed_url = urlparse(url)
        url_type = cls.URL_DOMAIN_DICT.get(parsed_url.hostname, UrlTypeEnum.WebNoInfo)
        embed_html = None
        url_info = None

        # 種別によって処理を分ける
        if url_type == UrlTypeEnum.X:
            # Xの場合は埋め込み用のhtmlを取得する
            safe_url = urllib.parse.quote_plus(url)
            embed_res = requests.get(
                "https://publish.twitter.com/oembed?url=" + safe_url
            )
            if embed_res.status_code == 200:
                res_json = embed_res.json()
                embed_html = res_json.get("html", None)
            # 埋め込みHTMLが取得できてない場合は種別をWebNoInfoに変更
            if embed_html == None:
                url_type = UrlTypeEnum.WebNoInfo
        elif url_type == UrlTypeEnum.WebNoInfo:
            # Webページの場合はOGPからサイト情報を取得
            url_info = cls.get_url_info_from_ogp(cls, url)
            if url_info != None:
                url_type = UrlTypeEnum.WebWithInfo

        return cls(str(uuid.uuid4()), url, url_type, url_info, embed_html)

    @classmethod
    def get_url_info_from_ogp(cls, url: str) -> UrlInfoServiceModel | None:
        # ogpからそのサイトの情報を取得する
        try:
            result_html = requests.get(url)
            soup_parser = bs4.BeautifulSoup(result_html, "html.parser")
            title = cls.get_contents_ogp_property(soup_parser, "og:title")
            image_url = cls.get_contents_ogp_property(soup_parser, "og:image")
            site_name = cls.get_contents_ogp_property(soup_parser, "og:site_name")

            if title == None:
                return None

            return UrlInfoServiceModel(title, image_url, site_name)
        except Exception as e:
            # エラーの場合はNoneを返す
            return None

    @classmethod
    def get_contents_ogp_property(
        soup_parser: bs4.BeautifulSoup, property: str
    ) -> str | None:
        # ogpのpropertyからコンテンツを取得
        try:
            og_elems = soup_parser.select(f'[property="{property}"]')
            if len(og_elems) == 0:
                return None

            return og_elems[0].get("content")
        except Exception as e:
            # エラーの場合はNoneを返す
            return None
