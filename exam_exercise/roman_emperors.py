def list_roman_emperors(*args, **kwargs):
    result = [f"Total number of emperors: {len(args)}"]
    emperors = {"Successful emperors": {},
                "Unsuccessful emperors": {}}

    for name, status in args:
        if status is True:
            emperors["Successful emperors"][name] = kwargs[name]
        else:
            emperors["Unsuccessful emperors"][name] = kwargs[name]

    for k, v in emperors.items():
        if len(v) > 0:
            result.append(f"{k}:")
            if k == "Successful emperors":
                [result.append(f"****{e}: {y}") for e, y in sorted(v.items(), key=lambda x: (-x[1], x[0]))]
            else:
                [result.append(f"****{e}: {y}") for e, y in sorted(v.items(), key=lambda x: (x[1], x[0]))]

    return "\n".join(result)


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))
