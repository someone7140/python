test_list = ["a", "b", "c", "d", "e", "f"]
output_list = list(map(lambda x: x[1] + str(x[0]), enumerate(test_list)))

print(output_list)
