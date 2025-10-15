import requests

def obter_info_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        nome = dados['name']
        tipos = [t['type']['name'] for t in dados['types']]
        habilidades = [h['ability']['name'] for h in dados['abilities']]

        print(f"Pokémon: {nome.capitalize()}")
        print("Tipos:", ", ".join(tipos))
        print("Habilidades:", ", ".join(habilidades))
    else:
        print(f"Pokémon '{nome}' não encontrado.")

if __name__ == "__main__":
    nome_pokemon = input("Digite o nome do Pokémon: ")
    obter_info_pokemon(nome_pokemon)