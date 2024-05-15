label session_4_dialogues_i0:

# abel, jorge, manuela (+nando)
label .chat_i0_cb:
    $ active_rooms = [0, 1, 2, 7, 8, 19]
    $ drag_game = True
    $ situation = 100
    if (not tasks_discovered[session][2]):
        $ tasks_discovered[session][2] = True
        $ taskNew = True
        $ ping = True
    call setup_dialogue("chat_i0_cb_idle")
    call pass_time_dialogue
    j sad "Que cena foi aquela?"
    call pass_time_dialogue
    a normal "Pá, nem quero saber se queres que te diga."
    call pass_time_dialogue
    j sad "Então mas existe alguma foto?"
    call pass_time_dialogue
    m angry "Ai Jorge não te metas!"
    call pass_time_dialogue
    j normal "Estou só preocupado. É isso que os amigos fazem."
    call pass_time_dialogue
    m sad "Só sei que a Patrícia não se pode enervar mais, malta..."
    call pass_time_dialogue
    a normal "Tranquila... Se o gajo fizer mais alguma ameaça eu apanho-o lá fora."
    call pass_time_dialogue
    j sad "Como é que está a Patrícia afinal?"
    call pass_time_dialogue
    m sad "Continua internada, mas está melhor. Tem de fazer bué exames..."
    "*o Nando junta-se ao grupo*"
    n annoyed "Abel, mano, temos de falar!"
    m sad "Nando, não me digas que acreditaste naquilo?"
    n annoyed "Isto não é contigo! Tou a falar com o Abel."
    a normal "Estou aqui, podes falar, mas olha que eu não tenho nada para te dizer."
    n angry "De certeza? Que foto é que tu tens com a minha miúda?"
    a laugh "Deves estar a gozar! Foste atrás daquela conversa?"
    n angry "Tás a ser falso! Diz a verdade."
    a laugh "Estás-te a passar, mano. Vou andando para o judo. Até logo pessoal."
    jump chat_exit

# abel, rui (+jorge) - sinal 1
label .chat_i0_g0:
    $ tras_pavilhao = True
    $ chats_i0[0] = -1
    call setup_dialogue("chat_i0_g0_idle")
    call pass_time_dialogue
    a laugh "Conheces a piada do iogurte?"
    call pass_time_dialogue
    r normal "Não."
    call pass_time_dialogue
    a laugh "É natural."
    call pass_time_dialogue
    r laugh "Ahaha, mano, essa é mesma seca!"
    "*aparece o Jorge*"
    call pass_time_dialogue
    j sad "Não ias ao judo?"
    call pass_time_dialogue
    a angry "Mas és meu pai agora? Queres ver se fiz o TPC também?"
    call pass_time_dialogue
    r sad "Calma! Que é que se passa contigo?"
    jump chat_exit

# isabel, samuel, tatiana - sinal 2
label .chat_i0_g1:
    $ chats_i0[1] = -1
    call setup_dialogue("chat_i0_g1_idle")
    call pass_time_dialogue
    t sad "Ontem no torneio de futebol o Abel bateu num jogador da outra equipa."
    call pass_time_dialogue
    s surprise "A sério?"
    call pass_time_dialogue
    i sad "Acho que o estavam a provocar por causa do comentário sobre a Patrícia. O Abel passou-se e foi expulso."
    jump chat_exit

# estrela, helder - sinal 1
label .chat_i0_g2:
    $ chats_i0[2] = -1
    call setup_dialogue("chat_i0_g2_idle")
    call pass_time_dialogue
    e normal "Hélder, não acho boa ideia o que estás a fazer."
    call pass_time_dialogue
    h normal "Qual é a cena?"
    call pass_time_dialogue
    e sad "A Patrícia está no hospital!"
    call pass_time_dialogue
    h normal "E?"
    call pass_time_dialogue
    e sad "Não percebes que isto pode correr muita mal?"
    call pass_time_dialogue
    h normal "Por causa da foto? Que exagero! Só quero que admitam que erraram."
    jump chat_exit

