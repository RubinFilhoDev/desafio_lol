import requests
import pymysql

# Defina as informações de conexão
host = 'localhost'
database = 'desafio_lol'
user = 'root'
password = '1234'

# Estabeleça a conexão
conn = pymysql.connect(host=host, user=user, password=password, db=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

url = "http://ddragon.leagueoflegends.com/cdn/13.6.1/data/en_US/champion.json"
response = requests.get(url)

spells_key = {0: 'Q', 1: 'W', 2: 'E', 3: 'R'}

if response.status_code == 200:
  
    json_data = response.json()
    champions = json_data['data']

    for chave, value in champions.items():
        champion_data = {
            'id': value['id'], 
            'key': value['key'],  
            'name': value['name'], 
            'title': value['title'], 
            'blurb': value['blurb'],
            'version': value['version']
            }
    
        base_url_spells = "http://ddragon.leagueoflegends.com/cdn/13.6.1/data/en_US/champion/"+chave+".json"
        response_spells = requests.get(base_url_spells)
        json_spells = response_spells.json()
        for index, spell in enumerate(json_spells['data'][chave]['spells']):
            spell_champion = {
                'id': spell['id'], 
                'name': spell['name'], 
                'description': spell['description'],
                'champion_id' : value['id'],
                'spells_index' : index,
                'spells_key' : spells_key[index]
            }
            
            # Adiciona a lista de habilidades ao dicionário do campeão atual
            query_spells = "INSERT INTO spells (id, name, description, champion_id, spells_index, spells_key) VALUES (%s, %s, %s, %s, %s, %s)"
            values_spells = (spell_champion['id'].replace(value['id'], ''), spell_champion['name'], spell_champion['description'], spell_champion['champion_id'], index, spell_champion['spells_key'])
            cursor.execute(query_spells, values_spells)

        
else:
    
    print("Erro ao fazer a requisição HTTP: ", response.status_code)

conn.commit()
conn.close()

