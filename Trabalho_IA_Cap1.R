install.packages("dplyr") 
install.packages("httr")
install.packages("jsonlite")



# Carregar os pacotes necessários
library(httr)
library(jsonlite)
library(dplyr)

getwd()  # Mostra o diretório atual

# Ler o arquivo CSV com os dados
dados <- read.csv("dados_agricultura.csv", sep=",", header=TRUE)

# Ler o arquivo CSV com a localização
local <- read.csv("coordenadas.csv", sep=",", header=FALSE, stringsAsFactors=FALSE)

# Exibir os dados
print(dados)
print(local)

head(local)  # Exibe as cordenadas
head(dados)  # Exibe as primeiras linhas do CSV
str(dados)   # Mostra a estrutura dos dados

# Função para conectar na API e pegar dados climáticos
api_key <- "SUA_CHAVE_AQUI"

# Função para buscar dados climáticos por latitude e longitude
obter_dados_clima <- function(lat, lon) {
  url <- paste0("https://api.openweathermap.org/data/2.5/weather?lat=", 
                lat, "&lon=", lon, "&appid=", api_key, "&units=metric&lang=pt")

  # Requisição GET para a API
  resposta <- GET(url)

  # Verificar se a requisição foi bem-sucedida
  if (status_code(resposta) == 200) {
   local <- fromJSON(content(resposta, "text", encoding = "UTF-8"))

    # Extrair informações principais
    return(data.frame(
      temperatura =local$main$temp,
      sensacao_termica =local$main$feels_like,
      umidade =local$main$humidity,
      pressao =local$main$pressure,
      descricao =local$weather[[1]]$description
    ))
  } else {
    return(data.frame(temperatura=NA, sensacao_termica=NA, umidade=NA, pressao=NA, descricao="Erro na API"))
  }
}

# Aplicando a função
# Criar um novo dataframe com os dados climáticos
dados_climaticos <- local %>%
  rowwise() %>%
  mutate(info_clima = list(obter_dados_clima(Latitude, Longitude))) %>%
  unnest(info_clima)


# Calcular estatísticas básicas
media_area <- mean(dados$area, na.rm = TRUE)
desvio_area <- sd(dados$area, na.rm = TRUE)

# Exibir os resultados
cat("Média da área plantada:", media_area, "m²\n")
cat("Desvio padrão da área plantada:", desvio_area, "m²\n")

# Exibir os dados meteorológicos
print(dados_climaticos)

