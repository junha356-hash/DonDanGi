import pandas as pd
from goldsilver.models import GoldPrice, SilverPrice

# 금
gold_df = pd.read_excel('./assets/Gold_prices.xlsx')
for _, row in gold_df.iterrows():
    GoldPrice.objects.update_or_create(
        date=row['Date'],
        defaults={'price': row['Close/Last']}
    )

# 은
silver_df = pd.read_excel('./assets/Silver_prices.xlsx')
for _, row in silver_df.iterrows():
    SilverPrice.objects.update_or_create(
        date=row['Date'],
        defaults={'price': row['Close/Last']}
    )
