from datetime import datetime
import sqlite3

personagens = {
    1:{
        "nome": "carlos",
        "raca": "bruxo",
        "casa": "leao",
        "altura": 1.70,
        "nascimento" : "31/10/2000",
        "imagem" : "https://33giga.com.br/wp-content/uploads/2020/06/46.-Izuku-Midoriya.jpg"
    },
    2: {
        "nome": "Sophia",
        "raca": "elfo",
        "casa": "grifo",
        "altura": 1.65,
        "nascimento": "15/04/1995",
        "imagem": "https://s2-techtudo.glbimg.com/2LWiKq2laIqzrH82P_NrYc8MTkQ=/1200x/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2023/j/C/i4AoaQRxSKmo3a33cB3Q/1.jpg"
    },
    3: {
        "nome": "Liam",
        "raca": "bruxo",
        "casa": "serpente",
        "altura": 1.75,
        "nascimento": "22/07/1998",
        "imagem": "https://orgulhootaku.files.wordpress.com/2014/02/21.jpg?w=584"
    },
    4: {
        "nome": "Aria",
        "raca": "humano",
        "casa": "coruja",
        "altura": 1.68,
        "nascimento": "03/12/2002",
        "imagem": "https://pbs.twimg.com/profile_images/1327466942081486850/kfRpwVfu_400x400.jpg"
    },
    5: {
        "nome": "Lucas",
        "raca": "elfo",
        "casa": "leão",
        "altura": 1.80,
        "nascimento": "10/09/1997",
        "imagem": "https://redeardente.com/wp-content/uploads/2023/05/As-10-Personagens-de-Animes-Negras-Mais-Lindas.webp"
    },
    6: {
        "nome": "Mia",
        "raca": "bruxo",
        "casa": "grifo",
        "altura": 1.63,
        "nascimento": "28/06/2001",
        "imagem": "https://img.ibxk.com.br/2022/11/16/16134543848513.jfif?ims=328x"
    },
    7: {
        "nome": "Ethan",
        "raca": "humano",
        "casa": "serpente",
        "altura": 1.70,
        "nascimento": "09/03/1996",
        "imagem": "https://metagalaxia.com.br/wp-content/uploads/2022/07/L-_Death-Note_.webp"
    },
    8: {
        "nome": "Olivia",
        "raca": "elfo",
        "casa": "coruja",
        "altura": 1.72,
        "nascimento": "14/01/1999",
        "imagem": "https://geekninja.com.br/wp-content/uploads/2023/07/Personagens-de-Animes.jpg"
    }
}

#tratamento de datas
def tratarIsoParaDMA(data:str):
    if '-' in data:
        data = datetime.strptime(data, '%Y-%m-%d')
        return data.strftime('%d/%m/%Y')
    else:
        return data
def tratarDMYParaIso(data:str):
    if '/' in data:
        data = datetime.strptime(data, '%d/%m/%Y')
        return data.strftime('%Y-%m-%d')
    else:
        return data

def gerar_id():
    conn = sqlite3.connect('jogo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='personagens'")
    next_id = cursor.fetchone()[0]
    return next_id + 1

def createPersonagem(nome, raca, casa, altura, nascimento, imagem):
    try:
        conn = sqlite3.connect('jogo.db')
        cursor = conn.cursor()
        sql_insert = "INSERT INTO personagens (nome , raca , casa , altura , nascimento , imagem ) values (?,?,?,?,?,?)"
        cursor.execute(sql_insert, (nome, raca, casa, altura, nascimento, imagem))
        personagem_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return personagem_id
    except Exception as ex:
        print(ex)
        return 0 

def returnPersonagens():
    try:
        conn = sqlite3.connect('jogo.db')
        cursor = conn.cursor()
        sql_select= "SELECT * FROM personagens"
        cursor.execute(sql_select )
        personagens = cursor.fetchall()
        conn.close()
        return personagens
    except:
        return False

def returnPersonagem(id:int):
    try:
        if id  == 0:
            return gerar_id(), "" , "", "", "", "", ""
        conn = sqlite3.connect('jogo.db')
        cursor = conn.cursor()

        sql_select = "SELECT * FROM personagens WHERE id  = ?"
        cursor.execute(sql_select, (id,))
        id, nome, raca, casa, altura, nascimento, imagem = cursor.fetchone()
        print('1')
        conn.close()
        return id, nome, raca, casa, altura, nascimento, imagem
    except:
        return False

def updatePersonagem(id:int, nome, raca, casa, altura, nascimento, imagem):
    try:
        conn = sqlite3.connect('jogo.db')
        cursor = conn.cursor()
        sql_update = "UPDATE personagens SET nome = ?, raca = ?, casa  = ?, altura  = ?, nascimento  = ?,  imagem  = ? WHERE id  = ?"
        cursor.execute(sql_update, (nome, raca, casa, altura, nascimento, imagem, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False



def removePersonagem(id:int):
    try:
        conn = sqlite3.connect('jogo.db')
        cursor = conn.cursor()
        sql_delete = "DELETE FROM personagens WHERE id  = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

'''
nome = "Viktor"
raca = "Humano"
casa = "Apartamento"
altura = 1.70
nascimento = "12/12/2020"
imagem = "casa"

id = createPersonagem (nome, raca, casa, altura, nascimento, imagem)
print (id)
print(returnPersonagem(id))

id, nome, raca, casa, altura, nascimento, imagem = returnPersonagem(id)
updatePersonagem(id, "nanana", raca, casa, altura, nascimento, imagem)

print(returnPersonagem(id))
id, nome, raca, casa, altura, nascimento, imagem = returnPersonagem(id)

print(returnPersonagens())

removePersonagem(id)

print(returnPersonagem())
'''
