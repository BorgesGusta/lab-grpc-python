from concurrent import futures
import time
import grpc
import calculadora_pb2
import calculadora_pb2_grpc

class CalculadoraLentaServicer(calculadora_pb2_grpc.CalculadoraServicer):
    def Somar(self, request, context):
        print(f"Processando soma pesada: {request.a} + {request.b} (aguarde 4s)...")
        time.sleep(4)
        return calculadora_pb2.ResultadoResponse(resultado=request.a + request.b)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
calculadora_pb2_grpc.add_CalculadoraServicer_to_server(CalculadoraLentaServicer(), server)
server.add_insecure_port('[::]:50054')
server.start()
print("Servidor gRPC Lento rodando na porta 50054...")
server.wait_for_termination()
