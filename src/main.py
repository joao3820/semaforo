from led import Led
from utime import ticks_ms
from botao import Button

verde = Led(21)
amarelo = Led(22)
vermelho = Led(19)

def passar_vermelho():
    verde.off()
    amarelo.on()
    test = ticks_ms()
    while True:
        if ticks_ms() - test >= 1000:
            amarelo.off()
            vermelho.on()
        if ticks_ms() - test >= 6000:
            vermelho.off()
            verde.on()
            bp.flag = True  # dar reset à flag dos peões
            break


def peoes(p):
    global contagem
    if bp.flag is True:  # testa se a flag do objeto "bp" é True (significando que ainda não foi clicado)
        contagem -= 5000
        bp.flag = False


amarelo.blink(1000)
def intermitente(p):
    global contagem
    contagem -= 9000
    bi.flag = not bi.flag


bp = Button(23, peoes)
bi = Button(18, intermitente)

verde.on()
contagem = ticks_ms()
while True:
    if bi.flag is False:
        amarelo.proc()
        verde.off()
        vermelho.off()
    elif ticks_ms() - contagem >= 9000:
        passar_vermelho()
        contagem = ticks_ms()
