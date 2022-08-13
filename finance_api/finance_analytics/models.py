from django.db import models


class CompanyMaster(models.Model):
    code = models.CharField(max_length=1000, unique=True)
    name = models.CharField(max_length=1000)
    market_code = models.CharField(max_length=100)
    next_ir_date = models.DateField()
    update_date = models.DateTimeField()

    class Meta:
        db_table = "company_master"


class CompanyFinance(models.Model):
    code = models.CharField(max_length=1000, db_index=True)
    ir_date = models.DateField(db_index=True)
    total_revenue = models.BigIntegerField(db_index=True)
    operating_income = models.BigIntegerField(db_index=True)
    net_income = models.BigIntegerField(db_index=True)
    update_date = models.DateTimeField()

    class Meta:
        db_table = "company_finance"
