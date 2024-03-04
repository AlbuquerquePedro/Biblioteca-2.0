#banco_de_dados.py
import sqlite3


def create_tables():
    # Conectar ao banco de dados ou criar um novo
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Criar uma tabela para os livros
    cursor.execute('CREATE TABLE IF NOT EXISTS livros (\
                    id INTEGER PRIMARY KEY,\
                    titulo TEXT,\
                    autor TEXT,\
                    editora TEXT,\
                    ano_publicacao INTEGER,\
                    isbn TEXT,\
                    status TEXT DEFAULT "Disponível")')

    # Criar uma tabela para as revistas
    cursor.execute('CREATE TABLE IF NOT EXISTS revistas (\
                    id INTEGER PRIMARY KEY,\
                    titulo TEXT,\
                    autor TEXT,\
                    editora TEXT,\
                    ano_publicacao INTEGER,\
                    issn TEXT,\
                    volume INTEGER,\
                    status TEXT DEFAULT "Disponível")')

    # Criar uma tabela para as teses
    cursor.execute('CREATE TABLE IF NOT EXISTS teses (\
                    id INTEGER PRIMARY KEY,\
                    titulo TEXT,\
                    autor TEXT,\
                    programa_de_pos_graduacao TEXT,\
                    ano_publicacao INTEGER,\
                    orientador TEXT,\
                    co_orientador TEXT,\
                    status TEXT DEFAULT "Disponível")')

    # Criar uma tabela para os usuarios
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (\
                    id INTEGER PRIMARY KEY,\
                    nome TEXT,\
                    filiacao TEXT,\
                    endereco TEXT,\
                    email TEXT,\
                    telefone TEXT,\
                    tipo_usuario TEXT,\
                    status TEXT DEFAULT "nada consta",\
                    debito REAL DEFAULT 0.0)')

    # Criar uma tabela para os emprestimos
    cursor.execute('CREATE TABLE IF NOT EXISTS emprestimos (\
                    id INTEGER PRIMARY KEY,\
                    id_livro INTEGER,\
                    id_revista INTEGER,\
                    id_tese INTEGER,\
                    id_usuario INTEGER,\
                    data_emprestimo TEXT,\
                    data_devolucao TEXT,\
                    loan_type TEXT,\
                    FOREIGN KEY(id_livro) REFERENCES livros(id),\
                    FOREIGN KEY(id_revista) REFERENCES revistas(id),\
                    FOREIGN KEY(id_tese) REFERENCES teses(id),\
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')

    # Fechar a conexao com o banco de dados
    conn.commit()
    conn.close()


# Chamada da função para criar as tabelas
create_tables()
