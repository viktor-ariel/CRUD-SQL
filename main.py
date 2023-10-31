from flask import Flask, render_template, request, redirect,url_for
import repositorio

app= Flask(__name__)

@app.route("/")
def home():
    lista_personagens = repositorio.returnPersonagens()
    return render_template("index.html", dados=lista_personagens)

@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editePersonagem(id):
     if request.method == "POST":
        if "excluir" in request.form:
            repositorio.removePersonagem(id)
            return redirect(url_for('home'))
        # esta mandando dados
        elif "salvar" in request.form:
            id = request.form["id"] 
            nome = request.form["nome"]            
            raca = request.form["raca"]
            casa = request.form["casa"]
            altura = request.form["altura"]
            nascimento = request.form["nascimento"]
            imagem = request.form["imagem"]
            dados_retornados = repositorio.returnPersonagem(id)

            if dados_retornados:
                repositorio.updatePersonagem(id=id, nome=nome, raca=raca, casa=casa, altura=altura, nascimento=nascimento, imagem=imagem)
            else:
                repositorio.createPersonagem(nome=nome, raca=raca, casa=casa, altura=altura, nascimento=nascimento, imagem=imagem)

            return redirect(url_for('home'))
     else:
        # retorna os dados de um personagem de cadastro
        id, nome, raca, casa, altura, nascimento, imagem = repositorio.returnPersonagem(id)      
        
        return render_template("cadastro.html", id=id, nome=nome, raca=raca, casa=casa, altura=altura, nascimento=nascimento, imagem=imagem)


    
app.run(debug=True)

'''
@app.route("/personagem", methods=["GET", "POST"]) 
def criar_personagem():
    if request.method == "POST":
        personagem = {}
        personagem['nome'] = request.form['nome']
        personagem['casa'] = request.form['casa']
        personagem['raca'] = request.form['raca']
        personagem['altura'] = request.form['altura'] 
        personagem['nascimento'] = request.form['nascimento']
        personagem['imagem'] = request.form['imagem']
        repositorio.createPersonagem(**personagem)
        return redirect (url_for('home'))
    else:
        return render_template('cadastro.html',id=repositorio.gerar_id())

'''