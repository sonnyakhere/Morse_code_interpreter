

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
	".":".-.-.-",",": "--..--",":":"---...","?": "..--..",
	"'": ".----.","-": "-....-","/": "-..-.","\"":".-..-.",
	"@":".--.-.","=":"-...-"," ": " ","\n": "\n"
}
dict_decrypt = dict([(v, k) for k, v in dict_encrypt.items()])


def encrypt():
    translation = ""
    for x in txt:
        translation += dict_encrypt.get(x) + " "
    print(translation)
    return

def decrypt():
	global txt
	translation = ""
	txt = txt.split(" ")
	for i, x in enumerate(txt):
		if x == "" and txt[i + 1] == "":
			translation += " "
		elif x == "" and txt[i + 1] != "":
			pass
		else:
			translation += dict_decrypt.get(x)
	print(translation)
	return

def main():
	global txt
	txt = input("Input morse code or text here: ")
	if txt.startswith('.') or txt.startswith('-'):
		decrypt()
	else:
		txt = txt.lower()
		encrypt()
	return main()

main()
