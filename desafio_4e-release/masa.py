def kilogramos_gramos(kilos):
    formula = kilos * 1000
    return f"El resultado es {formula}"

def toneladas_gramos(toneladas):
    formula = toneladas * 1000000
    return f"El resultado es {formula}"


if __name__ == '__main__':
    kilo = 20
    tonelada = 20
    print(kilogramos_gramos(kilo))
    print(toneladas_gramos(tonelada))