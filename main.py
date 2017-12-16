# -*- coding: UTF-8 -*-
import sys
import kivy
#kivy.require('1.10.0')
from kivy.app import App
import urllib.request
from screeninfo import get_monitors
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
#Instancia a qual a classe principal deve herda-lá
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty
#Propriedades que permitem a mudança de valores dos elementos ids
#da linguagem de marcação .kv .
#StringProperty --> para tipos strings
#NumericProperty --> para tipos numericos
from kivy.clock import Clock
#Propriedade assíncrona que agenda eventos na
#execução da aplicação
from kivy.animation import Animation
#instancia resposanvel por plotar animações
from kivy.uix.video import Video
from datetime import datetime
from random import randint
import os
#biblioteca resposánvel por fornecer o tempo
import json

class layout_9(BoxLayout):
    title = StringProperty()
    paragraphe = StringProperty()
    img = StringProperty()
    time = StringProperty()
    setOpacity = NumericProperty()
    x = NumericProperty()
    y = NumericProperty()
    def update(self, *args): #método que será atualizado pelo gerenciador de eventos
        #animações:
        self.horas()

        Clock.schedule_once(self.anime_time_logo, 3)
        if self.anime == True:
            anime = Animation(opacity = 0.65,duration= 0.1)
            anime.start(self.ids.anime_text)
            Clock.schedule_once(self.anime_text_f, 4)

        if self.effect == 1:
            self.anime1()
        else:
            self.anime2()
#animações
    def anime1(self):
        anime = Animation(opacity=1, duration=1)
        anime.start(self.ids.layout_9)

    def anime2(self):
        anime = Animation(x=0,y=0, duration=1)
        anime.start(self.ids.layout_9)

    def anime_time_logo(self, *args):
        anim1 = Animation(opacity = 0.9, duration=3) #animção de mudança de opacidade
        anim1.start(self.ids.time_logo) #iniciando a segunda animação e como parâmetro o id do elemento

    def anime_text_f(self, *args):
        anim = Animation(x=0,y=0, duration=1)   #animação de mudança de posição
        anim.start(self.ids.anime_text) #iniciando a primeira animação e como parâmetro o id do elemento

    def horas(self):
        now = datetime.now() # instancia que fornece a data
        dia = now.day
        mes = now.month
        ano = now.year
        horas = now.hour
        minutos = now.minute
        aux = [dia,mes,ano,horas,minutos]
        for i in range(len(aux)):
            if aux[i] <= 9:
                aux[i] = "0" + str(aux[i])
            else:
                aux[i] = str(aux[i])
        self.time = aux[0] + "/" + aux[1] + "/" + aux[2]  + "\n    " + aux[3] +":"+ aux[4]

    def set(self, title, paragraphe, anime, effect, img):
        self.title = title
        self.paragraphe = paragraphe
        self.anime = anime
        self.img = img
        if effect == 1:
            self.setOpacity = 0
            self.x = 0
            self.y = 0

        elif effect == 2:
            self.setOpacity = 1
            num = int(Window.size[0])
            self.x = -num
            self.y = 0

        elif effect == 3:
            self.setOpacity = 1
            num = int(Window.size[0])
            self.x = num*2
            self.y = 0

        elif effect == 4:
            self.setOpacity = 1
            num = int(Window.size[1])
            self.x = 0
            self.y = num*2

        else:
            self.setOpacity = 1
            num = int(Window.size[1])
            self.x = 0
            self.y = -num

        self.effect = effect

class layout_15(FloatLayout):
    title = StringProperty()
    paragraphe = StringProperty()
    time = StringProperty()

    def update(self, *args):  #metodo que será atualizado pelo clock
        self.horas()
        anim = Animation(x=0,y=0, duration=3)
        #instancia de animação onde os parametros são a
        #posição, de x e y finais e a duração da animação
        anim.start(self.ids.anime_text1)
        anim1 = Animation(opacity = 0.9, duration=4)
        anim1.start(self.ids.time_logo1)

    def horas(self):
        now = datetime.now() # instancia que fornece a data
        dia = now.day
        mes = now.month
        ano = now.year
        horas = now.hour
        minutos = now.minute
        aux = [dia,mes,ano,horas,minutos]
        for i in range(len(aux)):

            if aux[i] <= 9:
                aux[i] = "0" + str(aux[i])

            else:
                aux[i] = str(aux[i])

        self.time = aux[0] + "/" + aux[1] + "/" + aux[2]  + "\n    " + aux[3] +":"+ aux[4]

    def set(self, title, paragraphe):
        self.title = title
        self.paragraphe = paragraphe


