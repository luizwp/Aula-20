import pymysql.cursors
from tkinter import*


def criarConexao():
    try:
        conexao = pymysql.connect(user='root',
                                  password='',
                                  host='localhost',
                                  database='escola')
        return conexao
    except Exception as error:
        print(f'Erro ao conectar! {error}')

def cadastrarAluno():
    try:
        nome = txt_nome.get()
        nota = float(txt_nota.get())
        turma_id = int(txt_turma.get())
        sql = "INSERT INTO aluno (nome, nota, turma_id) VALUES (%s, %s, %s)"
        conexao = criarConexao()
        cursor = conexao.cursor()
        cursor.execute(sql, (nome, nota, turma_id))
        conexao.commit()
        print('Dados cadastrados com sucesso!')


    except Exception as error:
        print(f'Erro ao cadastrar! Erro: {error}')



janela = Tk()

janela.title('Cadastro de alunos')
label_matricula = Label(janela, text='Matricula:', font ='Tahoma 16')
label_matricula.grid(row=0, column=0)

txt_matricula = Entry(janela, font ='Tahoma 16')
txt_matricula.grid(row=0, column=1)


label_nome = Label(janela, text='Nome:', font ='Tahoma 16')
label_nome.grid(row=1, column=0)

txt_nome = Entry(janela, font='Tahoma 16')
txt_nome.grid(row=1, column=1)


label_turma = Label(janela, text='Turma:', font ='Tahoma 16')
label_turma.grid(row=2, column=0)

txt_turma = Entry(janela, font='Tahoma 16')
txt_turma.grid(row=2, column=1)


label_nota = Entry(janela, font ='Tahoma 16')
label_nota.grid(row=3, column=0)

txt_nota = Entry(janela, font='Tahoma 16')
txt_nota.grid(row=3, column=1)

btn_cadastrar = Button(janela, text='Cadastrar', font='Tahoma 16', fg='blue', bg='#14964c',
                        command=cadastrarAluno)


btn_cadastrar.grid(row=4, column=0)

janela.mainloop()