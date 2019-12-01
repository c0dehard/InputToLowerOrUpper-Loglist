#!/usr/bin/env python
# -*- coding: utf-8 -*-
verlauf,i,programAn = [],0,True

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def abfrage(text,eingabe):
    if eingabe.casefold() == "g":print(text.upper())
    elif eingabe.casefold() == "k":print(text.lower())
    elif eingabe.casefold()=="u":print(reverse(text))
    elif eingabe.casefold() == "l":print(text.strip())
    elif eingabe.casefold() == "a":print(str(text.replace(input('Tausche: '),input('mit:'))))
    global i;i = i + 1
    verlauf.append(f"{i}) {text}");weiter = input('Weiter? <J/N>')
    if weiter == "n".casefold():programAn=False
    
while programAn:
    print("Im Verlauf: ",verlauf);abfrage(input('Gib ein Wort ein\n> '),input('''
Alles g\u0332roß, Alles k\u0332lein, Ohne L\u0332eerzeichen oder A\u0332ustauschen< g/k/L/A>\n> '''))
