from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox


from PIL import Image, ImageTk

# tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

from datetime import datetime

# importando o TkScrolledframe
from tkscrolledframe import ScrolledFrame

# importar view
from view import *

# cores ---------------------

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#E9A178"
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 = "#6e8faf"  #
co11 = "#f2f4f2"

# Criando janela ---------------------------------------------

janela = Tk()
janela.title("")
janela.geometry('1260x660')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")


# Frames -----------------------------------------------------

frameCima = Frame(janela, width=1540, height=100, bg=co6,  relief="flat",)
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=300, height=530, bg=co4,  relief="solid",)
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=1200, height=530, bg=co1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)


# Logo -----------------------------------------------------

# abrindo imagem
app_img = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/logo.png')
app_img = app_img.resize((80, 80))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=2000,
                 compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co6, fg=co1)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Sistema de Gerenciamento de Bibliotecas - UFPE", compound=LEFT,
             padx=5, relief=FLAT, anchor=NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
app_.place(x=100, y=25)

l_linha = Label(frameCima, width=1260, height=1, anchor=NW,
                font=('Verdana 1 '), bg=co3, fg=co1)
l_linha.place(x=0, y=93)


# Novo usuario
def novo_usuario():

    global img_salvar

    def add():

        first_name = e_p_nome.get()
        type_name = e_filiacao.get()
        address = e_endereco.get()
        email = e_email.get()
        phone = e_numero.get()

        lista = [first_name, type_name, address, email, phone]

        # Verificando caso algum campo esteja vazio ou nao
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # Inserindo os dados no banco de dados
        insert_user(first_name, type_name, address, email, phone)

        # Mostrando mesnsagem de sucesso
        messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso!')

        # limpando os campos de entradas
        e_p_nome.delete(0, END)
        e_filiacao.delete(0, END)
        e_endereco.delete(0, END)
        e_email.delete(0, END)
        e_numero.delete(0, END)

    app_ = Label(frameDireita, text="Inserir um novo usuário", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    l_p_nome = Label(frameDireita, text="Nome Completo*",
                     height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_p_nome.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_p_nome = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_p_nome.grid(row=2, column=1, pady=10, sticky=NSEW)

    l_filiacao = Label(frameDireita, text="Filiacao*",
                       height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_filiacao.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_filiacao = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_filiacao.grid(row=3, column=1, pady=5, sticky=NSEW)

    l_endereco = Label(frameDireita, text="Endereço do usuário*",
                       height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_endereco = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_endereco.grid(row=4, column=1, pady=5, sticky=NSEW)

    l_email = Label(frameDireita, text="Endereço de e-mail*",
                    height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_email = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_email.grid(row=5, column=1, pady=5, sticky=NSEW)

    l_numero = Label(frameDireita, text="Número de telefone*",
                     height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_numero.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_numero = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_numero.grid(row=6, column=1, pady=5, sticky=NSEW)

    # Botao Salvar--------------------
    img_salvar = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
    img_salvar = img_salvar.resize((36, 36))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                      width=200, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)


# Novo livro
def novo_livro():

    global img_salvar

    def add():

        title = e_titlo.get()
        author = e_autor.get()
        publisher = e_editora.get()
        year = e_ano.get()
        isbn = e_isbn.get()

        lista = [title, author, publisher, year, isbn]

        # Verificando caso algum campo esteja vazio ou nao
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # Inserindo os dados no banco de dados
        insert_book(title, author, publisher, year, isbn)

        # Mostrando mesnsagem de sucesso
        messagebox.showinfo('Sucesso', 'Livro inserido com sucesso!')

        # limpando os campos de entradas
        e_titlo.delete(0, END)
        e_autor.delete(0, END)
        e_editora.delete(0, END)
        e_ano.delete(0, END)
        e_isbn.delete(0, END)

    app_ = Label(frameDireita, text="Inserir um Novo Livro", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_titlo = Label(frameDireita, text="Título do livro*",
                    height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_titlo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_titlo = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_titlo.grid(row=2, column=1, pady=10, sticky=NSEW)

    l_autor = Label(frameDireita, text="Autor do livro*",
                    height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_autor.grid(row=3, column=1, pady=5, sticky=NSEW)

    l_editora = Label(frameDireita, text="Editora do livro*",
                      height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_editora.grid(row=4, column=1, pady=5, sticky=NSEW)

    l_ano = Label(frameDireita, text="Ano de publicação do livro*",
                  height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_ano.grid(row=5, column=1, pady=5, sticky=NSEW)

    l_isbn = Label(frameDireita, text="ISBN do livro*", height=1,
                   anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_isbn = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_isbn.grid(row=6, column=1, pady=5, sticky=NSEW)

    # Botao Salvar--------------------
    img_salvar = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
    img_salvar = img_salvar.resize((36, 36))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                      width=200, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# nova revista


def nova_revista():

    global img_salvar

    def add():

        title = e_titlo.get()
        author = e_autor.get()
        publisher = e_editora.get()
        year = e_ano.get()
        issn = e_issn.get()
        volume = e_volume.get()

        lista = [title, author, publisher, year, issn, volume]

        # Verificando caso algum campo esteja vazio ou nao
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # Inserindo os dados no banco de dados
        insert_magazine(title, author, publisher, year, issn, volume)

        # Mostrando mesnsagem de sucesso
        messagebox.showinfo('Sucesso', 'Revista inserido com sucesso!')

        # limpando os campos de entradas
        e_titlo.delete(0, END)
        e_autor.delete(0, END)
        e_editora.delete(0, END)
        e_ano.delete(0, END)
        e_issn.delete(0, END)
        e_volume.delete(0, END)

    app_ = Label(frameDireita, text="Inserir uma Nova Revista", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_titlo = Label(frameDireita, text="Título da Revista*",
                    height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_titlo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_titlo = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_titlo.grid(row=2, column=1, pady=10, sticky=NSEW)

    l_autor = Label(frameDireita, text="Autor da Revista*",
                    height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_autor.grid(row=3, column=1, pady=5, sticky=NSEW)

    l_editora = Label(frameDireita, text="Editora da Revista*",
                      height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_editora.grid(row=4, column=1, pady=5, sticky=NSEW)

    l_ano = Label(frameDireita, text="Ano de publicação da Revista*",
                  height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_ano.grid(row=5, column=1, pady=5, sticky=NSEW)

    l_issn = Label(frameDireita, text="ISSN da Revista*", height=1,
                   anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_issn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_issn = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_issn.grid(row=6, column=1, pady=5, sticky=NSEW)

    l_volume = Label(frameDireita, text="volume da Revista*", height=1,
                     anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
    l_volume.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)
    e_volume = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_volume.grid(row=7, column=1, pady=5, sticky=NSEW)

    # Botao Salvar--------------------
    img_salvar = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
    img_salvar = img_salvar.resize((36, 36))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                      width=200, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=8, column=1, pady=5, sticky=NSEW)


# funcao ver usuarios
def ver_usuarios():

    app_ = Label(frameDireita, text="Todos Usuarios", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_users()

    # creating a treeview with dual scrollbars
    list_header = ['ID', 'Nome', 'Filiacao', 'Endereço', 'Email', 'Telefone']

    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [40, 195, 180, 180, 90, 100, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)


# funcao ver livros
def ver_livros():

    app_ = Label(frameDireita, text="Todos os livros", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_books()

    # creating a treeview with dual scrollbars
    list_header = ['ID', 'Título', 'Autor', 'Editora', 'Ano', 'ISBN']

    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [40, 195, 180, 180, 90, 100, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)

# funcao ver revistas


def ver_revistas():
    app_ = Label(frameDireita, text="Todas as Revistas", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_magazine()

    # creating a treeview with dual scrollbars
    list_header = ['ID', 'Título', 'Autor', 'Editora', 'Ano', 'ISSN', "Volume"]

    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [40, 170, 130, 130, 70, 80, 80]

    for n, col in enumerate(list_header):
        tree.heading(col, text=col, anchor='nw')
        # adjust the column's width to the header string
        if n < len(h) and n < len(hd):  # Verifica se n não ultrapassa o comprimento de h e hd
            tree.column(col, width=h[n], anchor=hd[n])

    for item in dados:
        tree.insert('', 'end', values=item)

# Realizar um empréstimo


def realizar_emprestimo():

    global img_salvar

    def add():
        user_id = e_id_usuario.get()
        book_id = e_id_livro.get()
        magazine_id = e_id_revista.get()

        if user_id and ((book_id and not magazine_id) or
                        (magazine_id and not book_id) or
                        (book_id and magazine_id)):
            # Verificando se algum campo está vazio
            # ou se todos estão preenchidos corretamente
            if not book_id:  # Se o ID do livro estiver em branco, é um empréstimo apenas de revista
                insert_loan(None, magazine_id, user_id, None, None)
            elif not magazine_id:  # Se o ID da revista estiver em branco, é um empréstimo apenas de livro
                insert_loan(book_id, None, user_id, None, None)
            else:  # Se ambos os IDs estiverem preenchidos, é um empréstimo de livro e revista
                insert_loan(book_id, magazine_id, user_id, None, None)

            messagebox.showinfo('Sucesso', 'Empréstimo realizado com sucesso!')
            # limpando os campos de entradas
            e_id_usuario.delete(0, 'end')
            e_id_livro.delete(0, 'end')
            e_id_revista.delete(0, 'end')
        else:
            messagebox.showerror(
                'Erro', 'Preencha todos os campos corretamente')

    app_ = Label(frameDireita, text="Realizar empréstimo", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_id_usuario = Label(frameDireita, text="Digite o ID do usuário*",
                         height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_id_usuario.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_id_usuario = Entry(frameDireita, width=50,
                         justify='left', relief="solid")
    e_id_usuario.grid(row=2, column=1, pady=10, sticky=NSEW)

    l_id_livro = Label(frameDireita, text="Digite o ID do livro",
                       height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_id_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_livro = Entry(frameDireita, width=50, justify='left', relief="solid")
    e_id_livro.grid(row=3, column=1, pady=5, sticky=NSEW)

    l_id_revista = Label(frameDireita, text="Digite o ID da revista",
                         height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_id_revista.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_revista = Entry(frameDireita, width=50,
                         justify='left', relief="solid")
    e_id_revista.grid(row=4, column=1, pady=5, sticky=NSEW)

    # Botao Salvar--------------------
    img_salvar = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
    img_salvar = img_salvar.resize((36, 36))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                      width=200, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=5, column=1, pady=5, sticky=NSEW)
# livros emprestados no momento


def ver_livros_emprestados():

    app_ = Label(frameDireita, text="Todos os livros emprestados no momento", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = []

    books_on_loan = get_books_on_loan()

    for book in books_on_loan:
        dado = [f"{book[0]}", f"{book[1]}", f"{book[2]} {
            book[3]}", f"{book[4]}", f"{book[5]}"]
        dados.append(dado)

    # creating a treeview with dual scrollbars
    list_header = ['ID', 'Titlo', 'Nome do usuário',
                   'D.mpréstimo', 'D.devolução']

    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "ne", "ne", "ne", "ne"]
    h = [60, 225, 200, 190, 110, 120, 105]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)

# ver revistas emprestadas


def ver_revistas_emprestados():

    app_ = Label(frameDireita, text="Todas as revistas emprestadas no momento", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = []

    magazine_on_loan = get_magazine_on_loan()

    for magazine in magazine_on_loan:
        dado = [f"{magazine[0]}", f"{magazine[1]}", f"{magazine[2]} {
            magazine[3]}", f"{magazine[4]}", f"{magazine[5]}"]
        dados.append(dado)

    # creating a treeview with dual scrollbars
    list_header = ['ID', 'Titlo', 'Nome do usuário',
                   'D.mpréstimo', 'D.devolução']

    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "ne", "ne", "ne", "ne"]
    h = [20, 175, 120, 90, 90, 100, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)


# Devolução de um empréstimo


def devolucao_emprestimo():

    global img_salvar

    def add():

        loan_id = e_id_emprestimo.get()
        return_date = e_data_retorno.get()

        lista = [loan_id, return_date]

        # Verificando caso algum campo esteja vazio ou nao
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # Inserindo os dados no banco de dados
        update_loan_return_date(loan_id, return_date)

        # Mostrando mesnsagem de sucesso
        messagebox.showinfo(
            'Sucesso', 'Data de devolução atualizada com sucesso!')

        # limpando os campos de entradas
        e_id_emprestimo.delete(0, END)
        e_data_retorno.delete(0, END)

    app_ = Label(frameDireita, text="Atualizar data de devolucao do emprestimo", width=100, compound=LEFT,
                 padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,
                    anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_id_emprestimo = Label(frameDireita, text="ID do empréstimo*",
                            height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_id_emprestimo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_id_emprestimo = Entry(frameDireita, width=30,
                            justify='left', relief="solid")
    e_id_emprestimo.grid(row=2, column=1, pady=10, sticky=NSEW)

    l_data_retorno = Label(frameDireita, text="Nova data de devolução (formato: AAAA-MM-DD)*",
                           height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
    l_data_retorno.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_data_retorno = Entry(frameDireita, width=30,
                           justify='left', relief="solid")
    e_data_retorno.grid(row=3, column=1, pady=5, sticky=NSEW)

    # Botao Salvar--------------------
    img_salvar = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
    img_salvar = img_salvar.resize((36, 36))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                      width=200, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=4, column=1, pady=5, sticky=NSEW)


# Frame Esquerda --------------------------------------------------

# Funcao para controlar o Menu
def control(i):

    # novo usuario
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_usuario()

    # novo livro
    if i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_livro()

     # nova revista
    if i == 'nova_revista':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        nova_revista()

    # Ver livros
    if i == 'ver_livros':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_livros()

    # Ver revistas
    if i == 'ver_revistas':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_revistas()

    # Ver usuarios
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_usuarios()

    # Realizar um empréstimo
    if i == 'realizar_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        realizar_emprestimo()

    # Livros emprestados no momento
    if i == 'ver_livros_emprestados':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_livros_emprestados()

    # Revistas emprestadas no momento
    if i == 'ver_revistas_emprestadas':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_revistas_emprestados()

    # Devolução de um empréstimo
    if i == 'devolucao_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        devolucao_emprestimo()


# Menu ------------------------------------------------------------

# Novo usuario
img_usuario = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/add.png')
img_usuario = img_usuario.resize((36, 36))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, command=lambda: control('novo_usuario'), image=img_usuario, compound=LEFT,
                   anchor=NW, text='  Novo usuário', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo livro
img_novo_livro = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/add.png')
img_novo_livro = img_novo_livro.resize((36, 36))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda, command=lambda: control('novo_livro'), image=img_novo_livro, compound=LEFT,
                      anchor=NW, text='  Novo livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

img_ver_livros = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/logo.png')
img_ver_livros = img_ver_livros.resize((36, 36))
img_ver_livros = ImageTk.PhotoImage(img_ver_livros)
b_ver_livros = Button(frameEsquerda, command=lambda: control('ver_livros'), image=img_ver_livros, compound=LEFT,
                      anchor=NW, text=' Exibir todos os livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livros.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Nova revista
img_novo_revista = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/add.png')
img_novo_revista = img_novo_revista.resize((36, 36))
img_novo_revista = ImageTk.PhotoImage(img_novo_revista)
b_novo_revista = Button(frameEsquerda, command=lambda: control('nova_revista'), image=img_novo_revista, compound=LEFT,
                        anchor=NW, text='  Nova revista', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_revista.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

img_ver_revistas = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/logo.png')
img_ver_revistas = img_ver_revistas.resize((36, 36))
img_ver_revistas = ImageTk.PhotoImage(img_ver_revistas)
b_ver_revistas = Button(frameEsquerda, command=lambda: control('ver_revistas'), image=img_ver_revistas, compound=LEFT,
                        anchor=NW, text=' Exibir todos as revistas', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_revistas.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Ver usuário
img_ver_usuario = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/user.png')
img_ver_usuario = img_ver_usuario.resize((36, 36))
img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda, command=lambda: control('ver_usuarios'), image=img_ver_usuario, compound=LEFT,
                       anchor=NW, text='  Exibir todos os usuarios', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar um empréstimo
img_emprestimo = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/add.png')
img_emprestimo = img_emprestimo.resize((36, 36))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
b_emprestimo = Button(frameEsquerda, command=lambda: control('realizar_emprestimo'), image=img_emprestimo, compound=LEFT,
                      anchor=NW, text=' Realizar um empréstimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestimo.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

# Devolução de um empréstimo
img_devolucao = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/update.png')
img_devolucao = img_devolucao.resize((36, 36))
img_devolucao = ImageTk.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda, command=lambda: control('devolucao_emprestimo'), image=img_devolucao, compound=LEFT,
                     anchor=NW, text='  Devolução de um empréstimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_devolucao.grid(row=7, column=0, sticky=NSEW, padx=5, pady=6)

# Livros emprestados no momento
img_livros_emprestados = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/livro2.png')
img_livros_emprestados = img_livros_emprestados.resize((36, 36))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_livros_emprestados = Button(frameEsquerda, command=lambda: control('ver_livros_emprestados'), image=img_livros_emprestados,
                              compound=LEFT, anchor=NW, text=' Livros emprestados no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.grid(row=8, column=0, sticky=NSEW, padx=5, pady=6)


# Revistas emprestadas no momento
img_revistas_emprestadas = Image.open(
    'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/livro2.png')
img_revistas_emprestadas = img_revistas_emprestadas.resize((36, 36))
img_revistas_emprestadas = ImageTk.PhotoImage(img_revistas_emprestadas)
b_revistas_emprestadas = Button(frameEsquerda, command=lambda: control('ver_revistas_emprestadas'), image=img_revistas_emprestadas,
                                compound=LEFT, anchor=NW, text=' Revistas emprestadas no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_revistas_emprestadas.grid(row=9, column=0, sticky=NSEW, padx=5, pady=6)


janela.mainloop()
