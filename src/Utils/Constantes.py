# Placa
CELAVAZIA = [0, 0, 0, 0, 0, 0,]

# Página inicial 
OPCOESPAGINAINICIAL =[
		'1- Reprodução de partitura',
		'2- Escrita de partitura.',
		'3- Escrita direta para plataforma.',
		'9- Página de configurações.',
		'10- Abrir documentação / Ajuda.',
		'0- Finalizar programa.'] 

# Página de controle direto 
OPCAOESPAGINACONTROLEDIRETO = [
	'0- Retornar a tela inicial.',
	'1- Iniciar envio de comandos.',
	'10- Ajuda'
]
TEXTOAJUDAPAGINACONTROLEDIRETO = 'Utilize as teclas s, d, f, j, k, e l para representar uma cela braille e pressione a tecla enter para enviar a informação para a plataforma. Digite 0 ou sair para finalizar o programa.'
#Página de execução 
OPCOESPAGINAEXECUCAO = [
	'0- Retornar a página inicial.',
	'1- Iniciar reprodução',
	'2- Escolher partitura.',
	'10- Ajuda'
]
TEXTOAJUDAEXECUCAO = "Ao iniciar a execução os pontos da placa apresentarão as notas da partitura do documento escolhido. Pressione o botão de avanço para proceguir com a execução, pressione o botão de recuo para voltar a nota anterior e pressione o botão de função junto com o botão de recuo para retornar ao início da partitura ou com o botão de avanço para finalizar a execução.\nConsulte a documentação, na página inicial, para maiores informações."

#Página de execução 
OPCOESPAGINAESCRITA = [
	'0- Retornar a página inicial.',
	'1- Iniciar escrita de uma nova partitura.',
	'10- Ajuda'
]
TEXTOAJUDAPAGINAEXECUCAO = "Ao selecionar a opção para escrever uma nova partitura será possível utilizar as teclas s, d, f, j, k e l para digitar as notas. A tecla enter deve ser pressionada depois de cada nota. Digite 0 para finalizar a edição."

#Página de configurações 
OPCOESPAGINACONFIGURACOES = [
		'1- Iniciar/Desligar sintetizador de voz.',
		'2- Ligar/Desligar bips da placa',
		'3- Alterar voz do sintetizador.',
		'8- Alterar porta de comunicação com placa arduíno.',
		'9- Retornar aos padrões de configuração.',
		'0- Retornar a página anterior.']

Constantes = {
	"PaginaInicial" : {
		"MensagemDeFinalizacao" : "Fim do programa"
	},
	"PaginaDeExecucao" : {
		"MensagemDeInicializacao":"Página de execução de partitura",
		"MensagemDeFinalizacao": "Fim da Execução da partitura"
	}
}