# manuela, nando
label .chat_i0_g3:
    $ chats_i0[3] = -1
    call setup_dialogue("chat_i0_g3_idle")
    call pass_time_dialogue
    n sad "O que é que a Cármen disse?"
    call pass_time_dialogue
    m sad "A Cármen está a vir para a escola agora. Ela diz que a Patrícia está a repousar."
    call pass_time_dialogue
    n sad "..."
    jump chat_exit

##########

# jorge, rui - sinal 3
label .chat_i0_g4:
    $ chats_i0[4] = -1
    if chats_i0[5] == -1:
        $ chats_i0[4] = 9
    call setup_dialogue("chat_i0_g4_idle")
    call pass_time_dialogue
    r sad "Temos de falar com o Abel. Acho que ele anda bué agressivo."
    call pass_time_dialogue
    j sad "Ya, no ano passado andava quase sempre enervado. Às vezes até dava murros e partia coisas na escola e nem ia às aulas."
    call pass_time_dialogue
    r normal "Sim, mas isso foi antes de ele entrar para o Judo. Depois deixou de fazer essas cenas."
    call pass_time_dialogue
    j sad "Pois, mas com esta história toda da Patrícia..."
    call pass_time_dialogue
    r sad "Ya, acho que se as cenas continuam assim ele vai desistir e voltar ao que era."
    jump chat_exit

# helder, nando - sinal 2
label .chat_i0_g5:
    $ chats_i0[5] = -1
    if chats_i0[4] == -1:
        $ chats_i0[5] = 9
    call setup_dialogue("chat_i0_g5_idle")
    call pass_time_dialogue
    n sad "Hélder, dá para conversar?"
    call pass_time_dialogue
    h laugh "Então? Agora já querem falar?"
    call pass_time_dialogue
    n sad "Eu só quero saber a verdade. Existe foto?"
    call pass_time_dialogue
    h laugh "Vais ter de esperar para ver."
    call pass_time_dialogue
    n sad "É a minha vida. Tás-te a meter com a minha namorada e o meu melhor amigo."
    call pass_time_dialogue
    h angry "Estou-me a lixar para isso! Vocês trataram bué mal o Samuel e a Tatiana. Agora é a vossa vez de sofrerem as consequências."
    jump chat_exit

# estrela, samuel, tatiana
label .chat_i0_g6:
    $ chats_i0[6] = -1
    call setup_dialogue("chat_i0_g6_idle")
    call pass_time_dialogue
    e normal "A Cármen ainda está no hospital?"
    call pass_time_dialogue
    t normal "Pelo que percebi sim. Foi visitar a Patrícia."
    call pass_time_dialogue
    s sad "Esta situação ficou muito grave pessoal."
    call pass_time_dialogue
    e sad "Pois..."
    jump chat_exit

# isabel, manuela
label .chat_i0_g7:
    $ chats_i0[7] = -1
    call setup_dialogue("chat_i0_g7_idle")
    call pass_time_dialogue
    i normal "Há novidades?"
    call pass_time_dialogue
    m normal "A Cármen está a caminho da escola agora e depois falamos melhor."
    call pass_time_dialogue
    i normal "OK, obrigada."
    jump chat_exit

# abel - sinal 4 (pavilhao)
label .chat_i0_g8:
    call toggle_UI
    call set_scene(20, True)
    show image "chats/session_4/chat_i0_g8_idle.png":
        zoom 2
        xalign 0.5
        yalign 0.2
    auxiliar "O que é que o menino tá aí a fazer? Conhece as regras. Vou fazer queixa sua!"
    call pass_time_dialogue
    a angry "Deixe-me! Também não quero estar nesta estúpida escola. Vou bazar."
    $ tras_pavilhao = False
    jump pavilhao

# sinal de alerta, substitui chats 4 e 5

# helder, jorge - sinal 3
label .chat_i0_g9:
    #$ chats_i0[9] = -1
    $ chats_i0[4] = -1
    $ chats_i0[5] = -1
    call setup_dialogue("chat_i0_g9_idle")
    call pass_time_dialogue
    h happy "Meteram-se com as pessoas erradas e agora estão cheios de medo."
    call pass_time_dialogue
    j surprise "Tás a falar do quê?"
    call pass_time_dialogue
    h happy "Depois vês. Ainda me vão agradecer!"
    jump chat_exit
