import math
import sys
from colorama import Fore
from PIL import Image

def main():
	try:
		if sys.argv[1] == "--hide":
			unitoascii(sys.argv[2])

		elif sys.argv[1] == "--image":
			image(sys.argv[2])
	except:
		pass

def unitoascii(message):
	try:
		vide = []
		for x in message:
			vide.append(ord(x))

		encode = []
		for x in vide:
			enc = (x+5)/(2*5)*(3+2)/(12-5)
			encode.append(enc)

		print(f"{Fore.GREEN}[Encoded RGB]: {Fore.YELLOW}[" + ", ".join([str(x) for x in encode]) + "]")

		message = []
		decode = []
		for x in encode:
			dec = x*14-5
			a = chr(math.trunc(dec))
			message.append(a)
			b = math.trunc(dec)
			decode.append(b)

		print(f"{Fore.GREEN}[Decoded RGB]: {Fore.YELLOW}[" + ", ".join([str(x) for x in decode]) + "]")

		for x in message:
			print(f"{Fore.GREEN}[Message]: {Fore.YELLOW}" + "".join(message))
			break
	except:
		pass

def image(image):
	try:
		pixels = list(lol.getdata())
		array = [str(x) for x in pixels]
		with open("rgb.png", "w") as file:
			for line in array:
				file.write(line)
			file.close()
			print(f"{Fore.GREEN}[File]: {Fore.YELLOW}" + "".join(str(file)))
	except:
		pass

main()
