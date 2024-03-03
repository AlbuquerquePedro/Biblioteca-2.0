from datetime import timedelta
import sqlite3
from datetime import datetime, timedelta
from tkinter import messagebox
import itertools
# Função para conectar ao banco de dados


def connect():
    conn = sqlite3.connect('biblioteca.db')
    return conn

# Função para inserir um novo livro na tabela "livros" com status inicial de disponível


def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn, status) VALUES (?, ?, ?, ?, ?, ?)",
                 (titulo, autor, editora, ano_publicacao, isbn, "disponível"))
    conn.commit()
    conn.close()

# Função para inserir uma nova revista na tabela "revista" com status inicial de disponível


def insert_magazine(titulo, autor, editora, ano_publicacao, issn, volume):
    conn = connect()
    conn.execute("INSERT INTO revistas (titulo, autor, editora, ano_publicacao, issn, volume, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (titulo, autor, editora, ano_publicacao, issn, volume, "disponível"))
    conn.commit()
    conn.close()

# Função para inserir uma nova tese na tabela "tese" com status inicial de disponível


def insert_thesis(titulo, autor, programa_de_pos_graduacao, ano_publicacao, orientador, co_orientador):
    conn = connect()
    conn.execute("INSERT INTO teses (titulo, autor, programa_de_pos_graduacao, ano_publicacao, orientador, co_orientador, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (titulo, autor, programa_de_pos_graduacao, ano_publicacao, orientador, co_orientador, "disponível"))
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


# Método para gerar IDs de empréstimo exclusivos com base na combinação de itens emprestados
def generate_loan_id(cursor):
    cursor.execute("SELECT MAX(id) FROM emprestimos")
    last_id = cursor.fetchone()[0]
    return last_id + 1 if last_id is not None else 1

# Função para inserir um empréstimo no banco de dados


def insert_loan(id_livro, id_revista, id_tese, id_usuario, data_emprestimo):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    try:
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

        is_book = is_magazine = is_thesis = False

        # Verificar se é um empréstimo de livro, revista e/ou tese
        if id_livro:
            is_book = True
        if id_revista:
            is_magazine = True
        if id_tese:
            is_thesis = True

        # Obter o tipo de usuário
        user_type = get_user_type(id_usuario)
        if user_type:
            # Converter data_emprestimo para um objeto datetime
            data_emprestimo = datetime.strptime(
                data_emprestimo, "%Y-%m-%d").date()
            devolution_date = calculate_devolution_date(
                user_type, data_emprestimo)

            # Inserir o empréstimo na tabela para cada tipo de item emprestado
            if is_book:
                loan_id = generate_loan_id(cursor)
                cursor.execute("INSERT INTO emprestimos (id, id_livro, id_usuario, data_emprestimo, data_devolucao, loan_type) VALUES (?, ?, ?, ?, ?, ?)",
                               (loan_id, id_livro, id_usuario, data_emprestimo, devolution_date.isoformat(), "Livro"))
                cursor.execute(
                    "UPDATE livros SET status='alugado' WHERE id=?", (id_livro,))
                conn.commit()
            if is_magazine:
                loan_id = generate_loan_id(cursor)
                cursor.execute("INSERT INTO emprestimos (id, id_revista, id_usuario, data_emprestimo, data_devolucao, loan_type) VALUES (?, ?, ?, ?, ?, ?)",
                               (loan_id, id_revista, id_usuario, data_emprestimo, devolution_date.isoformat(), "Revista"))
                cursor.execute(
                    "UPDATE revistas SET status='alugado' WHERE id=?", (id_revista,))
                conn.commit()
            if is_thesis:
                loan_id = generate_loan_id(cursor)
                cursor.execute("INSERT INTO emprestimos (id, id_tese, id_usuario, data_emprestimo, data_devolucao, loan_type) VALUES (?, ?, ?, ?, ?, ?)",
                               (loan_id, id_tese, id_usuario, data_emprestimo, devolution_date.isoformat(), "Tese"))
                cursor.execute(
                    "UPDATE teses SET status='alugado' WHERE id=?", (id_tese,))
                conn.commit()
        else:
            raise ValueError("ID de usuário inválido ou não encontrado.")
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()


def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.tipo_usuario, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM livros \
                           INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.loan_type = 'Livro'").fetchall()
    conn.close()
    return result


def get_magazine_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, revistas.titulo, usuarios.nome, usuarios.tipo_usuario, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM revistas \
                           INNER JOIN emprestimos ON revistas.id = emprestimos.id_revista \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.loan_type = 'Revista'").fetchall()
    conn.close()
    return result


def get_thesis_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, teses.titulo, usuarios.nome, usuarios.tipo_usuario, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM teses \
                           INNER JOIN emprestimos ON teses.id = emprestimos.id_tese \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.loan_type = 'Tese'").fetchall()
    conn.close()
    return result


def get_status_usuario(id_usuario):
    conn = connect()
    cursor = conn.cursor()

    # Consulta ao banco de dados para obter o status do usuário com base no ID
    cursor.execute(
        "SELECT status FROM usuarios WHERE id=?", (id_usuario,))
    status = cursor.fetchone()

    conn.close()

    # Se o status existir no banco de dados, retorna o valor correspondente
    if status:
        return status[0]  # Retorna o status
    else:
        return None  # Retorna None se o usuário não for encontrado


def calcular_multa(dias_atraso):
    valor_base = 2.50
    multa = valor_base * dias_atraso
    if dias_atraso > 30:
        multa *= 2  # Multa dobra a cada 30 dias de atraso
    return round(multa, 2)


# ver emprestimo atrasado


def get_emprestimos_atrasados():
    conn = connect()
    cursor = conn.cursor()

    # Obter todos os empréstimos com data de devolução passada
    cursor.execute("SELECT emprestimos.id, emprestimos.loan_type, usuarios.tipo_usuario, usuarios.status, emprestimos.data_devolucao, livros.titulo, revistas.titulo, teses.titulo \
                    FROM emprestimos \
                    INNER JOIN usuarios ON emprestimos.id_usuario = usuarios.id \
                    LEFT JOIN livros ON emprestimos.id_livro = livros.id \
                    LEFT JOIN revistas ON emprestimos.id_revista = revistas.id \
                    LEFT JOIN teses ON emprestimos.id_tese = teses.id \
                    WHERE emprestimos.data_devolucao < ? AND (usuarios.status = 'débito' OR usuarios.status = 'nada consta')", (datetime.now().date(),))

    emprestimos_atrasados = cursor.fetchall()
    dados = []

    for emprestimo in emprestimos_atrasados:
        id_emprestimo, loan_type, tipo_usuario, status_usuario, data_devolucao, livro_titulo, revista_titulo, tese_titulo = emprestimo
        titulo = livro_titulo if loan_type == 'Livro' else revista_titulo if loan_type == 'Revista' else tese_titulo
        dias_atraso = (datetime.now().date() -
                       datetime.strptime(data_devolucao, "%Y-%m-%d").date()).days
        valor_multa = calcular_multa(dias_atraso)
        dados.append((id_emprestimo, titulo, loan_type, tipo_usuario,
                     status_usuario, dias_atraso, valor_multa))

    conn.close()
    return dados


def update_loan_return_date(loan_id, return_date):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Verificar se o empréstimo existe
    if not verificar_emprestimo_existe(loan_id):
        conn.close()
        return "Empréstimo não encontrado."

    # Verificar se a data de retorno está no formato correto AAAA-MM-DD
    try:
        data_devolucao = datetime.strptime(return_date, '%Y-%m-%d').date()
    except ValueError:
        conn.close()
        return "Formato de data inválido. Use o formato AAAA-MM-DD."

    # Verificar se a data de retorno está dentro do intervalo permitido
    data_emprestimo, _ = obter_datas_emprestimo(loan_id)
    data_atual = datetime.now().date()
    if data_devolucao < data_emprestimo or data_devolucao > data_atual:
        conn.close()
        return "Data de devolução fora do intervalo permitido."

    # Verificar se o usuário possui débitos
    if verificar_debitos_usuario(loan_id):
        conn.close()
        return "Usuário possui débitos pendentes. Não é possível atualizar a data de devolução."

    # Atualizar a data de devolução do empréstimo
    try:
        cursor.execute(
            "UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (return_date, loan_id))
        conn.commit()
        conn.close()
        return "Data de devolução atualizada com sucesso."
    except Exception as e:
        conn.rollback()
        conn.close()
        return str(e)


def verificar_emprestimo_existe(id_emprestimo):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM emprestimos WHERE id=?", (id_emprestimo,))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0


def obter_datas_emprestimo(id_emprestimo):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT data_emprestimo, data_devolucao FROM emprestimos WHERE id=?", (id_emprestimo,))
    data_emprestimo, data_devolucao = cursor.fetchone()
    conn.close()
    return datetime.strptime(data_emprestimo, '%Y-%m-%d').date(), datetime.strptime(data_devolucao, '%Y-%m-%d').date()


def verificar_debitos_usuario(loan_id):
    conn = connect()
    cursor = conn.cursor()

    try:
        # Obter o ID do usuário associado ao empréstimo
        cursor.execute(
            "SELECT id_usuario FROM emprestimos WHERE id=?", (loan_id,))
        id_usuario = cursor.fetchone()[0]

        # Verificar o status do usuário
        cursor.execute("SELECT status FROM usuarios WHERE id=?", (id_usuario,))
        status_usuario = cursor.fetchone()[0]

        if status_usuario == 'débito':
            conn.close()
            return True
        else:
            conn.close()
            return False
    except Exception as e:
        conn.close()
        raise e


def realizar_devolucao_emprestimo(id_emprestimo):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT loan_type, id_livro, id_revista, id_tese FROM emprestimos WHERE id=?", (id_emprestimo,))
    emprestimo = cursor.fetchone()
    if emprestimo:
        loan_type, id_livro, id_revista, id_tese = emprestimo
        item_id = id_livro or id_revista or id_tese
        if item_id:
            if loan_type == 'Livro':
                cursor.execute(
                    "UPDATE livros SET status='disponível' WHERE id=?", (item_id,))
            elif loan_type == 'Revista':
                cursor.execute(
                    "UPDATE revistas SET status='disponível' WHERE id=?", (item_id,))
            elif loan_type == 'Tese':
                cursor.execute(
                    "UPDATE teses SET status='disponível' WHERE id=?", (item_id,))
        cursor.execute("DELETE FROM emprestimos WHERE id=?", (id_emprestimo,))
        conn.commit()
        conn.close()
        return "Empréstimo devolvido com sucesso."
    else:
        conn.close()
        return "Empréstimo não encontrado."


def renovar_emprestimo(id_emprestimo, data_atual):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT tipo_usuario FROM usuarios JOIN emprestimos ON usuarios.id=emprestimos.id_usuario WHERE emprestimos.id=?", (id_emprestimo,))
    tipo_usuario = cursor.fetchone()[0]
    nova_data_devolucao = calculate_devolution_date(data_atual, tipo_usuario)
    cursor.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?",
                   (nova_data_devolucao.strftime('%Y-%m-%d'), id_emprestimo))
    conn.commit()
    conn.close()


def calculate_devolution_date(data_atual, tipo_usuario):
    prazos_emprestimo = {
        "Aluno de graduação": 7,
        "Aluno de pós-graduação": 15,
        "Professor": 60
    }
    prazo_emprestimo = prazos_emprestimo.get(tipo_usuario)
    if prazo_emprestimo is None:
        raise ValueError("Tipo de usuário inválido.")
    return data_atual + timedelta(days=prazo_emprestimo)

# insert_book("One Piece", "Oda", "Nao sei", 5662, "5788598270692")


'''# Exemplo de uso das funções
insert_book("One Piece", "Oda", "Nao sei", 5662, "5788598270692")
insert_user("João", "Silva", "Rua A, 123", "joao.silva@email.com", "(11) 1234-5678")
insert_loan(1, 1, "2022-03-25", None)
books_on_loan = get_books_on_loan()
print(books_on_loan)
update_loan_return_date(1, "2022-03-28")'''
