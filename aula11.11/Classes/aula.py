class Ventilador:
    def __init__(self):
        self.marca = ""
        self.voltagem = 0
        self.total_velocidades = 0
        self.velocidade_atual = 0

def aumentarVelocidade(ventilador):
    if(ventilador.velocidade_atual < ventilador.total_velocidades):
        ventilador.velocidade_atual += 1

ventiladorParede = Ventilador()
ventiladorParede.marca = "Ventisol"
ventiladorParede.voltagem = 220
ventiladorParede.velocidade_atual = 4
ventiladorParede.velocidade_atual = 1

aumentarVelocidade(ventiladorParede)
aumentarVelocidade(ventiladorParede)
aumentarVelocidade(ventiladorParede)
aumentarVelocidade(ventiladorParede)
aumentarVelocidade(ventiladorParede)

print("Velocidade atual: ", ventiladorParede.velocidade_atual)



class Televisao:
    def __init__(self):
        self.status = False
        self.canal = 0
        self.volume = 0


tv = Televisao()


def ligar(tv):
    tv.status = True
    tv.canal = 1

def desligar(tv):
    tv.status = False
    tv.canal = 0

def aumentarCanal(tv):
    if(tv.canal < 5):
        tv.canal += 1

def mudarCanal(tv, canal):
    if(canal <= 5):
        tv.canal = canal


tv = Televisao()
