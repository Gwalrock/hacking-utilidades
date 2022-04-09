'''
Script que decodifica el campo SPAMCAUSE
Uso : python spamcause.py cadena_de_la_etiqueta_X-VR-SPAMCAUSE
'''

def decode(msg):
   text = []
   for i in range(0, len(msg), 2):
       text.append(unrot(msg[i: i + 2]))
   return str.join('', text)


def unrot(pair, key=ord('x')):
   offset = 0
   for c in 'cdefgh':
       if c in pair:
           offset = (ord('g') - ord(c)) * 16
           break
   return chr(sum(ord(c) for c in pair) - key - offset)

 
if __name__ == '__main__':
   import sys
   if len(sys.argv) < 2:
      print("Debe introducir la cadena contenida después de la etiqueta X-VR-SPAMCAUSE")
   else:
      print(decode(sys.argv[1]))
