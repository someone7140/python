import yfinance as yf
from finance_analytics.domain.company_finance_info import CompanyFinanceInfo
from finance_analytics.models import CompanyMaster


def get_all_companies_in_master():
    return CompanyMaster.objects.all().order_by('next_ir_date', 'code')


def register_company_master(id, code, name, market_code, next_ir_date, update_date):
    CompanyMaster(
        id=id,
        code=code,
        name=name,
        market_code=market_code,
        next_ir_date=next_ir_date,
        update_date=update_date
    ).save()
