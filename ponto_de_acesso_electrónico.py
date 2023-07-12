identidade=input("qual é o número do seu bilhete?")
resultado=identidade.strip()
base_de_dados={
  "04965392LA041":
  {
  "nome":"Elsira Eduardo",
  "cursos":["Pythonolvimento","Desenvolmimento Web"],
  "computador": "Mediateca"
  }
}
aluna=base_de_dados.get(resultado)
if aluna:
    print("Aluna foi encontrada com sucesso!")
      
else:
    print(" O bilhete não corresponde a nenhuma aluna")
