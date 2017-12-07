# -*- coding:utf-8 -*-
import json
import urllib.request, urllib.parse , urllib.error
"""class Mensagem:
    def __init__(self, title, paragraphe, index_img, tipo):
        self.title = title
        self.paragraphe = paragraphe
        self.index_img = index_img
        self.tipo = tipo"""
"""class main:
    if __name__ == '__main__':
        t = input("TITLO")
        m = input("PARAGRAFO")
        tipo = input('TIPO')

        msg = Mensagem(t,m,"",tipo)
        js = json.dumps(msg.__dict__)
        a = open("dados.txt", "w")
        a.write(js)
        a.close()
        print("Feito")"""
class Data:
    def __init__(self, id, url_image, message, trusted, twitter_name, user_twitter, notice, type_notice, title, date_message, source):
        self.id = id
        self.url_image = url_image
        self.message = message
        self.trusted = trusted
        self.twitter_name = twitter_name
        self.user_twitter = user_twitter
        self.notce = notice
        self.type_notice = type_notice
        self.title = title
        self.date_message = date_message
        self.source = source
