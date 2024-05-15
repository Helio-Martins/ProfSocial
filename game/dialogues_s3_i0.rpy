label session_3_dialogues_i0:

# jorge, manuela, nando, patricia, rui (+helder)
label .chat_i0_cb:
    $ active_rooms = [0, 1, 2, 3, 5, 7, 8, 19]
    $ drag_game = True
    $ situation = 70
    if (not tasks_discovered[session][2]):
        $ tasks_discovered[session][2] = True
        $ taskNew = True
        $ ping = True
    call setup_dialogue("chat_i0_cb_idle")
    n normal "Mano, não percebi aquele post que puseste ontem no Com@Viver."
    r normal "Acho que as pessoas deviam saber que o cyberbullying pode acontecer a qualquer um."
    n laugh "Isso é estúpido!"
    p laugh "*risos*"
    m normal "Mas o que é que o Rui pôs no Com@Viver? Eu não vi."
    p disgust "Ai, como é que era? Era qualquer coisa tipo: “Quem cala consente.”"
    m disgust "Qual foi a ideia?"
    j normal "Rui, não ligues, eu concordo contigo. Acho que é preciso falar com alguém quando se sabe alguma coisa."
    n laugh "Vocês são é muita betinhos!"
    m normal "Eu acho que se vires alguma coisa, é melhor não dizeres nada. Depois caem em cima de ti."
    p angry "Ya, ninguém tem nada a ver com isso!"
    "*O Hélder junta-se ao grupo*"
    h angry "Malta, é bom que aquilo que aconteceu não se repita, estou a avisar!"
    n angry "Hélder, já te disse uma vez. É melhor bazares!"
    h angry "Não penses que tenho medo de ti ou de algum de vocês."
    n angry "Mas olha que é melhor teres."
    h angry "Também gostavas que te chamassem paneleiro?"
    n angry "Se lhe chamaram, é porque o gajo é capaz de ser."
    "*O Hélder empurra o Nando. O Rui segura-o.*"
    r angry "Tenham lá calma pessoal!"
    jump chat_exit

# estrela, helder, rui
label .chat_i0_g0:
    $ chats_i0[0] = -1
    call setup_dialogue("chat_i0_g0_idle")
    call pass_time_dialogue
    h normal "Vocês já fizeram a fase 2 do projeto? Nós ainda não acabámos a primeira."
    call pass_time_dialogue
    e normal "Ainda não."
    call pass_time_dialogue
    r normal "Nós já começámos essa parte. Não é muito difícil."
    call pass_time_dialogue
    h laugh "Bom saber. Nós estamos a ficar sem tempo para acabar o projeto!"
    jump chat_exit

# abel, jorge - sinal 1
label .chat_i0_g1:
    $ chats_i0[1] = -1
    call setup_dialogue("chat_i0_g1_idle")
    call pass_time_dialogue
    j normal "Já falaste com o Samuel hoje?"
    call pass_time_dialogue
    a normal "Népia. Acho que ele ficou a xonar."
    call pass_time_dialogue
    j sad "Tínhamos combinado ver umas cenas para o trabalho de grupo."
    call pass_time_dialogue
    a normal "Não sei se vai dar. O Samuel às 3 da manhã estava online a jogar. Vi uma mensagem dele hoje quando acordei. Acho que não se levantou da cama."
    call pass_time_dialogue
    j sad "Epá, depois do que aconteceu também não sei se tinha vontade de vir hoje olhar para aqueles palhaços."
    jump chat_exit

# nando
label .chat_i0_g2:
    $ chats_i0[2] = -1
    call setup_dialogue("chat_i0_g2_idle")
    call pass_time_dialogue
    n laugh "*a rir-se enquanto usa o telemóvel*"
    jump chat_exit

