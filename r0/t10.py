morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9'
    }

encoded = input()
words = encoded.split('/')
#print(words)

def decoding(morse):
  decoded_word = ''
  morse_letter = morse.split(' ')
  #print(decoding1)
  for i in morse_letter:
    #print(i)
    for key, value in morse_code_dict.items():
      if i == key:
        decoded_word += value
  decoded_word += ' '
  return decoded_word

def decode(words):
  decoded_message = ''
  for word in words:
    morse = ''
    #print(word)
    chars = word.split()
    #print(chars)
    for char in chars:
      #print(char)
      for i in char:
        if i.isupper():
          morse += '-'
        elif i.islower():
          morse += '.'
      morse += ' '
    decoded_message += decoding(morse)
  return decoded_message


print(decode(words))
