
def get_actual_currency() -> list[str]:
	data_cur = []
	with open("data_currency.txt", "r", encoding="utf-8") as file:
		data = file.readlines()
		for i in data:
			data_cur.append(i.strip())

	return data_cur