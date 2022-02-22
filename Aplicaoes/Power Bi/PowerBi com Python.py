#### Como integrar o python com Power Bi ####

# Baixar o cmd ANACONDA

# Criar a maquina virtual dentro do CMD anaconda
# create --name envpowebi python=3.6

# Aperte em confirmar para continuar
# y

# ativar pasta no anaconda
# conda activate envpowebi  //  (envpowebi e só exemplo de nome da pasta)

# importar bibliotecas
# pip install pandas
# pip install numpy
# pip install matplotlib
# pip install pandas_datareader

#### Configurar o Power Bi ####

# Arquivo > Opções e configurações > Opções > Script Python > Outro > encontrar local da maquina virtual criada.

# Importar dataset

# Baixar arquivo na sua maquina com formato em jupyter
# Obter dados > mais > escrever scrpit Python > e colar script criado
# Selecionar e carregar Dataset

#### Consultas em Python ####

# Também é possivel criar consultas em python
# Ex: dataset['Coluna nova'] = dataset['Coluna1'] - dataset['Coluna2']

#### Criar Graficos em Python ####

# Dica: mais complicado, o melhor e usar o power bi mesmo
