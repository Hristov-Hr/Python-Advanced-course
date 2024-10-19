def draw_cards(*args, **kwargs):
    cards = {"monster": [], "spell": []}

    for k, v in args:
        cards[v].append(k)
    for k, v in kwargs.items():
        cards[v].append(k)

    result = []
    if len(cards["monster"]) > 0:
        result.append("Monster cards:")
        [result.append(f"  ***{monster}") for monster in sorted(cards["monster"], reverse=True)]
    if len(cards["spell"]) > 0:
        result.append("Spell cards:")
        [result.append(f"  $$${spell}") for spell in sorted(cards["spell"])]

    return "\n".join(result)


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
