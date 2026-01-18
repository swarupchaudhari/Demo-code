try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error:", e)