#coding: utf-8

try:
	import Algorithmia
	import json
	from ibm_watson import NaturalLanguageUnderstandingV1
	from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

except:
	print('(°_°)	As dependencias não foram instaladas! Leia as instruções em README.md')

try:
	from credentials import Algorithmia_apiKey , Watson_credentials    # importa as credenciais!

except:
	print('(°_°)	Não foi posivel encontrar suas credenciais! Leia as instruções em README.md')
	exit()

Algorithmia_Autenticado = Algorithmia.client(Algorithmia_apiKey)	# Autentica o Algorithmia usando a apiKey

############################################################
#############       primeiro BOT bot_txt       #############
############################################################

def bot_txt(input_do_usuario):

	def download_from_Wikipedia():	# Primeira função do bot, baixar o conteudo!
		tema = {
		'articleName':input_do_usuario,
		'lang':'en'
		}	# o algoritimo do Algorithmia requer esete formato para fazer a busca.

		algo01 = Algorithmia_Autenticado.algo('web/WikipediaParser/0.1.2')
		algo01.set_options(timeout=120)
		conteudo = algo01.pipe(tema).result

		print('(^ ^)	conteudo baixado com sucesso!')
		return conteudo['content']	# por padrão o metodo devolve um dicionario, neste caso, precisamos apenas do conteudo principal, por isso ['content']

	def sanitize_content(conteudo_bruto):	# segunda função, sanitizar o texto!
		conteudo_bruto_dividido_em_linhas = conteudo_bruto.split('\n')

		conteudo_sanitizado = ''

		for line in conteudo_bruto_dividido_em_linhas:
			if line.isspace() or line.startswith('=') or len(line) < 15:
				pass
			else:
				conteudo_sanitizado += (line + '\n')

		print('(^ ^)	conteudo sanitizado com sucesso!')
		return conteudo_sanitizado

	def break_sentences(conteudo_sanitizado):	# terceira função, quebrar em sentenças!
		algo02 = Algorithmia_Autenticado.algo('StanfordNLP/SentenceSplit/0.1.0')
		sentenças = algo02.pipe(conteudo_sanitizado).result

		print('(^ ^)	o conteudo foi dividito em sentenças!')
		return sentenças

	def select_relevant_sentences(lista_de_sentenças):
		service = NaturalLanguageUnderstandingV1(
			version=Watson_credentials['version'],
			url=Watson_credentials['url'],
			iam_apikey = Watson_credentials['apiKey']
			)	# Autenticação do Watson para o serviço de interpretação de linguagem natural

		sentenças_selecionadas = []

		for sentença in lista_de_sentenças:
			response = service.analyze(
				text = sentença,
				features = Features(
					keywords = KeywordsOptions()
					),
				language = 'en').get_result()

			for key_words in response['keywords']:

				if len(sentenças_selecionadas) < 10:

					if key_words['relevance'] > 0.97:
						sentenças_selecionadas.append([ sentença , key_words ])
						break	# para de iterar sobre as key_words

					else:
						pass

			if len(sentenças_selecionadas) >= 10:
				break # parar de iterar as sob as sentenças

		return sentenças_selecionadas


	#iniciação das funções do bot
	download_wikipedia = download_from_Wikipedia()
	texto_sanitizado = sanitize_content(download_wikipedia)
	texto_em_sentenças = break_sentences(texto_sanitizado)
	conteudo_final = select_relevant_sentences(texto_em_sentenças)

	return conteudo_final

############################################################
#############          funçao iniciar          #############
############################################################

def iniciar():

	def iniciar_robo_de_texto():
		tema = input('Qual o tema que você deseja?\n>>>')
		dados_coletados = bot_txt(tema)

	iniciar_robo_de_texto()

iniciar()
