import requests  # Importa a biblioteca requests para fazer a solicitação HTTP em Python.
from bs4 import BeautifulSoup  # Importa a classe BeautifulSoup do módulo bs4.

def extract_data(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    
    figure_element = soup.find('table', id='table')
    
    items = {}

    if figure_element: #Achar o nome dos itens
        tbody_element = figure_element.find('tbody')
        if tbody_element:
            tr_elements = tbody_element.find_all('tr')
            
            for tr_element in tr_elements:
                code = tr_element.find_all('td')[1].text.strip()
                code = treat_code(code)
                name = tr_element.find_all('a')[0].text.strip()
                
                original_name = name
                suffix = 2
                while name in items:
                    name = f'{original_name}{suffix}'
                    suffix += 1
                
                items[name] = code
    return items

def treat_code(code):
    if 'Dawnguard DLC Code' in code:
        treated_code = code.replace('Dawnguard DLC Code + ', '02')
        return treated_code
    elif 'Hearthfire DLC Code' in code:
        treated_code = code.replace('Hearthfire DLC Code + ', '03')
        return treated_code
    elif 'Dragonborn DLC Code' in code:
        treated_code = code.replace('Dragonborn DLC Code + ', '04')
        return treated_code
    return code

def collect_all_items(base_url):
    page_number = 1
    all_items = {}

    while True:
        if page_number == 1:
            url_now = base_url
        else:
            url_now = f'{base_url}{page_number}'

        print(f'Coletando dados de: {url_now}')

        items = extract_data(url_now)
        if items:
            all_items.update(items)
        else:
            print('Fim das páginas ou página não encontrada.')
            break

        page_number += 1
    return all_items