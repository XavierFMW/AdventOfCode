
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


def get_shared_items(bunches):
    sets = [set(b) for b in bunches]
    duplicates = sets[0]
    for s in sets[1:]:
        duplicates &= s
    return list(duplicates)


def get_badge_sum(rucksacks):
    badge_sum = 0
    group = []

    for line in rucksacks.readlines():
        rucksack = line.strip()
        if rucksack:

            group.append(rucksack)
            if len(group) >= 3:
                badge = get_shared_items(group)[0]
                badge_sum += get_item_priority(badge)
                group.clear()

    return badge_sum


def check_rucksacks(path_in):
    with open(path_in, "r") as rucksacks:
        return get_badge_sum(rucksacks)


if __name__ == "__main__":
    print(check_rucksacks(INPUT))
