# tela.py part 1
from datetime import datetime
from PIL import ImageTk
from tkcalendar import Calendar
from tkinter import ttk, messagebox
from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox, Label


from PIL import Image, ImageTk

# tkcalendarx
from tkcalendar import Calendar, DateEntry
from datetime import date
import datetime as dt  # Usando um alias para evitar conflitos de nomes

from datetime import datetime, timedelta

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


# janela.mainloop()


class InterfaceInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.geometry('500x300')
        self.root.configure(background=co1)
        self.root.resizable(width=False, height=False)

        style = Style(root)
        style.theme_use("clam")

        # Logo (substitua pelo caminho da sua logo)
        self.logo_label = Label(
            root, text="Sua Logo Aqui", bg=co1, fg=co0, font=("Arial", 24))
        self.logo_label.pack(pady=20)

        # Breve frase
        self.frase_label = Label(
            root, text="Bem-vindo ao Sistema de Gerenciamento", bg=co1, fg=co0, font=("Arial", 16))
        self.frase_label.pack()

        # Campos para inserir data e hora
        self.data_entry = Entry(root, width=20)
        self.data_entry.insert(0, "AAAA-MM-DD")
        self.data_entry.pack()

        self.hora_entry = Entry(root, width=20)
        self.hora_entry.insert(0, "HH:MM")
        self.hora_entry.pack()

        # Botão "Confirmar"
        self.confirmar_button = Button(
            root, text="Confirmar", command=self.verificar_data_hora, bg=co2, fg=co1)
        self.confirmar_button.pack(pady=20)

    def verificar_data_hora(self):
        data = self.data_entry.get()
        hora = self.hora_entry.get()

        try:
            # Verifica se a data e a hora estão no formato correto
            datetime.strptime(data, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")

            # Exibe mensagem com data e hora adicionadas
            resposta = messagebox.askquestion("Confirmação", f"Data: {data}\nHora: {
                                              hora}\nIniciar o programa?")
            if resposta == "yes":
                # Inicia o programa principal
                self.root.destroy()  # Fecha a janela de interface inicial
                iniciar_programa(data, hora)
            else:
                # Reexibe a interface inicial
                self.data_entry.delete(0, 'end')
                self.hora_entry.delete(0, 'end')
        except ValueError:
            messagebox.showerror(
                "Erro", "Formato de data ou hora inválido. Use AAAA-MM-DD e HH:MM.")


def iniciar_programa(data, hora):
    # Aqui você pode chamar a função principal do seu sistema de gerenciamento
    # Por exemplo: janela_principal()
    janela = Tk()
    janela.title("")
    janela.geometry('1420x640')
    janela.configure(background=co1)
    janela.resizable(width=TRUE, height=TRUE)

    style = Style(janela)
    style.theme_use("clam")

    # Frames -----------------------------------------------------

    frameCima = Frame(janela, width=1420, height=100, bg=co6,  relief="flat",)
    frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    frameEsquerda = Frame(janela, width=710, height=540,
                          bg=co4,  relief="solid",)
    frameEsquerda.grid(row=1, column=0, sticky=NSEW)

    frameDireita = Frame(janela, width=650, height=540,
                         bg=co1, relief="raised")
    frameDireita.grid(row=1, column=1, sticky=NSEW)

    # Logo -----------------------------------------------------

    # abrindo imagem
    app_img = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/logo.png')
    app_img = app_img.resize((80, 80))
    app_img = ImageTk.PhotoImage(app_img)

    app_logo = Label(frameCima, image=app_img, width=1000,
                     compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co6, fg=co1)
    app_logo.place(x=5, y=0)

    app_ = Label(frameCima, text="Sistema de Gerenciamento de Bibliotecas - UFPE", compound=LEFT,
                 padx=5, relief=FLAT, anchor=NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
    app_.place(x=100, y=25)

    l_linha = Label(frameCima, width=1570, height=1, anchor=NW,
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
            # Obtendo o tipo de usuário selecionado no combobox
            user_type = combo_tipo_usuario.get()

            lista = [first_name, type_name, address, email, phone]

            # Verificando caso algum campo esteja vazio ou nao
            for i in lista:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            # Inserindo os dados no banco de dados
            insert_user(first_name, type_name, address,
                        email, phone, user_type)

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
        l_linha = Label(frameDireita, width=200, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

        l_p_nome = Label(frameDireita, text="Nome Completo:*",
                         height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_p_nome.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_p_nome = Entry(frameDireita, width=25,
                         justify='left', relief="solid")
        e_p_nome.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_filiacao = Label(frameDireita, text="Filiação [departamento ou curso]*",
                           height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_filiacao.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_filiacao = Entry(frameDireita, width=25,
                           justify='left', relief="solid")
        e_filiacao.grid(row=3, column=1, pady=5, sticky=NSEW)

        l_endereco = Label(frameDireita, text="Endereço do usuário:",
                           height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
        e_endereco = Entry(frameDireita, width=25,
                           justify='left', relief="solid")
        e_endereco.grid(row=4, column=1, pady=5, sticky=NSEW)

        l_email = Label(frameDireita, text="Endereço de e-mail:*",
                        height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
        e_email = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_email.grid(row=5, column=1, pady=5, sticky=NSEW)

        l_numero = Label(frameDireita, text="Número de telefone:*",
                         height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_numero.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
        e_numero = Entry(frameDireita, width=25,
                         justify='left', relief="solid")
        e_numero.grid(row=6, column=1, pady=5, sticky=NSEW)

        # Combobox para selecionar o tipo de usuário
        l_tipo_usuario = Label(frameDireita, text="Tipo de Usuário:",
                               height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_tipo_usuario.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)
        combo_tipo_usuario = ttk.Combobox(frameDireita, values=[
            "Aluno de graduação", "Aluno de pós-graduação", "Professor"])
        combo_tipo_usuario.grid(row=7, column=1, pady=5, sticky=NSEW)

        # Botao Salvar--------------------
        img_salvar = Image.open(
            'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
        img_salvar = img_salvar.resize((36, 36))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                          width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=8, column=1, pady=5, sticky=NSEW)

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
        l_linha = Label(frameDireita, width=100, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        l_titlo = Label(frameDireita, text="Título do livro*",
                        height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_titlo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_titlo = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_titlo.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_autor = Label(frameDireita, text="Autor do livro*",
                        height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_autor = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_autor.grid(row=3, column=1, pady=5, sticky=NSEW)

        l_editora = Label(frameDireita, text="Editora do livro*",
                          height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
        e_editora = Entry(frameDireita, width=25,
                          justify='left', relief="solid")
        e_editora.grid(row=4, column=1, pady=5, sticky=NSEW)

        l_ano = Label(frameDireita, text="Ano de publicação do livro*",
                      height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
        e_ano = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_ano.grid(row=5, column=1, pady=5, sticky=NSEW)

        l_isbn = Label(frameDireita, text="ISBN do livro*", height=1,
                       anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
        e_isbn = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_isbn.grid(row=6, column=1, pady=5, sticky=NSEW)

        # Botao Salvar--------------------
        img_salvar = Image.open(
            'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
        img_salvar = img_salvar.resize((36, 36))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                          width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
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
        l_linha = Label(frameDireita, width=200, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        l_titlo = Label(frameDireita, text="Título da Revista*",
                        height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_titlo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_titlo = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_titlo.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_autor = Label(frameDireita, text="Autor da Revista*",
                        height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_autor = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_autor.grid(row=3, column=1, pady=5, sticky=NSEW)

        l_editora = Label(frameDireita, text="Editora da Revista*",
                          height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
        e_editora = Entry(frameDireita, width=25,
                          justify='left', relief="solid")
        e_editora.grid(row=4, column=1, pady=5, sticky=NSEW)

        l_ano = Label(frameDireita, text="Ano de publicação da Revista*",
                      height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
        e_ano = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_ano.grid(row=5, column=1, pady=5, sticky=NSEW)

        l_issn = Label(frameDireita, text="ISSN da Revista*", height=1,
                       anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_issn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
        e_issn = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_issn.grid(row=6, column=1, pady=5, sticky=NSEW)

        l_volume = Label(frameDireita, text="volume da Revista*", height=1,
                         anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_volume.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)
        e_volume = Entry(frameDireita, width=25,
                         justify='left', relief="solid")
        e_volume.grid(row=7, column=1, pady=5, sticky=NSEW)

        # Botao Salvar--------------------
        img_salvar = Image.open(
            'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
        img_salvar = img_salvar.resize((36, 36))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                          width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=8, column=1, pady=5, sticky=NSEW)

    # nova tese

    def nova_tese():

        global img_salvar

        def add():

            title = e_titlo.get()
            author = e_autor.get()
            graduate_program = e_programa_de_pos_graduacao.get()
            year = e_ano.get()
            advisor = e_orientador.get()
            co_supervisor = e_co_orientador.get()

            lista = [title, author, graduate_program,
                     year, advisor,  co_supervisor]

            # Verificando caso algum campo esteja vazio ou nao
            for i in lista:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            # Inserindo os dados no banco de dados
            insert_thesis(title, author, graduate_program,
                          year, advisor,  co_supervisor)

            # Mostrando mesnsagem de sucesso
            messagebox.showinfo('Sucesso', 'Tese inserido com sucesso!')

            # limpando os campos de entradas
            e_titlo.delete(0, END)
            e_autor.delete(0, END)
            e_programa_de_pos_graduacao.delete(0, END)
            e_ano.delete(0, END)
            e_orientador.delete(0, END)
            e_co_orientador.delete(0, END)

        app_ = Label(frameDireita, text="Inserir uma Nova Tese", width=100, compound=LEFT,
                     padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=200, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        l_titlo = Label(frameDireita, text="Título da Tese*",
                        height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_titlo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
        e_titlo = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_titlo.grid(row=2, column=1, pady=10, sticky=NSEW)

        l_autor = Label(frameDireita, text="Autor da Tese*",
                        height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
        e_autor = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_autor.grid(row=3, column=1, pady=5, sticky=NSEW)

        l_programa_de_pos_graduacao = Label(frameDireita, text="Programa de pós-graduação da Tese*",
                                            height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_programa_de_pos_graduacao.grid(
            row=4, column=0, padx=5, pady=5, sticky=NSEW)
        e_programa_de_pos_graduacao = Entry(
            frameDireita, width=25, justify='left', relief="solid")
        e_programa_de_pos_graduacao.grid(row=4, column=1, pady=5, sticky=NSEW)

        l_ano = Label(frameDireita, text="Ano de publicação da Tese*",
                      height=1, anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
        e_ano = Entry(frameDireita, width=25, justify='left', relief="solid")
        e_ano.grid(row=5, column=1, pady=5, sticky=NSEW)

        l_orientador = Label(frameDireita, text="Orientador da Tese*", height=1,
                             anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_orientador.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
        e_orientador = Entry(frameDireita, width=25,
                             justify='left', relief="solid")
        e_orientador.grid(row=6, column=1, pady=5, sticky=NSEW)

        l_co_orientador = Label(frameDireita, text="Co-orientador da Tese*", height=1,
                                anchor=NW, font=(' Ivy 10 '), bg=co1, fg=co4)
        l_co_orientador.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)
        e_co_orientador = Entry(frameDireita, width=25,
                                justify='left', relief="solid")
        e_co_orientador.grid(row=7, column=1, pady=5, sticky=NSEW)

        # Botao Salvar--------------------
        img_salvar = Image.open(
            'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
        img_salvar = img_salvar.resize((36, 36))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                          width=100, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=8, column=1, pady=5, sticky=NSEW)

    # funcao ver usuarios

    def ver_usuarios():
        app_ = Label(frameDireita, text="Todos Usuarios", width=100, compound=LEFT,
                     padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=100, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = get_users()

        # Criando uma nova lista de cabeçalhos com a coluna "Valor Total da Multa"
        list_header = ['ID', 'Nome', 'Filiação', 'Endereço',
                       'Email', 'Telefone', 'Tipo de Usuário', 'Multa']

        global tree

        tree = ttk.Treeview(frameDireita, selectmode="extended",
                            columns=list_header, show="headings")

        # Definindo as barras de rolagem
        vsb = ttk.Scrollbar(
            frameDireita, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(
            frameDireita, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        # Definindo largura e alinhamento das colunas
        hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw", "nw"]
        h = [3, 150, 130, 70, 120, 100, 100, 30]  # Largura das colunas
        n = 0

        for col in list_header:
            tree.heading(col, text=col, anchor='nw')
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for item in dados:
            # Adicionando o tipo de usuário na exibição
            user_type = item[6]  # Índice 6 corresponde ao tipo de usuário
            if user_type == 1:
                user_type_str = "Aluno de graduação"
            elif user_type == 2:
                user_type_str = "Aluno de pós-graduação"
            elif user_type == 3:
                user_type_str = "Professor"
            else:
                user_type_str = "Tipo não especificado"

            # Calculando o valor total da multa
            # Coloque o número de dias de atraso aqui
            valor_multa = calcular_multa(10)
            if valor_multa == 0.0:
                multa_str = "Nada Consta"
            else:
                # Formatando para exibir duas casas decimais
                multa_str = f"R${valor_multa:.2f}"

            tree.insert('', 'end', values=item + (user_type_str, multa_str))

    # funcao ver livros

    # Função para exibir todos os livros

    def ver_livros():
        app_ = Label(frameDireita, text="Todos os livros", width=100, compound=LEFT,
                     padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=200, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = get_books()

        # Criando um treeview com rolagem dupla
        list_header = ['ID', 'Título', 'Autor',
                       'Editora', 'Ano', 'ISBN', 'Disponibilidade']

        global tree

        tree = ttk.Treeview(frameDireita, selectmode="extended",
                            columns=list_header, show="headings")
        # Barra de rolagem vertical
        vsb = ttk.Scrollbar(
            frameDireita, orient="vertical", command=tree.yview)

        # Barra de rolagem horizontal
        hsb = ttk.Scrollbar(
            frameDireita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw"]
        h = [3, 195, 180, 75, 35, 75, 110]

        for n, col in enumerate(list_header):
            tree.heading(col, text=col, anchor='nw')
            # Ajustando a largura da coluna para a string do cabeçalho
            if n < len(h) and n < len(hd):
                tree.column(col, width=h[n], anchor=hd[n])

        for item in dados:
            disponibilidade = "Disponível" if item[-1] == 1 else "Alugado"
            # Convertendo item para lista antes da concatenação
            item_list = list(item)
            tree.insert('', 'end', values=item_list + [disponibilidade])

    # funcao ver revistas

    def ver_revistas():
        app_ = Label(frameDireita, text="Todas as Revistas", width=100, compound=LEFT,
                     padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=200, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = get_magazine()

        # creating a treeview with dual scrollbars
        list_header = ['ID', 'Título', 'Autor', 'Editora',
                       'Ano', 'ISSN', 'Volume', 'Disponibilidade']

        global tree

        tree = ttk.Treeview(frameDireita, selectmode="extended",
                            columns=list_header, show="headings")
        # vertical scrollbar
        vsb = ttk.Scrollbar(
            frameDireita, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(
            frameDireita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw"]
        h = [3, 130, 110, 100, 40, 55, 10, 110]

        for n, col in enumerate(list_header):
            tree.heading(col, text=col, anchor='nw')
            # adjust the column's width to the header string
            if n < len(h) and n < len(hd):  # Verifica se n não ultrapassa o comprimento de h e hd
                tree.column(col, width=h[n], anchor=hd[n])

        for item in dados:
            disponibilidade = "Disponível" if item[-1] == 1 else "Alugado"
            # Convertendo item e [disponibilidade] em tuplas antes de concatená-las
            tree.insert('', 'end', values=tuple(item) + (disponibilidade,))

    # Função para ver teses

    def ver_teses():
        app_ = Label(frameDireita, text="Todas as Teses", width=100, compound=LEFT,
                     padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=200, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        dados = get_thesis()

        # creating a treeview with dual scrollbars
        list_header = ['ID', 'Título', 'Autor',
                       'Programa de Pos Graduacao', 'Ano', 'Orientador', 'Co-orientador', 'Disponibilidade']

        global tree

        tree = ttk.Treeview(frameDireita, selectmode="extended",
                            columns=list_header, show="headings")
        # vertical scrollbar
        vsb = ttk.Scrollbar(
            frameDireita, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(
            frameDireita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw", "nw"]
        h = [3, 120, 110, 110, 40, 75, 75, 110]

        for n, col in enumerate(list_header):
            tree.heading(col, text=col, anchor='nw')
            # adjust the column's width to the header string
            if n < len(h) and n < len(hd):
                tree.column(col, width=h[n], anchor=hd[n])

        for item in dados:
            disponibilidade = "Disponível" if item[-1] == 1 else "Alugado"
            # Convertendo item em uma tupla antes de concatená-lo com [disponibilidade]
            tree.insert('', 'end', values=tuple(item) + (disponibilidade,))

    # Realizar um empréstimo

    def realizar_emprestimo():

        global img_salvar

        def add():
            user_id = e_id_usuario.get()
            book_id = e_id_livro.get()
            magazine_id = e_id_revista.get()
            thesis_id = e_id_tese.get()
            data_emprestimo = e_data_emprestimo.get()

            # Verifique se todos os campos estão preenchidos
            if user_id and data_emprestimo:
                try:
                    # Converta a data do empréstimo para o formato adequado
                    data_emprestimo = dt.datetime.strptime(
                        data_emprestimo, "%Y-%m-%d").date()
                except ValueError:
                    messagebox.showerror(
                        'Erro', 'Formato de data inválido. Use o formato AAAA-MM-DD')
                    return

                # Obter o tipo de usuário correspondente ao ID do usuário
                user_type = get_user_type(user_id)
                if user_type:
                    # Faça a chamada adequada para a função insert_loan com a data de empréstimo
                    try:
                        # Empréstimo de apenas um livro
                        if book_id and not magazine_id and not thesis_id:
                            insert_loan(book_id, None, None, user_id,
                                        data_emprestimo.isoformat())
                        # Empréstimo de apenas uma revista
                        elif magazine_id and not book_id and not thesis_id:
                            insert_loan(None, magazine_id, None,
                                        user_id, data_emprestimo.isoformat())
                        # Empréstimo de apenas uma tese
                        elif thesis_id and not book_id and not magazine_id:
                            insert_loan(None, None, thesis_id, user_id,
                                        data_emprestimo.isoformat())
                        # Empréstimo de um livro e uma revista
                        elif book_id and magazine_id and not thesis_id:
                            insert_loan(book_id, magazine_id, None,
                                        user_id, data_emprestimo.isoformat())
                        # Empréstimo de um livro e uma tese
                        elif book_id and thesis_id and not magazine_id:
                            insert_loan(book_id, None, thesis_id,
                                        user_id, data_emprestimo.isoformat())
                        # Empréstimo de uma revista e uma tese
                        elif magazine_id and thesis_id and not book_id:
                            insert_loan(None, magazine_id, thesis_id,
                                        user_id, data_emprestimo.isoformat())
                        # Empréstimo de um livro, uma revista e uma tese
                        elif book_id and magazine_id and thesis_id:
                            insert_loan(book_id, magazine_id, thesis_id,
                                        user_id, data_emprestimo.isoformat())
                        else:
                            raise ValueError(
                                "Combinação de itens inválida para empréstimo.")

                        messagebox.showinfo(
                            'Sucesso', 'Empréstimo realizado com sucesso!')
                        # Limpe os campos de entrada
                        e_id_usuario.delete(0, 'end')
                        e_id_livro.delete(0, 'end')
                        e_id_revista.delete(0, 'end')
                        e_id_tese.delete(0, 'end')
                        e_data_emprestimo.delete(0, 'end')
                    except ValueError as e:
                        messagebox.showerror('Erro', str(e))
                else:
                    messagebox.showerror(
                        'Erro', 'ID de usuário inválido ou não encontrado.')
            else:
                messagebox.showerror(
                    'Erro', 'Preencha todos os campos corretamente.')
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
        e_id_livro = Entry(frameDireita, width=50,
                           justify='left', relief="solid")
        e_id_livro.grid(row=3, column=1, pady=5, sticky=NSEW)

        l_id_revista = Label(frameDireita, text="Digite o ID da revista",
                             height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id_revista.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
        e_id_revista = Entry(frameDireita, width=50,
                             justify='left', relief="solid")
        e_id_revista.grid(row=4, column=1, pady=5, sticky=NSEW)

        l_id_tese = Label(frameDireita, text="ID da Tese",
                          height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_id_tese.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
        e_id_tese = Entry(frameDireita, width=50,
                          justify='left', relief="solid")
        e_id_tese.grid(row=5, column=1, pady=5, sticky=NSEW)

        l_data_emprestimo = Label(frameDireita, text="Data do empréstimo*",
                                  height=1, anchor=NW, font=(' Ivy 10'), bg=co1, fg=co4)
        l_data_emprestimo.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
        e_data_emprestimo = Entry(frameDireita, width=50,
                                  justify='left', relief="solid")
        e_data_emprestimo.grid(row=6, column=1, pady=5, sticky=NSEW)

        # Botao Salvar--------------------
        img_salvar = Image.open(
            'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/save.png')
        img_salvar = img_salvar.resize((36, 36))
        img_salvar = ImageTk.PhotoImage(img_salvar)
        b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT,
                          width=200, text='  Salvar', bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE)
        b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

    # tela.py part 2
    # livros emprestados no momento

    def ver_livros_emprestados():
        # Cabeçalho
        app_ = Label(frameDireita, text="Todos os livros emprestados no momento", width=100, compound=LEFT,
                     padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        # Linha
        l_linha = Label(frameDireita, width=200, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        # Obter dados dos livros emprestados
        dados = get_books_on_loan()

        # Cabeçalhos da lista
        list_header = ['ID', 'Título', 'Tipo do usuário', 'Tipo de usuario',
                       'Data de empréstimo', 'Data de devolução']

        create_treeview(dados, list_header)

    # Revistas emprestadas no momento

    def ver_revistas_emprestados():
        # Cabeçalho
        app_ = Label(frameDireita, text="Todas as revistas emprestadas no momento", width=100, compound=LEFT,
                     padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        # Linha
        l_linha = Label(frameDireita, width=400, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        # Obter dados das revistas emprestadas
        dados = get_magazine_on_loan()

        # Cabeçalhos da lista
        list_header = ['ID', 'Título', 'Tipo do usuário', 'Tipo de usuario',
                       'Data de empréstimo', 'Data de devolução']

        # Criar Treeview com scrollbars
        create_treeview(dados, list_header)

    # Teses emprestadas no momento

    def ver_teses_emprestados():
        # Cabeçalho
        app_ = Label(frameDireita, text="Todas as teses emprestadas no momento", width=100, compound=LEFT,
                     padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        # Linha
        l_linha = Label(frameDireita, width=400, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        # Obter dados das teses emprestadas
        dados = get_thesis_on_loan()

        # Cabeçalhos da lista
        list_header = ['ID', 'Título', 'Tipo do usuário', 'Tipo de usuario',
                       'Data de empréstimo', 'Data de devolução']

        # Criar Treeview com scrollbars
        create_treeview(dados, list_header)

    # Atrasos no momento

    def ver_emprestimos_atrasados():
        # Cabeçalho
        app_ = Label(frameDireita, text="Empréstimos atrasados e multas", width=100, compound=LEFT,
                     padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        # Linha
        l_linha = Label(frameDireita, width=400, height=1,
                        anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
        l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

        # Obter dados dos empréstimos atrasados
        dados = get_emprestimos_atrasados()

        # Cabeçalhos da lista
        list_header = ['ID Empréstimo', 'Título',
                       'Tipo do Empréstimo', 'Dias de Atraso', 'Valor da Multa']

        # Criar Treeview com scrollbars
        create_treeview(dados, list_header)

    def create_treeview(dados, list_header):
        # Criar Treeview com scrollbars
        global tree
        tree = ttk.Treeview(frameDireita, selectmode="extended",
                            columns=list_header, show="headings")
        vsb = ttk.Scrollbar(
            frameDireita, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(
            frameDireita, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(column=0, row=2, sticky='nsew')
        vsb.grid(column=1, row=2, sticky='ns')
        hsb.grid(column=0, row=3, sticky='ew')
        frameDireita.grid_rowconfigure(0, weight=12)

        # Larguras das colunas e alinhamentos
        # 5 elementos, correspondendo aos 5 cabeçalhos
        hd = ["nw", "nw", "ne", "ne", "ne", "ne"]
        # 5 elementos, correspondendo às larguras das colunas
        h = [20, 175, 120, 90, 90, 90]

        # Configurar cabeçalhos e larguras das colunas
        for col, width, anchor in zip(list_header, h, hd):
            tree.heading(col, text=col, anchor='nw')
            tree.column(col, width=width, anchor=anchor)

        # Inserir dados na treeview
        for item in dados:
            tree.insert('', 'end', values=item)

    # Devolução de um empréstimo

    def devolucao_emprestimo():
        global img_salvar

        def add():
            loan_id = e_id_emprestimo.get()
            return_date = e_data_retorno.get()

            # Verificar se o campo do ID do empréstimo e a data de retorno estão preenchidos
            if loan_id == '' or return_date == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

            # Verificar se a data de retorno está no formato correto AAAA-MM-DD
            try:
                datetime.strptime(return_date, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror(
                    'Erro', 'Formato de data inválido. Use o formato AAAA-MM-DD.')
                return

            # Verificar se o empréstimo existe
            if not verificar_emprestimo_existe(loan_id):
                messagebox.showerror('Erro', 'Empréstimo não encontrado.')
                return

            # Verificar se a data de retorno está dentro do intervalo permitido
            data_emprestimo, data_devolucao = obter_datas_emprestimo(loan_id)
            data_atual = datetime.strptime(return_date, '%Y-%m-%d').date()
            if data_atual < data_emprestimo or data_atual > data_devolucao:
                messagebox.showerror(
                    'Erro', 'Data atual fora do intervalo permitido.')
                return

            # Verificar se o usuário possui débitos
            if verificar_debitos_usuario(loan_id):
                messagebox.showerror(
                    'Erro', 'Você possui débitos. Não pode realizar a devolução.')
                return

            # Verificar se a data atual é posterior à data de devolução
            if data_atual > data_devolucao:
                messagebox.showerror(
                    'Erro', 'A data atual é posterior à data de devolução. Você possui débitos.')
                return

            # Perguntar ao usuário se deseja renovar o empréstimo
            resposta = messagebox.askyesno(
                'Renovar empréstimo', 'Deseja renovar o empréstimo?')
            if resposta:
                try:
                    renovar_emprestimo(loan_id, data_atual)
                    messagebox.showinfo(
                        'Sucesso', 'Empréstimo renovado com sucesso.')
                except Exception as e:
                    messagebox.showerror('Erro', str(e))
            else:
                realizar_devolucao_emprestimo(loan_id)
                messagebox.showinfo(
                    'Sucesso', 'Empréstimo devolvido com sucesso.')

            # Limpar os campos de entrada
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

        l_data_retorno = Label(frameDireita, text="Dia atual (formato: AAAA-MM-DD)*",
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

    # Pagar multa de um emprestimo

    def pagar_multa():

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

        app_ = Label(frameDireita, text="Pagar as multas atrasadas", width=100, compound=LEFT,
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

        l_data_retorno = Label(frameDireita, text="valor total da multa:*",
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

        # nova teses
        if i == 'nova_tese':
            for widget in frameDireita.winfo_children():
                widget.destroy()
            nova_tese()

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

        # Ver teses
        if i == 'ver_teses':
            for widget in frameDireita.winfo_children():
                widget.destroy()
            ver_teses()

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

        # Teses emprestadas no momento
        if i == 'ver_teses_emprestadas':
            for widget in frameDireita.winfo_children():
                widget.destroy()
            ver_teses_emprestados()

            # Atrasos  no momento
        if i == 'ver_emprestimos_atrasados':
            for widget in frameDireita.winfo_children():
                widget.destroy()
            ver_emprestimos_atrasados()

        # Devolução de um empréstimo
        if i == 'devolucao_emprestimo':
            for widget in frameDireita.winfo_children():
                widget.destroy()
            devolucao_emprestimo()

        # pagar a multa de um empréstimo
        if i == 'pagar_multa':
            for widget in frameDireita.winfo_children():
                widget.destroy()
            pagar_multa()

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
    b_novo_livro.grid(row=0, column=1, sticky=NSEW, padx=5, pady=6)

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
    b_ver_revistas.grid(row=3, column=1, sticky=NSEW, padx=5, pady=6)

    # Nova tese
    img_nova_tese = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/add.png')
    img_nova_tese = img_nova_tese.resize((36, 36))
    img_nova_tese = ImageTk.PhotoImage(img_nova_tese)
    b_nova_tese = Button(frameEsquerda, command=lambda: control('nova_tese'), image=img_nova_tese, compound=LEFT,
                         anchor=NW, text='  Nova tese', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_nova_tese.grid(row=2, column=1, sticky=NSEW, padx=5, pady=6)

    img_ver_teses = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/logo.png')
    img_ver_teses = img_ver_teses.resize((36, 36))
    img_ver_teses = ImageTk.PhotoImage(img_ver_teses)
    b_ver_teses = Button(frameEsquerda, command=lambda: control('ver_teses'), image=img_ver_teses, compound=LEFT,
                         anchor=NW, text=' Exibir todas as teses', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_teses.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

    # Ver usuário
    img_ver_usuario = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/user.png')
    img_ver_usuario = img_ver_usuario.resize((36, 36))
    img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
    b_ver_usuario = Button(frameEsquerda, command=lambda: control('ver_usuarios'), image=img_ver_usuario, compound=LEFT,
                           anchor=NW, text='  Exibir todos os usuarios', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_usuario.grid(row=4, column=1, sticky=NSEW, padx=5, pady=6)

    # Realizar um empréstimo
    img_emprestimo = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/add.png')
    img_emprestimo = img_emprestimo.resize((36, 36))
    img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
    b_emprestimo = Button(frameEsquerda, command=lambda: control('realizar_emprestimo'), image=img_emprestimo, compound=LEFT,
                          anchor=NW, text=' Realizar um empréstimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_emprestimo.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

    # Devolução de um empréstimo
    img_devolucao = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/update.png')
    img_devolucao = img_devolucao.resize((36, 36))
    img_devolucao = ImageTk.PhotoImage(img_devolucao)
    b_devolucao = Button(frameEsquerda, command=lambda: control('devolucao_emprestimo'), image=img_devolucao, compound=LEFT,
                         anchor=NW, text='  Devolução de um empréstimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_devolucao.grid(row=5, column=1, sticky=NSEW, padx=5, pady=6)

    # Pagamento de multa
    img_pagar_multa = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/update.png')
    img_pagar_multa = img_pagar_multa.resize((36, 36))
    img_pagar_multa = ImageTk.PhotoImage(img_pagar_multa)
    b_pagar_multa = Button(frameEsquerda, command=lambda: control('pagar_multa'), image=img_pagar_multa, compound=LEFT,
                           anchor=NW, text='  Pagar a multa de um empréstimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_pagar_multa.grid(row=8, column=0, sticky=NSEW, padx=5, pady=6)

    # Livros emprestados no momento
    img_livros_emprestados = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/livro2.png')
    img_livros_emprestados = img_livros_emprestados.resize((36, 36))
    img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
    b_livros_emprestados = Button(frameEsquerda, command=lambda: control('ver_livros_emprestados'), image=img_livros_emprestados,
                                  compound=LEFT, anchor=NW, text=' Livros emprestados no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

    # Revistas emprestadas no momento
    img_revistas_emprestadas = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/livro2.png')
    img_revistas_emprestadas = img_revistas_emprestadas.resize((36, 36))
    img_revistas_emprestadas = ImageTk.PhotoImage(img_revistas_emprestadas)
    b_revistas_emprestadas = Button(frameEsquerda, command=lambda: control('ver_revistas_emprestadas'), image=img_revistas_emprestadas,
                                    compound=LEFT, anchor=NW, text=' Revistas emprestadas no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_revistas_emprestadas.grid(row=6, column=1, sticky=NSEW, padx=5, pady=6)

    # teses emprestadas no momento
    img_teses_emprestadas = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/livro2.png')
    img_teses_emprestadas = img_teses_emprestadas.resize((36, 36))
    img_teses_emprestadas = ImageTk.PhotoImage(img_teses_emprestadas)
    b_teses_emprestadas = Button(frameEsquerda, command=lambda: control('ver_teses_emprestadas'), image=img_teses_emprestadas,
                                 compound=LEFT, anchor=NW, text=' teses emprestadas no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_teses_emprestadas.grid(row=7, column=0, sticky=NSEW, padx=5, pady=6)

    # ver emprestimos atrasados
    img_emprestimos_atrasados = Image.open(
        'c:/Users/ExPed/OneDrive/Área de Trabalho/Python/Biblioteca/images/livro2.png')
    img_emprestimos_atrasados = img_emprestimos_atrasados.resize((36, 36))
    img_emprestimos_atrasados = ImageTk.PhotoImage(img_emprestimos_atrasados)
    b_emprestimos_atrasados = Button(frameEsquerda, command=lambda: control('ver_emprestimos_atrasados'), image=img_emprestimos_atrasados,
                                     compound=LEFT, anchor=NW, text=' Atrasos no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_emprestimos_atrasados.grid(row=7, column=1, sticky=NSEW, padx=5, pady=6)

    janela.mainloop()


root = Tk()
app = InterfaceInicial(root)
root.mainloop()
