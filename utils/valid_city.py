

def valid_city(text: str) -> str | None:
    try:
        if text.isalpha():
            return str(text)
    except:
        return None