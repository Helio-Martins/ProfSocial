label session_1_dialogues_i2:

# abel, carmen, estrela, helder, manuela, nando, patricia
label .chat_i2_cb:
    $ active_rooms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 19]
    $ drag_game = True
    $ situation = 30
    call setup_dialogue("chat_i2_cb_idle")
    call pass_time_dialogue
    n laugh "Mano, a Tatiana é o maior desperdício de oxigénio que anda por aí!"
    call pass_time_dialogue
    p disgust "Tem a mania que é melhor do que os outros, só porque passa os dias a estudar. Normal, não tem vida."
    call pass_time_dialogue
    a laugh "Não tem vida, mas anda com todos."
    call pass_time_dialogue
    c laugh "*risos*"
    call pass_time_dialogue
    m happy "*risos*"
    call pass_time_dialogue
    e sad "Não veem que ela está bué mal? O que fizeram foi horrível!"
    call pass_time_dialogue
    n laugh "*finge que chora* Ah, coitadinha! Buáaaaa."
    call pass_time_dialogue
    p angry "Ela sabe bem o que me fez primeiro!"
    call pass_time_dialogue
    e angry "Se fizerem mais alguma cena vou falar com o DT."
    call pass_time_dialogue
    c angry "Não sejas uma falsa, Estrela. Lá porque és delegada de turma, pensas que mandas."
    call pass_time_dialogue
    n angry "Cala a boca, Estrela! Quem se meter nisto leva no focinho! E os seus amiguinhos todos."
    call pass_time_dialogue
    h angry "Epá, calma que eu não tenho nada a ver com isto."
    call pass_time_dialogue
    e disgust "Queres ser outra vez suspenso, Nando? Não te bastou o ano passado?"
    call pass_time_dialogue
    n laugh "Eu faço o que quero! Ninguém manda em mim, ainda não percebeste?"
    jump chat_exit

# abel, jorge, rui
label .chat_i2_g0:
    $ chats_i2[0] = -1
    call setup_dialogue("chat_i2_g0_idle")
    call pass_time_dialogue
    a normal "Jorge, tu vens ao torneio sexta feira não vens? Tens andado meio desaparecido."
    call pass_time_dialogue
    j normal "Epa ya, tive uma consulta de dentista e outras coisas, tudo ao mesmo tempo. Em princípio na sexta vou ao torneio. "
    call pass_time_dialogue
    a laugh "Fixe! Vê lá se consegues tirar a bola ao adversário desta vez!"
    call pass_time_dialogue
    r laugh "*risos*"
    call pass_time_dialogue
    j happy "Metes muita piada Abel, mas da outra vez fui eu que marquei o golo de vitória!"
    call pass_time_dialogue
    a happy "Lá isso é verdade, e honestamente foi um bom golo!"
    call pass_time_dialogue
    j happy "Então e tu Rui, não queres vir também? Há sempre a chance de alguém faltar."
    call pass_time_dialogue
    r happy "Até ia mas futebol não é comigo. Mas obrigado pelo convite."
    call pass_time_dialogue
    a laugh "Não sei até que ponto alguém faltaria, depois tinham de enfrentar o Nando."
    call pass_time_dialogue
    r normal "Por falar em Nando, onde é que ele anda? Queria falar com ele que ultimamente ele anda a abusar um bocado."
    call pass_time_dialogue
    j angry "Rui, faz como eu e não te metas nisso. Se não tem nada a ver contigo, para quê te meteres ao barulho?"
    call pass_time_dialogue
    r angry "Pah eu não sou assim, se eu vejo uma cena mal, vou dizer o que penso."
    jump chat_exit

# samuel, tatiana - posts
label .chat_i2_g1:
    $ chats_i2[1] = -1
    call setup_dialogue("chat_i2_g1_idle")
    call pass_time_dialogue
    s sad "Não fiques assim, não vale a pena."
    call pass_time_dialogue
    t sad "Eu sei. Não te preocupes. Isto já passa."
    call pass_time_dialogue
    s sad "Chegaste a falar com a tua irmã? Sempre vamos sair todos amanhã à tarde?"
    call pass_time_dialogue
    t sad "Não, desculpa, esqueci-me. Hoje quando chegar a casa eu falo com ela."
    call pass_time_dialogue
    s sad "Ok, sem problemas. Se precisares de alguma coisa, diz."
    call pass_time_dialogue
    t sad "..."
    jump chat_exit

# estrela, helder - atividades
label .chat_i2_g2:
    $ chats_i2[2] = -1
    call setup_dialogue("chat_i2_g2_idle")
    call pass_time_dialogue
    h normal "Que atividades tens planeadas, Estrela?"
    call pass_time_dialogue
    e normal "Por agora, ainda só tenho duas. Estou à espera de resposta do Jorge para avançar com esta parte."
    call pass_time_dialogue
    h normal "Ah ok. E em relação à viagem, já sabes se vamos para a Costa ou para o Algarve?"
    call pass_time_dialogue
    e normal "Ainda não está definido, mas parece-me que vai ser no Algarve."
    call pass_time_dialogue
    h happy "Fixe!"
    call pass_time_dialogue
    e normal "Pena que nem toda a gente partilhe do teu entusiasmo, senão isto já estava decidido."
    call pass_time_dialogue
    h normal "Pois, a Cármen não tem facilitado a marcação da viagem. Já para não falar do que elas andam a dizer no Com@Viver."
    call pass_time_dialogue
    e angry "A este ponto é só vergonhoso o que estão a fazer."
    jump chat_exit

