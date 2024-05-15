label session_3_dialogues_i2:

# samuel, tatiana
label .chat_i2_cb:
    $ active_rooms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 19]
    $ drag_game = True
    $ situation = 90
    call setup_dialogue("chat_i2_cb_idle")
    call pass_time_dialogue
    t sad "Samuel, espera! Quero falar contigo."
    call pass_time_dialogue
    s sad "Hum... Depois falamos. Tenho de ir."
    call pass_time_dialogue
    t sad "Samuel, eu já percebi tudo... Acho que o problema é comigo e tu foste apanhado no meio. Tu estás bem? Estou preocupada."
    call pass_time_dialogue
    s sad "É na boa, eu vou ficar bem, não te preocupes."
    call pass_time_dialogue
    t normal "Eu estou do teu lado. Queria que soubesses."
    call pass_time_dialogue
    s normal "Eu sabia que tu eras especial..."
    call pass_time_dialogue
    t happy "Obrigada..."
    call pass_time_dialogue
    s normal "Eu é que não vou deixar que te voltem a desrespeitar outra vez, vais ver. Até amanhã!"
    call pass_time_dialogue
    t sad "Samuel, o que é que queres dizer com isso? Não faças nada, ok?"
    call pass_time_dialogue
    s normal "Não te preocupes. Vai correr tudo bem!"
    jump chat_exit

# abel, rui
label .chat_i2_g0:
    $ chats_i2[0] = -1
    call setup_dialogue("chat_i2_g0_idle")
    call pass_time_dialogue
    a normal "Achas que vão fechar a escola por causa das cheias?"
    call pass_time_dialogue
    r normal "Eu espero que não... Os professores têm andado a preparar as coisas do picnic, e acho que ainda faltam coisas para fazer."
    call pass_time_dialogue
    a normal "Pois, se o picnic fosse cancelado isso seria uma treta autêntica."
    jump chat_exit

# samuel, tatiana
label .chat_i2_g1:
    $ chats_i2[1] = -1
    jump chat_exit

# estrela, helder, jorge - picnic
label .chat_i2_g2:
    $ chats_i2[2] = -1
    call setup_dialogue("chat_i2_g2_idle")
    call pass_time_dialogue
    h normal "Vais levar comida feita para o picnic? Ouvi dizer que és uma grande cozinheira."
    call pass_time_dialogue
    e happy "Haha, sabes muito. Talvez, vou pensar no assunto."
    call pass_time_dialogue
    j happy "Eu é que sou um grande cozinheiro, os meus cereais são os melhores do mundo!"
    call pass_time_dialogue
    h laugh "*risos*"
    jump chat_exit

# isabel, manuela
label .chat_i2_g3:
    $ chats_i2[3] = -1
    call setup_dialogue("chat_i2_g3_idle")
    call pass_time_dialogue
    i angry "Diz à tua amiga Patrícia que o que ela fez não se faz."
    call pass_time_dialogue
    m disgust "Podes dizer-lhe pessoalmente, não precisas de vir falar comigo."
    call pass_time_dialogue
    i angry "Olha, esquece. Não dá para falar convosco."
    jump chat_exit

# carmen, nando, patricia
label .chat_i2_g4:
    $ chats_i2[4] = -1
    call setup_dialogue("chat_i2_g4_idle")
    call pass_time_dialogue
    p angry "Agora fazem parecer que eu é que sou a má da fita."
    call pass_time_dialogue
    c disgust "Pois. É mesmo preciso ter lata."
    call pass_time_dialogue
    n annoyed "Há pessoal que não presta mesmo."
    jump chat_exit

#####

# carmen, patricia
label .chat_i2_g5:
    $ chats_i2[5] = -1
    call setup_dialogue("chat_i2_g5_idle")
    call pass_time_dialogue
    p disgust "Esta situação deixou-me toda stressada. Que nervos."
    call pass_time_dialogue
    c happy "Eu percebo-te amiga. Mas olha, já falta pouquíssimo tempo para o concerto!"
    call pass_time_dialogue
    p normal "Verdade, já quase me esquecia disso."
    call pass_time_dialogue
    c happy "Sim, vai ser brutal!"
    call pass_time_dialogue
    p happy "Tens razão, vamos divertir-nos à brava!"
    jump chat_exit

# abel, nando - canil
label .chat_i2_g6:
    $ chats_i2[6] = -1
    call setup_dialogue("chat_i2_g6_idle")
    call pass_time_dialogue
    n normal "Hoje à tarde sempre vens ao canil?"
    call pass_time_dialogue
    a normal "Yeap, vou visitar os teus primos."
    call pass_time_dialogue
    n laugh "Que comediante que tu és!"
    call pass_time_dialogue
    a laugh "*risos*"
    jump chat_exit

# manuela
label .chat_i2_g7:
    $ chats_i2[7] = -1
    call setup_dialogue("chat_i2_g7_idle")
    call pass_time_dialogue
    m normal "*a mexer no telemóvel*"
    jump chat_exit

# helder, jorge
label .chat_i2_g8:
    $ chats_i2[8] = -1
    call setup_dialogue("chat_i2_g8_idle")
    call pass_time_dialogue
    h normal "*a comer uma merenda*"
    call pass_time_dialogue
    j normal "O bar ainda tem merendas?"
    call pass_time_dialogue
    h happy "Quando fui tinha ainda uma ou duas. Se fores a correr acho que ainda apanhas."
    call pass_time_dialogue
    j laugh "Já estou lá!"
    jump chat_exit

# samuel, tatiana
label .chat_i2_g9:
    $ chats_i2[9] = -1
    jump chat_exit

# estrela, isabel, rui
label .chat_i2_g10:
    $ chats_i2[10] = -1
    call setup_dialogue("chat_i2_g10_idle")
    call pass_time_dialogue
    i sad "Pessoal, esta situação é horrível."
    call pass_time_dialogue
    e disgust "Pois, que maravilha de colegas que temos."
    call pass_time_dialogue
    r annoyed "Precisamos de ter calma. Isto vai ficar resolvido."
    call pass_time_dialogue
    r normal "Eventualmente."
    call pass_time_dialogue
    r sad "Espero eu..."
    jump chat_exit
