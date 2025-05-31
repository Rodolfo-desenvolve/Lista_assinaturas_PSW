# 📌 Projeto de Gerenciamento de Assinaturas e Pagamentos #

## 🚀 1. Configuração do Ambiente Virtual ##

Antes de iniciar o projeto, é fundamental criar e ativar um ambiente virtual para gerenciar as dependências de forma isolada. Siga os passos abaixo:

## 1️⃣ Criar o ambiente virtual: ##

``` python -m venv venv ```

## 2️⃣ Ativar o ambiente virtual: ##

Windows:
``` venv\Scripts\activate ```

Mac/Linux:
``` source venv/bin/activate ```

## 3️⃣ Instalar as dependências necessárias: ##

``` pip install sqlmodel matplotlib ```

<hr>

## 🏗 2. Inicialização do Banco de Dados ##

Após configurar o ambiente virtual e instalar as dependências, é necessário criar o banco de dados e suas tabelas. Para isso, execute o seguinte comando:

``` python models/deta_base.py ```

Isso criará automaticamente o arquivo ```database.db```, onde os dados das assinaturas e pagamentos serão armazenados.

<hr>

## 📂 3. Estrutura do Projeto ##

Este projeto possui três principais diretórios:

**models/ →** Define os modelos do banco de dados e configura a conexão com SQLite.

**views/ →** Contém a lógica principal para gerenciar assinaturas e pagamentos.

**templates/ →** Possui a interface do usuário, permitindo a interação com o sistema.

## 📁 Estrutura Completa: ##

```
/meu_projeto

│──── models/

│   ├──── deta_base.py   # Configuração do banco de dados

│   ├──── model.py       # Modelos das tabelas

│──── templates/         # Estrutura do projeto

│   ├──── __init__.py    # Configuração de caminhos para importação de módulos

│   ├──── app.py         # Interface do usuário para interação com assinaturas

│──── views/             # Lógica de funcionamento

│   ├──── __init__.py    # Configuração de caminhos para importação de módulos

│   ├──── view.py        # Serviço responsável por assinaturas e pagamentos

│──── venv/              # Ambiente virtual

│──── database.db        # Arquivo do banco de dados
```

<hr>


## 🚀 4. Como Executar o Sistema ##

Depois de inicializar o banco, execute o arquivo ```app.py``` para interagir com o sistema:

``` python templates/app.py ``` 

Isso ativará um menu no terminal, permitindo que o usuário gerencie assinaturas e pagamentos.

<hr>

## 🎯 5. Exemplo Prático de Uso ##

Abaixo está um exemplo real de interação com o sistema:

## 1️⃣ O programa inicia com um menu no terminal: ##

``` [1] -> Adicionar assinatura
[2] -> Remover assinatura
[3] -> Valor total
[4] -> Gastos últimos 12 meses
[5] -> Sair
Escolha uma opção: 1
 ```

## 2️⃣ Adicionando uma assinatura: ##

```
Empresa: Netflix
Site: www.netflix.com
Data de assinatura: 15/03/2024
Valor: 39.90
Assinatura adicionada com sucesso!
```

## 3️⃣ Consultando o valor total mensal das assinaturas: ##

```
[1] -> Adicionar assinatura
[2] -> Remover assinatura
[3] -> Valor total
[4] -> Gastos últimos 12 meses
[5] -> Sair
Escolha uma opção: 3
Seu valor total mensal em assinatura é: 39.90
```

## 4️⃣ Gerando gráfico dos gastos nos últimos 12 meses: ##

```
[1] -> Adicionar assinatura
[2] -> Remover assinatura
[3] -> Valor total
[4] -> Gastos últimos 12 meses
[5] -> Sair
Escolha uma opção: 4
(Grafico exibido mostrando os valores pagos em cada mês)
```
## 5️⃣ Removendo uma assinatura: ##

```
[1] -> Adicionar assinatura
[2] -> Remover assinatura
[3] -> Valor total
[4] -> Gastos últimos 12 meses
[5] -> Sair
Escolha uma opção: 2

Escolha qual assinatura deseja excluir:
1 -> Netflix
Escolha a assinatura: 1
Assinatura excluída com sucesso.

```
**📜 6. Licença**
Este projeto está disponível sob a licença **MIT**.


