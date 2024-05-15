label session_2_dialogues_i1:

# estrela, isabel, helder - sinal
label .chat_i1_g0:
    $ chats_i1[0] = 9
    call setup_dialogue("chat_i1_g0_idle")
    call pass_time_dialogue
    i normal "Bora ao cinema depois das aulas ver aquele filme fixe que eu falei?"
    call pass_time_dialogue
    e sad "Não sei, está-me a apetecer ir para casa, fica para outro dia."
    call pass_time_dialogue
    i normal "Então combinamos para amanhã?"
    call pass_time_dialogue
    e sad "Amanhã não devo ir às aulas, não tou com cabeça para isso."
    jump chat_exit

# abel, nando
label .chat_i1_g1:
    $ chats_i1[1] = -1
    call setup_dialogue("chat_i1_g1_idle")
    call pass_time_dialogue
    a normal "Estás a pensar ir ao jogo no sábado?"
    call pass_time_dialogue
    n normal "Não sei, tenho que falar com a Patrícia primeiro. Tu vais?"
    call pass_time_dialogue
    a normal "Em princípio sim, mas preferia não estar a ir sozinho."
    call pass_time_dialogue
    n normal "Tá-se bem, eu depois digo-te qualquer coisa."
    jump chat_exit

# samuel, tatiana
label .chat_i1_g2:
    $ chats_i1[2] = -1
    call setup_dialogue("chat_i1_g2_idle")
    call pass_time_dialogue
    s normal "Preciso de passar na biblioteca daqui a bocado. Vens comigo?"
    call pass_time_dialogue
    t normal "Sim, vamos. Aproveito para ver se há algum livro de interesse lá."
    call pass_time_dialogue
    s happy "Fixe."
    jump chat_exit

# carmen, manuela, patricia
#label .chat_i1_g3:
#    $ chats_i1[3] = -1
#    call setup_dialogue("chat_i1_g3_idle")
#    call pass_time_dialogue
#    m happy "A ida à praia no outro dia foi mesmo fixe!"
#    call pass_time_dialogue
#    c happy "Claro, quem tem as melhores ideias sempre? Sou eu!"
#    call pass_time_dialogue
#    p happy "Vocês querem ir este fim de semana novamente?"
#    call pass_time_dialogue
#    c normal "Tenho que falar com os meus pais primeiro."
#    call pass_time_dialogue
#    m happy "Eu vou!"
#    jump chat_exit

# manuela, patricia
label .chat_i1_g3:
    $ chats_i1[3] = -1
    call setup_dialogue("chat_i1_g3_idle")
    call pass_time_dialogue
    m happy "A ida à praia no outro dia foi mesmo fixe!"
    call pass_time_dialogue
    p happy "Claro, quem tem as melhores ideias sempre? Sou eu!"
    call pass_time_dialogue
    c happy "Queres ir este fim de semana novamente?"
    call pass_time_dialogue
    p normal "Tenho que falar com os meus pais primeiro, mas à partida sim"
    jump chat_exit

# jorge, rui
label .chat_i1_g4:
    $ chats_i1[4] = -1
    call setup_dialogue("chat_i1_g4_idle")
    call pass_time_dialogue
    j normal "Hoje à noite, queres jogar um bocado? Amanhã não vai haver a primeira aula."
    call pass_time_dialogue
    r normal "Ainda vou passar na Associação mas depois disso estou disponível."
    call pass_time_dialogue
    j normal "Mais ou menos a que horas, 18h00?"
    call pass_time_dialogue
    r normal "Aponta para as 18h30, mais coisa menos coisa."
    jump chat_exit

#####

# nando, patricia
label .chat_i1_g5:
    $ chats_i1[5] = -1
    call setup_dialogue("chat_i1_g5_idle")
    call pass_time_dialogue
    p happy "Este fim de semana vens jantar a casa dos meus pais, não te esqueças."
    call pass_time_dialogue
    n normal "Sim, sim. Não vou esquecer."
    call pass_time_dialogue
    p normal "Disseste isso da outra vez. Certifica-te que não te esqueces mesmo."
    call pass_time_dialogue
    n annoyed "Pronto, eu coloco um alarme no telemóvel. Contente?"
    call pass_time_dialogue
    p happy "Sim!"
    jump chat_exit

