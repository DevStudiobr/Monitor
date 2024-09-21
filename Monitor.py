import requests

# Lista de sites para monitorar
sites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.example.com"  # Adicione outros sites aqui
]

def check_sites():
    for site in sites:
        try:
            response = requests.get(site)
            if response.status_code == 200:
                print(f"{site} está online.")
            else:
                print(f"{site} está fora do ar. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {site}: {e}")

if __name__ == "__main__":
    check_sites()
