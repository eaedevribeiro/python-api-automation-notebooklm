import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status:", response.status_code)

if response.status_code == 200:
    dados = response.json()

    print("ID:", dados["id"])
    print("Título:", dados["title"])
    print("Conteúdo:", dados["body"])
else:
    print("Erro ao consultar a API.")
