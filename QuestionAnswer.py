'''
Created on 13/08/2013

@author: lgomide
'''
#!/usr/bin/python

import random

class QuestionAnswer:
    #Cadastra as questions
    def Questions(self):
        return [
                    ["Qual e a idade de seu pai?"], 
                    ["Voce possui carro?"], 
                    ["Qual a idade da sua mae?"], 
                    ["Quantos irmaos voce tem?"] , 
                    ["Quantas irmas voce tem?"], 
                    ["Voce pratica esportes?"]
                ]
        
    
    #Seleciona randomicamente uma pergunta, e retona um numero
    def randomQuestion(self, q):
        try:
            size = len(q)
            i = random.randint(1, size)
            return i
        except:
            print ("Nao existem perguntas")
    
    #Seleciona randomicamente uma pergunta
    def chooseQuestion(self):
        q = self.Questions()
        i = self.randomQuestion(q) - 1
        return q[i][0]
            
    def runQuestion(self):
        try:
            question = self.chooseQuestion()
            resposta = raw_input(question+ '\n')
            while not resposta:
                print ("-- A resposta nao pode estar em branco. --")
                resposta = raw_input(question + '\n')
            else:
                print ("Sua resposta de \n\t --- " + question + "\n\t --- " + resposta)
        except Exception as e:
            print (e)
    
q = QuestionAnswer()
q.runQuestion()