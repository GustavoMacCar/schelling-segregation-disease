library(tidyverse) # carrega o pacote tidyverse

SchellingSick <- read.csv(file = 'data/SchellingSickData.csv') #change according to work directory

SchellingSick <- SchellingSick[SchellingSick$density > 0,] #remove do dataset linhas de simulações sem agentes

ggplot(data = SchellingSick) +
  geom_bar(mapping = aes(x = sick)) #faz um histograma mostrando a contagem de agentes doentes ao final da simulação

ggplot(data = SchellingSick) +
  geom_bar(mapping = aes(x = happy)) #faz um histograma mostrando a contagem de agentes felizes ao final da simulação

ggplot(data = SchellingSick, mapping = aes(x = sick, colour = happy)) +
  geom_freqpoly(binwidth = 0.1) #faz um diagrama de frequências com linhas mostrando como o número de agentes felizes varia conforme o número de agentes doentes

ggplot(data = SchellingSick, mapping = aes(x = sick, y = happy)) + 
  geom_point() #faz um diagrama de frequências com pontos mostrando como o número de agentes felizes varia conforme o número de agentes doentes

ggplot(data = SchellingSick, mapping = aes(group = sick, y = happy)) +
  geom_boxplot() #faz um diagrama de boxplots mostrando como o número de agentes felizes varia conforme o número de agentes doentes

