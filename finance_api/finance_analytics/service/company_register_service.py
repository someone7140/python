from django.utils import timezone
from finance_analytics.domain.company_finance_info import CompanyFinanceInfo, FinanceByYear
from finance_analytics.models import CompanyMaster
from finance_analytics.repository.company_finance_repository import get_finance_info_by_company_code, insert_finance_info_list
from finance_analytics.repository.company_master_repository import get_all_companies_in_master, register_company_master


def register_company_finance_info(
        company_finance_info: CompanyFinanceInfo,
        all_master_companies: list[CompanyMaster]
):
    dt_now_jst = timezone.now()
    # 企業マスタの登録
    registered_company_info = next(
        (c for c in all_master_companies if c.code == company_finance_info.code), None)
    if registered_company_info == None:
        register_company_master(
            None,
            company_finance_info.code,
            company_finance_info.name,
            company_finance_info.market.code,
            company_finance_info.next_ir_date,
            dt_now_jst
        )
    else:
        register_company_master(
            registered_company_info.id,
            company_finance_info.code,
            company_finance_info.name,
            company_finance_info.market.code,
            company_finance_info.next_ir_date,
            dt_now_jst
        )
    # 財務情報の登録
    registered_finance_info_list = list(get_finance_info_by_company_code(
        company_finance_info.code))
    add_finance_list: list[FinanceByYear] = list(filter(
        lambda x: not any(
            x.ir_date == f.ir_date for f in registered_finance_info_list), company_finance_info.finance_by_year_list))
    insert_finance_info_list(
        add_finance_list, company_finance_info.code, dt_now_jst)


def get_registered_companies():
    all_companies: list[CompanyMaster] = list(get_all_companies_in_master())

    # 決算情報登録済みの会社絞り込み（次の決算日が過ぎていない会社）
    dt_now_jst = timezone.now()
    finance_registered_company: list[CompanyMaster] = list(filter(
        lambda x: x.next_ir_date > dt_now_jst.date(), all_companies))

    return all_companies, finance_registered_company
