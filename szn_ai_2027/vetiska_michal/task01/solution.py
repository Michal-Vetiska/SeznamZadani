"""CLI: největší skupina dvouciferných čísel, kde každá dvojice sdílí cifru."""

from __future__ import annotations

import sys


def digits(n: int) -> set[int]:
    return {int(ch) for ch in str(n)}


def solution(numbers: list[int]) -> int:
    """Vrátí velikost největší platné skupiny ze zadaných čísel."""
    digit_sets = [digits(n) for n in numbers]
    best = 0

    for d in range(10):
        count = 0
        for dset in digit_sets:
            if d in dset:
                count += 1
        if count > best:
            best = count

    for a in range(10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                ab = {a, b}
                bc = {b, c}
                ac = {a, c}
                count = 0
                for dset in digit_sets:
                    if dset == ab or dset == bc or dset == ac:
                        count += 1
                if count > best:
                    best = count

    return best


def parse_args(argv: list[str]) -> list[int]:
    if not argv:
        raise ValueError(
            "Očekáván alespoň 1 argument: dvouciferné číslo (N mezi 1 a 100000)."
        )
    if len(argv) > 100_000:
        raise ValueError("Příliš mnoho argumentů: N musí být nejvýše 100000.")

    numbers: list[int] = []
    for raw in argv:
        try:
            value = int(raw)
        except ValueError as exc:
            raise ValueError(f"Neplatný vstup '{raw}': očekáváno celé číslo.") from exc
        if value < 10 or value > 99:
            raise ValueError(
                f"Neplatné číslo {value}: očekáváno dvouciferné číslo v rozsahu 10–99."
            )
        numbers.append(value)
    return numbers


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    try:
        numbers = parse_args(args)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(solution(numbers))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
