import mesa
# importa o modelo de simula cã o desenvolvido
from model import Schelling
import numpy as np
# inicio do design do experiments
# defini cã o das vari á veis dos experimentos
# que ser ã o controladas ( valor fixo ) ou manipuladas
params = { 
"width": 10, 
"height": 10, 
"density": np.arange(0, 0.5, 0.1), 
"minority_pc": 0.5, 
"homophily": np.arange(0, 5, 1), 
"disease_probability": 50, 
"spread_probability": 50 
}
# define a quantidade de experimentos
# que ser ã o repetidos para cada configura cã o de valores
# para as vari á veis ( de controle e independentes )
experiments_per_parameter_configuration = 50
# quantidade de passos suficientes para que a simula cã o
# alcance um estado de equil í brio ( steady state )
max_steps_per_simulation = 100
# executa a simulacoes / experimentos , e coleta dados em mem ó ria
results = mesa.batch_run(
Schelling,
parameters = params,
iterations = experiments_per_parameter_configuration,
max_steps = max_steps_per_simulation ,
data_collection_period = -1,
display_progress = True,
)
import pandas as pd
# converte os dados das simula cõ es em planilhas ( dataframes )
results_df = pd.DataFrame(results)
# gera uma string com data e hora
from datetime import datetime
now = str (datetime.now()).replace(":", "-").replace(" ", "-")
# define um prefixo para o nome do arquivo que vai guardar os dados do modelo
# contendo alguns dados dos experimentos
file_name_suffix = ("_iter_" + str(  ) +
"_steps_" + str(max_steps_per_simulation) + "_" + now)
# define um prefixo para o nome para o arquivo de dados
model_name_preffix = "SchellingSickModel"
# define o nome do arquivo
file_name = model_name_preffix + "_model_data" + file_name_suffix + ".csv"
results_df.to_csv(file_name)