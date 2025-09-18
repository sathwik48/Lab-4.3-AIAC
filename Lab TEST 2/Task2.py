from collections import defaultdict
from typing import List, Tuple, Dict

def aggregate_tuples(data: List[Tuple[str, int]]) -> Dict[str, int]:
    
    result: Dict[str, int] = defaultdict(int)
    for key, value in data:
        result[key] += value
    return dict(result)

# Sample Input
data = [('a',1),('b',2),('a',3)]
print(aggregate_tuples(data))  # Output: {'a': 4, 'b': 2}

# --- Unit Test ---
def test_aggregate_tuples():
    assert aggregate_tuples([('a',1),('b',2),('a',3)]) == {'a': 4, 'b': 2}
    assert aggregate_tuples([]) == {}
    assert aggregate_tuples([('x', 10)]) == {'x': 10}
    assert aggregate_tuples([('a', 1), ('a', -1)]) == {'a': 0}

test_aggregate_tuples()
print("All tests passed.")