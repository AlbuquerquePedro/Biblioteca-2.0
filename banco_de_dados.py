import sqlite3

# Conectar ao banco de dados ou criar um novo
conn = sqlite3.connect('biblioteca.db')

# Criar uma tabela para os livros
conn.execute('CREATE TABLE livros (\
                id INTEGER PRIMARY KEY,\
                titulo TEXT,\
                autor TEXT,\
                editora TEXT,\
                ano_publicacao INTEGER,\
                isbn TEXT)')

# Criar uma tabela para as revistas
conn.execute('CREATE TABLE revistas (\
                id INTEGER PRIMARY KEY,\
                titulo TEXT,\
                autor TEXT,\
                editora TEXT,\
                ano_publicacao INTEGER,\
                issn TEXT,\
                volume INTEGER)')

# Criar uma tabela para as teses
conn.execute('CREATE TABLE teses (\
                id INTEGER PRIMARY KEY,\
                titulo TEXT,\
                autor TEXT,\
                programa_de_pos_graduacao TEXT,\
                ano_publicacao INTEGER,\
                orientador TEXT,\
                co_orientador TEXT)')

# Criar uma tabela para os usuarios
conn.execute('CREATE TABLE usuarios (\
                id INTEGER PRIMARY KEY,\
                nome TEXT,\
                filiacao TEXT,\
                endereco TEXT,\
                email TEXT,\
                telefone TEXT,\
                tipo_usuario TEXT)')

# Criar uma tabela para os emprestimos
conn.execute('CREATE TABLE emprestimos (\
                id INTEGER PRIMARY KEY,\
                id_livro INTEGER,\
                id_revista INTEGER,\
                id_tese INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                is_book INTEGER,\
                is_magazine INTEGER,\
                is_thesis INTEGER,\
                FOREIGN KEY(id_livro) REFERENCES livros(id),\
                FOREIGN KEY(id_revista) REFERENCES revistas(id),\
                FOREIGN KEY(id_tese) REFERENCES teses(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')

# Fechar a conexao com o banco de dados
conn.close()
