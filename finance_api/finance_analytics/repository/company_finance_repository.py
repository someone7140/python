from finance_analytics.domain.company_finance_info import FinanceByYear
from finance_analytics.models import CompanyFinance


def get_finance_info_by_company_code(code):
    return CompanyFinance.objects.filter(code=code).order_by('ir_date')


def insert_finance_info_list(finance_info_list: list[FinanceByYear], company_code, update_date):
    add_finance_list: list[CompanyFinance] = []
    for finance_info in finance_info_list:
        add_finance_list.append(CompanyFinance(
            code=company_code,
            ir_date=finance_info.ir_date,
            total_revenue=finance_info.total_revenue,
            operating_income=finance_info.operating_income,
            net_income=finance_info.net_income,
            update_date=update_date
        ))
    CompanyFinance.objects.bulk_create(add_finance_list)
