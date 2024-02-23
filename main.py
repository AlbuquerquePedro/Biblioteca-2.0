import sqlite3
from view import *

# Define a função para exibir o menu e receber a entrada do usuário


def show_menu():
    print("Selecione uma opção:")
    print("1. Inserir um novo livro")
    print("2. Inserir uma nova revista")
    print("3. Inserir uma nova tese")
    print("4. Inserir um novo usuário")
    print("5. Exibir todos os usuarios")
    print("6. Realizar um empréstimo")
    print("7. Atualizar a data de devolução de um empréstimo")
    print("8. Exibir todos os livros emprestados no momento")
    print("9. Exibir todas as revistas emprestadas no momento")
    print("10. Exibir todas as teses emprestadas no momento")
    print("11. Exibir todos os livros do banco de dados")
    print("12. Exibir todos as revistas do banco de dados")
    print("13. Exibir todos as teses do banco de dados")
    print("0. Sair")

    choice = input("Digite o número da opção desejada: ")
    return choice


# Loop principal do programa
while True:
    choice = show_menu()

    if choice == "1":
        title = input("Digite o título do livro: ")
        author = input("Digite o nome do autor do livro: ")
        publisher = input("Digite o nome da editora do livro: ")
        year = input("Digite o ano de publicação do livro: ")
        isbn = input("Digite o ISBN do livro: ")

        insert_book(title, author, publisher, year, isbn)
        print("Livro inserido com sucesso!")

    if choice == "2":
        title = input("Digite o título da revista: ")
        author = input("Digite o nome do autor da revista: ")
        publisher = input("Digite o nome da editora da revista: ")
        year = input("Digite o ano de publicação da revista: ")
        issn = input("Digite o ISSN da revista: ")
        volume = input("Digite o volume da revista: ")

        insert_magazine(title, author, publisher, year, issn, volume)
        print("Revista inserida com sucesso!")

    if choice == "3":
        title = input("Digite o título da tese: ")
        author = input("Digite o nome do autor da tese: ")
        graduate_program = input(
            "Digite o nome do programa de pós-graduação: ")
        year = input("Digite o ano de publicação da tese: ")
        advisor = input("Digite o orientador da tese: ")
        co_supervisor = input("Digite o co-orientador da tese: ")

        insert_thesis(title, author, graduate_program,
                      year, advisor, co_supervisor)
        print("Tese inserida com sucesso!")

    elif choice == "4":
        first_name = input("Digite o primeiro nome do usuário: ")
        last_name = input("Digite a filiação do usuário: ")
        address = input("Digite o endereço do usuário: ")
        email = input("Digite o endereço de e-mail do usuário: ")
        phone = input("Digite o número de telefone do usuário: ")
        user_type = input(
            "Digite o tipo de usuário (Aluno de graduação, Aluno de pós-graduação, Professor): ")

        insert_user(first_name, last_name, address, email, phone, user_type)
        print("Usuário inserido com sucesso!")

    elif choice == '5':
        print("Listando todos os usuários...\n")
        users = get_users()
        for user in users:
            print(f"ID: {user[0]}\nNome: {user[1]}\nTelefone: {
                  user[5]}\nEmail: {user[4]}\nTipo: {user[6]}\n")

    elif choice == "6":
        user_id = input("Digite o ID do usuário: ")
        book_id = input("Digite o ID do livro: ")
        loan_date = input(
            "Digite a data de empréstimo (formato: AAAA-MM-DD): ")

        insert_loan(book_id, None, None, user_id, loan_date)
        print("Empréstimo realizado com sucesso!")

    elif choice == "7":
        loan_id = input("Digite o ID do empréstimo: ")
        return_date = input(
            "Digite a nova data de devolução (formato: AAAA-MM-DD): ")

        update_loan_return_date(loan_id, return_date)
        print("Data de devolução atualizada com sucesso!")

    elif choice == "8":
        books_on_loan = get_books_on_loan()
        print("Livros emprestados no momento:")
        for book in books_on_loan:
            print(f"ID empréstimo: {book[0]}, Título: {book[1]}, Nome do usuário: {book[2]} {
                  book[3]}, Data do empréstimo: {book[4]}, Data da devolução: {book[5]}")

    elif choice == "9":
        magazine_on_loan = get_magazine_on_loan()
        print("Revistas emprestadas no momento:")
        for magazine in magazine_on_loan:
            print(f"ID empréstimo: {magazine[0]}, Título: {magazine[1]}, Nome do usuário: {magazine[2]} {
                  magazine[3]}, Data do empréstimo: {magazine[4]}, Data da devolução: {magazine[5]}")

    elif choice == "10":
        thesis_on_loan = get_thesis_on_loan()
        print("Teses emprestadas no momento:")
        for thesis in thesis_on_loan:
            print(f"ID empréstimo: {thesis[0]}, Título: {thesis[1]}, Nome do usuário: {thesis[2]} {
                  thesis[3]}, Data do empréstimo: {thesis[4]}, Data da devolução: {thesis[5]}")

    elif choice == "11":
        books = get_books()
        print("Livros:")
        for book in books:
            print(f"Título: {book[1]}, Autor: {book[2]}, Editora: {
                  book[3]}, Ano: {book[4]}, ISBN: {book[5]}")

    elif choice == "12":
        magazines = get_magazine()
        print("Revistas:")
        for magazine in magazines:
            print(f"Título: {magazine[1]}, Autor: {magazine[2]}, Editora: {
                  magazine[3]}, Ano: {magazine[4]}, ISSN: {magazine[5]}, Volume: {magazine[6]}")

    elif choice == "13":
        theses = get_thesis()
        print("Teses:")
        for thesis in theses:
            print(f"Título: {thesis[1]}, Autor: {thesis[2]}, Programa de pós-graduação: {
                  thesis[3]}, Ano: {thesis[4]}, Orientador: {thesis[5]}, Co-orientador: {thesis[6]}")

    elif choice == "0":
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
