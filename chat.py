def read_file(filename):
	content = []
	with open(filename, 'r' , encoding='utf-8-sig') as f:
		for lines in f:
			lines = lines.strip()
			content.append(lines)
	return content

def convert(lines):
	new = []
	person = None
	for line in lines:
		if 'Allen' in line:
			person = 'Allen'
			continue
		elif 'Tom' in line:
			person = 'Tom'
			continue

		new.append(person + ': ' + line)

	return new

def print_data(new):
	for line in new:
		print(line)

def write_data(filename, new):
	with open(filename, 'w') as f:
		for line in new:
			f.write(line + '\n')

def main():
	input_filename = 'input.txt'
	output_filename = 'output.txt'
	content = read_file(input_filename)
	content = convert(content)
	write_data(output_filename, content)



main()
