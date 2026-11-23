import grpc
import calculadora_pb2
import calculadora_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = calculadora_pb2_grpc.CalculadoraStub(channel)
    resposta = stub.Somar(calculadora_pb2.NumerosRequest(a=40, b=60))
    print(f"Resposta recebida via gRPC: {resposta.resultado}")
