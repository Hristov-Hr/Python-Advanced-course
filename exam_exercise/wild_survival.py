from collections import deque


def fight(bee, eaters):
    if bee >= eaters * 7:
        bee -= eaters * 7
        eaters = 0
    else:
        eaters -= bee // 7
        bee = 0
    return bee, eaters


beehive = deque(int(x) for x in input().split())
bee_eaters = [int(x) for x in input().split()]

while beehive and bee_eaters:

    bee_group, bee_eaters_group = fight(beehive.popleft(), bee_eaters.pop())
    beehive.append(bee_group) if bee_group else None
    bee_eaters.append(bee_eaters_group) if bee_eaters_group else None

print("The final battle is over!")
if not beehive and not bee_eaters:
    print("But no one made it out alive!")
else:
    winner = ', '.join(str(x) for x in beehive) if beehive else ', '.join(str(x) for x in bee_eaters)
    print(f"{'Bee' if beehive else 'Bee-eater'} groups left: {winner}")
