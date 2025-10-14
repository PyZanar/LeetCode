from collections import defaultdict
import pytest

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        max_freq = 0
        max_len = 0

        counts = defaultdict(int)

        for right in range(len(s)):
            counts[s[right]] += 1
            max_freq = max(max_freq, counts[s[right]])

            # 本当は無効なウィンドウが有効と判定される可能性があるが、最終結果には影響なし
            while (right-left+1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            
            # 無効なウィンドウの長さによって、max_lenの値が更新(増加)されることはない
            max_len = max(max_len, right-left+1)

        return max_len


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("ABAB", 0, 1),
    ]
)
def test_case(s, k, expected):
    actual = Solution().characterReplacement(s, k)
    assert actual == expected