
import requests

if __name__ == "__main__":
    bank = 1
    resp = requests.get(f"https://brasilapi.com.br/api/banks/v1/{bank}")
    if resp.ok:
        data = resp.json()
        with open("script-result.txt", "wt") as f:
            f.write(f"Code: {bank}, Bank: {data['name']}")
    else:
        raise Exception("Error when attempt to connect with BrasilAPI")

