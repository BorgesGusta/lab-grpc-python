# lab-grpc-python

Este repositório contém um experimento prático de **RPC (Remote Procedure Call)** utilizando **Python** e **gRPC** com **Protocol Buffers**. O objetivo é demonstrar a comunicação cliente-servidor através da invocação de métodos remotos.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **gRPC (`grpcio`)**
* **Protocol Buffers (`grpcio-tools`)**

## 📁 Estrutura do Projeto

* `calculadora.proto`: Contrato da interface RPC definindo o serviço `Calculadora` e as mensagens de requisição/resposta.
* `calculadora_pb2.py` & `calculadora_pb2_grpc.py`: Código gerado automaticamente pelo compilador `protoc` a partir do arquivo `.proto`.
* `servidor.py`: Implementação do servidor gRPC que escuta na porta `50051`.
* `cliente.py`: Cliente gRPC que envia parâmetros e recebe o resultado processado remotamente.

## 🚀 Como Executar o Projeto

### 1. Clone o repositório e acesse a pasta
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd lab-grpc-python
```

### 2. Crie e ative o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. (Opcional) Recompile o arquivo `.proto`
Caso faça alterações no contrato `calculadora.proto`, gere os arquivos novamente:
```bash
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto
```

### 5. Inicie o Servidor (Terminal 1)
```bash
python3 servidor.py
```

### 6. Execute o Cliente (Terminal 2)
Em uma nova aba do terminal (com o ambiente virtual ativado):
```bash
python3 cliente.py
```

## 📊 Resultado Esperado

* **Terminal do Servidor:** `Chamada gRPC recebida: 40 + 60`
* **Terminal do Cliente:** `Resposta recebida via gRPC: 100`
