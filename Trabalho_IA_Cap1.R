install.packages("dplyr")   # Para processamento de dados

# Carregar os pacotes necessários
library(dplyr)

getwd()  # Mostra o diretório atual

# Ler o arquivo CSV
dados <- read.csv("dados_agricultura.csv", sep=",", header=TRUE)

# Exibir os dados
print(dados)

head(dados)  # Exibe as primeiras linhas do CSV
str(dados)   # Mostra a estrutura dos dados


# Calcular estatísticas básicas
media_area <- mean(dados$area, na.rm = TRUE)
desvio_area <- sd(dados$area, na.rm = TRUE)

# Exibir os resultados
cat("Média da área plantada:", media_area, "m²\n")
cat("Desvio padrão da área plantada:", desvio_area, "m²\n")



