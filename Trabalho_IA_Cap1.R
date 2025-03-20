# Instalando os pacotes
install.packages("dplyr") 
install.packages("jsonlite")
install.packages("tidyr")
install.packages("httr")


# Ativando as bibliotecas
library(jsonlite)
library(dplyr)
library(tidyr)
library(httr)

# Mostrando o diretório atual
getwd()  


# Lendo os arquivos

# Ler o arquivo CSV de dados, gerado pela aplicação Python
dados <- read.csv("dados_agricultura.csv", stringsAsFactors=FALSE)

# Ler o arquivo CSV de coordenadas tambpém gerado pela aplicação Python
local <- read.csv("coordenadas.csv", header = FALSE, sep = ",", stringsAsFactors = FALSE)

# Usando API e criando função para obter dados meteorológicos

# Renomeando as colunas do arquivo de coordenadas
colnames(local) <- c("Cidade", "Latitude", "Longitude")

# Visualizar o dataframe
print(local)


# Chave da API do OpenWeatherMap
api_key <- "6ba409b8620d6bf2d4c2b890be5015e9"

# Função para obter o clima com base em latitude e longitude
obter_clima <- function(lat, lon, api_key) {
  url <- paste0("http://api.openweathermap.org/data/2.5/weather?lat=", lat,
                "&lon=", lon, "&appid=", api_key, "&units=metric&lang=pt")
  
  resposta <- GET(url)
  
  if (status_code(resposta) == 200) {
    dados <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
    
    # Retornar um dataframe com informações relevantes
    return(data.frame(
      temperatura = dados$main$temp,
      condicao = dados$weather[[1]]$description,
      umidade = dados$main$humidity,
      velocidade_vento = dados$wind$speed
    ))
  } else {
    return(data.frame(temperatura = NA, condicao = NA, umidade = NA, velocidade_vento = NA))
  }
}

# Aplicar a função para cada cidade
clima_dados <- local %>%
  rowwise() %>%
  mutate(clima = list(obter_clima(Latitude, Longitude, api_key))) %>%
  unnest(clima)

# Funções para obter a média e desvio padrão da Área e dos Insumos utilizados.

# Visualizar os primeiros registros
head(dados)

# Função para converter a string JSON em lista
processar_insumos <- function(insumos) {
  if (insumos == "[]") {
    return(data.frame(produto=NA, dose_por_metro=NA, total=NA))
  }
  
  insumos <- gsub("'", "\"", insumos)
  
  # Converter de JSON para lista
  lista <- fromJSON(insumos)
  
  # Transformar em DataFrame
  return(as.data.frame(lista))
}

# Aplicar a função para cada linha da coluna 'insumos'
dados_expandido <- dados %>%
  rowwise() %>%
  mutate(insumos_df = list(processar_insumos(insumos))) %>%
  unnest(insumos_df)

# Visualizar os dados convertidos
head(dados_expandido)

# Calcular estatísticas por cultura
estatisticas <- dados_expandido %>%
  summarise(
    media_area = mean(area, na.rm=TRUE),
    desvio_area = sd(area, na.rm=TRUE),
    media_dose = mean(dose_por_metro, na.rm=TRUE),
    desvio_dose = sd(dose_por_metro, na.rm=TRUE),
    media_total = mean(total, na.rm=TRUE),
    desvio_total = sd(total, na.rm=TRUE)
  )

# Exibir resultado
print(estatisticas)

# Exibir os dados de clima junto com a cidade
print(clima_dados)
