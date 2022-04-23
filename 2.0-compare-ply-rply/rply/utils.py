from typing import Dict, List, Union, Iterator
from rply.grammar import LRItem
from collections.abc import MutableMapping


KeyType = Union[LRItem, List[LRItem], str]


class IdentityDict(MutableMapping[KeyType, int]):
    def __init__(self) -> None:
        self._contents: Dict[int, "tuple[KeyType, int, int]"] = {}
        self._keepalive: List[KeyType] = []

    def __getitem__(
        self, key: KeyType
    ) -> Union[
        int,
        Dict[LRItem, Dict[LRItem, Dict[str, List[LRItem]]]],
        Dict[str, List[LRItem]],
    ]:
        return self._contents[id(key)][1]

    def __setitem__(self, key: KeyType, value: int) -> None:
        idx = len(self._keepalive)
        self._keepalive.append(key)
        self._contents[id(key)] = key, value, idx

    def __delitem__(self, key: KeyType) -> None:
        del self._contents[id(key)]
        for idx, obj in enumerate(self._keepalive):
            if obj is key:
                del self._keepalive[idx]
                break

    def __len__(self) -> int:
        return len(self._contents)

    def __iter__(self) -> Iterator[KeyType]:
        for key, _, _ in self._contents.values():
            yield key


class Counter:
    def __init__(self) -> None:
        self.value = 0

    def incr(self) -> None:
        self.value += 1
