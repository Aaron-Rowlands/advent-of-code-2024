import sys
import re


class OrderingRule:
    def __init__(self, first: int, second: int):
        self.first = first
        self.second = second

    def check(self, sequence: list[int]) -> bool:
        """
        Returns False iff the sequence contains an instance of 'second'
        before an instance of 'first' anywhere.
        """
        return self._get_first_invalid_index(sequence) is None

    def _get_first_invalid_index(self, sequence: list[int]) -> int | None:
        for i in range(len(sequence) - 1):
            if sequence[i] == self.second:
                for j in range(i + 1, len(sequence)):
                    if sequence[j] == self.first:
                        return i
        return None

    def fix(self, sequence: list[int]) -> None:
        while (not self.check(sequence)):
            first_index = sequence.index(self.first)
            second_index = sequence.index(self.second)
            sequence[first_index], sequence[second_index] = (
                sequence[second_index], sequence[first_index])


def main():
    rules = read_rules(sys.argv[1])
    sequences = read_sequences(sys.argv[1])

    if any(len(sequence) % 2 == 0 for sequence in sequences):
        raise Exception(
            "There is at least one sequence with even length!")

    valid_sequences = [
        sequence for sequence in sequences
        if all(rule.check(sequence) for rule in rules)
    ]
    sum_of_middle_values = sum(
        sequence[len(sequence) // 2] for sequence in valid_sequences)
    print(f"Sum of middle values of the valid sequences: {sum_of_middle_values}")

    invalid_sequences = [
        sequence for sequence in sequences if sequence not in valid_sequences
    ]
    for sequence in invalid_sequences:
        while not all(rule.check(sequence) for rule in rules):
            for rule in rules:
                rule.fix(sequence)

    sum_of_fixed_middle_values = sum(
        sequence[len(sequence) // 2] for sequence in invalid_sequences
    )
    print(f"Sum of middle values of the fixed invalid sequences: {sum_of_fixed_middle_values}")

def read_rules(filename: str):
    rule_pattern = r"^(\d+)\|(\d+)$"
    rules = []

    with open(filename) as inputfile:
        for line in inputfile:
            match = re.match(rule_pattern, line)
            if match:
                rules.append(OrderingRule(
                    int(match.group(1)), int(match.group(2))))

    return rules


def read_sequences(filename: str):
    sequence_pattern = r"^\d+(,\d+)*$"
    sequences = []

    with open(filename) as inputfile:
        for line in inputfile:
            match = re.match(sequence_pattern, line)
            if match:
                sequence = [int(num) for num in line.split(",")]
                sequences.append(sequence)

    return sequences


if __name__ == "__main__":
    main()