class RootWidgets(BoxLayout): #Classe seletora de layouts
    __numReload = None
    __count = None
    __start = None
    inum = 0

    def __init__(self, **kwargs):
        super(RootWidgets, self).__init__(**kwargs)
        try:
            self.set()
            self.run()
        #    Clock.schedule_once(self.run, 26)
        except Exception as error:
            self.clear_widgets()
            lay = BoxLayout(orientation='vertical')
            lay.add_widget(Label(text="[b]Conecte a internet[/b]", markup='true', font_size='40sp'))


            btn = Button(text="Recarregar", size_hint=(1,None), height=100)
            btn.bind(on_press= self.reload)

            lay2 = BoxLayout(padding= [400,0,400,100])
            lay2.add_widget(btn)

            lay.add_widget(lay2)

            self.canvas.add(Color(0.3, 0.6, 0.3))
            self.canvas.add(Rectangle(pos=self.pos, size=(Window.size[0],Window.size[1]) ) )
            self.add_widget(lay)
    def reload(self, *args):
        self.canvas.clear()
        self.__init__()
    def run(self, *args):
        if self.__start == None:
            self.root()
        Clock.schedule_interval(self.root, 15) # aqui o código entra num loop, que repetirá a cada 15 segundos

    def updateData(self):
        url = "http://interacao.ifrn.edu.br/messages/load_messages.json?campi_id=7"
        urllib.request.urlretrieve(url, "dados.txt")


    def set(self):
        self.updateData()

        a = open('dados.txt' , 'r', encoding='utf-8')
        read = a.read()
        a.close()

        self.js = json.loads(read)
        self.__numReload = len(self.js)

        self.__count = self.__numReload - 1


    def root(self, *args):
        num = randint(1,5)
        self.effect = num
        if self.__numReload == 0:
            self.set()

        self.inum += 1
        urllib.request.urlretrieve("http://interacao.ifrn.edu.br" + self.js[self.__count]["url_image"], "Imagens/" + str(self.inum) + ".jpg")
        self.get()

    def get(self, *args):
        self.__start = 0
        self.clear_widgets() #Limpa a tela e remove todos elementos
        #Carrega uma imagem da internet e altera o arquivo Imagens/1.jpg
        if(self.js[self.__count]["type_notice"] == 1):
            lay = layout_9()
            lay.set(self.js[self.__count]["title"], self.js[self.__count]["message"], True, self.effect, "Imagens/" + str(self.inum) + ".jpg")
            lay.update() #espera 1 segundo para mostrar as animações e o conteúdo
            self.clear_widgets() #Limpa a tela e remove todos elementos
            self.add_widget(lay) #adiciona o elemeto no Widget da propria instancia

        else: #(self.js[self.__count]["type_notice"] == 3):
            lay = layout_9()
            lay.set("","", False, self.effect, "Imagens/" + str(self.inum) + ".jpg")
            lay.update() #espera 1 segundo para mostrar as animações e o conteúdo
            self.clear_widgets() #Limpa a tela e remove todos elementos
            self.add_widget(lay) #adiciona o elemeto no Widget da propria instancia

        if self.inum > 1:
            os.remove("Imagens/" + str(self.inum - 1) + ".jpg")
        self.__numReload -= 1
        self.__count -= 1


class tvApp(App):
    x = None
    y = None

    def setSize(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def build(self):
        Window.size = (self.x, self.y)
        Window.clearcolor = (1,1,1,0.4)
        Window.maximize()
        Window.minimum_height = 600
        Window.minimum_width = 1000
        #Window.fullscreen = True
        #Window.borderless = True
        self.title = "InteraçãoTV-CCSL" #título da janela
        self.icon = "Imagens/ifrn.png" #icone
        root = RootWidgets()
        return root


class main:
    def clear_buffer_imgs():
        files = os.listdir("Imagens/")
        for i in files:
            f = i.split(".")
            if(f[0].isnumeric()):
                os.remove("Imagens/" + i)
                break
    if __name__ == '__main__':
        clear_buffer_imgs()
        a = get_monitors()
        a = str(a[0])
        a = a.replace('monitor','')
        a = a.replace('+0','')
        a = a.replace('(', '')
        a = a.replace(')','')
        a = a.split('x')
        x = a[0]
        y = a[1]
        root = tvApp()
        root.setSize(x,y)
        root.run()
