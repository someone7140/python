from finance_analytics.domain.market import Market


class CompanyMarketInfo:
    def __init__(self, code, name, market: Market):
        self.code = code
        self.name = name
        self.market: Market = market
