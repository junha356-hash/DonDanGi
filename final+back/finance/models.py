from django.db import models
# 주택담보대출 모델
class LoanProduct(models.Model):
    product_code = models.CharField(max_length=50, unique=True)       # 고유 식별자
    product_name = models.CharField(max_length=200)                   # 상품명
    bank_name = models.CharField(max_length=100)                      # 금융회사명
    loan_type = models.CharField(max_length=50)                       # 예: 주택담보
    join_way = models.TextField(blank=True, null=True)                # 가입 방법
    erly_rpay_fee = models.TextField(blank=True, null=True)           # 중도상환수수료
    dly_rate = models.CharField(max_length=100, blank=True, null=True) # 연체이자율
    loan_lmt = models.TextField(blank=True, null=True)                # 대출한도

    def __str__(self):
        return f"{self.bank_name} - {self.product_name}"

class LoanOption(models.Model):
    product = models.ForeignKey(LoanProduct, on_delete=models.CASCADE, related_name='options')
    rpay_type_nm = models.CharField(max_length=100, blank=True, null=True)         # 상환 방식명
    lend_rate_type_nm = models.CharField(max_length=100, blank=True, null=True)    # 금리 유형명
    lend_rate_min = models.FloatField(blank=True, null=True)                       # 최소 금리
    lend_rate_max = models.FloatField(blank=True, null=True)                       # 최대 금리

    def __str__(self):
        return f"{self.product.product_name} - {self.rpay_type_nm} - {self.lend_rate_type_nm}"

# 전세자금대출 모델 
class RentLoanProduct(models.Model):
    product_code = models.CharField(max_length=50, unique=True)       # 상품 코드
    product_name = models.CharField(max_length=200)                   # 상품명
    bank_name = models.CharField(max_length=100)                      # 금융회사명
    loan_type = models.CharField(max_length=50, default='전세자금')   # 대출 유형 (고정값)
    join_way = models.TextField(blank=True, null=True)                # 가입 방법
    erly_rpay_fee = models.TextField(blank=True, null=True)           # 중도상환수수료
    dly_rate = models.CharField(max_length=100, blank=True, null=True) # 연체이자율
    loan_lmt = models.TextField(blank=True, null=True)                # 대출한도

    def __str__(self):
        return f"{self.bank_name} - {self.product_name}"

class RentLoanOption(models.Model):
    product = models.ForeignKey(RentLoanProduct, on_delete=models.CASCADE, related_name='options')
    rpay_type_nm = models.CharField(max_length=100, blank=True, null=True)         # 상환 방식명
    lend_rate_type_nm = models.CharField(max_length=100, blank=True, null=True)    # 금리 유형명
    lend_rate_min = models.FloatField(blank=True, null=True)                       # 최소 금리
    lend_rate_max = models.FloatField(blank=True, null=True)                       # 최대 금리

    def __str__(self):
        return f"{self.product.product_name} - {self.rpay_type_nm} - {self.lend_rate_type_nm}"

# 개인신용대출 모델 
class CreditLoanProduct(models.Model):
    product_code = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=100)
    crdt_prdt_type_nm = models.CharField(max_length=100, blank=True, null=True)
    dcls_month = models.CharField(max_length=10, blank=True, null=True)
    raw_json = models.JSONField()

    def __str__(self):
        return f"{self.bank_name} - {self.product_name}"

class CreditLoanOption(models.Model):
    product = models.ForeignKey(CreditLoanProduct, on_delete=models.CASCADE, related_name='options')
    crdt_lend_rate_type_nm = models.CharField(max_length=100, blank=True, null=True)
    crdt_grad_avg = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.crdt_lend_rate_type_nm}"


# 정기 예금 상품
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_member = models.TextField()
    join_way = models.TextField()
    
# 정기 예금 상품 옵션
class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete = models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=100)
    save_trm = models.IntegerField(null=True)
    intr_rate = models.FloatField(null=True)

# 정기 적금상품
class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()

# 정기 적금 상품 옵션
class SavingOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(SavingProducts, on_delete = models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=100)
    save_trm = models.IntegerField(null=True)
    intr_rate = models.FloatField(null=True)
