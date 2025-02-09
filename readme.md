
# PT-BR

# MONT - Capturador de Dados do GitLab

## Descrição
Este projeto tem como objetivo capturar dados de um ou mais projetos do GitLab através de sua API e gerar um arquivo CSV com os dados formatados.

## Instale as dependências
pip install -r requirements.txt

## Nomecaltua dos arquivos

A nomeclatura dos arquivos segue o seguinte template:
- Tipo de arquivo
- Código do Projeto
- Data inicial da coleta da informação

Exemplo: issues_1_2024-06-09, esse arquivo tem todas as issues do projeto com id = 1 com issues criadas a partir do dia 09/06/2024

## Tipo de arquivos

- issues_origin = Lista todas as issues
- issues_related_issues = Lista todos as issues que se relacionam com as issues encontradas no arquivo "issues_{code_project}_(data)" 
- merges_origin = Lista todos os merges
- issues_related_merges = Lista todas as issues que se relacionam com os merges encontrados no arquivo  "issues_related_merges_{code_project}_{data}"

## Arquivo de confioguração

```yml
gitlabUrl: {host gitlab server}
daysToExport: {number of days}
exportProjectId: {Project ID}
dateType: {updated_after. updated_before}
```


Exemplo:

```yml
gitlabUrl: http://192.168.1.1
daysToExport: 30
exportProjectId: 68
dateType: updated_after
```


## Autor
* **Mattheus Cassundé**
* **cassunde.com.br**