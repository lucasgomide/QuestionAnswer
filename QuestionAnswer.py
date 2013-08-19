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
                    ["Voce possui um automovel? ",
                        ["Qual o modelo? ", "Qual o ano? ", "Quanto pagou? "]
                    ]
                ]
    
    def countQuestion(self, qBase = None):
        q = self.Questions()
        if qBase >= 0:
            return len(q[qBase][1])
        else:
            return len(q)
        
    #Seleciona randomicamente uma pergunta, e retona um numero
    def randomQuestion(self, q):
        try:
            size = self.countQuestion()
            i = random.randint(1, size)
            return i
        except:
            print ("Nao existem perguntas")
    
    #Seleciona randomicamente uma pergunta
    def chooseQuestion(self, qBase = None, qNext = None):
        q = self.Questions()
        i = self.randomQuestion(q) - 1
        if qBase >= 0:
            return q[qBase][1][qNext]
        return [q[i][0], i]

    def runQuestion(self):
        try:
            question = self.chooseQuestion()
            resposta = raw_input(question[0])
            #respostas = {0: [], 1 : []}
            respostas, ressub = [], []
            while not resposta:
                print ("-- A resposta nao pode estar em branco. --")
                resposta = raw_input( question[0] )
            respostas.insert(question[1], {question[0] : resposta})
#             respostas.append({question[0] : resposta})
            size = self.countQuestion(question[1])
            if size > 0:
                i = 0
                while i < size:
                    pergunta = self.chooseQuestion(question[1], i)
                    resposta = raw_input( pergunta )
                    i += 1
                    ressub.append({ pergunta : resposta} )
                respostas.insert(question[1], ressub)
                print respostas
        except Exception as e:
            print (e)
    
    
    
q = QuestionAnswer()
q.runQuestion()