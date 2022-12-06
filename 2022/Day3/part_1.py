
INPUT = "input.txt"


def get_item_priority(item):
    try:
        if item.isupper():
            return ord(item) - 38
        else:
            return ord(item) - 96

    except TypeError:
        msg = "Invalid item type"
        raise TypeError(msg)


def get_duplicate_item_sum(items):
    pivot = len(items) // 2
    first, second = set(items[:pivot]), set(items[pivot:])
    duplicates = first & second
    return sum(
        get_item_priority(i) for i in duplicates
    )


def check_rucksacks(path_in):
    duplicate_sum = 0
    with open(path_in, "r") as rucksacks:

        for line in rucksacks.readlines():
            rucksack = line.strip()
            if rucksack:
                duplicate_sum += get_duplicate_item_sum(rucksack)

    return duplicate_sum


if __name__ == "__main__":
    print(check_rucksacks(INPUT))
