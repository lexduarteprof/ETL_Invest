import pandas as pd
import requests 
import json
import openai


df = pd.read_csv('Clientes.csv')

clientes_id = df['idcliente'].tolist()

print(clientes_id)

url_base = 'http://localhost:8080'

def getCliente (id):
    response = requests.get(f'{url_base}/cliente/{id}')

    return response.json() if response.status_code == 200 else None

clientes = [cliente for id in clientes_id if (cliente := getCliente(id)) is not None]

#print(json.dumps(clientes , indent=2, ensure_ascii=False))

openIA_apk_key = '---------'

openai.api_key = openIA_apk_key

def mensagem(cliente):
    
    msg = f"Redija uma mensagem sugerindo um investimento do banco Santander para o cliente {cliente['nome']} que trabalha como " \
    + f"{cliente['profissao']} tem renda mensal de {cliente['rendaMensal']} e patrimônio de " \
    + f"{cliente['patrimonio']} " \
    + f"para o valor de R$ {cliente['valorAInvestir']} durante {cliente['horizonteInvestimentoEmAnos']} anos " \
    + f", ele é {cliente['estadoCivil']} e pretente " \
    + f"{cliente['objetivoInvestimento']}." \
    + 'a resposta deve ter no máximo 300 caracteres' 

    return(msg)

for cliente in clientes:
    print(mensagem(cliente))


def genareteSugestaoInvestimento (cliente):
        
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
            "role": "system",
            "content": "Você é um especialista em Investimentos no Brasil."
            },
            {
                "role": "user",
                "content": mensagem(cliente)
            },
        ]
        )
    return completion.choices[0].message.content


        
def updatesujetaocliente(cliente):
    response = requests.post(f'{url_base}/investimentossugeridos/incluirInvestimento', json=cliente)
    return True if response.status_code == 200 else False

    

clienteupdated = {}
    
for cliente in clientes:
    sugestao = genareteSugestaoInvestimento(cliente)
    
    print(sugestao)
    
    clienteupdated["cliente"] = cliente
    clienteupdated["invetimentoSugerido"] = sugestao
    updatesujetaocliente(clienteupdated)
    
    clienteupdated = {}
    

clientes = [cliente for id in clientes_id if (cliente := getCliente(id)) is not None]

print(json.dumps(clientes , indent=2, ensure_ascii=False))



