from concurrent import futures
import grpc
import calculadora_pb2
import calculadora_pb2_grpc

class CalculadoraServicer(calculadora_pb2_grpc.CalculadoraServicer):
    def Somar(self, request, context):
        print(f"Chamada gRPC recebida: {request.a} + {request.b}")
        return calculadora_pb2.ResultadoResponse(resultado=request.a + request.b)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
calculadora_pb2_grpc.add_CalculadoraServicer_to_server(CalculadoraServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("Servidor gRPC rodando na porta 50051...")
server.wait_for_termination()
