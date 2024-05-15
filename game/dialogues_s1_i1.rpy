label session_1_dialogues_i1:

# estrela
label .chat_i1_g0:
    $ chats_i1[0] = -1
    call setup_dialogue("chat_i1_g0_idle")
    call pass_time_dialogue
    e disgust "*concentrada a ler documentos relacionados com a viagem*"
    call pass_time_dialogue
    if male:
        e happy "Olá professor!"
    else:
        e happy "Olá professora!"
    jump chat_exit

# samuel, tatiana
label .chat_i1_g1:
    $ chats_i1[1] = -1
    call setup_dialogue("chat_i1_g1_idle")
    call pass_time_dialogue
    s sad "Estás melhor?"
    call pass_time_dialogue
    t sad "Sim, está tudo bem. Mais do mesmo."
    call pass_time_dialogue
    s happy "Que tal irmos sair hoje à tarde? Podemos passar naquele parque ao pé do rio."
    call pass_time_dialogue
    t happy "Boa ideia, talvez me dê um bocadinho de sossego."
    call pass_time_dialogue
    s happy "Ok, então depois das aulas eu passo pela biblioteca para imprimir um documento e depois vou ter contigo à entrada."
    call pass_time_dialogue
    t normal "Está bem."
    jump chat_exit

# jorge, nando
label .chat_i1_g2:
    $ chats_i1[2] = 12
    call setup_dialogue("chat_i1_g2_idle")
    call pass_time_dialogue
    n annoyed "*a olhar para o telemóvel*"
    call pass_time_dialogue
    j normal "Nando! Então? O que é tás a fazer?"
    call pass_time_dialogue
    n normal "Ah, nada, nada. Onde é que íamos?"
    call pass_time_dialogue
    j normal "Ao bar. Tá tudo bem?"
    call pass_time_dialogue
    n sad "Ya, tudo. Por acaso não viste a Patrícia, pois não?"
    call pass_time_dialogue
    j happy "Não. É a tua namorada, não a minha."
    call pass_time_dialogue
    n normal "Muito engraçado. Anda masé ao bar."
    jump chat_exit

# rui, isabel, abel
label .chat_i1_g3:
    $ chats_i1[3] = -1
    call setup_dialogue("chat_i1_g3_idle")
    call pass_time_dialogue
    r normal "Pessoal, como querem fazer com o projeto? Podemos começar a distribuir tarefas se quiserem."
    call pass_time_dialogue
    i normal "Por mim tanto faz, é como preferirem."
    call pass_time_dialogue
    a normal "Eu não me faz diferença, podemos reunir já hoje à tarde se quiserem."
    call pass_time_dialogue
    r normal "Por mim tudo bem. E contigo Isabel?"
    call pass_time_dialogue
    i happy "Eu também posso! Passamos na biblioteca então?"
    call pass_time_dialogue
    a normal "Ya, pode ser."
    call pass_time_dialogue
    r normal "Falamos mais tarde então."
    jump chat_exit

# helder
label .chat_i1_g4:
    $ chats_i1[4] = -1
    call setup_dialogue("chat_i1_g4_idle")
    call pass_time_dialogue
    h happy "*focado no telemóvel*"
    jump chat_exit

# carmen, manuela, patricia
label .chat_i1_g5:
    $ chats_i1[5] = -1
    call setup_dialogue("chat_i1_g5_idle")
    call pass_time_dialogue
    p disgust "Ela agora vai acalmar."
    call pass_time_dialogue
    c disgust "E se não acalmar, já sabe o que acontece se continua com as tretas dela."
    call pass_time_dialogue
    m happy "Mudando de assunto, vocês já viram quem vai dar um concerto no verão? Tou bué entusiasmada!"
    call pass_time_dialogue
    p happy "Sim, temos de ir ver!"
    call pass_time_dialogue
    c happy "Bora! Eu já falei com os meus pais, eles deixam-me ir!"
    jump chat_exit

