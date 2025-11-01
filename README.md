# 🏦 BankSystem - Projeto de Automação RPA

Este projeto implementa um *robô RPA (Robotic Process Automation)* desenvolvido em *Python com BotCity*, responsável por automatizar operações em um sistema bancário local.  
O objetivo é ler dados de extratos em planilhas Excel e realizar lançamentos automáticos (débito e crédito) diretamente no aplicativo desktop do banco.

---

## 🧠 Visão Geral

O *BankSystem Bot* foi projetado para:

- Ler automaticamente um extrato bancário em formato Excel.  
- Abrir o sistema bancário local (.exe).  
- Preencher campos como descrição, valor e tipo de operação.  
- Verificar se a transação é *débito* ou *crédito* e clicar no botão correspondente.  
- Repetir o processo para todas as linhas da planilha, reduzindo erros manuais e tempo operacional.

---

## ⚙ Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
| 🐍 *Python 3* | Linguagem base do projeto |
| 🤖 *BotCity Framework* | Automação de aplicações desktop e controle de UI |
| 📊 *Excel / BotCity Excel Plugin* | Leitura e manipulação dos extratos |
| 🧩 *Datetime* | Controle de logs e horários |
| 🪟 *Automação Desktop (.exe)* | Interação com o aplicativo bancário |
| 🔐 *.env* | Armazenamento seguro de configurações |

---
