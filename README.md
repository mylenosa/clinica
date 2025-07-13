# Projeto Clínica - Dashboard Gerencial

## Sobre o Projeto

Este projeto foi desenvolvido como parte da avaliação da disciplina de Análise e Desenvolvimento de Sistemas. O objetivo é criar uma aplicação web utilizando o framework Django para se conectar a um banco de dados pré-existente de uma clínica, e a partir desses dados, gerar visualizações gerenciais.

A aplicação apresenta um dashboard com gráficos interativos e uma seção de relatórios tabulados, permitindo uma análise rápida e eficiente dos dados da clínica.

**Autor:** [Seu Nome Completo Aqui]

---

## Funcionalidades Implementadas

-   **Dashboard Interativo:** Página inicial com 3 gráficos para análise visual dos dados:
    1.  **Volume de Consultas por Dia:** Gráfico de linhas (Plotly) que mostra a quantidade de consultas ao longo do tempo.
    2.  **Pacientes por Ambulatório:** Gráfico de barras (Chart.js) que exibe a distribuição de pacientes nos diferentes ambulatórios.
    3.  **Médicos por Especialidade:** Gráfico de rosca (Chart.js) que mostra a proporção de médicos em cada especialidade.

-   **Relatórios Gerenciais:** Seção com 3 relatórios detalhados:
    1.  Relatório de Pacientes agrupados por Cidade.
    2.  Relatório de total de Consultas realizadas por cada Médico.
    3.  Relatório de utilização de Convênios nas consultas.

-   **Painel Administrativo Otimizado:** O admin do Django foi configurado para facilitar a busca, filtragem e visualização dos dados das tabelas.

-   **Boas Práticas:**
    -   Uso de variáveis de ambiente (`.env`) para proteger dados sensíveis (credenciais do banco de dados).
    -   Mapeamento de um banco de dados legado (`managed = False`).
    -   Estrutura de templates organizada e reutilizável.

---

## Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o ambiente de desenvolvimento.

### Pré-requisitos

-   Python 3.10+
-   MySQL (ou um SGBD compatível)
-   Git

### 1. Clonar o Repositório

```bash
git clone [https://github.com/desktop/desktop/issues/18661](https://github.com/desktop/desktop/issues/18661)
cd nome-da-pasta-do-projeto
```

### 2. Criar e Ativar o Ambiente Virtual

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as Dependências

O arquivo `requirements.txt` contém todas as bibliotecas necessárias.

```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados

-   Crie um banco de dados no seu MySQL com o nome `clinicaads`.
-   Importe o arquivo `.sql` fornecido para popular o banco com as tabelas e os dados.

### 5. Configurar as Variáveis de Ambiente

-   Renomeie o arquivo `.env.example` para `.env` (ou crie um novo arquivo `.env`).
-   Preencha as variáveis com as suas credenciais do banco de dados:

```ini
SECRET_KEY='django-insecure-sua-chave-secreta-aleatoria'
DEBUG=True
DB_NAME=clinicaads
DB_USER=seu_usuario_mysql
DB_PASSWORD=sua_senha_mysql
DB_HOST=localhost
DB_PORT=3306
```

### 6. Rodar o Servidor

Com tudo configurado, inicie o servidor Django:

```bash
python manage.py runserver
```

A aplicação estará disponível em `http://127.0.0.1:8000/`.
