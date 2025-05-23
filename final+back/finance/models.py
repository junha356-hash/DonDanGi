from django.db import models

# 연금저축 모델 
# class PensionProduct(models.Model):
#     product_code = models.CharField(max_length=50, unique=True)
#     product_name = models.CharField(max_length=200)
#     bank_name = models.CharField(max_length=100)
#     fin_co_no = models.CharField(max_length=20, blank=True, null=True)
#     join_way = models.TextField(blank=True, null=True)
#     pnsn_kind = models.CharField(max_length=50, blank=True, null=True)
#     pnsn_kind_nm = models.CharField(max_length=100, blank=True, null=True)
#     sale_strt_day = models.CharField(max_length=20, blank=True, null=True)
#     mntn_cnt = models.CharField(max_length=50, blank=True, null=True)
#     prdt_type = models.CharField(max_length=50, blank=True, null=True)
#     prdt_type_nm = models.CharField(max_length=100, blank=True, null=True)
#     dcls_rate = models.FloatField(blank=True, null=True)
#     guar_rate = models.FloatField(blank=True, null=True)
#     btrm_prft_rate_1 = models.FloatField(blank=True, null=True)
#     btrm_prft_rate_2 = models.FloatField(blank=True, null=True)
#     btrm_prft_rate_3 = models.FloatField(blank=True, null=True)
#     etc = models.TextField(blank=True, null=True)
#     sale_co = models.TextField(blank=True, null=True)
#     dcls_month = models.CharField(max_length=10, blank=True, null=True)
#     dcls_strt_day = models.CharField(max_length=20, blank=True, null=True)
#     dcls_end_day = models.CharField(max_length=20, blank=True, null=True)
#     fin_co_subm_day = models.CharField(max_length=20, blank=True, null=True)
#     raw_json = models.JSONField()

#     def __str__(self):
#         return f"{self.bank_name} - {self.product_name}"

# class PensionOption(models.Model):
#     product = models.ForeignKey(PensionProduct, on_delete=models.CASCADE, related_name='options')
#     intr_rate_type = models.CharField(max_length=50, blank=True, null=True)
#     intr_rate_type_nm = models.CharField(max_length=100, blank=True, null=True)
#     rsrv_type = models.CharField(max_length=50, blank=True, null=True)
#     rsrv_type_nm = models.CharField(max_length=100, blank=True, null=True)
#     save_trm = models.CharField(max_length=20, blank=True, null=True)
#     intr_rate = models.FloatField(blank=True, null=True)
#     intr_rate2 = models.FloatField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.product.product_name} - {self.intr_rate_type_nm} - {self.rsrv_type_nm}"

# 주택담보대출 모델
class LoanProduct(models.Model):
    product_code = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=100)
    loan_type = models.CharField(max_length=50)
    join_way = models.TextField(blank=True, null=True)
    loan_inci_expn = models.TextField(blank=True, null=True)
    erly_rpay_fee = models.TextField(blank=True, null=True)
    dly_rate = models.CharField(max_length=100, blank=True, null=True)
    loan_lmt = models.TextField(blank=True, null=True)
    dcls_month = models.CharField(max_length=10, blank=True, null=True)
    dcls_strt_day = models.CharField(max_length=20, blank=True, null=True)
    dcls_end_day = models.CharField(max_length=20, blank=True, null=True)
    fin_co_subm_day = models.CharField(max_length=20, blank=True, null=True)
    raw_json = models.JSONField()

    def __str__(self):
        return f"{self.bank_name} - {self.product_name}"

class LoanOption(models.Model):
    product = models.ForeignKey(LoanProduct, on_delete=models.CASCADE, related_name='options')
    mrtg_type = models.CharField(max_length=100, blank=True, null=True)
    mrtg_type_nm = models.CharField(max_length=100, blank=True, null=True)
    rpay_type = models.CharField(max_length=100, blank=True, null=True)
    rpay_type_nm = models.CharField(max_length=100, blank=True, null=True)
    lend_rate_type = models.CharField(max_length=100, blank=True, null=True)
    lend_rate_type_nm = models.CharField(max_length=100, blank=True, null=True)
    lend_rate_min = models.FloatField(blank=True, null=True)
    lend_rate_max = models.FloatField(blank=True, null=True)
    lend_rate_avg = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.mrtg_type_nm} - {self.lend_rate_type_nm}"

