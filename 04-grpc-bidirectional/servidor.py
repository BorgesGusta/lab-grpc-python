from concurrent import futures
import grpc
import chat_pb2
import chat_pb2_grpc

class ChatServicer(chat_pb2_grpc.ChatServicer):
    def Conversar(self, request_iterator, context):
        for msg in request_iterator:
            print(f"[{msg.usuario}]: {msg.texto}")
            yield chat_pb2.Mensagem(
                usuario="Servidor",
                texto=f"Recebi sua mensagem: '{msg.texto}'"
            )

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
chat_pb2_grpc.add_ChatServicer_to_server(ChatServicer(), server)
server.add_insecure_port('[::]:50053')
server.start()
print("Servidor gRPC Bidirectional rodando na porta 50053...")
server.wait_for_termination()
