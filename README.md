<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/Loja-Desconto%20Progressivo-00A86B?style=for-the-badge&logo=shopping-cart&logoColor=white" alt="Loja">
</p>

<h1 align="center">🛒 Sistema de Desconto Progressivo</h1>

<p align="center">
  Uma aplicação simples em Python para calcular descontos progressivos em compras de loja online.
</p>

## 📌 Sobre o projeto

O **Sistema de Desconto Progressivo** foi desenvolvido para aplicar descontos de acordo com o valor total da compra. O programa solicita o valor da compra e calcula automaticamente o desconto aplicavel, exibindo o valor original, o valor descontado e o valor final a ser pago.

O projeto foi criado para praticar entrada de dados, estrutura condicional (if/elif/else), operações matemá­ticas e exibiçã­o de resultados em Python. 🐍

## 🎯 Objetivo do sistema

- Aplicar descontos progressivos conforme o valor da compra.
- Calcular o valor do desconto e o valor final a ser pago.
- Exibir os resultados de forma clara e formatada.
- Praticar conceitos fundamentais de programação em Python.

## 🛠️ Linguagem utilizada

- **Python 3.x**

## 🧮 Regras de desconto

O desconto é aplicado de acordo com o valor total da compra:

| Valor da Compra           | Desconto |
|---------------------------|----------|
| < R$ 200,00               | 5%       |
| ≥ R$ 200,00 e < R$ 300,00 | 10%      |
| ≥ R$ 300,00               | 15%      |

O cálculo do valor final é realizado da seguinte forma:

```text
valor_final = valor - (valor × desconto)
```

Onde:

- **Valor** é o valor total da compra informado pelo usuário.
- **Desconto** é a porcentagem aplicavel conforme a faixa de valor.

## ▶️ Como executar

### Pré-requisitos

- Ter o [Python](https://www.python.org/downloads/) 3.x instalado.
- Ter acesso a um terminal ou ao Visual Studio Code.

### Execuçã­o pelo terminal

1. Clone o repositório:

```bash
git clone https://github.com/Prada-07/desconto-progressivo.git
```

2. Acesse a pasta do projeto:

```bash
cd desconto-progressivo
```

3. Execute o programa:

```bash
python desconto_progressivo.py
```

4. Informe o valor da compra em reais.

## 💻 Exemplo de resultado

```text
Digite o valor da compra:
-> 250
VALOR DA COMPRA: R$250.00
DESCONTO: R$25.00
VALOR FINAL: R$225.00
```

## 📁 Estrutura do projeto

```text
desconto-progressivo/
├── desconto_progressivo.py   # Código principal do sistema de desconto
└── README.md                 # Documentaçã­o do projeto
```

## ℹ️ Observação

O programa aceita apenas valores numé­ricos. Caso o usuário informe um valor inválido, o sistema exibe uma mensagem de erro e encerra a execuçã­o.

## 👤 Autor

Desenvolvido por **Leonardo Prada**.

[![GitHub](https://img.shields.io/badge/Leonardo%20Prada-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Prada-07)

---

<p align="center">🛒 Projeto desenvolvido para fins educacionais.</p>