# 전세자금대출 모델 
class RentLoanProduct(models.Model):
    product_code = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=100)
    fin_co_no = models.CharField(max_length=20, blank=True, null=True)
    loan_type = models.CharField(max_length=50, default='전세자금')
    join_way = models.TextField(blank=True, null=True)
    loan_inci_expn = models.TextField(blank=True, null=True)
    erly_rpay_fee = models.TextField(blank=True, null=True)
    dly_rate = models.CharField(max_length=100, blank=True, null=True)
    loan_lmt = models.TextField(blank=True, null=True)
    dcls_month = models.CharField(max_length=10, blank=True, null=True)
    dcls_strt_day = models.CharField(max_length=20, blank=True, null=True)
    dcls_end_day = models.CharField(max_length=20, blank=True, null=True)
    fin_co_subm_day = models.CharField(max_length=20, blank=True, null=True)
    raw_json = models.JSONField()

    def __str__(self):
        return f"{self.bank_name} - {self.product_name}"

class RentLoanOption(models.Model):
    product = models.ForeignKey(RentLoanProduct, on_delete=models.CASCADE, related_name='options')
    rpay_type = models.CharField(max_length=100, blank=True, null=True)
    rpay_type_nm = models.CharField(max_length=100, blank=True, null=True)
    lend_rate_type = models.CharField(max_length=100, blank=True, null=True)
    lend_rate_type_nm = models.CharField(max_length=100, blank=True, null=True)
    lend_rate_min = models.FloatField(blank=True, null=True)
    lend_rate_max = models.FloatField(blank=True, null=True)
    lend_rate_avg = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.rpay_type_nm} - {self.lend_rate_type_nm}"

# 개인신용대출 모델 
class CreditLoanProduct(models.Model):
    product_code = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=100)
    fin_co_no = models.CharField(max_length=20, blank=True, null=True)
    join_way = models.TextField(blank=True, null=True)
    crdt_prdt_type = models.CharField(max_length=50, blank=True, null=True)
    crdt_prdt_type_nm = models.CharField(max_length=100, blank=True, null=True)
    cb_name = models.CharField(max_length=100, blank=True, null=True)
    dcls_month = models.CharField(max_length=10, blank=True, null=True)
    dcls_strt_day = models.CharField(max_length=20, blank=True, null=True)
    dcls_end_day = models.CharField(max_length=20, blank=True, null=True)
    fin_co_subm_day = models.CharField(max_length=20, blank=True, null=True)
    raw_json = models.JSONField()

    def __str__(self):
        return f"{self.bank_name} - {self.product_name}"

class CreditLoanOption(models.Model):
    product = models.ForeignKey(CreditLoanProduct, on_delete=models.CASCADE, related_name='options')
    crdt_lend_rate_type = models.CharField(max_length=50, blank=True, null=True)
    crdt_lend_rate_type_nm = models.CharField(max_length=100, blank=True, null=True)
    crdt_grad_1 = models.FloatField(blank=True, null=True)
    crdt_grad_4 = models.FloatField(blank=True, null=True)
    crdt_grad_5 = models.FloatField(blank=True, null=True)
    crdt_grad_6 = models.FloatField(blank=True, null=True)
    crdt_grad_10 = models.FloatField(blank=True, null=True)
    crdt_grad_11 = models.FloatField(blank=True, null=True)
    crdt_grad_12 = models.FloatField(blank=True, null=True)
    crdt_grad_13 = models.FloatField(blank=True, null=True)
    crdt_grad_avg = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.crdt_lend_rate_type_nm}"