# estrela, samuel, tatiana
label .chat_i1_g6:
    $ chats_i1[6] = -1
    call setup_dialogue("chat_i1_g6_idle")
    call pass_time_dialogue
    e normal "Pessoal, podíamos ver do projeto já este fim de semana? Tenho receio que depois não tenha tempo para fazer tudo, já assumindo que o plano da viagem corre perfeitamente."
    call pass_time_dialogue
    t normal "Sim, sem problemas. Eu este sábado à tarde estou disponível."
    call pass_time_dialogue
    s normal "Eu também. Falamos online?"
    call pass_time_dialogue
    e normal "Sim, acho que para primeiro dia não precisamos de estar presentes."
    call pass_time_dialogue
    t normal "A que horas querem marcar?"
    call pass_time_dialogue
    e normal "Por mim pode ser logo a seguir ao almoço, às 13h00."
    call pass_time_dialogue
    s normal "Às 13h00 eu ainda não estou em casa, podemos fazer às 14h00?"
    call pass_time_dialogue
    e normal "Claro, por mim é na boa."
    call pass_time_dialogue
    t normal "Está bem, fica marcado para as 14h00."
    jump chat_exit

# nando
label .chat_i1_g7:
    $ chats_i1[7] = 13
    call setup_dialogue("chat_i1_g7_idle")
    call pass_time_dialogue
    n mean "Pensava que te tinha avisado para não passares nesta zona!"
    call pass_time_dialogue
    aluno "Desculpa Nando, foi sem querer... Eu vou embora!"
    call pass_time_dialogue
    n mean "Vai, vai, eu ajudo-te!"
    call pass_time_dialogue
    n mean "*empurra o outro aluno*"
    call pass_time_dialogue
    aluno "*foge a correr*"
    call pass_time_dialogue
    n mean "Bem me parecia..."
    jump chat_exit

# helder, isabel
label .chat_i1_g8:
    $ chats_i1[8] = -1
    call setup_dialogue("chat_i1_g8_idle")
    call pass_time_dialogue
    i happy "Só quero acabar o secundário para pedir aos meus pais para ir viajar!"
    call pass_time_dialogue
    h normal "Onde é que estás a pensar ir?"
    call pass_time_dialogue
    i normal "Não tenho nenhum país específico que queira ir, mas gostava de visitar cidades com arranhas céus. Nunca estive num prédio alto."
    call pass_time_dialogue
    h happy "Eu pessoalmente também gostaria de viajar daqui a uns anos, mas provavelmente seria para visitar sítios com serras, montanhas e paisagens. O melhor que a natureza tiver para oferecer."
    call pass_time_dialogue
    i happy "Esses sítios também parecem ser incriveís. Temos de combinar uma viagem para irmos e convidamos mais pessoas para virem também!"
    jump chat_exit

# carmen
label .chat_i1_g9:
    $ chats_i1[9] = -1
    call setup_dialogue("chat_i1_g9_idle")
    call pass_time_dialogue
    c normal "*a ouvir música*"
    jump chat_exit

# abel, jorge, rui
label .chat_i1_g10:
    $ chats_i1[10] = -1
    call setup_dialogue("chat_i1_g10_idle")
    call pass_time_dialogue
    a normal "Jorge, precisava de fala contigo acerca do torneio."
    call pass_time_dialogue
    j sad "Desculpa, agora não posso. Tou mesmo mega ocupado. Já falamos."
    call pass_time_dialogue
    j sad "*vai embora*"
    call pass_time_dialogue
    r normal "O que se passa com ele?"
    call pass_time_dialogue
    a normal "Não sei, mas ele anda a agir de forma bué estranha."
    jump chat_exit

# manuela, patricia
label .chat_i1_g11:
    $ chats_i1[11] = -1
    call setup_dialogue("chat_i1_g11_idle")
    call pass_time_dialogue
    p sad "O Nando já não pode dar mais faltas. Está sempre a ir para a rua. Já falei com ele, mas não quer saber."
    call pass_time_dialogue
    m sad "Linda, não fiques assim."
    jump chat_exit

# sinais de alerta, substituem chats 2 e 7

# jorge, nando
label .chat_i1_g12:
    $ chats_i1[2] = -1
    call setup_dialogue("chat_i1_g12_idle")
    call pass_time_dialogue
    j normal "O comentário do BossLikeMe_14 ontem às 2 da manhã era teu?"
    call pass_time_dialogue
    n normal "Ya, essa é a minha outra conta. Sabes como é mano, estou sempre ligado."
    jump chat_exit

# nando
label .chat_i1_g13:
    $ chats_i1[7] = -1
    call setup_dialogue("chat_i1_g13_idle")
    call pass_time_dialogue
    n mean "*chuta um caixote do lixo*"
    call pass_time_dialogue
    auxiliar "*aproxima-se do Nando com ar de zangada*"
    call pass_time_dialogue
    n laugh "*vira costas à auxiliar e vai-se embora*"
    jump chat_exit
