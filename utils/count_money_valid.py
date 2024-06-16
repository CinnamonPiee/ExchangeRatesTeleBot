
def valid_count_money(text: str) -> int | None:
    try:
        if int(text) == 0:
            count = 0
        count = int(text)
    except:
        return None

    return count