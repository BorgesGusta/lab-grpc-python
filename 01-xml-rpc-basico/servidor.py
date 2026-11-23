from xmlrpc.server import SimpleXMLRPCServer

def somar(a, b):
    print(f"Requisição recebida: somar {a} + {b}")
    return a + b

server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC escutando na porta 8000...")
server.register_function(somar, "somar")
server.serve_forever()
