from puzzle_201519_input import puzzleInput, replacement_list


def get_possible_next_molecules(
    replacements: list[tuple[str, str]], input: str, reverse: bool = False
) -> set[str]:
    possible_molecules = set()
    for replacement in replacements:
        new_value = None
        old_value = None
        if not reverse:
            old_value = replacement[0]
            new_value = replacement[1]
        else:
            new_value = replacement[0]
            old_value = replacement[1]

        all_occurrences = find_all_occurrences(old_value, input)
        for occurence in all_occurrences:
            prefix = input[:occurence]
            postfix = input[occurence + len(old_value) :]
            new_molecule = f"{prefix}{new_value}{postfix}"
            possible_molecules.add(new_molecule)

    possible_molecules.discard(input)
    return possible_molecules


def find_all_occurrences(substring: str, input: str) -> set[int]:
    start = 0
    occurrences = set()
    while start < len(input):
        found_at_index = input.find(substring, start)
        if found_at_index > -1:
            occurrences.add(found_at_index)
            start = found_at_index + 1
        else:
            start = len(input)
    return occurrences


def do_puzzle_part1(replacement_map: list[tuple[str, str]], input: str) -> int:
    return len(get_possible_next_molecules(replacement_map, input))


def do_puzzle_part2(
    replacement_map: list[tuple[str, str]], molecule_to_generate: str
) -> int:
    current_molecules = {molecule_to_generate}
    step = 0
    while "e" not in current_molecules:
        next_possible_molecules = set()
        for molecule in current_molecules:
            next_possible_molecules.update(
                get_possible_next_molecules(replacement_map, molecule, reverse=True)
            )
        # Take only the first 100 shortest options into consideration. This is completely fine as we want to
        # find the smallest amount of steps. Most likely the shorter options quicker converge.
        # I don't know a proper way to define the amount of options to consider. So the number is arbitrary
        current_molecules = set(sorted(next_possible_molecules, key=len)[:100])
        step += 1
    return step


if __name__ == "__main__":
    print(do_puzzle_part1(replacement_list, puzzleInput))
    print(do_puzzle_part2(replacement_list, puzzleInput))
