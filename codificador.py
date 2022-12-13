    
class Codificador:

    def caesar(data, key, mode):
        alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
        new_data = ''
        for c in data:
            index = alphabet.find(c)
            if index == -1:
                new_data += c
            else:
                new_index = index + key if mode == 1 else index - key
                new_index = new_index % len(alphabet)
                new_data += alphabet[new_index:new_index+1]
        return new_data

    def codifica(mensagemembinario):
        indice = len(mensagemembinario) - 1
        verifica = 0
        codificacao = []

        while (verifica <= len(mensagemembinario)-1):
            par = 10*int(mensagemembinario[indice-1])
            par = par+int(mensagemembinario[indice])
            
            if(par == 0):
                codificacao.append(-1)
            if(par == 1):
                codificacao.append(-2)
            if(par == 10):
                codificacao.append(1)
            if(par == 11):
                codificacao.append(2)
            
            indice = indice - 2
            verifica = verifica + 2
        return codificacao

    def decodifica(mensagem):
        indice = len(mensagem) - 1
        verifica = 0
        decodificacao = []
        
        while(verifica <= len(mensagem)-1):
            sinal = int(mensagem[indice])
            
            if(sinal == -1):
                decodificacao.append(0)
                decodificacao.append(0)
            if(sinal == -2):
                decodificacao.append(0)
                decodificacao.append(1)
            if(sinal == 1):
                decodificacao.append(1)
                decodificacao.append(0)
            if(sinal == 2):
                decodificacao.append(1)
                decodificacao.append(1)
            indice = indice - 1
            verifica = verifica + 1
        return decodificacao        

    def codificaASCII(mensagem):
        lista = []
        for char in mensagem:
            lista.append(ord(char))
        return lista

    def decodificaASCII(mensagem):
        lista = []
        for char in mensagem:
            lista.append(chr(char))
        return ''.join(lista)

    def inteiroParaBinario(listaInteiros):
        listaBinario = []
        
        for i in listaInteiros:
            contador =0
            numero = i
            aux=[]
            while(numero/2 != 0):
                aux.append(numero%2)
                numero = int(numero/2)
                contador+=1
            if(numero == 1):
                aux.append(1)
                contador+=1
            while(contador <8):
                aux.append(0)
                contador+=1
            aux.reverse()        
            for j in aux:
                listaBinario.append(j)
        return listaBinario

    def binarioParaListaInteiro(listaBinario):
        listaInteiro =  []
        listaAux = []
        i=0
        
        while(i*8!=len(listaBinario)):
            listaAux = listaBinario[i*8+0:(i+1)*8]
            i+=1
            valor =0
            for j in listaAux:
                valor = 2*valor+j
            listaInteiro.append(valor)
            
        return listaInteiro

    def codificar_mensagem(self,mensagem):
        mensagem = Codificador.caesar(mensagem,2,1)
        asc = Codificador.codificaASCII(mensagem)
        binario = Codificador.inteiroParaBinario(asc)
        mensagem_codificada = Codificador.codifica(binario)
        #mensagem_codificada = [str(mnsg) for mnsg in mensagem_codificada ]

        return mensagem_codificada,binario

    def decodifica_mensagem(self,mensagem):
        mensagem = mensagem.split(',')
        mensagem_int = [int(mnsg) for mnsg in mensagem]
        mensagem_decodificada = Codificador.decodifica(mensagem_int)
        inteiro = Codificador.binarioParaListaInteiro(mensagem_decodificada)
        asc = Codificador.decodificaASCII(inteiro)
        mensagem = Codificador.caesar(asc,2,0)
        
        return mensagem,mensagem_int,mensagem_decodificada
