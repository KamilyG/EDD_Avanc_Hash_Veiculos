
#   ATENÇÃO!!! chaves inteiras e valores de dados de string É O QUE ESSE HASHTABLE CONSIDERA, 
#               VERIFICAR PARA A CHAVE PODER SER STRING (já que vai se tratar de placa de carro) ou seja, mudar a hashfunction!!
class HashTable:
    def __init__(self):
        self.size = 29
        self.vet = [None] * self.size
        self.dado = [None] * self.size

    def put(self,key,dado):
        indicehash = self.hashfunction(key,len(self.vet))

        if self.vet[indicehash] == None:
            self.vet[indicehash] = key
            self.dado[indicehash] = dado

        else: #se não haver slots vazios mas achar um que a chave for igual ela vai fazer replace pelo novo dado
            if self.vet[indicehash] == key:
                self.dado[indicehash] = dado  #replace

            else: #aqui faz a sondagem linear
                proxvet = self.rehash(indicehash,len(self.vet))
                while self.vet[proxvet] != None and self.vet[proxvet] != key:
                    proxvet = self.rehash(proxvet,len(self.vet))

                if self.vet[proxvet] == None:
                    self.vet[proxvet] = key
                    self.dado[proxvet] = dado
                else:
                    self.dado[proxvet] = dado #replace

    def hashfunction(self,key,size):
        return key % size

    def rehash(self,oldhash,size):
        return (oldhash+1) % size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.vet))

        dado = None
        stop = False
        found = False
        position = startslot
        while self.vet[position] != None and  \
                            not found and not stop:
            if self.vet[position] == key:
                found = True
                dado = self.dado[position]
            else: #se elemento não eestiver na posicao eel faz o rehash para econtra-lo, asism como fez para posiciona-lo
                position=self.rehash(position,len(self.vet))
                if position == startslot: #se voltou a posicao inicial do hash ele vai parar
                    stop = True
        return dado

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,dado):
        self.put(key,dado)