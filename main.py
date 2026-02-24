from composer.client import ComposerClient
from composer.models.common.symphony import *
from groups.safe_sectors_or_bonds.main import group_safe_sectors_or_bond_1011a315
import os
from dotenv import load_dotenv

load_dotenv()


symph = SymphonyDefinition(
    name="Example Group Import",
    description="Demonstrates importing a group from the shared collection",
    rebalance="daily",
    children=[
        WeightCashEqual(
            children=[
                group_safe_sectors_or_bond_1011a315
            ]
        ),
    ],
)

client = ComposerClient(
    api_key=os.getenv("COMPOSER_API_KEY"),
    api_secret=os.getenv("COMPOSER_API_SECRET"),
)

res = client.backtest.run_v2(symphony=symph)
print(res)
