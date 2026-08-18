# Sistema de Gerenciamento de Estoque e Produtos

Um sistema interativo em Python para controle, análise e gerenciamento de estoque de produtos via terminal.

## 👥 Dupla
- **Camila de Souza Santana**
- **Sophia Teixeira Ramada**

---

## 📌 Sobre o Projeto

Este projeto consiste em um script Python que implementa um menu interativo (CLI) para gerenciar um catálogo de produtos. Ele permite cadastrar novos itens, pesquisar produtos existentes, analisar métricas gerais de estoque, ordenar dados e remover produtos cadastrados.

---

## 🚀 Funcionalidades

1. **Listar Produtos:** Exibe todos os produtos atualmente cadastrados no estoque, incluindo nome, preço, quantidade e categoria.
2. **Cadastrar Produto:** Adiciona um novo produto ao sistema com validação de entradas (garante que valores numéricos e textos estejam dentro dos critérios aceitáveis).
3. **Buscar Produto:** Realiza a busca de um produto pelo nome (sem diferenciar maiúsculas e minúsculas).
4. **Exibir Análise do Estoque:** Apresenta relatórios e estatísticas com:
   - Quantidade total de produtos diferentes cadastrados.
   - Valor financeiro total do estoque em R$.
   - Produto com o maior valor unitário.
   - Produto com menor quantidade disponível.
   - Quantidade total de itens estocados.
5. **Ordenar Produtos:** Lista todos os produtos ordenados em ordem crescente pelo preço.
6. **Remover Produto:** Exclui um produto do sistema através da busca pelo nome.
7. **Sair:** Finaliza a execução do programa.

---

## 🛠️ Tecnologias e Conceitos Utilizados

- **Tuplas**
- **Estruturas de Dados:** Listas, Dicionários e Tuplas.
- **Controle de Fluxo:** Laços de repetição (`while`, `for`) e estrutura condicional `match/case`.
- **Tratamento de Exceções:** Bloco `try/except` com captura de `ValueError` para dados de entrada inválidos.
