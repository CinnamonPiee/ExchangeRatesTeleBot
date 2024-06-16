
def valid_age(text: str) -> int | None:
    try:
        if 1 <= int(text) <= 99:
            count = int(text)
    except:
        return None

    return count