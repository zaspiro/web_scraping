from dbconnection import create_database, insert_items, display_items
from webscrapping_skyrim import collect_all_items

def main():
    base_url = 'https://skyrimcommands.com/items/'
    db_name = 'items.db'

    # Criar o banco de dados e a tabela
    create_database(db_name)

    # Coletar todos os itens
    all_items = collect_all_items(base_url)

    # Inserir os itens no banco de dados
    insert_items(db_name, all_items)

    # Exibir os itens do banco de dados
    display_items(db_name)

if __name__ == '__main__':
    main()