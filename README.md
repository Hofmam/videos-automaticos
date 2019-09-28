# videos-automaticos
Projeto que cria videos automáticos para o youtube

26/09/2019
- Decidi mudar a estrutura original do projeto para conseguir uma melhor performance, coloquei os 4 bots e a função de iniciar no mesmo arquivo python.
- Comecei a implementação do robot_txt, que vai fazer o download e tratamento dos textos. Já consegui fazer o download atravez do algorithmia. Tive dificuldades em sanitizar o texto que vem estremamente contaminado e resolvi fazer uma pausa ^^
- Consegui sanitizar o texto (Não removi datas nem alguns caracteres especiais por enquanto)
- Usei outro algoritmo do Algorithmia para quebrar o Texto sanitizado em sentenças (Estou com algumas duvidas em relação ao funcionamento do mesmo kkkkk, mas por hora, vou manter do jeito que esta!)

27/09/2019
- Antes de qualquer coisa, eu apaguei os comentarios que tinha feito no código, começei a estudar os principios do "clean code" e percebi que estava fazendo um uso desnecesarios dessa ferramenta.
- Comecei a implementação do Watson da IBM no script! tive alguma dificuldade no começo, mas nada que o google não resolva!
- Iterei o Watson sobre algumas sentenças para retirar palavras chave(key words), em algumas sentenças ele retorna um erro que eu simplesmente não consegui resolver, fiz algumas pesquisas, mas nada!
- A unica coisa que pensei em relação a isso, é colocar um "Try/Except" e simplesmente ignorar o erro com um "pass" mas não estou confortavel com isso, e certamente, não é uma boa pratica.
- Dito isso, somado ao fato de eu estar exausto, decidi deixar do jeito que esta e resolver tudo amanhã.
- Ainda é possivel rodar o codigo, porém, em alguns casos isolados ele pode travar.