# isabel, tatiana - sinal 3
label .chat_i0_g3:
    $ chats_i0[3] = -1
    call setup_dialogue("chat_i0_g3_idle")
    call pass_time_dialogue
    i normal "Não desconfiavas que o Samuel gostava de ti?"
    call pass_time_dialogue
    t annoyed "Não! Ele nunca me diz nada. Está sempre calado."
    call pass_time_dialogue
    i sad "Pois, ele não se dá quase com ninguém."
    call pass_time_dialogue
    t sad "Nem acredito que lhe disseram aquilo para chegarem até mim..."
    call pass_time_dialogue
    i sad "Se o Samuel já tinha problemas em falar com as pessoas, agora imagino..."
    jump chat_exit

# carmen, manuela, patricia
label .chat_i0_g4:
    $ chats_i0[4] = -1
    call setup_dialogue("chat_i0_g4_idle")
    call pass_time_dialogue
    c happy "Esta semana querem ir às compras?"
    call pass_time_dialogue
    m normal "Outra vez? Fomos a semana passada."
    call pass_time_dialogue
    c happy "Anda lá!"
    call pass_time_dialogue
    p normal "Eu não me importo."
    call pass_time_dialogue
    m normal "..."
    m normal "Logo vejo."
    jump chat_exit

########

# samuel - sinal 5
label .chat_i0_g5:
    $ chats_i0[5] = -1
    call setup_dialogue("chat_i0_g5_idle")
    call pass_time_dialogue
    s sad "*a olhar à sua volta, com o telemóvel nas mãos*"
    jump chat_exit

# helder, rui
label .chat_i0_g6:
    $ chats_i0[6] = -1
    call setup_dialogue("chat_i0_g6_idle")
    call pass_time_dialogue
    r normal "Quando é que vai ser o picnic?"
    call pass_time_dialogue
    h normal "Para a semana. Quarta feira, para ser preciso."
    call pass_time_dialogue
    r normal "Ah, ok. Por momentos pensei que fosse na sexta feira. Eu não posso na sexta."
    call pass_time_dialogue
    h normal "Tens coisas planeadas?"
    r normal "Mais ou menos..."
    jump chat_exit

# estrela, isabel, tatiana
label .chat_i0_g7:
    $ chats_i0[7] = -1
    call setup_dialogue("chat_i0_g7_idle")
    call pass_time_dialogue
    e normal "Já sabem o que vão levar no picnic?"
    call pass_time_dialogue
    i happy "Ainda não, mas estou super empolgada!"
    call pass_time_dialogue
    t happy "Sim, acho que este picnic vai fazer bem a toda a gente."
    call pass_time_dialogue
    e sad "Pois, considerando o que tem acontecido nas últimas semanas..."
    jump chat_exit

# carmen, manuela, nando, patricia
label .chat_i0_g8:
    $ chats_i0[8] = -1
    call setup_dialogue("chat_i0_g8_idle")
    call pass_time_dialogue
    c normal "Pessoal, o concerto está-se a aproximar. Como estamos?"
    call pass_time_dialogue
    p happy "Por mim, vamos!"
    call pass_time_dialogue
    n normal "Já sabem, eu tou sempre disponível."
    call pass_time_dialogue
    m normal "Eu ainda tenho que confirmar com a minha mãe, por causa do ballet."
    call pass_time_dialogue
    p normal "Ah, pois é. Esqueci-me que tens isso."
    jump chat_exit

###########

# abel, jorge (+samuel) - sinal 4
label .chat_i0_g9:
    $ chats_i0[1] = -1
    $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 99, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    call setup_dialogue("chat_i0_g9_idle")
    call pass_time_dialogue
    j normal "Ali está ele."
    call pass_time_dialogue
    a normal "Samuel, espera aí mano. Vem falar connosco. O que é que se passa?"
    call pass_time_dialogue
    s sad "*sai a correr*"
    call pass_time_dialogue
    j sad "O que é que se passa com ele? Está a fugir de nós?"
    jump chat_exit

# samuel - sinal 2
label .chat_i0_g10:
    $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    call setup_dialogue("chat_i0_g10_idle")
    call pass_time_dialogue
    s sad "*a estudar sozinho*"
    jump chat_exit
