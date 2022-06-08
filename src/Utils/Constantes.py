# Placa
CELAVAZIA = [0, 0, 0, 0, 0, 0,]

# Página inicial 
OPCOESPAGINAINICIAL =[
		'1- Reprodução de partitura',
		'2- Escrita de partitura',
		'3- Escrita direta para plataforma',
		'8- Página de configurações',
		'9- Abrir documentação / Ajuda',
		'10- Ajuda',
		'0- Finalizar programa'] 
TEXTOAJUDAPAGINAINICIAL = "Digite o número correspondente a opção desejada e pressione a tecla enter para ser direcionado a função escolhida"

# Página de controle direto 
OPCAOESPAGINACONTROLEDIRETO = [
	'1- Iniciar envio de comandos',
	'10- Ajuda',
	'0- Retornar a tela inicial'
]
TEXTOAJUDAPAGINACONTROLEDIRETO = 'Utilize as teclas s, d, f, j, k, e l para representar uma cela braille e pressione a tecla enter para enviar a informação para a plataforma. Digite 0 ou sair para finalizar o programa.'

#Página de execução 
OPCOESPAGINAEXECUCAO = [
	'1- Iniciar reprodução',
	'2- Iniciar reprodução automatica',
	'3- Escolher partitura',
	'10- Ajuda',
	'0- Retornar a página inicial.'
]
TEXTOAJUDAEXECUCAO = "Ao iniciar a execução os pontos da placa apresentarão as notas da partitura do documento escolhido. Pressione o botão de avanço para proceguir com a execução, pressione o botão de recuo para voltar a nota anterior e pressione o botão de função junto com o botão de recuo para retornar ao início da partitura ou com o botão de avanço para finalizar a execução.\nConsulte a documentação, na página inicial, para maiores informações."

#Página de execução 
OPCOESPAGINAESCRITA = [
	'1- Iniciar escrita de uma nova partitura',
	'10- Ajuda',
	'0- Retornar a página inicial'
]
TEXTOAJUDAPAGINAEXECUCAO = "Ao selecionar a opção para escrever uma nova partitura será possível utilizar as teclas s, d, f, j, k e l para digitar as notas. A tecla enter deve ser pressionada depois de cada nota. Digite 0 para finalizar a edição."

#Página de configurações 
OPCOESPAGINACONFIGURACOES = [
		'1- Iniciar/Desligar sintetizador de voz',
		'2- Ligar/Desligar bips da placa',
		'3- Alterar voz do sintetizador',
		'4- Ativar/Desativar metronomo antes da execução da partitura',
		'5- Ativar/Desativar apresentação das informações da partitura antes da execução',
		'6- Ativar/Desativar bips ao iniciar novo compasso na partitura',
		'7- Ativar/Desativar apresentação de informações no início do compasso',
		'8- Apresentar informações de musicografia para cada nota',
		'9- Apresentar informação do alfabeto tradicional para cada nota',
		'10- Apresentar o vetor de acionamento de motores para cada nota',
		'11- Ativar/Desativar espaço entre notas seguidas idênticas',
		'18- Alterar porta de comunicação com placa arduíno',
		'19- Retornar aos padrões de configuração',
		'0- Retornar a página inicial']

# Método de definição de BPM
OPCOESBPM = [
	'0- Realizar nova amostragem',
	'1- Utilizar o BPM amostrado',
	'2- Inserir valor manualmente'
]

Constantes = {
	"PaginaInicial" : {
		"MensagemDeFinalizacao" : "Fim do programa"
	},
	"PaginaDeExecucao" : {
		"MensagemDeInicializacao":"Página de execução de partitura",
		"MensagemDeFinalizacao": "Fim da Execução da partitura"
	}
}
