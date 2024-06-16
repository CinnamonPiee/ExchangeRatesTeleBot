import phonenumbers


def valid_number(text: str) -> bool | None:
	try:
		my_number = phonenumbers.parse(text)
		return phonenumbers.is_valid_number(my_number)
	except:
		return None