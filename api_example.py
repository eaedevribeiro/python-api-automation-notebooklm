import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"


def buscar_post(url: str) -> dict | None:
    """Faz um GET na API e devolve o JSON como dicionário, ou None se falhar."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # levanta erro para status 4xx e 5xx
    except requests.Timeout:
        print("Erro: a API demorou demais para responder.")
        return None
    except requests.RequestException as erro:
        print(f"Erro ao consultar a API: {erro}")
        return None

    print("Status:", response.status_code)
    return response.json()


if __name__ == "__main__":
    dados = buscar_post(URL)
    if dados:
        print("ID:", dados["id"])
        print("Título:", dados["title"])
        print("Conteúdo:", dados["body"])
