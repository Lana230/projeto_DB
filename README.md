# Projeto DB - Sistema de Monitoramento de Saúde Básica

## Trabalho Prático 3

### Descrição 
Etapa de implementação e consolidação de um projeto de banco de dados previamente modelado. Implementação do esquema em SQL(incluindo criação de tabelas, chaves primárias, chaves estrangeiras e restrições de integridade), e integração do banco de dados a uma aplicação desenvolvida em Python, capaz de realizar operações como:
- Inserção de dados;
- Consulta de dados;
- Atualização de dados.

### **Requisitos:**
- Realizar ajustes estruturais necessários no esquema relacional para garantir integridade, coerência e funcionamento adequado do sistema;
- Implementar o banco de dados em SQL, utilizando corretamente comandos DDL e DML;
- Definir e aplicar restrições de integridade (PK, FK, UNIQUE, NOT NULL, CHECK e outras quando pertinente);
- Validar a aderência do modelo à 3° Forma Normal (3FN), reconhecendo possíveis problemas estruturais e prevenindo anomalias;
- Desenvolver consultas SQL relevantes e coerentes com os requisitos do sistema.

### **Implementação no SGBD:** 
SQLite Browser. Permitindo operações de:
- **Inserção:** em, pelo menos, em 3 tabelas (e, ao menos, 1 delas deve ser uma
tabela associativa de relacionamento N:N);
- **Consulta:** pelo menos 6 consultas distintas, com ao menos 3 delas
parametrizáveis (e, ao menos, uma delas com múltiplos parâmetros);
- **Atualização:** em, pelo menos, 1 tabela.

### **Interface da aplicação:** 
Linha de comando, com a implementação de menus estruturados e navegáveis. 

## Visão Geral

Este projeto é um sistema de monitoramento de saúde básica desenvolvido para gerenciar informações de cidadãos, profissionais de saúde (médicos e enfermeiros), UBSs (Unidades Básicas de Saúde), agendamentos, filas de atendimento, vacinas, exames e anamneses. O sistema visa otimizar o atendimento e a gestão de recursos em unidades de saúde, com foco na priorização de cidadãos vulneráveis e na transparência dos processos.

## Estrutura do Projeto

O projeto segue uma arquitetura modular, com as seguintes pastas principais:

*   `models/`: Contém as definições das entidades do sistema (Cidadão, Médico, UBS, Agendamento, etc.).
*   `repositories/`: Responsável pela interação com o banco de dados, persistindo e recuperando os objetos das entidades.
*   `menus/`: Define as interfaces de usuário baseadas em texto para interação com o sistema.
*   `database/`: Contém o script de criação do banco de dados (DDL) e a lógica de conexão.
*   `CRUD/`: Contém os arquivos de testes de conexão com o banco de dados e comandos de sql.

## Configuração e Execução

### Pré-requisitos

*   Python 3.x
*   SQLite (geralmente já incluído com Python)

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/Lana230/projeto_DB.git
    cd projeto_DB
    ```

2.  **Crie o banco de dados:**

   O script `ddl.sql` na pasta `database/` contém a definição do esquema do banco de dados. Você pode executá-lo manualmente ou usar um script Python para criar o banco de dados. Certifique-se de que o arquivo `ubs_teste.db` seja criado na pasta de `database/` ou que o caminho no `conexao.py` esteja correto.

    ```bash
    sqlite3 ubs_teste.db < database/ddl.sql
    ```
**Observação: caso o `ubs_teste.db` não esteja presente na pasta `database/`.**

### Execução

Para iniciar o sistema, execute o arquivo `main.py`:

```bash
python3 main.py
```

## Funcionalidades Principais

O sistema oferece as seguintes funcionalidades:

*   **Gestão de Usuários:** Cadastro e autenticação de diferentes tipos de usuários (Cidadão, Médico, Enfermeiro).
*   **Gestão de UBSs:** Cadastro e gerenciamento de Unidades Básicas de Saúde.
*   **Agendamentos:** Criação e gerenciamento de agendamentos para consultas e vacinas.
*   **Filas de Atendimento:** Organização de cidadãos em filas com base em prioridade.
*   **Gestão de Vacinas:** Registro de vacinas e controle de estoque por UBS.
*   **Consultas Médicas:** Registro de consultas, exames, hipóteses diagnósticas e medicamentos.
*   **Anamneses:** Registro de informações clínicas do cidadão.

## Melhorias Recentes (Baseado nas últimas alterações no GitHub)

As seguintes melhorias foram implementadas recentemente, com foco na construção e aprimoramento dos menus de usuário:

*   **Menus de Usuário Aprimorados:** Os menus em `menus/menu_sistema.py` foram expandidos para oferecer opções específicas para `Cidadão`, `Médico` e `Enfermeiro`.
*   **Integração de Agendamentos:** A classe `Class_menu_appointment` foi integrada para permitir que cidadãos visualizem suas consultas e médicos gerenciem as suas.
*   **Estrutura para Enfermeiros:** Um menu base para enfermeiros foi criado, preparando o terreno para futuras funcionalidades de gerenciamento de agendamentos e vacinação.

### Regras de Negócio

*   **Cálculo de Prioridade:** Estender a lógica de `calcular_prioridade` para incluir o `grau_urgencia` de exames como fator de priorização.
*   **Gestão de Filas Robusta:** Implementar validações para evitar múltiplos agendamentos do mesmo tipo para o mesmo cidadão na mesma data. Desenvolver mecanismos para atualização automática da `posicao_atual` e ordenação da fila com base na `prioridade_calculada`.
*   **Controle de Estoque de Vacinas:** Implementar a verificação de `quantidade_disponivel` antes da aplicação de vacinas e o decremento do estoque após o registro.
*   **Transparência Aprimorada:** Desenvolver interfaces claras para cidadãos consultarem sua posição e o motivo da prioridade, e para gestores configurarem e visualizarem os critérios de priorização.
