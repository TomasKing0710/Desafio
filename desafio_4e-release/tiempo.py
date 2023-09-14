def minutos_segundos(minutos):
    formula = minutos * 60
    return f"El resultado es {formula}"

def horas_minutos(horas):
    formula = horas * 60

    return f"El resultado es {formula}"

if __name__ == '__main__':
  minutos = 2
  horas = 2
  print(minutos_segundos(minutos))
  print(horas_minutos(horas))
