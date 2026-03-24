from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print("Conectado ao servidor.")
print("Operacoes disponiveis: upper, lower, alternate")
print("Formato: operacao:texto")
print("Digite 'exit' para sair.\n")

while True:
    message = input(">> ")

    if message.strip().lower() == 'exit':
        break

    s.send(message.encode())
    data = s.recv(1024)
    print("Resposta: " + data.decode() + "\n")

s.close()
print("Conexao encerrada.")
