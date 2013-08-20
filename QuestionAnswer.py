# -*- coding: utf-8 -*-
'''
Created on 13/08/2013

@author: lgomide
'''
#!/usr/bin/python
import random
class QuestionAnswer:
    
    def __init__(self):
        self.question = self.Questions()
        
    #Formata a string, removendo 
    def formatString(self, string):
        return string.decode('utf-8').lower()
    
    #Cadastra as questions
    def Questions(self):
        return [
                    ["Voce possui um automovel? ",
                        ["Qual o modelo? ", "Qual o ano? ", "Quanto pagou? "]
                    ],
                    ["Possui algum imovel ? ",
                        ["Quantos ? ", "Quais (separe por virgula) ?"]
                    ]
                ]
    
    #retorna a quantidade de itens dentro de uma lista
    def countQuestion(self, qBase = None):
        q = self.question
        if qBase >= 0:
            return len(q[qBase][1])
        else:
            return len(q)
        
    def deleteQuestion(self, indice):
        del self.question[indice]
        return self.question
        
    #Seleciona randomicamente uma pergunta, e retona um numero
    def randomQuestion(self, q ):
        try:
            size = self.countQuestion()
            i = random.randint(1, size)
            return i
        except:
            print ("Nao existem mais perguntas.")
    
    #Seleciona randomicamente uma pergunta
    def chooseQuestion(self, qBase = None, qNext = None):
        q = self.question
        i = self.randomQuestion(q) - 1
        if qBase >= 0:
            return q[qBase][1][qNext]
        return [q[i][0], i]

    def runQuestion(self):
        try:
            while self.countQuestion() > 0:
                question = self.chooseQuestion()
                resposta = self.formatString( raw_input(question[0]) )
                respostas, ressub = [], []
                while not resposta or resposta  not in ["sim", "não", "nao" ]:
                    print ("-- A resposta deve ser 'sim' ou 'nao'. --")
                    resposta = self.formatString( raw_input(question[0]) )
                respostas.insert(question[1], {question[0] : resposta})
                if resposta  in ["não", "nao"]:        
                    self.deleteQuestion(question[1])
                    continue
    #             respostas.append({question[0] : resposta})
                size = self.countQuestion(question[1])
                if size > 0:
                    i = 0
                    while i < size:
                        pergunta = self.chooseQuestion(question[1], i)
                        resposta = raw_input( self.formatString( pergunta ) )
                        i += 1
                        ressub.append({ pergunta : resposta} )
                    respostas.insert(question[1], ressub)
                    print respostas
                self.deleteQuestion(question[1])
            self.randomQuestion(self.question)
        except Exception as e:
            print (e)
    
    
    
q = QuestionAnswer()
q.runQuestion()