from sys import argv

def lexer(filename):
	list=[]
	file=open(filename, 'r')
	code=file.readlines()
	return list
	

def main():
	lexer(argv[1])
	return

main()
