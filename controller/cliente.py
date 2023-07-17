#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(name, idade, turno, matricula, periodo):
    db.cur.execute("""
                   INSERT into public.alunos (name, idade, turno, matricula, periodo)
                   VALUES ('%s','%s','%s','%s','%s')
                   """ % (name, idade, turno, matricula, periodo))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM alunos
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def deletar(matricula):
    db.cur.execute("""
                   DELETE FROM alunos WHERE matricula = '%s';
                   """ % (matricula))
    db.con.commit()

def atualizar(name, idade, turno, periodo):
    db.cur.execute("""
                   UPDATE alunos SET name = '%s', idade = '%s', turno = '%s', periodo = '%s' WHERE update_matricula = '%s';
                   """ % (name, idade, turno, periodo))
    db.con.commit()

