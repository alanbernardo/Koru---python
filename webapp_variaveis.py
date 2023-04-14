#Vamos criar um dicionário com duas chaves e tentar retornar seus dados pela rota
dicionario = {
    "nome":"Alan Bernardo",
    "nascimento": 1996
}
#importar flask
from flask import Flask
#criar a aplicação Flask
app = Flask(_name_)

#A rota abaixo aciona uma função que retorna um dicionário 
@app. route("/teste")
def mostra_dicionario():
    return dicionario

@app. route ("/")
def dados_usuario():
    return f"<br>O usuario {dicionario['nome']} nasceu em {dicionario['nascimento']}</br>"

#Colocar a aplicação para rodar
app.run (debug=True)
