
# Esse projeto foi concebido para o bootcamp python Santander 2023

## Consiste em utilizar as bibliotecas do python para criar um ETL, que recupera dados de clientes e com base em suas caracteristicas utiliza uma API da OpenIA, para fazer uma sugestão de investimentos que é salva através da API no banco de dados, para futuro envio aos clientes

### Um exemplo do uso da API

Dados do cliente:

~~~json
{
"idCliente": 8,
"nome": "Alvaro dos Anjos",
"profissao": "Ministro do STF",
"idade": 62,
"rendaMensal": 45000,
"patrimonio": 8000000,
"estadoCivil": "Casado",
"valorAInvestir": 2500000,
"objetivoInvestimento": "Obter renda mensal na aposentadoria",
"horizonteInvestimentoEmAnos": 10,
"investimentosSugeridos": []
}
~~~

**Mensagem enviada para a API da OpenIA:**

Redija uma mensagem sugerindo um investimento do banco Santander para o cliente Alvaro dos Anjos que trabalha como Ministro do STF tem renda mensal de 45000.0 e patrimônio de 8000000.0 para o valor de R$ 2500000.0 durante 10.0 anos , ele é Casado e pretente Obter renda mensal na aposentadoria.a resposta deve ter no máximo 300 caracteres



### O resultado

~~~json
{
    "idCliente": 8,
    "nome": "Alvaro dos Anjos",
    "profissao": "Ministro do STF",
    "idade": 62,
    "rendaMensal": 45000.0,
    "patrimonio": 8000000.0,
    "estadoCivil": "Casado",
    "valorAInvestir": 2500000.0,
    "objetivoInvestimento": "Obter renda mensal na aposentadoria",
    "horizonteInvestimentoEmAnos": 10.0,
    "investimentosSugeridos": [
      {
        "invetimentoSugerido": "Caro Sr. Álvaro, sugiro aplicar R$2.500.000,00 em LCI do Santander com prazo de 10 anos. Ótima opção 
para diversificar e garantir renda na aposentadoria. Contate-nos.",
        "idSugestaoInvestimento": 2
      }
    ]
  }
~~~

## O Resultado para uma consulta para a base de 8 clientes

