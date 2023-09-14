def celsius_fahrenheit(celsius):
    formula = (celsius * 9/5) + 32
    return f"El resultado es {formula}"


def celsius_kelvin(celsius):
    formula = celsius + 273.15

    return f"El resultado es {formula}"


if __name__ == '__main__':
    celsius = 10
    print(celsius_fahrenheit(celsius))
    print(celsius_kelvin(celsius))
    