from puzzle_201521_input import puzzleInput
import itertools
from dataclasses import dataclass


@dataclass
class Character:
    hp: int
    damage: int
    armor: int

    def attack(self, enemy: "Character") -> None:
        enemy.hp -= max(self.damage - enemy.armor, 1)


@dataclass
class Item:
    cost: int
    damage: int
    armor: int


def get_all_varations():
    available_weapons = [
        Item(8, 4, 0),
        Item(10, 5, 0),
        Item(25, 6, 0),
        Item(40, 7, 0),
        Item(74, 8, 0),
    ]
    available_armor = [
        Item(13, 0, 1),
        Item(31, 0, 2),
        Item(53, 0, 3),
        Item(75, 0, 4),
        Item(102, 0, 5),
    ]
    available_rings = [
        Item(25, 1, 0),
        Item(50, 2, 0),
        Item(100, 3, 0),
        Item(20, 0, 1),
        Item(40, 0, 2),
        Item(80, 0, 3),
    ]
    NO_ITEM = Item(0, 0, 0)
    zero_rings = [(NO_ITEM, NO_ITEM)]
    one_ring = [(ring, NO_ITEM) for ring in available_rings]
    two_rings = [rings for rings in itertools.combinations(available_rings, 2)]
    possible_variations = itertools.product(
        available_weapons,
        [NO_ITEM] + available_armor,
        zero_rings + one_ring + two_rings,
    )
    return possible_variations


def simulate_fight(player: Character, boss: Character) -> bool:
    attacker = player
    defender = boss
    while player.hp > 0 and boss.hp > 0:
        attacker.attack(defender)
        temp = attacker
        attacker = defender
        defender = temp

    return player.hp > 0


def do_puzzle_part1(input):
    lowest_equipment_cost = 999999
    for weapon, armor, (ring1, ring2) in get_all_varations():
        boss = Character(input["hp"], input["damage"], input["armor"])

        total_damage = weapon.damage + ring1.damage + ring2.damage
        total_armor = armor.armor + ring1.armor + ring2.armor
        player = Character(100, total_damage, total_armor)

        player_won = simulate_fight(player, boss)
        if player_won:
            total_cost = weapon.cost + armor.cost + ring1.cost + ring2.cost
            lowest_equipment_cost = min(lowest_equipment_cost, total_cost)

    return lowest_equipment_cost


def do_puzzle_part2(input):
    highest_equipment_cost = 0
    for weapon, armor, (ring1, ring2) in get_all_varations():
        boss = Character(input["hp"], input["damage"], input["armor"])

        total_damage = weapon.damage + ring1.damage + ring2.damage
        total_armor = armor.armor + ring1.armor + ring2.armor
        player = Character(100, total_damage, total_armor)

        player_won = simulate_fight(player, boss)
        if not player_won:
            total_cost = weapon.cost + armor.cost + ring1.cost + ring2.cost
            highest_equipment_cost = max(highest_equipment_cost, total_cost)

    return highest_equipment_cost


if __name__ == "__main__":
    print(do_puzzle_part1(puzzleInput))
    print(do_puzzle_part2(puzzleInput))
