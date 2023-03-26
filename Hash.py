class HashTable:
    def __init__(self):
        self.size = 29
        self.vet = [None] * self.size
        self.dado = [None] * self.size

    #insere o dado a partir da chave e dado
    def put(self,key,dado):
        key = key.lower()
        indicehash = self.hashfunction(key,len(self.vet))

        if self.vet[indicehash] == None or self.vet[indicehash] == 'empty':
            self.vet[indicehash] = key
            self.dado[indicehash] = dado

        else: #se não haver slots vazios mas achar um que a chave for igual ela vai fazer replace pelo novo dado
            if self.vet[indicehash] == key:
                self.dado[indicehash] = dado  #replace

            else: #aqui faz a sondagem linear
                proxvet = self.rehash(indicehash,len(self.vet))
                while self.vet[proxvet] != None and self.vet[proxvet] != key and self.vet[proxvet] != 'empty':
                    proxvet = self.rehash(proxvet,len(self.vet))

                if self.vet[proxvet] == None or self.vet[proxvet] == 'empty':
                    self.vet[proxvet] = key
                    self.dado[proxvet] = dado
                else:
                    self.dado[proxvet] = dado #replace

    def hashfunction(self,key,size):
        return ord(key.lower()[0]) % size   #pega a letra da posicao [0] da string e aplica funco ord() pra pegar o unicode, após isso encontra o % do size

    def rehash(self,oldhash,size):
        return (oldhash+1) % size

    #pega o dado a partir da chave
    def get(self,key):
        key = key.lower()
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
            else: #se elemento não estiver na posicao ele faz o rehash para encontra-lo, assim como fez para posiciona-lo
                position=self.rehash(position,len(self.vet))
                if position == startslot: #se voltou a posicao inicial do hash ele vai parar
                    stop = True
        return dado
    
    def remove(self, key):
        key = key.lower()
        indicehash = self.hashfunction(key,len(self.vet))

        if self.vet[indicehash] == key:
            self.vet[indicehash] = 'empty'
            self.dado[indicehash] = 'empty'  #replace

        else: #aqui faz a sondagem linear
            proxvet = self.rehash(indicehash,len(self.vet))
            while self.vet[proxvet] != None and self.vet[proxvet] != key:
                proxvet = self.rehash(proxvet,len(self.vet))

            if self.vet[proxvet] == key:
                self.vet[proxvet] = 'empty'
                self.dado[proxvet] = 'empty'
            else:
                print("Não foi possível encontrar o índice da chave informada e removê-lo!")
    
    def table(self):
        for item in self.vet:            
            if item != '':
                indice = self.vet.index(item)
                print("[{}] = {}".format(indice, item))

    def dados(self):
        for item in self.dado:            
            if item != '':
                indice = self.dado.index(item)
                print("[{}] = {}".format(indice, item))

    def getdadositem(self, key):
        return key, self.get(key)

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,dado):
        self.put(key,dado)