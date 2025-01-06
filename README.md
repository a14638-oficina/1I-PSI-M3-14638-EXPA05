# 1I-PSI-M3-14638-EXPA05.py

<h1>Função apresentar_questionario():</h1>
Exibe um questionário com várias perguntas sobre a satisfação em relação a uma escola.
As perguntas incluem avaliações de 1 a 5 e uma pergunta de sim/não.
As respostas são coletadas através de input() e armazenadas em uma lista que é retornada.

<h1>Função exportar_resultados(respostas):</h1>
Pede ao usuário um nome de arquivo para salvar as respostas.
Tenta abrir o arquivo em modo de escrita e registra as respostas no formato especificado.
Em caso de erro ao salvar, imprime uma mensagem de erro.

<h1>Função main():</h1>
Um loop que permite ao usuário escolher entre responder ao questionário ou sair do sistema.
Se o usuário escolher responder, chama a função de apresentar o questionário e depois exporta os resultados.

<h1>Execução do programa:</h1>
A função main() é chamada se o script for executado diretamente, iniciando o sistema.
