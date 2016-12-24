import os

def decoder ():

    shifter = -10
    shifters  = raw_input("Enter keyphrase : ")

#    print shifters[-1:]
    shifter = ord(shifters[-1:]) * -1

    file_content = open('cipher.txt', 'r')

    file_content_list = file_content.readlines()

    new_list = []
    for sentence in file_content_list:
        #remove the \n separator 
        newer = sentence.find('\\')
        sentence = sentence[:newer]
 #       print sentence
        new_list.append(sentence)
#    print 'New list is : ', new_list

    decrypted = []
    for sentence in new_list:
        dsentence = ""
        for character in sentence:
            dsentence = dsentence + ASCII(character,shifter)
#        print 'the en sent is :', esentence
        decrypted.append(dsentence)
#    print decrypted

    wfile = open('deciphed.txt',"w")
    for sentence in decrypted:
        wfile.write(sentence)
        wfile.write('\n')
    wfile.close()
    return

def ASCII(character, shifter):
    if ord(character) == 32:
        return character
    asciinum = ord(character)+shifter
    if asciinum < 0:
        asciinum = 255 + asciinum
 #   print 'new ascii num is : ', asciinum
#    print 'new ascii value is : ', chr(asciinum)
    return chr(asciinum)

decoder() 


