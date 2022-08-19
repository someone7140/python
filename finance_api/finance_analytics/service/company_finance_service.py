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
    # BS情報の取得
    ticker_bs_info = ticker_info.balance_sheet
    assets = ticker_bs_info.loc["Total Assets"].values
    liabilities = ticker_bs_info.loc["Total Liab"].values
    equities = ticker_bs_info.loc["Total Stockholder Equity"].values
    # CF情報の取得
    ticker_cf_info = ticker_info.cashflow
    operating_cf = ticker_cf_info.loc["Total Cash From Operating Activities"].values
    investment_cf = ticker_cf_info.loc["Total Cashflows From Investing Activities"].values
    finance_cf = ticker_cf_info.loc["Total Cash From Financing Activities"].values
    # 株価情報の取得
    ticker_stock_info = ticker_info.history(period="max")

    # 財務情報のリスト作成
    finance_info_year_list: list[FinanceByYear] = []
    for i, ir_date in enumerate(ir_date_list):
        stock_price = 0
        try:
            stock_price = round(ticker_stock_info.loc[ir_date.strftime(
                '%Y-%m-%d')]["Close"])
        except KeyError:
            stock_price = 0
        finance_info_year_list.append(
            FinanceByYear(
                ir_date,
                round(total_revenues[i]),
                round(operating_incomes[i]),
                round(net_income[i]),
                round(assets[i]),
                round(liabilities[i]),
                round(equities[i]),
                round(operating_cf[i]),
                round(investment_cf[i]),
                round(finance_cf[i]),
                stock_price,
            ))

    return CompanyFinanceInfo(
        company_market_info.code,
        company_market_info.name,
        company_market_info.market,
        next_ir_date,
        finance_info_year_list
    )
