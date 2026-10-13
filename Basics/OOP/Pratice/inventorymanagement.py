"""
claude
Don't generate lab for this
"""
from collections import UserDict


class InventoryManagement(UserDict):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key: str, item: int):
        if not isinstance(key, str) or not isinstance(item, int):
            raise TypeError('Key should be string and value should be int')
        super().__setitem__(key.casefold(), item)

    def __getitem__(self, item):
        if isinstance(item, str):
            return super().__getitem__(item.casefold())
        return None

    def __delitem__(self, key):
        if isinstance(key, str):
            return super().__delitem__(key)
        return None