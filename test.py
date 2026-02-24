from composer_trade_common import safe_sectors_or_bonds
from composer.client import ComposerClient
from composer.models.common.symphony import SymphonyDefinition, WeightCashEqual
import os
from dotenv import load_dotenv

load_dotenv()

symph = SymphonyDefinition(
    name="Test Import",
    description="Tests importing group from composer_trade_common package",
    rebalance="daily",
    children=[
        WeightCashEqual(children=[safe_sectors_or_bonds]),
    ],
)

client = ComposerClient(
    api_key=os.getenv("COMPOSER_API_KEY"),
    api_secret=os.getenv("COMPOSER_API_SECRET"),
)

res = client.backtest.run_v2(symphony=symph)
print(res)
