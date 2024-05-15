label session_1_dialogues_i0:

# carmen, manuela, patricia
label .chat_i0_cb:
    $ active_rooms = [0, 1, 2, 3, 5, 7, 8, 19]
    $ drag_game = True
    $ situation = 10
    if (not tasks_discovered[session][2]):
        $ tasks_discovered[session][2] = True
        $ taskNew = True
        $ ping = True
    call setup_dialogue("chat_i0_cb_idle")
    call pass_time_dialogue
    m happy "O título da foto podia ser: {i}\"A Baleia fora de água\"{/i}."
    call pass_time_dialogue
    p disgust "Eu meti um like. Se fosse eu a andar assim de biquíni, morria!"
    call pass_time_dialogue
    c laugh "Era o que ela devia fazer."
    call pass_time_dialogue
    m happy "*Risos*"
    call pass_time_dialogue
    c laugh "Da próxima vez escrevo isso mesmo. Mata-te!"
    call pass_time_dialogue
    m happy "Sim, não fazes falta a ninguém. Vai morrer longe!"
    call pass_time_dialogue
    c laugh "*Risos*"
    call pass_time_dialogue
    if male:
        p annoyed "Para, tá ali o stôr. Esconde o telemóvel."
    else:
        p annoyed "Para, tá ali a stôra. Esconde o telemóvel."
    jump chat_exit

# estrela, helder, rui
label .chat_i0_g0:
    $ chats_i0[0] = -1
    call setup_dialogue("chat_i0_g0_idle")
    call pass_time_dialogue
    h happy "Obrigada pela ajuda pessoal. Estrela, posso ficar com o teu caderno hoje e entrego-te amanhã?"
    call pass_time_dialogue
    e happy "Sem problema, mas não te esqueças!"
    call pass_time_dialogue
    h happy "Claro, não te preocupes."
    call pass_time_dialogue
    r normal "Olhem, vocês conseguiram resolver o exercício 3.2 do teste modelo? Eu ontem bem que tentei mas não consegui."
    call pass_time_dialogue
    e normal "O 3.2? Esse acho que não fiz."
    call pass_time_dialogue
    h normal "Pois eu não consegui o exercício 3 inteiro, por isso é que vim pedir apontamentos."
    call pass_time_dialogue
    if male:
        r normal "Hmm ok, eu depois pergunto ao professor na aula."
    else:
        r normal "Hmm ok, eu depois pergunto à professora na aula."
    call pass_time_dialogue
    r normal "Já agora, algum de vocês sabe do Jorge? Ele não veio à aula de ontem."
    call pass_time_dialogue
    e normal "Eu não o vi."
    call pass_time_dialogue
    h normal "Também não."
    jump chat_exit

# jorge, samuel
label .chat_i0_g1:
    $ chats_i0[1] = -1
    call setup_dialogue("chat_i0_g1_idle")
    call pass_time_dialogue
    s normal "Sempre vens a minha casa hoje à tarde?"
    call pass_time_dialogue
    j normal "Népia, hoje não posso."
    call pass_time_dialogue
    s normal "Então? Tavas todo entusiasmado no outro dia, e agora não podes?"
    call pass_time_dialogue
    j normal "Pois eu sei, mas hoje não dá mesmo jeito."
    call pass_time_dialogue
    j normal "*telefone a tocar*"
    call pass_time_dialogue
    j normal "Pera aí, preciso de atender isto, nós depois falamos mais tarde."
    call pass_time_dialogue
    s normal "Ok na boa, até já."
    jump chat_exit

# abel, nando
label .chat_i0_g2:
    $ chats_i0[2] = -1
    call setup_dialogue("chat_i0_g2_idle")
    call pass_time_dialogue
    n happy "Vais lá estar na sexta feira, não é, Abel? Estou a contar contigo!"
    call pass_time_dialogue
    a happy "Já sabes que sim Nando, futebol é comigo."
    call pass_time_dialogue
    n normal "Também convidei o Jorge, tou só à espera de resposta dele."
    call pass_time_dialogue
    a happy "Se ele vier, ficamos com a equipa cheia."
    call pass_time_dialogue
    n normal "Yeap, e ele joga bem, por isso já tá ganho."
    call pass_time_dialogue
    a laugh "Calma campeão, é o Jorge, não é o Ronaldo!"
    call pass_time_dialogue
    n laugh "*gargalhadas*"
    jump chat_exit

# isabel, tatiana
label .chat_i0_g3:
    $ chats_i0[3] = 9
    call setup_dialogue("chat_i0_g3_idle")
    call pass_time_dialogue
    t sad "Tens um comprimido para a dor de cabeça?"
    call pass_time_dialogue
    i sad "Acho que sim, deixa ver na mala. Tatiana, tens a certeza que estás bem?"
    call pass_time_dialogue
    t sad "Não tenho conseguido dormir nada de jeito, é só isso..."
    #t sad "Sim, isto já passa."
    #call pass_time_dialogue
    #i sad "..."
    #call pass_time_dialogue
    #i normal "Ah é verdade, acabei de ler o penúltimo livro há uns dias."
    #call pass_time_dialogue
    #t normal "O que achaste?"
    #call pass_time_dialogue
    #i normal "Gostei bastante, apesar de ter ficado um bocado em choque com o final."
    #call pass_time_dialogue
    #t normal "Sim, é a reação que o pessoal costuma ter. Agora só precisas de ler o último e acabaste a saga."
    jump chat_exit

