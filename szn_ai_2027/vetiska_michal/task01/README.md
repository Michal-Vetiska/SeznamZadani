# Task 01 – Největší skupina se společnými ciframi

## Co program dělá

Ze seznamu dvouciferných čísel (`10`–`99`) najde velikost největší skupiny, ve které **každá dvojice** čísel sdílí alespoň jednu cifru.

## Spuštění

```bash
python3 solution.py 10 11 12
# stdout: 4
```

Import jako modul:

```python
from solution import solution

assert solution([99, 88, 77]) == 1
assert solution([10, 11, 12, 91]) == 4
assert solution([50, 30, 15, 51, 10, 20, 15]) == 5
```
