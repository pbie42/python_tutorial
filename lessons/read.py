# ipsum_file = open('./files/ipsum.txt')

# # for line in ipsum_file:
# # 	print(f"{line}")

# # ipsum_file.seek(0)

# # lines = ipsum_file.readlines()
# # print(f"{lines}")

# ipsum_file.seek(50)
# file_txt = ipsum_file.read(100)
# print(f"{file_txt}")
# ipsum_file.close()

def sequence_filter(line):
	return '>' not in line

with open("files/dna_sequence.txt") as dna_file:
	lines = dna_file.readlines()
	print(list(filter(sequence_filter, lines)))