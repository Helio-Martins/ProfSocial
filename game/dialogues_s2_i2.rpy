label session_2_dialogues_i2:

# abel, manuela, nando, patricia
label .chat_i2_cb:
    $ active_rooms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 19]
    $ drag_game = True
    $ situation = 60
    call setup_dialogue("chat_i2_cb_idle")
    call pass_time_dialogue
    p angry "Acham normal que a Isabel tenha dito à Cármen que lhe fazia uma espera?"
    call pass_time_dialogue
    m angry "Sabiam que ela agora é super amiguinha da Tatiana?"
    call pass_time_dialogue
    a normal "O que ela precisa é que eu lhe ensine judo. Uahh!"
    call pass_time_dialogue
    a normal "*faz movimentos de judo*"
    call pass_time_dialogue
    n laugh "*risos*"
    call pass_time_dialogue
    n normal "Não se preocupem, comigo eles não se metem. Têm de passar por mim para chegar a vocês."
    call pass_time_dialogue
    p normal "O meu herói! O que era mesmo top era fazer um vídeo do Abel a treinar judo com a Cármen e meter na net. Tipo aquele filme, Karate Kid."
    call pass_time_dialogue
    n normal "Se queres eu faço o vídeo, na boa."
    call pass_time_dialogue
    a normal "Ya e identificamos a Estrela, a Isabel e a Tatiana."
    call pass_time_dialogue
    m sad "Não sei se é boa ideia..."
    call pass_time_dialogue
    p normal "Era só para as assustar, relaxa."
    call pass_time_dialogue
    a happy "Pessoal, ia ser excelente!"
    jump chat_exit

# abel, jorge, rui
label .chat_i2_g0:
    $ chats_i2[0] = -1
    call setup_dialogue("chat_i2_g0_idle")
    call pass_time_dialogue
    r normal "Abel, juntas-te a nós hoje?"
    call pass_time_dialogue
    a normal "A fazer o quê?"
    call pass_time_dialogue
    j laugh "Jogar obviamente!"
    call pass_time_dialogue
    a happy "Boooooooooooooooora!"
    jump chat_exit

# samuel, tatiana
label .chat_i2_g1:
    $ chats_i2[1] = -1
    call setup_dialogue("chat_i2_g1_idle")
    call pass_time_dialogue
    t surprise "Ah, esqueci-me de comprar folhas de teste!"
    call pass_time_dialogue
    s normal "Eu tenho a mais, posso-te emprestar."
    call pass_time_dialogue
    t happy "Obrigada, eu depois pago-te de volta."
    call pass_time_dialogue
    s happy "Não é preciso."
    jump chat_exit

# estrela, helder
label .chat_i2_g2:
    $ chats_i2[2] = -1
    call setup_dialogue("chat_i2_g2_idle")
    call pass_time_dialogue
    h normal "Precisas de ajuda com a viagem, Estrela?"
    call pass_time_dialogue
    e normal "Não, deixa estar. Estou a fazer uma pausa disso por agora."
    call pass_time_dialogue
    h normal "Ok, mas se precisares de alguma coisa, já sabes."
    call pass_time_dialogue
    e normal "Eu sei, obrigada."
    jump chat_exit

# isabel, manuela - ballet
label .chat_i2_g3:
    $ chats_i2[3] = -1
    call setup_dialogue("chat_i2_g3_idle")
    call pass_time_dialogue
    i normal "Vi o que escreveste no Com@Viver. Estás mesmo a pensar sair do ballet?"
    call pass_time_dialogue
    m sad "Não sei... Eu gosto daquilo mas não tenho a certeza se quero ficar lá para sempre."
    call pass_time_dialogue
    i sad "Eu percebo. É uma decisão dificíl."
    call pass_time_dialogue
    m sad "..."
    jump chat_exit

# carmen, nando, patricia
#label .chat_i2_g4:
#    $ chats_i2[4] = -1
#    call setup_dialogue("chat_i2_g4_idle")
#    call pass_time_dialogue
#    c happy "Patrícia, queres ir às compras esta semana?"
#    call pass_time_dialogue
#    p normal "Depende do dia. Se for sexta, nós vamos."
#    call pass_time_dialogue
#    n normal "Nós?"
#    call pass_time_dialogue
#    p happy "Claro, tens de vir connosco!"
#    call pass_time_dialogue
#    n annoyed "Que seca..."
#    jump chat_exit

# nando, patricia
label .chat_i2_g4:
    $ chats_i2[4] = -1
    call setup_dialogue("chat_i2_g4_idle")
    call pass_time_dialogue
    p normal "Nando, esta semana vamos às compras."
    call pass_time_dialogue
    n annoyed "Que seca... Porque não vais com a Cármen?"
    call pass_time_dialogue
    p happy "Não sei onde ela anda, mas de qualquer das formas, tu tens de vir connosco!"
    call pass_time_dialogue
    n annoyed "..."
    jump chat_exit

##########

# carmen, manuela
label .chat_i2_g5:
    $ chats_i2[5] = -1
    call setup_dialogue("chat_i2_g5_idle")
    call pass_time_dialogue
    c normal "E que tal sexta feira?"
    call pass_time_dialogue
    m normal "Parece-me bem."
    call pass_time_dialogue
    c happy "Ainda bem!"
    jump chat_exit

# abel, nando, patricia, manuela
label .chat_i2_g6:
    $ chats_i2[6] = -1
    call setup_dialogue("chat_i2_g6_idle")
    call pass_time_dialogue
    a happy "Pessoal, quando é que vamos a um concerto novamente? Não fui neste último por isso estou com a vontade toda."
    call pass_time_dialogue
    n happy "Por mim era já amanhã."
    call pass_time_dialogue
    p normal "Sim, nós não temos aulas nem nada."
    call pass_time_dialogue
    n laugh "Uma pessoa pode sempre imaginar!"
    jump chat_exit

# samuel, tatiana
label .chat_i2_g7:
    $ chats_i2[7] = -1
    call setup_dialogue("chat_i2_g7_idle")
    call pass_time_dialogue
    s normal "Este fim de semana queres ir dar um passeio àquele parque perto do da outra vez?"
    call pass_time_dialogue
    t normal "Por mim sim. Podemos falar com a Isabel e o resto do pessoal para virem também."
    call pass_time_dialogue
    s normal "Yeap, eu falo com eles."
    jump chat_exit

# estrela, helder, isabel
label .chat_i2_g8:
    $ chats_i2[8] = -1
    call setup_dialogue("chat_i2_g8_idle")
    call pass_time_dialogue
    i happy "O que nós devíamos fazer era uma viagemzinha nas férias."
    call pass_time_dialogue
    e normal "Aonde?"
    call pass_time_dialogue
    i happy "Não interessa o lugar! Um sítio qualquer para relaxar."
    call pass_time_dialogue
    e happy "E o dinheiro para isso?"
    call pass_time_dialogue
    h laugh "Pois, sonhar também é relaxante e custa menos!"
    jump chat_exit

# jorge, rui
label .chat_i2_g9:
    $ chats_i2[9] = -1
    call setup_dialogue("chat_i2_g9_idle")
    call pass_time_dialogue
    j normal "Depois manda-me uma mensagem quando estiveres despachado."
    call pass_time_dialogue
    r normal "Yeap, não te preocupes. Tenta não jogar muito sem mim."
    call pass_time_dialogue
    j happy "Claro!"
    jump chat_exit
