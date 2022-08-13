class Market:
    __market_dict = {'prime': 'プライム', 'standard': 'スタンダード', 'growth': 'グロース'}

    def __init__(self, market_code, market_name):
        self.code = market_code
        self.name = market_name

    @classmethod
    def make_market_from_name(cls, market_name):
        market_code = cls.__get_code_from_name(cls, market_name)
        return cls(market_code, market_name)

    def __get_code_from_name(self, market_name):
        market_code = ""
        for code, name in self.__market_dict.items():
            if market_name.startswith(name):
                market_code = code
                break
        return market_code
