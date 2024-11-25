# **Airflow ETL com Jupyter Notebook e MySQL**

Este projeto implementa um processo básico de ETL utilizando o Apache Airflow, com integração ao MySQL e suporte para análises no Jupyter Notebook. Siga as instruções abaixo para configurar e executar o ambiente.

---

## **Como Startar o Ambiente**

### **1. Pré-requisitos**
Certifique-se de ter as ferramentas abaixo instaladas em sua máquina:

- **Docker**
- **Docker Compose**

### **2. Passos para Iniciar o Ambiente**

#### **Acesse a Pasta do Projeto**
Abra o terminal (ou prompt de comando) como administrador e entre na pasta onde o arquivo `docker-compose.yml` está localizado:
cd /caminho/para/sua/pasta/airflow-docker


Execute o comando abaixo para subir os serviços configurados no Docker Compose:
```` bash 
docker-compose up -d
````


Verifique o Status dos Containers (precisa estar up)
``` bash
docker ps
```

Entre em:
http://localhost:8080 
