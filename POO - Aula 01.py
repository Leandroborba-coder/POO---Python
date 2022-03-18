from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
                    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo == True:
            print(f'{self.nome} já está comendo {self.alimento}.')
            return
    
        
        self.alimento = alimento
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True


    def parar_comer(self):
        if self.comendo == True:
            print(f'{self.nome} acabou de parar de comer.')
            self.comendo = False

        else:
            print(f'{self.nome} não está comendo. Nao tem como parar!')


    def falar(self,assunto):
        if self.comendo == True:
            print(f'{self.nome} não pode falar comendo!')
            return

        elif self.falando == True:
            print(f'{self.nome} já está falando!')
            return
            
        else:
            print(f'{self.nome} está falando sobre {assunto}.')
            self.falando = True
            

    def parar_falar(self):
        if self.falando == True:
            print(f'{self.nome} parou de falar!')
            self.falando = False

        else:
            print(f'{self.nome} não está falando. Não tem como.')

    def get_ano_nascimento(self):
        return print(self.ano_atual - self.idade)
            
