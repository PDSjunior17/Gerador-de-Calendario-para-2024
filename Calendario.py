import calendar
import datetime
def menu():
    print("\nDigite a opcao para qual mes do ano de 2024 voce quer saber:")
    print("    1.Janeiro       5.Maio        9.Setembro")
    print("    2.Fevereiro     6.Junho       10.Outubro")
    print("    3.Marco         7.Julho       11.Novembro")
    print("    4.Abril         8.Agosto      12.Dezembro")

menu()
print("")
opcao1 = 1
while 1:
    opcao = float(input())
    if opcao > 0 and opcao < 13:
        opcao1 = int(opcao)
        break

data = datetime.date.today()
ano = 2024
mes = opcao1
print(calendar.month(ano,mes))








