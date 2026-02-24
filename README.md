# Common-Composer-Blocks

[composer-trade-py](https://github.com/SolarWolf-Code/composer-trade-py/tree/main) SDK allows you to easily reference other building blocks based on defined variables within your project. This repo serves as a common collection of commonly used building blocks.



## Usage

In this example we can import the defined group `Safe Sectors or Bonds` by importing it from a different file. 

### Input:
```py
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

```
### Output:
```bash
BacktestResult(stats=Stats(sharpe=1.71, cumulative=7095.53%, drawdown=18.00%, ann_return=25.53%), final_value=719,553.16, days=6880)
```