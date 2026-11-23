from concurrent import futures
import time
import grpc
import monitor_pb2
import monitor_pb2_grpc

class MonitorServicer(monitor_pb2_grpc.MonitorServicer):
    def AcompanharProcessamento(self, request, context):
        print(f"Iniciando tarefa remota: {request.nome_tarefa}")
        etapas = [
            (25, "Carregando dados..."),
            (50, "Processando cálculos..."),
            (75, "Validando resultados..."),
            (100, "Tarefa concluída com sucesso!")
        ]
        for progresso, msg in etapas:
            time.sleep(1)  # Simula tempo de processamento
            yield monitor_pb2.StatusResponse(progresso=progresso, mensagem=msg)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
monitor_pb2_grpc.add_MonitorServicer_to_server(MonitorServicer(), server)
server.add_insecure_port('[::]:50052')
server.start()
print("Servidor gRPC Streaming rodando na porta 50052...")
server.wait_for_termination()
