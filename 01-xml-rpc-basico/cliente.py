import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
resultado = proxy.somar(15, 27)
print(f"Resultado retornado pelo servidor: {resultado}")
