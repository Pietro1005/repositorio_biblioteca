import requests

url = "https://www.carqueryapi.com/api/0.3/?cmd=getMakes"

response = requests.get(url)

if response.status_code == 200:

    text = response.text

    json_str = text.strip()
    if json_str.startswith("var makes ="):
        json_str = json_str[len("var makes = "):]
    if json_str.endswith(";"):
        json_str = json_str[:-1]
    
    import json
    data = json.loads(json_str)
    
    makes = data.get('Makes', [])
    
    print("Marcas de carros encontradas:")
    for make in makes[:10]:
        print(f"- {make['make_display']} ({make['make_country']})")
else:
    print(f"Erro ao acessar API. Status: {response.status_code}")