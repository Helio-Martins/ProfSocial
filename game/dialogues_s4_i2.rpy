label session_4_dialogues_i2:

# carmen, manuela, nando
label .chat_i2_cb:
    $ active_rooms = [0, 1, 2, 3, 5, 7, 8, 19]
    $ drag_game = True
    $ situation = 120
    call setup_dialogue("chat_i2_cb_idle")
    call pass_time_dialogue
    n annoyed "O que é que sabem que eu não sei?"
    call pass_time_dialogue
    c sad "Nando, tem calma. De certeza que há uma explicação."
    call pass_time_dialogue
    n annoyed "Explicação para quê?"
    call pass_time_dialogue
    m sad "Tens de prometer que não te vais passar com a Patrícia. Ela não está bem."
    call pass_time_dialogue
    n annoyed "Digam de uma vez por todas!"
    call pass_time_dialogue
    c normal "Existe uma foto do Abel e da Patrícia que andam a partilhar..."
    call pass_time_dialogue
    n angry "..."
    call pass_time_dialogue
    m normal "Antes que te passes. Eu tenho a certeza que ela e o Abel são só amigos e que a foto é falsa."
    call pass_time_dialogue
    c normal "Sim, vê-se perfeitamente que não é ela. É fake."
    call pass_time_dialogue
    n angry "Quero ver essa foto e é já!"
    call pass_time_dialogue
    c sad "Tens de prometer que não te vais passar."
    call pass_time_dialogue
    n angry "Daqui a nada passo-me é com vocês!"
    "*som de notificação no telemóvel do Nando*"
    n annoyed "*olha para o telemóvel*"
    n angry "*sai a correr*"
    call pass_time_dialogue
    m sad "Nando, espera!"
    call pass_time_dialogue
    c sad "Não faças nada parvo! Nando, volta!"
    jump chat_exit

# carmen, manuela
label .chat_i2_g0:
    $ chats_i2[0] = -1
    call setup_dialogue("chat_i2_g0_idle")
    call pass_time_dialogue
    c normal "Na sexta feira vou visitar a Patrícia outra vez. Vens também?"
    call pass_time_dialogue
    m normal "Claro que sim."
    call pass_time_dialogue
    c normal "As visitas são de manhã, depois combinamos horas."
    call pass_time_dialogue
    m normal "Parece-me bem."
    jump chat_exit

# helder
label .chat_i2_g1:
    $ chats_i2[1] = -1
    call setup_dialogue("chat_i2_g1_idle")
    call pass_time_dialogue
    h laugh "*a mexer no telemóvel*"
    jump chat_exit

# abel, rui
label .chat_i2_g2:
    $ chats_i2[2] = -1
    call setup_dialogue("chat_i2_g2_idle")
    call pass_time_dialogue
    r normal "Abel, não queres falar sobre a situação?"
    call pass_time_dialogue
    a normal "Não, deixa estar. Estou bem."
    call pass_time_dialogue
    r sad "Tens a certeza?"
    call pass_time_dialogue
    a angry "Já disse que sim. Não sejas chato."
    jump chat_exit

# samuel, tatiana
label .chat_i2_g3:
    $ chats_i2[3] = -1
    call setup_dialogue("chat_i2_g3_idle")
    call pass_time_dialogue
    s normal "Queres passar no café depois das aulas?"
    call pass_time_dialogue
    t normal "Sim, podemos ir. Com sorte ainda apanho o último bolo de arroz."
    call pass_time_dialogue
    s laugh "*risos*"
    jump chat_exit

# estrela, isabel, jorge
label .chat_i2_g4:
    $ chats_i2[4] = -1
    call setup_dialogue("chat_i2_g4_idle")
    call pass_time_dialogue
    j normal "Amanhã dá para juntar ao grupo de estudo?"
    call pass_time_dialogue
    i happy "Claro que sim!"
    call pass_time_dialogue
    e normal "Obviamente."
    call pass_time_dialogue
    j normal "Têm de ter muita paciencia comigo, eu estou um pouco fraco no estudo."
    call pass_time_dialogue
    e happy "Não te preocupes, nós ajudamos-te."
    jump chat_exit

##########

# carmen, manuela
label .chat_i2_g5:
    $ chats_i2[5] = -1
    call setup_dialogue("chat_i2_g5_idle")
    call pass_time_dialogue
    m normal "Com esta situação toda, esqueci-me do trabalho de grupo. Como vamos fazer agora?"
    call pass_time_dialogue
    if male:
        c normal "Se falarem com o professor, de certeza que ele vos dá tempo extra. Ele vai compreender."
    else:
        c normal "Se falarem com a professora, de certeza que ela vos dá tempo extra. Ela vai compreender."
    call pass_time_dialogue
    m normal "Espero que sim..."
    jump chat_exit

# helder, rui
label .chat_i2_g6:
    $ chats_i2[6] = -1
    call setup_dialogue("chat_i2_g6_idle")
    call pass_time_dialogue
    r normal "Não achas que isto foi longe demais?"
    call pass_time_dialogue
    h normal "Talvez. Mas agora também já é demasiado tarde."
    call pass_time_dialogue
    r normal "Ainda vais a tempo de apagar a foto."
    call pass_time_dialogue
    h normal "Hmm, vou pensar no assunto."
    jump chat_exit

# abel, jorge - situaçao
label .chat_i2_g7:
    $ chats_i2[7] = -1
    call setup_dialogue("chat_i2_g7_idle")
    call pass_time_dialogue
    j normal "Abel, amanhã queres estudar aqui na escola?"
    call pass_time_dialogue
    a normal "Não, obrigado."
    call pass_time_dialogue
    j normal "Já não falta muito para o exame, tens a certeza?"
    call pass_time_dialogue
    a normal "Sim, eu estudo melhor sozinho. Não te preocupes."
    jump chat_exit

# estrela, isabel, samuel, tatiana
label .chat_i2_g8:
    $ chats_i2[8] = -1
    call setup_dialogue("chat_i2_g8_idle")
    call pass_time_dialogue
    t normal "De certeza que os professores vão querer reunir com toda a gente."
    call pass_time_dialogue
    i normal "Sim. Há uma aluna no hospital. Se não dissessem nada era muito estranho."
    call pass_time_dialogue
    s sad "Só quero passar à frente disto. Já estou farto."
    call pass_time_dialogue
    e sad "Sou da mesma opinião..."
    jump chat_exit
