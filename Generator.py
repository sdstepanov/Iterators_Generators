def flat_generator(my_list):
	index = 0
	index_1 = 0
	while True:
		yield my_list[index][index_1]
		index_1 += 1
		if index_1 == len(my_list[index]):
			index_1 = 0
			index += 1
		if index == len(my_list):
			break


def flat_generator_2(my_list):
	for item in my_list:
		if isinstance(item, list):
			for element in flat_generator_2(item):
				yield element
		else:
			yield item
