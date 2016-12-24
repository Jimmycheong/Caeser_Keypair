import os

def coder():

    file_name = raw_input("Enter a file name : ")
    shifters  = raw_input("Enter keyphrase : ")

    print shifters[-1:]
    shifter = ord(shifters[-1:])
    
    file_content = open(file_name, 'r')

    file_content_list = file_content.readlines()

    new_list = []
    for sentence in file_content_list:
        #remove the \n separator 
        newer = sentence.find('\\')
        sentence = sentence[:newer]
 #       print sentence
        new_list.append(sentence)
    print 'New list is : ', new_list

    encrypted = []
    for sentence in new_list:
        esentence = ""
        for character in sentence:
            esentence = esentence + ASCII(character,shifter)
#        print 'the en sent is :', esentence
        encrypted.append(esentence)
    print encrypted

    wfile = open('cipher.txt',"w")
    for sentence in encrypted:
        wfile.write(sentence)
        wfile.write('\n')
    wfile.close()
    return

def ASCII(character, shifter):
    if ord(character) == 32:
        return character
    asciinum = ord(character)+shifter
    if asciinum > 255:
        asciinum = asciinum - 256 
 #   print 'new ascii num is : ', asciinum
#    print 'new ascii value is : ', chr(asciinum)
    return chr(asciinum)
    
coder() 