# helder, isabel
label .chat_i0_g4:
    $ chats_i0[4] = -1
    call setup_dialogue("chat_i0_g4_idle")
    call pass_time_dialogue
    h normal "Sempre consegues vir este fim de semana ao Centro de Apoio?"
    call pass_time_dialogue
    i happy "Sim! Tenho tarde livre por isso só preciso das horas."
    call pass_time_dialogue
    h normal "Fixe, em princípio podes aparecer lá a partir das 9h. Tens forma de ir para lá ou precisas de boleia?"
    call pass_time_dialogue
    i normal "Aquilo fica perto da estação não é?"
    call pass_time_dialogue
    h normal "Sim, são por volta de 10 minutos a pé."
    call pass_time_dialogue
    i happy "Então sem problema, eu vou de comboio e depois faço o resto a pé."
    call pass_time_dialogue
    h happy "Ok, então eu depois falo com eles e confirmo-te as horas."
    jump chat_exit

# jorge, nando
label .chat_i0_g5:
    $ chats_i0[5] = -1
    call setup_dialogue("chat_i0_g5_idle")
    call pass_time_dialogue
    n normal "Na sexta vamos ter aquele torneio de futebol."
    call pass_time_dialogue
    j normal "Huh-huh."
    call pass_time_dialogue
    n normal "Queres aparecer lá?"
    call pass_time_dialogue
    j normal "Hum não sei, tenho de ver."
    call pass_time_dialogue
    n annoyed "Meu, como assim tens de ver. Parece que tás com a cabeça na lua..."
    call pass_time_dialogue
    j sad "Desculpa Nando, tou só a pensar noutras cenas. Futebol? Ya, parece-me bem, mas amanhã confirmo-te, sem falta."
    call pass_time_dialogue
    n happy "Pronto, era só isso que eu queria."
    jump chat_exit

# abel, rui
label .chat_i0_g6:
    $ chats_i0[6] = -1
    call setup_dialogue("chat_i0_g6_idle")
    call pass_time_dialogue
    a normal "Chegaste a ver o último episódio?"
    call pass_time_dialogue
    r happy "Sim! Não estava nada à espera do final, apanhou-me completamente de surpresa..."
    call pass_time_dialogue
    a happy "É né?! Eu fiquei à toa, como é que eles vão continuar a história na segunda temporada? Estou para ver."
    call pass_time_dialogue
    r happy "Também estou curioso, agora que a personagem principal ficou do lado dos maus, tudo pode acontecer."
    call pass_time_dialogue
    a normal "Olha, não comentes o final com o Jorge, ele ainda não viu o episódio!"
    call pass_time_dialogue
    r normal "Não percebo o que é que ele anda a fazer, ele hoje de manhã também não apareceu na aula."
    call pass_time_dialogue
    a normal "Eu acho que ele foi sair ontem à tarde com mais pessoal, mas não tenho a certeza. Se calhar teve a ver com isso."
    jump chat_exit

# estrela, samuel
label .chat_i0_g7:
    $ chats_i0[7] = -1
    call setup_dialogue("chat_i0_g7_idle")
    call pass_time_dialogue
    #e normal "Tava a pensar que podíamos ver do projeto este fim de semana. Tenho receio que depois não tenha tempo para fazer tudo, já assumindo que o plano da viagem corre perfeitamente."
    #call pass_time_dialogue
    #s normal "Sim, sem problemas. Eu este sábado à tarde estou disponível."
    #call pass_time_dialogue
    #e normal "Eu também. Falamos online?"
    #call pass_time_dialogue
    #s normal "Sim, acho que para primeiro dia não precisamos de estar presentes."
    call pass_time_dialogue
    e normal "A Tatiana? Sabes dela?"
    call pass_time_dialogue
    s sad "Tem estado na casa de banho a maior parte do dia."
    call pass_time_dialogue
    e sad "Então? Ela está mal disposta ou algo assim?"
    call pass_time_dialogue
    s sad "Não, tu não viste o que lhe fizeram?"
    call pass_time_dialogue
    e sad "Não..."
    call pass_time_dialogue
    s sad "Eu depois desta aula conto-te."
    jump chat_exit

# tatiana
label .chat_i0_g8:
    $ chats_i0[8] = 10
    call setup_dialogue("chat_i0_g8_idle")
    call pass_time_dialogue
    t sad "*a olhar para o telemóvel*"
    jump chat_exit

# sinais de alerta, substituem chats 3 e 8

# tatiana
label .chat_i0_g9:
    $ chats_i0[3] = -1
    call setup_dialogue("chat_i0_g9_idle")
    call pass_time_dialogue
    t normal "*a ouvir música*"
    call pass_time_dialogue
    grupo_alunos "*apontam para a Tatiana enquanto riem*"
    call pass_time_dialogue
    t sad "*esconde a cabeça entre os braços*"
    jump chat_exit

# tatiana
label .chat_i0_g10:
    $ chats_i0[8] = -1
    $ tras_pavilhao = True
    call setup_dialogue("chat_i0_g10_idle")
    call pass_time_dialogue
    t normal "*a mexer no telemóvel*"
    call pass_time_dialogue
    t normal "*som de mensagem*"
    call pass_time_dialogue
    t sad "..."
    call pass_time_dialogue
    t cry "*vai-se embora em direção ao pátio*"
    jump chat_exit

# tatiana
label .chat_i0_g11:
    call toggle_UI
    call set_scene(20, True)
    show image "chats/session_1/chat_i0_g9_idle.png":
        zoom 2
        xalign 0.5
        yalign 0.2
    t cry "..."
    $ tras_pavilhao = False
    jump pavilhao
