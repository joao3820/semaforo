from machine import Pin

class Button:
    def __init__(self, pin, callback):
        self.pin = pin
        self.callback = callback
        self.but = Pin(self.pin, Pin.IN, Pin.PULL_UP)
        self.but.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

    flag = True  # flag associada à classe, indicando alguma propriedade sobre o objeto
