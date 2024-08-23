elementos = {
  'H': (1, 'Hidrogênio', 1.008),
  'He': (2, 'Hélio', 4.0026),
  'Li': (3, 'Lítio', 6.94),
  'Be': (4, 'Berílio', 9.0122),
  'B': (5, 'Boro', 10.81),
  'C': (6, 'Carbono', 12.011),
  'N': (7, 'Nitrogênio', 14.007),
  'O': (8, 'Oxigênio', 15.999),
  'F': (9, 'Flúor', 18.998),
  'Ne': (10, 'Neônio', 20.180)
}

def mostrar_elemento(sigla):
  if sigla in elementos:
      numero_atomico, nome, massa = elementos[sigla]
      print(f"Sigla: {sigla}")
      print(f"Número Atômico: {numero_atomico}")
      print(f"Nome: {nome}")
      print(f"Massa: {massa} g/mol")
  else:
      print("Elemento não encontrado.")

sigla = input("Digite a sigla do elemento químico (ex: H, He): ")
mostrar_elemento(sigla)