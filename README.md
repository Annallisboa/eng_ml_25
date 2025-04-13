# kobe_dataset
Esse repositório contém o Projeto da disciplina de engenharia de ML do curso de MIT em Inteligência Artificial do Infnet.
A ideia do projeto é validar o conhecimento sobre Engenharia de Machine Learning, aplicando conceitos de AutoML, MLOps, Visualização de Dados e Estrutura de Projetos. 

## Prevendo arremessos do Kobe 
Nesse projetos iremos trabalhar os datasets disponíveis no  [https://www.kaggle.com/c/kobe-bryant-shot-selection/data]. Utilizei o Kedro para organizar os dados do projeto, realizar os pipelines e integra-lo junto ao MLFLOW

![Estrutura do projeto](https://github.com/Annallisboa/kobe_dataset/blob/main/framework%20tdsp.png)

# Estrutura dos dados no Kedro
## Dados
- **01_raw:** estão os dados brutos que ainda não foram trabalhos
- **04_feature:** estão os dados filtrados, treino e teste.  
- **Docs:** documentação

## Pipelines
Foram criadas 3 pipelines no Kedro:
- **Preparação dos dados (nomeiei erreneamente como nome_do_pipeline):** onde salvei o data_filtered.parquet, removendo NA e filtrando as colunas solicitadas
- **split_train_teste:** onde os dados separados em 80% treino e 20% teste
- **treinamento:** onde os dados são treinados. 

## Notebooks
Foram usados apenas para validação dos códigos e analises rápidas. 

## MLFLOW
Após a escolha do modelo de arvore de decisão, servi o modelo com MLFLOW:
![Modelos Treinados](https://github.com/Annallisboa/eng_ml_25/blob/main/Modelos%20treinados%20mlflow.png)

![Servindo o Modelo na porta 5001](https://github.com/Annallisboa/eng_ml_25/blob/main/modelo%20servido%20na%20porta%205001.png)

![Validando a API do Modelo](https://github.com/Annallisboa/eng_ml_25/blob/main/validando%20a%20api%20do%20modelo.png)

## Streamlit
Depois de servir o modelo criei a visualização no streamlit 
![Visualização do Modelo](https://github.com/Annallisboa/eng_ml_25/blob/main/streamlit%20do%20kobe.png)



# Perguntas do PD  
## Como as ferramentas Streamlit, MLFlow, PyCaret e Scikit-Learn auxiliam na construção dos pipelines descritos anteriormente? A resposta deve abranger os seguintes aspectos:

- **Rastreamento de Experimentos**: O MLFLOW permite o armazenamento de vários coisas automaticamente, sendo elas: parametros, métricas, artefatos e modelos treinados. Além disso, permite a comparação de métricas para decidir qual modelo é melhor. 
- **Funções de Treinamento**: o Pycaret ajuda bastante na hora de treinar vários modelos ao mesmo tempo (apesar do consumo excessivo de CPU's), basta usar um comando como setup() para treinar vários modelos automaticamente. O sckit-learn ajuda no controle da pipeline de modelagem no pré-processamneto, validação cruzada e treino.
- **Monitoramento da Saúde do Modelo**: O MLFLOW possui o histórico das métircas dos modelos, permitindo verificar como ele está performando ao longo do tempo. Para ter uma acompanhamento mais visual e disponivel para outros times, o Streamlit pode ser usado para montar dashboard e acompanhamentos das métricas totalmente customizavéis em tempo real. 
- **Atualização do Modelo:** com Pycaret podemos re-treinar os dados juntamente com o MLFLOW que possui o controle das versões anteriores, podendo ser substituido, atualizado ou até mesmo reprocessar com novos dados.
- **Deployment**: O MLFLOW consegue servir o modelo com uma API através de um unico comando, além disso, você pode "unir" ele ao Streamlit para disponibilizr o mesmo via uma interface simples da web, onde o usuário pode interagir com o modelo.

## A variável shot_made_flag será seu alvo, onde 0 indica que Kobe errou e 1 que a cesta foi realizada. O dataset resultante será armazenado na pasta "/data/processed/data_filtered.parquet". Ainda sobre essa seleção, qual a dimensão resultante do dataset?
A dimensão foi (20285,7)

## Quais estratégias ajudam a minimizar os efeitos de viés de dados.

## Treinamento do modelo: Selecione um dos dois modelos para finalização e justifique sua escolha.
A escolha do modelo foi a Arvore de Decisão (0.6750), pois o valor log_loss foi um pouco menor que a Regressão Logistica (0.6768), dessa forma com o log loss menor significa que o modelo errou menos e está um pouco mais confiante nas previsões. 

## Aplicação
### O modelo é aderente a essa nova base? O que mudou entre uma base e outra? Justifique.
Acredito que modelo tenha uma aderencia limitada, já que teve um desempenho limitado. Ele não conseguiu generalizar bem para dados muito diferentes

### Descreva como podemos monitorar a saúde do modelo no cenário com e sem a disponibilidade da variável resposta para o modelo em operação.
Podemos monitorar a saúde do modelo através do log loss, caso ele seja superior a 0.7, significa que o modelo está perdendo a confiança. Para F_score, abaixo de 0.35 temos um alerta crítico. 

### Descreva as estratégias reativa e preditiva de retreinamento para o modelo em operação.

