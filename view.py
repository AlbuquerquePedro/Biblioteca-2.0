import sqlite3
from datetime import datetime, timedelta
# Função para conectar ao banco de dados


def connect():
    conn = sqlite3.connect('biblioteca.db')
    return conn

# Função para inserir um novo livro na tabela "livros"


def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)",
                 (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Função para inserir uma nova revista na tabela "revista"


def insert_magazine(titulo, autor, editora, ano_publicacao, issn, volume):
    conn = connect()
    conn.execute("INSERT INTO revistas (titulo, autor, editora, ano_publicacao, issn, volume) VALUES (?, ?, ?, ?, ?, ?)",
                 (titulo, autor, editora, ano_publicacao, issn, volume))
    conn.commit()
    conn.close()

# Função para inserir uma nova tese na tabela "tese"


def insert_thesis(titulo, autor, programa_de_pos_graduacao, ano_publicacao, orientador, co_orientador):
    conn = connect()
    conn.execute("INSERT INTO teses (titulo, autor, programa_de_pos_graduacao, ano_publicacao, orientador, co_orientador) VALUES (?, ?, ?, ?, ?, ?)",
                 (titulo, autor, programa_de_pos_graduacao, ano_publicacao, orientador, co_orientador))
    conn.commit()
    conn.close()

# Função que retorna todos os livros do banco de dados


def get_books():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("SELECT * FROM livros")
    magazine = c.fetchall()
    conn.close()
    return magazine

# Função que retorna todos as revistas do banco de dados


def get_magazine():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("SELECT * FROM revistas")
    magazine = c.fetchall()
    conn.close()
    return magazine

# Função que retorna todos as teses do banco de dados


def get_thesis():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("SELECT * FROM teses")
    thesis = c.fetchall()
    conn.close()
    return thesis

# Função para inserir um novo usuário na tabela "usuarios"


# Adicionando o novo parâmetro tipo_usuario
def insert_user(nome, filiacao, endereco, email, telefone, tipo_usuario):
    conn = connect()
    conn.execute("INSERT INTO usuarios (nome, filiacao, endereco, email, telefone, tipo_usuario) VALUES (?, ?, ?, ?, ?, ?)",  # Incluindo o tipo_usuario na consulta SQL
                 (nome, filiacao, endereco, email, telefone, tipo_usuario))
    conn.commit()
    conn.close()
# Função que retorna todos os usuários do banco de dados


def get_users():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users


def get_user_type(user_id):
    # Função para obter o tipo de usuário a partir do ID do usuário
    # Você precisa implementar essa função para consultar o banco de dados e retornar o tipo de usuário correspondente ao ID fornecido
    # Aqui está um exemplo de como fazer isso:
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT tipo_usuario FROM usuarios WHERE id=?", (user_id,))
    user_type = cursor.fetchone()
    conn.close()
    if user_type:
        return user_type[0]
    else:
        return None


# Função para inserir um novo empréstimo na tabela "emprestimos"


def insert_loan(id_livro, id_revista, id_tese, id_usuario, data_emprestimo):
    conn = connect()

    # Função para calcular a data de devolução com base no tipo de usuário
    def calculate_devolution_date(user_type, emprestimo_date):
        if user_type == "Aluno de graduação":
            return emprestimo_date + timedelta(days=7)
        elif user_type == "Aluno de pós-graduação":
            return emprestimo_date + timedelta(days=15)
        elif user_type == "Professor":
            return emprestimo_date + timedelta(days=60)
        else:
            raise ValueError("Tipo de usuário inválido.")

    # Verificar se os IDs dos itens existem no banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM livros WHERE id=?", (id_livro,))
    livro_exists = cursor.fetchone()[0] > 0
    cursor.execute("SELECT COUNT(*) FROM revistas WHERE id=?", (id_revista,))
    revista_exists = cursor.fetchone()[0] > 0
    cursor.execute("SELECT COUNT(*) FROM teses WHERE id=?", (id_tese,))
    tese_exists = cursor.fetchone()[0] > 0

    if livro_exists or revista_exists or tese_exists:
        # Obter o último ID de empréstimo na tabela
        cursor.execute("SELECT MAX(id) FROM emprestimos")
        last_id = cursor.fetchone()[0]
        new_id = last_id + 1 if last_id is not None else 1

        # Obter o tipo de usuário
        user_type = get_user_type(id_usuario)
        if user_type:
            # Converter data_emprestimo para um objeto datetime
            data_emprestimo = datetime.strptime(
                data_emprestimo, "%Y-%m-%d").date()
            devolution_date = calculate_devolution_date(
                user_type, data_emprestimo)

            # Determinar se é um empréstimo de livro, revista, tese ou uma combinação
            if id_livro and not id_revista and not id_tese:  # Empréstimo de apenas um livro
                is_book = 1
                is_magazine = 0
                is_thesis = 0
                data_devolucao = devolution_date
            elif id_revista and not id_livro and not id_tese:  # Empréstimo de apenas uma revista
                is_book = 0
                is_magazine = 1
                is_thesis = 0
                data_devolucao = devolution_date
            elif id_tese and not id_livro and not id_revista:  # Empréstimo de apenas uma tese
                is_book = 0
                is_magazine = 0
                is_thesis = 1
                data_devolucao = devolution_date
            elif id_livro and id_revista and not id_tese:  # Empréstimo de um livro e uma revista
                is_book = 1
                is_magazine = 1
                is_thesis = 0
                data_devolucao = devolution_date
            elif id_livro and id_tese and not id_revista:  # Empréstimo de um livro e uma tese
                is_book = 1
                is_magazine = 0
                is_thesis = 1
                data_devolucao = devolution_date
            elif id_revista and id_tese and not id_livro:  # Empréstimo de uma revista e uma tese
                is_book = 0
                is_magazine = 1
                is_thesis = 1
                data_devolucao = devolution_date
            elif id_livro and id_revista and id_tese:  # Empréstimo de um livro, uma revista e uma tese
                is_book = 1
                is_magazine = 1
                is_thesis = 1
                data_devolucao = devolution_date
            else:
                raise ValueError(
                    "Combinação de itens inválida para empréstimo.")

            # Inserir o empréstimo no banco de dados
            cursor.execute("INSERT INTO emprestimos (id, id_livro, id_revista, id_tese, id_usuario, data_emprestimo, data_devolucao, is_book, is_magazine, is_thesis) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (new_id, id_livro, id_revista, id_tese, id_usuario, data_emprestimo, data_devolucao, is_book, is_magazine, is_thesis))
            conn.commit()
            conn.close()
        else:
            raise ValueError("ID de usuário inválido ou não encontrado.")
    else:
        raise ValueError(
            "Pelo menos um dos IDs de item fornecidos não existe.")


def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.filiacao, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM livros \
                           INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.data_devolucao  AND emprestimos.is_book = 1 AND emprestimos.is_magazine = 0 AND emprestimos.is_thesis = 0 OR emprestimos.is_book = 1 AND emprestimos.is_magazine = 1 AND emprestimos.is_thesis = 0 OR emprestimos.is_book = 1 AND emprestimos.is_magazine = 1 AND emprestimos.is_thesis = 1").fetchall()
    conn.close()
    return result


def get_magazine_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, revistas.titulo, usuarios.nome, usuarios.filiacao, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM revistas \
                           INNER JOIN emprestimos ON revistas.id = emprestimos.id_revista \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.data_devolucao AND emprestimos.is_magazine = 1 AND emprestimos.is_book = 0 AND emprestimos.is_thesis = 0 OR emprestimos.is_magazine = 1 AND emprestimos.is_book = 1 AND emprestimos.is_thesis = 0 OR emprestimos.is_magazine = 1 AND emprestimos.is_book = 1 AND emprestimos.is_thesis = 1").fetchall()
    conn.close()
    return result


def get_thesis_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, teses.titulo, usuarios.nome, usuarios.filiacao, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM teses \
                           INNER JOIN emprestimos ON teses.id = emprestimos.id_tese \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.data_devolucao AND emprestimos.is_thesis = 1 AND emprestimos.is_book = 0 AND emprestimos.is_magazine = 0 OR emprestimos.is_thesis = 1 AND emprestimos.is_book = 1 AND emprestimos.is_magazine = 0 OR emprestimos.is_thesis = 1 AND emprestimos.is_book = 1 AND emprestimos.is_magazine = 1").fetchall()
    conn.close()
    return result

# Função para atualizar a data de devolução de um empréstimo


def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?",
                 (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()

# insert_book("One Piece", "Oda", "Nao sei", 5662, "5788598270692")


'''# Exemplo de uso das funções
insert_book("One Piece", "Oda", "Nao sei", 5662, "5788598270692")
insert_user("João", "Silva", "Rua A, 123", "joao.silva@email.com", "(11) 1234-5678")
insert_loan(1, 1, "2022-03-25", None)
books_on_loan = get_books_on_loan()
print(books_on_loan)
update_loan_return_date(1, "2022-03-28")'''
