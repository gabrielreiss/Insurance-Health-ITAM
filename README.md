# Projeto Insurance Health ITAM

## Descrição
Explorando os dados de seguro saúde disponíveis no [Kaggle](https://www.kaggle.com/omartronco/health-insurance-data), criado e disponbilizado aos estudantes de Actuarial Science at ITAM (Mexico).

<div style="text-align: justify"> 
Segundo a descrição, os dados estão relacionados ao seguro de saúde para um grupo de apólices de seguro. Este conjunto de dados também inclui cobertura de acidentes. Embora as doenças sejam difíceis de classificar, esse conjunto de dados é dividido em 3 tipos: agudo, subagudo e crônico. O grupo possui 5 tipos de segurados, cada grupo com diferentes modificações de cobertura.
</div>


## Target, ideias e implementações

- [x] Upar dados no sqlite
- [x] Montar tabela de probabilidade por número de sinistros
- [x] Montar tabela de soma de sinistros por ano, agrupadas por grupo
- [x] Montar tabela de soma de sinistros por ano, agrupadas por grupo e tipo
- [x] Carregar os dados do banco para o python
- [x] Exploração dos dados e gráficos 
- [ ] Acrescentar texto decente na exploração dos dados
- [ ] Acrescentar média de valores pagos por tipo e grupo de claim via sql
- [ ] Cálculo do prêmio médio de risco para o ano de 2019

## Exploração dos dados

<div style="text-align: justify"> 
Analisando os dados, verificamos as seguintes informações:
</div>

### Distribuição da quantidade de reclamações por segurado
![svg](plots/claim_distribution.svg)

### Boxplot dos valores de indenizações por grupo
![svg](plots/boxplot_por_grupo.svg)

### Boxplot dos valores de indenizações por tipo
![svg](plots/boxplot_por_tipo.svg)

### Indenizações por ano e grupo

![svg](plots/boxplot_por_grupo2015.svg)
![svg](plots/boxplot_por_grupo2016.svg)
![svg](plots/boxplot_por_grupo2017.svg)
![svg](plots/boxplot_por_grupo2018.svg)

### Indenizações por ano e tipo

![svg](plots/boxplot_por_tipo2015.svg)
![svg](plots/boxplot_por_tipo2016.svg)
![svg](plots/boxplot_por_tipo2017.svg)
![svg](plots/boxplot_por_tipo2018.svg)