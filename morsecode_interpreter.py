
#encryption dictionary
dict_encrypt = {
	"a":".-","b":"-...","c":"-.-.","d":"-..",
	"e":".","f":"..-.","g":"--.","h":"....",
	"i":"..","j":".---","k":"-.-","l":".-..",
	"m":"--","n":"-.","o":"---","p":".--.",
	"q":"--.-","r":".-.","s":"...","t":"-",
	"u":"..-","v":"...-","w":".--","x":"-..-",
	"y":"-.--","z":"--..","0": "-----","1":".----",
	"2":"..---","3":"...--","4":"....-","5":".....",
	"6":"-....","7":"--...","8":"---..","9":"----.",
	".":".-.-.-",",": "--..--",":":"---...","!":"-.-.--","?": "..--..",
	"'": ".----.","-": "-....-","/": "-..-.","\"":".-..-.",
	"@":".--.-.","=":"-...-"," ": " ","\n": "\n"
}

#decrypton dictonary
dict_decrypt = dict([(v, k) for k, v in dict_encrypt.items()])

#encryption function
def encrypt():
    translation = ""
    for x in txt:
        translation += dict_encrypt.get(x) + " "	#add single space after every character map
    print(translation)
    return

#decryption function
def decrypt():
	translation = ""
	txt = txt.split(" ")
	for i, x in enumerate(txt):
		if x == "" and txt[i + 1] == "":	#check for concuring whitespacces and interprete as single space
			translation += " "
		elif x == "" and txt[i + 1] != "":	#check for single white space and does nothing
			pass
		else:
			translation += dict_decrypt.get(x)
	print(translation)
	return

def main():
	global txt
	txt = input("Input morsecode or text here: ")
	if txt.startswith('.') or txt.startswith('-'):	#checks if the input is a morsecode
		decrypt()
	elif txt == "exit":		#type "exit" to return to command line
		exit()
	else:					#if it is a plaintext input
		txt = txt.lower()
		encrypt()
	return main()

main()
