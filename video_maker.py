#coding: utf-8

import Algorithmia
from AlgorithmiaKey import apiKey	# importa a apiKey salva no arquivo AlgorithmiaKey.py

Algorithmia_Autenticado = Algorithmia.client(apiKey)	# Autentica o Algorithmia usando a apiKey

############################################################
#############       primeiro BOT bot_txt       #############
############################################################

def bot_txt(input_do_usuario):

	def download_from_Wikipedia():	# Primeira função do bot, baixar o conteudo!
		tema = {
		'articleName':input_do_usuario,
		'lang':'en'
		}	# dicionario no formato do algoritimo

		algo01 = Algorithmia_Autenticado.algo('web/WikipediaParser/0.1.2')	# declaria uma variavel com o primeiro algoritimo a ser usado
		algo01.set_options(timeout=120)	# define o tempo maximo para 2 minutos! (120 segundos)
		conteudo = algo01.pipe(tema).result	# chama o metodo que ira baixar o conteudo e salva tudo em uma variavel

		print('(^ ^)	conteudo baixado com sucesso!')
		return conteudo['content']	# por padrão o metodo devolve um dicionario, neste caso, precisamos apenas do conteudo principal, por isso ['content']

	def sanitize_content(conteudo_bruto):	# segunda função, sanitizar o texto!
		conteudo_bruto_dividido_em_linhas = conteudo_bruto.split('\n')	# divide o conteudo em linhas para facilitar a sanitização!

		conteudo_sanitizado = ''	# define uma string em branco que ira receber todas as linhas que paçarem pelo teste logico de pre sanitização.

		for line in conteudo_bruto_dividido_em_linhas:
			if line.isspace() or line.startswith('=') or len(line) < 15:	# apaga todas as linhas em branco ou com menos de 15 caracteres e os marks do wikipedia
				pass
			else:
				conteudo_sanitizado += (line + '\n')	# soma todas as linhas a uma string e "devolve" as linhas!

		print('(^ ^)	conteudo sanitizado com sucesso!')
		return conteudo_sanitizado	# retorna o conteudo sanitizado

	def break_sentences(conteudo_sanitizado):	# terceira função, quebrar em sentenças!
		algo02 = Algorithmia_Autenticado.algo('StanfordNLP/SentenceSplit/0.1.0')	# segundo algoritimo, usado para separar um texto em sentenças.
		sentenças = algo02.pipe(conteudo_sanitizado).result

		print('(^ ^)	o conteudo foi dividito em sentenças!')
		return sentenças	#retorna uma lista com as sentenças encontradas!

	#iniciação das funções do bot
	download = download_from_Wikipedia()			# baixa informações sobre o tema
	sanitizado = sanitize_content(download)			# sanitiza as informações baixadas
	conteudo_final = break_sentences(sanitizado)	# separa as informações em sentenças 
	return conteudo_final

############################################################
#############          funçao iniciar          #############
############################################################

def iniciar():
	tema = input('Qual o tema que você deseja?\n>>>')
	texto_sanitizado = bot_txt(tema)

	################################################################################
	print(texto_sanitizado) # apenas para textar como os dados estão indo até aqui #
	################################################################################
iniciar()
