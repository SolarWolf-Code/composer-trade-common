# composer-trade-common

A collection of common groups used in Composer symphonies. Install with:

```bash
pip install composer-trade-common
```

Then import groups directly:

```python
from composer_trade_common import safe_sectors_or_bonds
```



## Usage

In this example we can import the defined group `Safe Sectors or Bonds`.

### Input:
```py
from composer.client import ComposerClient
from composer.models.common.symphony import *
from composer_trade_common import safe_sectors_or_bonds
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
                safe_sectors_or_bonds
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