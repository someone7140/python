import time
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from finance_analytics.service.company_finance_service import get_company_finance_info
from finance_analytics.service.company_list_service import get_company_list_from_market
from finance_analytics.service.company_register_service import get_registered_companies, register_company_finance_info


@api_view(['POST'])
def update_company_info(request):
    # マーケット情報から会社の一覧を取得
    company_list_market = get_company_list_from_market()
    # DBから会社の登録情報を取得
    company_master_results = get_registered_companies()
    all_master_companies = company_master_results[0]
    registered_finance_master_companies = company_master_results[1]

    # DBの財務情報更新済みリストにない企業を最大20個まで登録
    registered_count = 0
    for company in company_list_market:
        if registered_count > 0:
            break
        else:
            registered_flag = any(
                c.code == company.code for c in registered_finance_master_companies)
            # 登録済みでなければ登録処理
            if not registered_flag:
                company_finance_info = get_company_finance_info(company)
                register_company_finance_info(
                    company_finance_info, all_master_companies)
                registered_count += 1
                # 連続してアクセスしないようスリープを入れる
                time.sleep(0.5)

    return Response({"success": True}, status=status.HTTP_200_OK)
