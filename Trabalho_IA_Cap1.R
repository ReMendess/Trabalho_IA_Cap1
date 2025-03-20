install.packages("dplyr") 
install.packages("jsonlite")
install.packages("tidyr")


library(jsonlite)
library(dplyr)
library(tidyr)


# Ler o arquivo CSV
dados <- read.csv("dados_agricultura.csv", stringsAsFactors=FALSE)

# Visualizar os primeiros registros
head(dados)

# Função para converter a string JSON em lista
processar_insumos <- function(insumos) {
  if (insumos == "[]") {
    return(data.frame(produto=NA, dose_por_metro=NA, total=NA))
  }
  
  # Substituir aspas simples por duplas para ser JSON válido
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

