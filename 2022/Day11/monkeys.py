from monkey import Monkey


monkey_0 = Monkey(
    (72, 64, 51, 57, 93, 97, 68),
    lambda i: i*19,
    lambda i: i % 17 == 0,
)
monkey_1 = Monkey(
    (62,),
    lambda i: i*11,
    lambda i: i % 3 == 0,
)
monkey_2 = Monkey(
    (57, 94, 69, 79, 72),
    lambda i: i+6,
    lambda i: i % 19 == 0,
)
monkey_3 = Monkey(
    (80, 64, 92, 93, 64, 56),
    lambda i: i+5,
    lambda i: i % 7 == 0,
)
monkey_4 = Monkey(
    (70, 88, 95, 99, 78, 72, 65, 94),
    lambda i: i+7,
    lambda i: i % 2 == 0,
)
monkey_5 = Monkey(
    (57, 95, 81, 61),
    lambda i: i*i,
    lambda i: i % 5 == 0,
)
monkey_6 = Monkey(
    (79, 99),
    lambda i: i+2,
    lambda i: i % 11 == 0,
)
monkey_7 = Monkey(
    (68, 98, 62),
    lambda i: i+3,
    lambda i: i % 13 == 0,
)

monkey_0.set_partners(monkey_4, monkey_7)
monkey_1.set_partners(monkey_3, monkey_2)
monkey_2.set_partners(monkey_0, monkey_4)
monkey_3.set_partners(monkey_2, monkey_0)
monkey_4.set_partners(monkey_7, monkey_5)
monkey_5.set_partners(monkey_1, monkey_6)
monkey_6.set_partners(monkey_3, monkey_1)
monkey_7.set_partners(monkey_5, monkey_6)

MONKEYS = (
    monkey_0,
    monkey_1,
    monkey_2,
    monkey_3,
    monkey_4,
    monkey_5,
    monkey_6,
    monkey_7,
)
