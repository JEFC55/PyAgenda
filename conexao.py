import sqlite3
class conexao(object):
    def __init__(self):
        #Conexão Máquina Local
        self.db = sqlite3.connect(r'C:\sqlite3\banco.db')


    def gravar(self, sql):
        try:
            cur=self.db.cursor()
            cur.execute(sql)
            cur.close()
            self.db.commit()
        except:
             return False;
        return True;
        
    def consultar(self, sql):
        rs=None
        try:
            cur=self.db.cursor()
            cur.execute(sql)
            rs=cur.fetchone()
        except:
            return None
        return rs

    def consultar_tree(self, sql):
        rs=None
        try:
            cur=self.db.cursor()
            cur.execute(sql)
            rs=cur.fetchall()
        except:
            return None
        return rs    


    def fechar(self):
        self.db.close()
