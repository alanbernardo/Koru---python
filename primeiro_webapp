#Importando o flask para podermos usar no nosso programa
from flask import Flask

#Vamos criar uma variável (neste caso, um objeto) para representar nossa aplicação web
app = Flask(_name_)

#Vamos criar uma variável uma rota para acessar o servidor
@app.route("/")
#Ao acessar esta rota, a função abaixo é executada e ela devolve (return) o texto "deu certo!"
def exibir_mensagem():
    return "deu certo!"

#A linha abaixo executa a aplicação web que foi criada apartir do Flask
app.run (debug=True)
