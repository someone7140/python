import requests
import pandas as pd

from finance_analytics.domain.company_market_info import CompanyMarketInfo
from finance_analytics.domain.market import Market


def get_company_list_from_market():
    response = requests.get(
        "https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls")
    df = pd.read_excel(
        response.content, sheet_name="Sheet1", index_col=0)
    company_list: list[CompanyMarketInfo] = []
    for row in df.values:
        # プライム/スタンダード/グロースが対象
        market_name = row[2]
        if (market_name.startswith('プライム') or
                market_name.startswith('スタンダード') or
                market_name.startswith('グロース')):
            company_list.append(CompanyMarketInfo(
                str(row[0]), row[1], Market.make_market_from_name(market_name)))
    return company_list
