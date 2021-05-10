# modelagem-censo-escolar
Modelagem de dados do Censo Escolar 2020

Perguntas:
- Quais são os 10 municípios (pode ser apenas a sigla) que têm o maior número de pessoas no “Ensino Fundamental de 9 anos - 9º Ano”?;
- Qual a distribuição de cores/raças (Branca, Pretas, Pardas, Amarelas e Indígenas) entre os estados (pode ser apenas a sigla)?

Pacotes PIP utilizados:
- OS
- Pandas
- Sqlite3


## Casos de solução

&emsp;(sol_1.py) A primeira solução teve somente a inclusão dos dados de maneira bruta no banco de dados local e querys aplicadas para obtenção de resultado.Alto consumo dos processadores e memoria.<br />
(sol_2.py) No caso da segunda foi aplicada uma limpeza de dados e modelagem. Remoção de nulos; Tipo do dado da coluna; Seleção de colunas utilizadas;

### Fluxo de execução

- Busca todos os caminhos dos arquivos na localidade x escolhida; Grava em uma lista;
- Criar um DataFrame composto por todos os arquivos;
- Envia o DF para o banco
- Query para respondar pergunta 1
- Query para responder pergunta 2
