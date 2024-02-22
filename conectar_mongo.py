from pymongo import MongoClient

client = MongoClient("mongodb://root:senac123@127.0.0.1:37452")

# selecionando o banco de dados loja_db
db = client.loja_db

# Estamos obtendo os dados que sestao cadastrados na tabela (coleçao) usuario. usamos db[""].find()
# O comando find localiza os dados e retorna com todos eles para a variavel us.
# Depois fazemos a leitura de tds linhas com o for e exibimos na tela

# for us in db["usuario"].find():
#     print(us)


#Abaixo a consulta realiza o cadastro de um novo usuário e retorna o id do usuario cadastrado 

# usuario_id = db["usuario"].insert_one({"nomeusuario":"du","senha":"123","nível":"usuario"}).inserted_id
# print(usuario_id)


#Localizar apenas um usuario no banco de dados

# rs = db["usuario"].find_one({"nível":"usuario"})
# print(rs)


#Localizar todos os dados com o nivel de acesso usuario

# for rs in db["usuario"].find({"nível":"usuario"}):
# print(rs)