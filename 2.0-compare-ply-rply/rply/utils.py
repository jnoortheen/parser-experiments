from typing import Dict, List, Union, MutableMapping
from rply.grammar import LRItem


class IdentityDict(MutableMapping[int, int]):
    def __init__(self) -> None:
        self._contents: "dict[int, tuple[list, int, int]]" = {}
        self._keepalive: "list[]" = []

    def __getitem__(self, key: Union[LRItem, List[LRItem], str]) -> Union[int, Dict[LRItem, Dict[LRItem, Dict[str, List[LRItem]]]], Dict[str, List[LRItem]]]:
        return self._contents[id(key)][1]

    def __setitem__(self, key: Union[LRItem, List[LRItem], str], value: int) -> None:
        idx = len(self._keepalive)
        self._keepalive.append(key)
        self._contents[id(key)] = key, value, idx

    def __delitem__(self, key):
        del self._contents[id(key)]
        for idx, obj in enumerate(self._keepalive):
            if obj is key:
                del self._keepalive[idx]
                break

    def __len__(self):
        return len(self._contents)

    def __iter__(self):
        for key, _, _ in self._contents.values():
            yield key


class Counter:
    def __init__(self) -> None:
        self.value = 0

    def incr(self) -> None:
        self.value += 1
