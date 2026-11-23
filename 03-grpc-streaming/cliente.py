import grpc
import monitor_pb2
import monitor_pb2_grpc

with grpc.insecure_channel('localhost:50052') as channel:
    stub = monitor_pb2_grpc.MonitorStub(channel)
    respostas = stub.AcompanharProcessamento(
        monitor_pb2.TarefaRequest(nome_tarefa="Relatório Mensal")
    )
    for status in respostas:
        print(f"[{status.progresso}%] {status.mensagem}")
