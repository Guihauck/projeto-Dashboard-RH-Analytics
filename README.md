# 📊 RH Analytics: Análise de Dados de Recursos Humanos

Bem-vindo ao repositório `rh_analytics`! Este projeto é dedicado à **análise e visualização de dados de Recursos Humanos** para extrair *insights* valiosos, apoiar a tomada de decisões estratégicas e otimizar processos de gestão de pessoas.

## 🖼️ Visualização

![Dashboard de Análise de RH](/rh_analytics/assets/Projeto.png)

---

## ✨ Destaques do Projeto

* **Dashboards de Desempenho:** Visualizações interativas sobre performance, engajamento e retenção.
* **Análise Preditiva:** Modelos para prever *turnover* (rotatividade) e identificar fatores de risco.
* **Automatização:** Scripts para ingestão e processamento automatizado de dados.

## 📁 Estrutura do Repositório

O projeto está organizado da seguinte forma:

| Diretório/Arquivo | Descrição |
| :--- | :--- |
| `rh_analytics/BaseRH.xlsx` | **Dados de Amostra:** Planilha base com dados brutos de RH (salários, cargos, desempenho, etc.). |
| `rh_analytics/scripts/` | **Scripts de Processamento:** Contém *scripts* Python (como `import_excel.py`) para limpeza, transformação e análise de dados. |
| `rh_analytics/notebooks/` | **Análises Exploratórias:** *Jupyter notebooks* com análises detalhadas e protótipos de modelos. |
| `rh_analytics/reports/` | **Relatórios e Dashboards:** Arquivos de *dashboards* (ex: Power BI, Tableau) ou relatórios gerados. |
| **`assets/image_21aedd.jpg`** | **Imagem de Exemplo/Dashboard.** |

## 🚀 Como Começar

### Pré-requisitos

Para rodar os scripts de análise, você precisará ter instalado:

* [Python 3.x](https://www.python.org/downloads/)
* Gerenciador de pacotes `pip`

### Instalação

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SEU_USUARIO/rh_analytics.git](https://github.com/SEU_USUARIO/rh_analytics.git)
    cd rh_analytics
    ```
2.  Instale as dependências necessárias (se aplicável, crie um arquivo `requirements.txt`):
    ```bash
    # Exemplo:
    pip install pandas openpyxl scikit-learn
    ```

### Execução dos Scripts

Para importar e processar a base de dados:

```bash
python rh_analytics/scripts/import_excel.py