# Sample Input - "xyz", 2
# Sampel Output - "zab"
# Time - O(N) Space - O(N)
def caesarCipherEncryptor(string, key):
	newLetter = []
	key = key % 26
	# Unicode a = 97
	# Unicode z = 122
	for i in string:
		letter_unicode = ord(i)+key
		if letter_unicode > 122:
			letter_unicode = 96 + letter_unicode % 122
		newLetter.append(chr(letter_unicode))
	return ''.join(newLetter)