# isabel, manuela - ballet
label .chat_i2_g3:
    $ chats_i2[3] = -1
    call setup_dialogue("chat_i2_g3_idle")
    call pass_time_dialogue
    i happy "Ainda não acredito que ganhaste o concurso Manuela! Parabéns!"
    call pass_time_dialogue
    m happy "Obrigada! Nem imaginas o quão nervosa eu estava no dia da prova!"
    call pass_time_dialogue
    i happy "Nem quero imaginar. Mas o ano passado já tinhas ido a um concurso não era?"
    call pass_time_dialogue
    m normal "Sim, mas este ano a pressão era maior. Deve ser o último ano em que vou competir."
    call pass_time_dialogue
    i normal "A sério? Pensava que ias continuar no ballet durante muito tempo."
    call pass_time_dialogue
    m sad "Não sei, já estou no ballet há imensos anos e queria tentar outras coisas. Ainda tenho de decidir."
    jump chat_exit

# carmen, nando, patricia
label .chat_i2_g4:
    $ chats_i2[4] = -1
    call setup_dialogue("chat_i2_g4_idle")
    call pass_time_dialogue
    n mean "Viste bem Patrícia? Ela nem falou mais depois do meu post."
    call pass_time_dialogue
    c disgust "Ela também não ia adicionar nada de relevante."
    call pass_time_dialogue
    p disgust "Com sorte aprendeu a lição e não volta a colocar aqueles posts provocadores que ela mete."
    call pass_time_dialogue
    n normal "De qualquer das formas, se ela te volta a chatear diz-me que eu trato da situação."
    call pass_time_dialogue
    p normal "Eu sei. Mas tens de ter cuidado, no outro dia vi oS professores a falarem entre si."
    call pass_time_dialogue
    n normal "Não te preocupes, eles não sabem de nada."
    jump chat_exit

# carmen, patricia
label .chat_i2_g5:
    $ chats_i2[5] = -1
    call setup_dialogue("chat_i2_g5_idle")
    call pass_time_dialogue
    c disgust "É preciso ter lata. Agora anda pela escola a fingir que chora."
    call pass_time_dialogue
    p disgust "Era tão mais simples se ela mudasse de escola. A vida de todos melhorava."
    call pass_time_dialogue
    c disgust "Sim, ela não ia fazer falta a ninguém."
    call pass_time_dialogue
    p disgust "A ninguém não. Ia fazer falta ao Samuel. Já viste como ele anda colado a ela?"
    call pass_time_dialogue
    c disgust "Claro, ele sabe que não arranja melhor."
    call pass_time_dialogue
    p disgust "Mesmo. Lá nisso eles são perfeitos um para outro."
    jump chat_exit

# abel, nando - generico
label .chat_i2_g6:
    $ chats_i2[6] = -1
    call setup_dialogue("chat_i2_g6_idle")
    call pass_time_dialogue
    a normal "Viste o jogo de ontem?"
    call pass_time_dialogue
    n happy "Ya, cheguei a pensar que távamos a jogar sozinhos. A outra equipa parecia que estava a jogar com a equipa B."
    call pass_time_dialogue
    a happy "Curtiste do ponta de lança a levar 3 foras de jogo?"
    call pass_time_dialogue
    n laugh "YA! Ele não deve ter dormido como deve ser."
    call pass_time_dialogue
    a laugh "Pois, só pode!"
    jump chat_exit

# manuela
label .chat_i2_g7:
    $ chats_i2[7] = -1
    call setup_dialogue("chat_i2_g7_idle")
    call pass_time_dialogue
    m normal "*a ouvir música*"
    jump chat_exit

# helder
label .chat_i2_g8:
    $ chats_i2[8] = -1
    call setup_dialogue("chat_i2_g8_idle")
    call pass_time_dialogue
    h normal "*a comer uma sandes*"
    jump chat_exit

# jorge, samuel, tatiana
label .chat_i2_g9:
    $ chats_i2[9] = -1
    call setup_dialogue("chat_i2_g9_idle")
    call pass_time_dialogue
    s normal "Olha ele, então? Onde tens andado?"
    call pass_time_dialogue
    j normal "Dentista, e muitas outras coisas. Tenho andado ocupado."
    call pass_time_dialogue
    t normal "Tem cuidado, os professores não gostam que faltem às aulas."
    call pass_time_dialogue
    if male:
        j normal "Eu sei, tenho de pedir à minha mãe um atestado do dentista para dar ao stôr."
    else:
        j normal "Eu sei, tenho de pedir à minha mãe um atestado do dentista para dar à stôra."
    call pass_time_dialogue
    s happy "Bom saber que não se passa nada contigo. Para a próxma diz alguma cena ao pessoal."
    call pass_time_dialogue
    j happy "Ya, não te preocupes."
    jump chat_exit

# estrela, isabel, rui
label .chat_i2_g10:
    $ chats_i2[10] = -1
    call setup_dialogue("chat_i2_g10_idle")
    call pass_time_dialogue
    r angry "Ele disse isso?"
    call pass_time_dialogue
    e angry "Sim."
    call pass_time_dialogue
    i sad "Isto está bué grave pessoal."
    call pass_time_dialogue
    e angry "Pois. Acho que tenho mesmo de falar com o D.T."
    call pass_time_dialogue
    r angry "Não fales já. Eu quero falar com ele primeiro."
    call pass_time_dialogue
    i sad "Rui, não sei se isso é boa ideia... Vocês ainda vão entrar numa luta."
    call pass_time_dialogue
    r angry "Eu não tenciono lutar, e nem o Nando é assim tão parvo."
    call pass_time_dialogue
    e angry "Tens mesmo a certeza disso? Tens mais fé nele do que devias."
    jump chat_exit
