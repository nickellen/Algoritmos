# Código Morse
morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
while True:
    mensagem = input('Mensagem original:')
    nova_mensagem=''
    for caracter in mensagem.upper():
        if caracter in morse:
            nova_mensagem+= morse[caracter]+ ' '

    print('Mensagem em código morse:',nova_mensagem)