# estrela, helder, isabel, samuel, tatiana - sinal 1
label .chat_i1_g6:
    $ chats_i1[6] = 11
    call setup_dialogue("chat_i1_g6_idle")
    call pass_time_dialogue
    t happy "A sério?"
    call pass_time_dialogue
    i happy "Sim, isso aconteceu mesmo!"
    call pass_time_dialogue
    h laugh "*risos*"
    call pass_time_dialogue
    e normal "*recebe uma notificação no telemóvel*"
    e normal "..."
    e angry "..."
    call pass_time_dialogue
    e angry "*atira com o telemóvel para dentro da mochila*"
    jump chat_exit

# carmen, manuela
#label .chat_i1_g7:
#    $ chats_i1[7] = -1
#    call setup_dialogue("chat_i1_g7_idle")
#    call pass_time_dialogue
#    c normal "Precisava de comprar umas calças novas, queres passar no centro comercial a seguir às aulas?"
#    call pass_time_dialogue
#    m normal "Hoje não me dava jeito... Que tal falarmos com a Patrícia e combinarmos um dia para irmos as três?"
#    call pass_time_dialogue
#    c happy "Ya, boa ideia. Falo com ela depois!"
#    call pass_time_dialogue
#    jump chat_exit

# manuela
label .chat_i1_g7:
    $ chats_i1[7] = -1
    call setup_dialogue("chat_i1_g7_idle")
    call pass_time_dialogue
    m normal "*a utilizar o telemóvel*"
    jump chat_exit

# abel, jorge, rui
label .chat_i1_g8:
    $ chats_i1[8] = -1
    call setup_dialogue("chat_i1_g8_idle")
    call pass_time_dialogue
    j normal "É verdade Rui, como anda isso da Associação?"
    call pass_time_dialogue
    r normal "Vai bem, o pessoal anda a fazer um bom trabalho."
    call pass_time_dialogue
    a normal "Não sei como arranjas tempo para isso, para as aulas e ainda consegues jogar connosco."
    call pass_time_dialogue
    r laugh "Muita força de vontade!"
    call pass_time_dialogue
    a laugh "*risos*"
    jump chat_exit

# sinais de alerta, substituem chats 0 e 5

# estrela - sinal
label .chat_i1_g9:
    $ chats_i1[0] = 10
    call setup_dialogue("chat_i1_g9_idle")
    call pass_time_dialogue
    e angry "Mãe, já disse que está tudo bem!"
    call pass_time_dialogue
    e normal "..."
    call pass_time_dialogue
    e normal "Tive nega mas não se passa nada. Só tenho de estudar mais aquela matéria."
    call pass_time_dialogue
    e normal "Não, não vi a tua mensagem porque tinha o telemóvel desligado."
    call pass_time_dialogue
    e angry "Porquê? Porque não me apetece ter o telemóvel ligado! Qual é o problema?"
    jump chat_exit

# estrela - sinal
label .chat_i1_g10:
    $ chats_i1[0] = -1
    call setup_dialogue("chat_i1_g9_idle")
    call pass_time_dialogue
    e sad "*a desenhar num caderno*"
    call screen chat_i1_g10
    jump chat_exit

screen chat_i1_g10:
    imagebutton:
        xalign 0.01 yalign 0.01 at rot(-90)
        idle im.Scale("x_idle.png", 100, 100, bilinear=True)
        hover im.Scale("x_hover.png", 100, 100, bilinear=True)
        action Jump("chat_exit")
        focus_mask True

# estrela, helder - sinal
label .chat_i1_g11:
    $ chats_i1[6] = -1
    call setup_dialogue("chat_i1_g11_idle")
    call pass_time_dialogue
    h normal "Tiveste quanto no teste?"
    call pass_time_dialogue
    e sad "Tirei negativa..."
    call pass_time_dialogue
    h sad "Então? Mas tu fartaste-te de estudar!"
    call pass_time_dialogue
    e sad "..."
    jump chat_exit
