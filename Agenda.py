# Programa Agenda Eletrônica
import tkinter as tk
from tkinter import messagebox
import conexao


tela = tk.Tk()
tela.geometry('1366x768+0+0')
tela.state('zoomed')
tela['bg'] = "#ff0000"
tela.title("Agenda Eletrônica 1.0")

def limpar():
    txtcodigo.delete(0,"end")
    txtnome.delete(0,"end")
    txtclassificacao.delete(0,"end")
    txtcelular.delete(0,"end")
    txttelefone.delete(0,"end")
    txtemail.delete(0,"end")
    txtobservacao.delete("0","end")
    txtcodigo.focus_set()

def gravar():
    var_codigo = txtcodigo.get()
    var_nome = txtnome.get()
    var_classificacao = txtclassificacao.get()
    var_celular = txtcelular.get()
    var_telefone = txttelefone.get()
    var_email = txtemail.get()
    var_observacao = txtobservacao.get()

    con=conexao.conexao()
    sql_txt = f"select codigo,nome,telefone,email,observacao from agenda where codigo = {var_codigo}"

    rs=con.consultar(sql_txt)

    if rs:
        sql_text = f"update agenda set nome='{var_nome}',classificacao='{var_classificacao}',celular='{var_celular}',telefone='{var_telefone}',email='{var_email}',observacao='{var_observacao}' where codigo = '{var_codigo}'"
    else:
        sql_text = f"insert into agenda(codigo,nome,classificacao,celular,telefone,email,observacao) values ({var_codigo},'{var_nome}','{var_classificacao}','{var_celular}','{var_telefone}','{var_email}','{var_observacao}')"

    print(sql_text)
    if con.gravar(sql_text):
        messagebox.showinfo("Aviso", "Item Gravado com Sucesso")
        limpar()
    else:
        messagebox.showerror("Erro", "Houve um Erro na Gravação")
        
def excluir():
    var_del = messagebox.askyesno("Exclusão", "Tem certeza que deseja excluir?")
    if var_del == True:
        var_codigo = txtcodigo.get()

        con=conexao.conexao()
        sql_text = f"delete from agenda where codigo = '{var_codigo}'"
        if con.gravar(sql_text):
              messagebox.showinfo("Aviso", "Item Excluído com Sucesso")
              limpar()
        else:
            messagebox.showerror("Erro", "Houve um Erro na Exclusão")

            
        con.fechar()

    else:
        limpar()

def sair():
    var_sair = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
    if var_sair == True:
         tela.destroy()
    else:
        messagebox.showinfo("Ótimo", "Que bom que você escolheu continuar")

def buscar():
    var_codigo = txtcodigo.get()
 
    con=conexao.conexao()
    sql_txt = f"select codigo,nome,classificacao,celular,telefone,email,observacao from agenda where codigo = {var_codigo}"
    rs=con.consultar(sql_txt)

    if rs:
    
        limpar()

        txtcodigo.insert(0,rs[0])
        txtnome.insert(0, rs[1])
        txtclassificacao.insert(0, rs[2])
        txtcelular.insert(0, rs[3])
        txttelefone.insert(0,rs[4])
        txtemail.insert(0,rs[5])
        txtobservacao.insert(0,rs[5])

lblcodigo = tk.Label(tela, text ="Código:", bg="gold", fg="black", font=('Calibri', 12), anchor = "w")
lblcodigo.place(x = 50, y = 60, width=90, height = 25)

btnpesquisar = tk.Button(tela, text ="Pesquisar", 
                       bg ='yellow',foreground='black', font=('Calibri', 12, 'bold'),command = buscar)
btnpesquisar.place(x = 280, y = 60, width = 75,  height = 25)

txtcodigo = tk.Entry(tela, font=('Calibri', 12))
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)

lblnome = tk.Label(tela, text ="Nome:", bg="gold", fg="black", font=('Calibri', 12), anchor = "w")
lblnome.place(x = 50, y = 100, width=90, height = 25)

txtnome = tk.Entry(tela, font=('Calibri', 12))
txtnome.place(x = 150, y = 100, width = 360, height = 25)

lblclassificacao = tk.Label(tela, text ="Classificação:", bg="gold", fg="black", font=('Calibri', 12), anchor = "w")
lblclassificacao.place(x = 50, y = 140, width=90, height = 25)

txtclassificacao = tk.Entry(tela, font=('Calibri', 12))
txtclassificacao.place(x = 150, y = 140, width = 200, height = 25)

lblcelular = tk.Label(tela, text ="Celular:", bg="gold", fg="black", font=('Calibri', 12), anchor = "w")
lblcelular.place(x = 50, y = 180, width=90, height = 25)

txtcelular = tk.Entry(tela, font=('Calibri', 12))
txtcelular.place(x = 150, y = 180, width = 140, height = 25)

lbltelefone = tk.Label(tela, text ="Telefone:", bg="gold", fg="black", font=('Calibri', 12), anchor = "w")
lbltelefone.place(x = 50, y = 220, width=90, height = 25)

txttelefone = tk.Entry(tela, font=('Calibri', 12))
txttelefone.place(x = 150, y = 220, width = 140, height = 25)

lblemail = tk.Label(tela, text ="Email:", bg="gold", fg="black", font=('Calibri', 12), anchor = "w")
lblemail.place(x = 50, y = 260, width=90, height = 25)

txtemail = tk.Entry(tela, font=('Calibri', 12))
txtemail.place(x = 150, y = 260, width = 360, height = 25)

lblobservacao = tk.Label(tela, text ="Observação:", bg="gold", fg="black", font=('Calibri', 12), anchor = "w")
lblobservacao.place(x = 50, y = 300, width=90, height = 25)

txtobservacao = tk.Entry(tela, font=('Calibri', 12))
txtobservacao.place(x = 150, y = 300, width = 360, height = 25)

btngravar = tk.Button(tela, text ="Gravar", 
                       bg ='black',foreground='white', font=('Calibri', 12, 'bold'),command =gravar)
btngravar.place(x = 150, y = 360, width = 65)

btnlimpar = tk.Button(tela, text ="Limpar", 
                       bg ='black',foreground='white', font=('Calibri', 12, 'bold'),command = limpar)
btnlimpar.place(x = 250, y = 360, width = 65)

btnexcluir = tk.Button(tela, text ="Excluir", 
                       bg ='black',foreground='white', font=('Calibri', 12, 'bold'),command = excluir)
btnexcluir.place(x = 350, y = 360, width = 65)

btnsair = tk.Button(tela, text ="Sair", 
                       bg ='black',foreground='white', font=('Calibri', 12, 'bold'),command = sair)
btnsair.place(x = 450, y = 360, width = 65)

txtcodigo.focus_set()

tela.mainloop()