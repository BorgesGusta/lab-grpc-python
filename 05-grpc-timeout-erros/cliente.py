import grpc
import calculadora_pb2
import calculadora_pb2_grpc

with grpc.insecure_channel('localhost:50054') as channel:
    stub = calculadora_pb2_grpc.CalculadoraStub(channel)
    try:
        print("Enviando requisição com limite de 2 segundos...")
        resposta = stub.Somar(
            calculadora_pb2.NumerosRequest(a=10, b=20),
            timeout=2.0
        )
        print(f"Sucesso: {resposta.resultado}")
    except grpc.RpcError as e:
        print(f"Chamada abortada pelo cliente! Código: {e.code()} | Detalhe: {e.details()}")
