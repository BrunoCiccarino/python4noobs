nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))


MEDIA = ((nota1 * 3.5) + (nota2 * 7.5)) / 11

if MEDIA >= 6:
    print(f"Aluno aprovado MEDIA = {MEDIA:.5f}".format(MEDIA))

else:
    print("Aluno reprovado!")