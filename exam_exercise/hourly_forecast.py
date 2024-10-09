def forecast(*args):
    dict_with_weather = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    for city, weather in args:
        dict_with_weather[weather].append(city)

    result = []
    for k, v in dict_with_weather.items():
        for c in sorted(v):
            result.append(f"{c} - {k}")

    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