~~~Json
[
  {
    "idCliente": 1,
    "nome": "Marcelo Diniz Almeida",
    "profissao": "Analista de Sistemas",
    "idade": 31,
    "rendaMensal": 10000,
    "patrimonio": 350000,
    "estadoCivil": "Casado",
    "valorAInvestir": 35000,
    "objetivoInvestimento": "Adiquirir um carro",
    "horizonteInvestimentoEmAnos": 5,
    "investimentosSugeridos": [
      {
        "invetimentoSugerido": "Sugiro a Marcelo investir no CDB do Santander com rentabilidade atrelada ao CDI, que oferece liquidez diária, é seguro e tem baixo risco. Adequado para o objetivo de adquirir um carro em 5 anos.",
        "idSugestaoInvestimento": 1
      },
      {
        "invetimentoSugerido": "Olá Marcelo, sugerimos o CDB Santander com liquidez no vencimento de 5 anos, com rendimento acima de 100% do CDI. É ideal para o seu plano de adquirir um carro, aliando rentabilidade e segurança.",
        "idSugestaoInvestimento": 3
      },
      {
        "invetimentoSugerido": "Prezado Marcelo, sugiro o investimento no CDB do Santander, com um prazo de 5 anos. Além de alta rentabilidade, oferece liquidez no vencimento. Ideal para seu objetivo de adquirir um carro.",
        "idSugestaoInvestimento": 4
      }
    ]
  },
  {
    "idCliente": 2,
    "nome": "Evandro Souza de Melo",
    "profissao": "Artista Plástico",
    "idade": 55,
    "rendaMensal": 55000,
    "patrimonio": 8000000,
    "estadoCivil": "divorciado",
    "valorAInvestir": 2000000,
    "objetivoInvestimento": "Aquisição de Chácara",
    "horizonteInvestimentoEmAnos": 10,
    "investimentosSugeridos": [
      {
        "invetimentoSugerido": "Caro Sr. Evandro, sugiro o investimento em nosso fundo imobiliário Santander Renda Imobiliária FI. Com rendimentos consistentes e baixo risco, será perfeito para a aquisição de sua chácara em 10 anos.",
        "idSugestaoInvestimento": 5
      }
    ]
  },
  {
    "idCliente": 3,
    "nome": "Jonas Negromonte de Araujo",
    "profissao": "Contador Pessoa Jurídica",
    "idade": 37,
    "rendaMensal": 10000,
    "patrimonio": 400000,
    "estadoCivil": "Casado",
    "valorAInvestir": 20000,
    "objetivoInvestimento": "Custear faculdade dos Filhos",
    "horizonteInvestimentoEmAnos": 10,
    "investimentosSugeridos": [
      {
        "invetimentoSugerido": "Olá Sr. Jonas, o Santander sugere o investimento em um CDB de longo prazo. Excelente para aumentar seu patrimônio com segurança, ideal para futuros gastos com a faculdade dos seus filhos.",
        "idSugestaoInvestimento": 6
      }
    ]
  },
  {
    "idCliente": 4,
    "nome": "Carlos Miragaia Ferreira",
    "profissao": "bancário",
    "idade": 42,
    "rendaMensal": 13000,
    "patrimonio": 1200000,
    "estadoCivil": "solteiro",
    "valorAInvestir": 300000,
    "objetivoInvestimento": "Iniciar um negócio para renda",
    "horizonteInvestimentoEmAnos": 12,
    "investimentosSugeridos": [
      {
        "invetimentoSugerido": "Olá Carlos, sugiro para você o investimento em CDB do Santander. O prazo de 12 anos é favorável e pode gerar rendimentos expressivos, fornecendo capital para iniciar seu negócio futuro.",
        "idSugestaoInvestimento": 7
      }
    ]
  },
  {
    "idCliente": 5,
    "nome": "João dos Santos Menegueli",
    "profissao": "Motorista de Ônibus",
    "idade": 25,
    "rendaMensal": 6000,
    "patrimonio": 70000,
    "estadoCivil": "Casado",
    "valorAInvestir": 10000,
    "objetivoInvestimento": "custear faculdade para o filho",
    "horizonteInvestimentoEmAnos": 15,
    "investimentosSugeridos": [
      {
        "invetimentoSugerido": "Olá Sr. João, sugerimos o investimento no CDB do Santander. Ele tem ótimos retornos, garantia do FGC e contribuirá para o fundo de faculdade do seu filho. Garanta o futuro dele!",
        "idSugestaoInvestimento": 8
      }
    ]
  },
  {
    "idCliente": 6,
    "nome": "Rodolfo Adamantes",
    "profissao": "Dentista",
    "idade": 45,
    "rendaMensal": 18000,
    "patrimonio": 2500000,
    "estadoCivil": "Casado",
    "valorAInvestir": 30000,
    "objetivoInvestimento": "Fazer viagem internacional",
    "horizonteInvestimentoEmAnos": 2,
    "investimentosSugeridos": [
      {
        "invetimentoSugerido": "Olá, Dr. Rodolfo. Sugiro nossa aplicação em CDB do Santander. É um investimento seguro, com rendimento acima da poupança e permite resgate após 2 anos, adequado para sua viagem.",
        "idSugestaoInvestimento": 9
      }
    ]
  },
  {
    "idCliente": 7,
    "nome": "Ivo de Souza Lira",
    "profissao": "Aposentado",
    "idade": 65,
    "rendaMensal": 5000,
    "patrimonio": 500000,
    "estadoCivil": "casado",
    "valorAInvestir": 15000,
    "objetivoInvestimento": "Realizar uma viagem para comemorar 30 anos de casado",
    "horizonteInvestimentoEmAnos": 3,
    "investimentosSugeridos": [
      {
        "invetimentoSugerido": "Olá Sr. Ivo, sugerimos o CDB do Santander com liquidez no vencimento de 3 anos. Com boa rentabilidade e segurança, será ideal para o seu plano de viagem de 30 anos de casado.",
        "idSugestaoInvestimento": 10
      }
    ]
  },
  {
    "idCliente": 8,
    "nome": "Alvaro dos Anjos",
    "profissao": "Ministro do STF",
    "idade": 62,
    "rendaMensal": 45000,
    "patrimonio": 8000000,
    "estadoCivil": "Casado",
    "valorAInvestir": 2500000,
    "objetivoInvestimento": "Obter renda mensal na aposentadoria",
    "horizonteInvestimentoEmAnos": 10,
    "investimentosSugeridos": [
      {
        "invetimentoSugerido": "Caro Sr. Álvaro, sugiro aplicar R$2.500.000,00 em LCI do Santander com prazo de 10 anos. Ótima opção para diversificar e garantir renda na aposentadoria. Contate-nos.",
        "idSugestaoInvestimento": 2
      },
      {
        "invetimentoSugerido": "Olá Alvaro, com base nos dados fornecidos, sugiro o investimento em CDB do Santander, considerando a solidez, segurança, rentabilidade e o prazo de 10 anos. Com o objetivo de gerar uma renda mensal na aposentadoria, esse pode ser um bom caminho.",
        "idSugestaoInvestimento": 11
      }
    ]
  }
]
~~~

