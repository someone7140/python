import yfinance as yf
from dateutil import relativedelta
from finance_analytics.domain.company_finance_info import CompanyFinanceInfo, FinanceByYear

from finance_analytics.domain.company_market_info import CompanyMarketInfo


def get_company_finance_info(company_market_info: CompanyMarketInfo):
    ticker_info = yf.Ticker(company_market_info.code + ".T")
    ticker_pl_info = ticker_info.financials
    # 決算日情報
    ir_date_list = ticker_pl_info.columns
    next_ir_date = ir_date_list[0] + relativedelta.relativedelta(years=1)
    # PL情報の取得
    total_revenues = ticker_pl_info.loc["Total Revenue"].values
    operating_incomes = ticker_pl_info.loc["Operating Income"].values
    net_income = ticker_pl_info.loc["Net Income"].values
    # 財務情報のリスト
    finance_info_year_list: list[FinanceByYear] = []

    for i, ir_date in enumerate(ir_date_list):
        finance_info_year_list.append(
            FinanceByYear(
                ir_date,
                round(total_revenues[i]),
                round(operating_incomes[i]),
                round(net_income[i]),
            ))

    return CompanyFinanceInfo(
        company_market_info.code,
        company_market_info.name,
        company_market_info.market,
        next_ir_date,
        finance_info_year_list
    )
