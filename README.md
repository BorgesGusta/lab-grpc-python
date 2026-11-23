# lab-grpc-python

Repositório de experimentos práticos sobre **RPC (Remote Procedure Call)** utilizando Python, explorando desde implementações nativas até o protocolo gRPC com Protocol Buffers.

## 📁 Experimentos

* **[`01-xml-rpc-basico/`](./01-xml-rpc-basico)**: Comunicação cliente-servidor simples utilizando o módulo nativo `xmlrpc` do Python (tráfego em XML sobre HTTP).
* **[`02-grpc-unary/`](./02-grpc-unary)**: Chamada de procedimento remoto padrão (Unary RPC) utilizando gRPC e serialização binária com Protocol Buffers (`.proto`).

## 🚀 Como Executar

### 1. Prepare o ambiente (na raiz do projeto)
```bash
git clone https://github.com
cd lab-grpc-python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Rode qualquer experimento
Abra **dois terminais** (ambos com o `venv` ativado), entre na pasta do experimento desejado e execute o servidor primeiro e depois o cliente:

```bash
# Terminal 1
cd 02-grpc-unary
python3 servidor.py

# Terminal 2
cd 02-grpc-unary
python3 cliente.py
```

* **[`03-grpc-streaming/`](./03-grpc-streaming)**: Server Streaming RPC, onde o cliente faz uma requisição e recebe um fluxo contínuo de atualizações em tempo real.
