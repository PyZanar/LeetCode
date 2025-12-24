from typing import List
from collections import defaultdict
import pytest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dct = defaultdict(list)

        for word in strs:
            dct["".join(sorted(word))].append(word)

        return list(dct.values())


cases = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    ([""], [[""]]),
    (["a"], [["a"]]),
]


@pytest.mark.parametrize(
    "strs, expected_list", cases, ids=[f"case_{i}" for i in range(1, len(cases) + 1)]
)
def test_case(strs, expected_list):
    res_list = Solution().groupAnagrams(strs)
    actual = sorted([sorted(lst) for lst in res_list])
    expected = sorted([sorted(lst) for lst in expected_list])
    assert actual == expected
