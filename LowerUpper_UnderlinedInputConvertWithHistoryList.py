#!/usr/bin/env python
# -*- coding: utf-8 -*-
verlauf,i,programAn = [],0,True

def abfrage(text,eingabe):
    if eingabe.casefold() == "g":print(text.upper())
    elif eingabe.casefold() == "k":print(text.lower());global i;i = i + 1
    verlauf.append(f"{i}) {text}");weiter = input('Weiter? <J/N>')
    if weiter == "n".casefold():programAn=False
    
while programAn:
    print("Im Verlauf: ",verlauf);abfrage(input('Gib ein Wort ein\n> '),input('Alles g\u0332roß, Alles k\u0332lein <G/K>\n> '))
