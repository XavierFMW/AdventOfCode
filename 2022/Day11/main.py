from monkeys import MONKEYS


ROUNDS = 10000


if __name__ == "__main__":
    for _ in range(ROUNDS):
        for monkey in MONKEYS:
            monkey.take_turn()

    inspected = tuple(m.inspected for m in sorted(MONKEYS, key=lambda m: m.inspected))
    print(inspected[-1] * inspected[-2])
