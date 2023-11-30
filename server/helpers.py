import requests


def get_all_berries_info():
    try:
        pokeapi_url = "https://pokeapi.co/api/v2/berry/"
        response = requests.get(pokeapi_url)
        data = response.json()
        all_berries = []

        for result in data.get("results"):
            berry_url = result.get("url")
            berry_info = get_berry_info_from_url(berry_url)
            all_berries.append(berry_info)

        return all_berries
    except Exception as e:
        print(e)
        raise e


def get_berry_info_from_url(berry_url):
    try:
        response = requests.get(berry_url)
        data = response.json()
        return data

    except Exception as e:
        print(e)
        raise e
