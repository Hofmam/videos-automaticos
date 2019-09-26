#coding: utf-8

import Algorithmia
from AlgorithmiaKey import apiKey # chave de autenticação do algorithmia salva
cliente = Algorithmia.client(apiKey) # aqui é declarada uma instancia autenticada do algorithmia

############################################################
#############  declararando funções dos bots!  #############
############################################################

def robot_txt(tema_para_busca): # ROBO DE TEXTO

	def baixar_conteudo(): # download do texto do wikipedia
		tema = {
		'articleName':tema_para_busca,
		'lang':'en'
		} # este é o dicionario que o algorithmia usa para fazer uma busca na Wikipedia

		algo = cliente.algo('web/WikipediaParser/0.1.2') # aqui, é declarado qual é o algoritmo a ser usado
		algo.set_options(timeout=300) # define o tempo para 300 segundos(300s é o padrão oque torna essa definição desnecesaria, mas eu preferi colocar caso se mostre nescesario ^^)
		conteudo = algo.pipe(tema).result # salva o conteudo do Wikipedia na variavel conteudo
		return conteudo['content'] # retorna o conteudo baixado!

	def saitizar_conteudo(texto_contaminado): # limpar o texto baixado!
		pass
	def quebrar_em_sentenças():
		pass

	conteudo_bruto = baixar_conteudo() # salva o resultado da primeira função em uma variavel
	conteudo_limpo = saitizar_conteudo(conteudo_bruto)
############################################################
#######    declararando função que chama os bots!    #######
############################################################
def start(): # start vai iniciar e gerenciar os bots!
	
	def perguntar_pelo_texto(): # função que pergunta qual o texto a ser buscado
		texto_da_busca = input('Qual o texto que deseja buscar?')

		if texto_da_busca.isspace() or texto_da_busca == '':
			return perguntar_pelo_texto() # reinicia a função caso o input esteja em branco
		else:
			return robot_txt(texto_da_busca) # retorna o texto em string

	def perguntar_pelo_prefixo(): # função pergunta pelo prefixo
		prefixos = ['Who is','What is','The history of']

		x = 0
		for prefixo in prefixos:
			x += 1
			print('[{0}]:{1}'.format(x,prefixo.rjust(14)))

		try:
			inp = int(input('Qual o prefixo: ')) - 1 # -1 para acertar o indice do prefixo na losta de prefixos
			return prefixos[inp]

		except:
			return perguntar_pelo_prefixo() # reinicia a função caso o usuario não digitar um numero

	texto = perguntar_pelo_texto() # chama o primeiro input
	prefixo = perguntar_pelo_prefixo() # chama o segundo input
	return [texto,prefixo] # retorna uma lista com os inputs do usuario.