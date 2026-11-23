import grpc
import chat_pb2
import chat_pb2_grpc

def gerar_mensagens():
    while True:
        texto = input("Você (digite 'sair' para encerrar): ")
        if texto.lower() == 'sair':
            break
        yield chat_pb2.Mensagem(usuario="Gustavo", texto=texto)

with grpc.insecure_channel('localhost:50053') as channel:
    stub = chat_pb2_grpc.ChatStub(channel)
    respostas = stub.Conversar(gerar_mensagens())
    for resposta in respostas:
        print(f"-> [{resposta.usuario}]: {resposta.texto}\n")
