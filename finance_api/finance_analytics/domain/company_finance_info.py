from finance_analytics.domain.market import Market


class FinanceByYear:
    def __init__(
        self,
        ir_date,
        total_revenue,
        operating_income,
        net_income,
        assets,
        liabilities,
        equities,
        operating_cf,
        investment_cf,
        finance_cf,
        stock_price
    ):
        self.ir_date = ir_date
        self.total_revenue = total_revenue
        self.operating_income = operating_income
        self.net_income = net_income
        self.assets = assets
        self.liabilities = liabilities
        self.equities = equities
        self.operating_cf = operating_cf
        self.investment_cf = investment_cf
        self.finance_cf = finance_cf
        self.stock_price = stock_price


class CompanyFinanceInfo:
    def __init__(self, code, name, market: Market, next_ir_date, finance_by_year_list: list[FinanceByYear]):
        self.code = code
        self.name = name
        self.market: Market = market
        self.next_ir_date = next_ir_date
        self.finance_by_year_list: list[FinanceByYear] = finance_by_year_list
