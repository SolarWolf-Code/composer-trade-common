import importlib
import pkgutil
from pathlib import Path
import composer_trade_common.groups

groups_path = Path(composer_trade_common.groups.__path__[0])

__all__ = []

for importer, modname, ispkg in pkgutil.iter_modules([str(groups_path)]):
    if ispkg:
        module = importlib.import_module(f"composer_trade_common.groups.{modname}")
        for attr_name in dir(module):
            if not attr_name.startswith("_"):
                globals()[attr_name] = getattr(module, attr_name)
                __all__.append(attr_name)
