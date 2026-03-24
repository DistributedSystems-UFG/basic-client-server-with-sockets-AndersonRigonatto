from socket import *
from constCS import *

def process_request(data):
    message = data.decode()

    if ':' not in message:
        return "Formato invalido. Use: upper|lower|alternate:texto"

    operation, text = message.split(':', 1)
    operation = operation.strip().lower()

    if operation == 'upper':
        result = text.upper()
    elif operation == 'lower':
        result = text.lower()
    elif operation == 'alternate':
        result = ''
        for i, char in enumerate(text):
            if i % 2 == 0:
                result += char.upper()
            else:
                result += char.lower()
    else:
        result = "Operacao desconhecida: " + operation + ". Use: upper, lower ou alternate"

    return result

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("Servidor aguardando conexao em " + HOST + ":" + str(PORT))

(conn, addr) = s.accept()
print("Cliente conectado: " + str(addr))

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Recebido: " + data.decode())
    result = process_request(data)
    print("Resposta: " + result)
    conn.send(result.encode())

conn.close()
print("Conexao encerrada.")
