"""This program is designed to find # of tea bags, treats and cost of a tea party"""

__author__: str = "730678802"


def main_planner(guests: int) -> None:
    """This is the entry point of the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculate quantity of tea bags needed."""
    return 2 * people


def treats(people: int) -> int:
    """Calculate quantity of treats needed."""
    return 1.5 * tea_bags(people=people) // 1  # type: ignore


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of the tea party."""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
