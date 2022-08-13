from finance_analytics.domain.market import Market


class FinanceByYear:
    def __init__(self, ir_date, total_revenue, operating_income, net_income):
        self.ir_date = ir_date
        self.total_revenue = total_revenue
        self.operating_income = operating_income
        self.net_income = net_income


class CompanyFinanceInfo:
    def __init__(self, code, name, market: Market, next_ir_date, finance_by_year_list: list[FinanceByYear]):
        self.code = code
        self.name = name
        self.market: Market = market
        self.next_ir_date = next_ir_date
        self.finance_by_year_list: list[FinanceByYear] = finance_by_year_list
