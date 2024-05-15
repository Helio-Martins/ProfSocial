label session_3_dialogues_i1:

# manuela, patricia - sinal 1
label .chat_i1_g0:
    $ chats_i1[0] = 9
    call setup_dialogue("chat_i1_g0_idle")
    call pass_time_dialogue
    p normal "Tens dados móveis? Os meus acabaram. Preciso de net."
    call pass_time_dialogue
    m normal "Podes usar os meus. É para quê?"
    call pass_time_dialogue
    p normal "É só para ver uma cena..."
    p sad "..."
    p sad "Não, olha deixa estar, já não é preciso. Tenho de ir."
    call pass_time_dialogue
    m normal "Mas eu empresto-te o telemóvel, linda. Onde vais?"
    call pass_time_dialogue
    p sad "Deixa, depois falamos."
    m sad "Patrícia, espera! O que é que se passa? Estás estranha! Estás chateada?"
    jump chat_exit

# abel, nando
label .chat_i1_g1:
    $ chats_i1[1] = -1
    call setup_dialogue("chat_i1_g1_idle")
    call pass_time_dialogue
    a normal "Hoje à tarde bora passar na loja de jogos."
    call pass_time_dialogue
    n normal "Siga, quero ver se há promoções de algum jogo novo."
    call pass_time_dialogue
    a happy "Exatamente o que eu pensei!"
    jump chat_exit

# samuel, tatiana
label .chat_i1_g2:
    $ chats_i1[2] = -1
    call setup_dialogue("chat_i1_g2_idle")
    call pass_time_dialogue
    s sad "Vou estar na biblioteca um bocado."
    call pass_time_dialogue
    t normal "Queres que vá contigo?"
    call pass_time_dialogue
    s sad "Não, deixa estar."
    call pass_time_dialogue
    t sad "Samuel, de certeza que a mensagem não te incomoda?"
    s sad "..."
    jump chat_exit

# estrela, isabel
label .chat_i1_g3:
    $ chats_i1[3] = -1
    call setup_dialogue("chat_i1_g3_idle")
    call pass_time_dialogue
    i normal "Como está a preparação do picnic?"
    call pass_time_dialogue
    e normal "Mais ou menos, está lentamente a avançar."
    call pass_time_dialogue
    i normal "Precisas de ajuda nalguma coisa?"
    call pass_time_dialogue
    e normal "Por agora não, mas eu digo-te se precisar."
    jump chat_exit

# helder, jorge, rui
label .chat_i1_g4:
    $ chats_i1[4] = -1
    call setup_dialogue("chat_i1_g4_idle")
    call pass_time_dialogue
    h normal "Vocês estão a pensar levar o quê para o picnic?"
    call pass_time_dialogue
    r normal "Ainda não decidi."
    call pass_time_dialogue
    j normal "Estou a debater entre sandes ou pizza."
    call pass_time_dialogue
    h happy "Pizza? Leva uma cena mais saudável rapaz!"
    call pass_time_dialogue
    j laugh "*risos*"
    jump chat_exit

#####

# nando, patricia - sinal 2
label .chat_i1_g5:
    $ chats_i1[5] = 11
    call setup_dialogue("chat_i1_g5_idle")
    call pass_time_dialogue
    p angry "O stôr vai ter de me tirar a falta! Se não tirar, vou falar com o Diretor."
    call pass_time_dialogue
    n sad "Tem calma, amor. É só uma falta."
    call pass_time_dialogue
    p angry "Só estava a mandar uma mensagem. Até parece que é motivo para ir para a rua."
    call pass_time_dialogue
    n normal "O stôr até tinha uma beca de razão. Passaste a aula toda agarrada ao telemóvel."
    call pass_time_dialogue
    p angry "Quando é para te escrever mensagens, não vês problema nisso, não é?"
    n sad "Amor, tem calma. Estou só preocupado. Não quero que fiques outra vez mal por causa das cenas com a Tatiana..."
    jump chat_exit

# tatiana, estrela, isabel
label .chat_i1_g6:
    $ chats_i1[6] = -1
    call setup_dialogue("chat_i1_g6_idle")
    call pass_time_dialogue
    t angry "Aquela Patrícia às vezes tira-me do sério."
    call pass_time_dialogue
    i normal "Estás a referir-te à mensagem?"
    call pass_time_dialogue
    t angry "Obviamente."
    call pass_time_dialogue
    e sad "Pois, acho que ela foi um bocado longe desta vez."
    jump chat_exit

# carmen
label .chat_i1_g7:
    $ chats_i1[7] = -1
    call setup_dialogue("chat_i1_g7_idle")
    call pass_time_dialogue
    c normal "*a ouvir música*"
    jump chat_exit

# helder, jorge, rui
label .chat_i1_g8:
    $ chats_i1[8] = -1
    call setup_dialogue("chat_i1_g8_idle")
    call pass_time_dialogue
    r normal "Viram as notícias? Uma rua aqui ao pé da escola ficou inundada por causa das chuvas no fim de semana."
    call pass_time_dialogue
    j normal "Ah sério? Mas houve algum ferido?"
    call pass_time_dialogue
    r normal "Não, mas houveram carros a ficarem presos nas estradas. Aquilo ficou mesmo grave."
    call pass_time_dialogue
    h laugh "A mãe Natureza não brinca em serviço!"
    call pass_time_dialogue
    j laugh "*risos*"
    jump chat_exit

# sinais de alerta, substituem chats 0 e 5

# carmen, patricia - sinal 3
label .chat_i1_g9:
    $ chats_i1[0] = 10
    call setup_dialogue("chat_i1_g9_idle")
    call pass_time_dialogue
    p disgust "Espero que ela já se tenha arrependido do que me fez! Agora é que todos vão ficar a saber quem tem razão."
    call pass_time_dialogue
    t normal "*passa e olha na direção de ambas*"
    call pass_time_dialogue
    p angry "Estás a olhar? Atreve-te."
    call pass_time_dialogue
    c sad "Deixa, linda, não fiques assim por causa dela..."
    jump chat_exit

# patricia - sinal 4
label .chat_i1_g10:
    $ chats_i1[0] = -1
    call setup_dialogue("chat_i1_g10_idle")
    call pass_time_dialogue
    p normal "*a ouvir música*"
    p normal "..."
    p angry "Porque é que esta porcaria não funciona? Que nervos!"
    p angry "*atira com os auscultadores para um caixote do lixo*"
    jump chat_exit

# abel, manuela, nando, patricia - sinal 5
label .chat_i1_g11:
    $ chats_i1[5] = -1
    call setup_dialogue("chat_i1_g11_idle")
    call pass_time_dialogue
    s sad "*ao longe, o Samuel tropeça e cai*"
    call pass_time_dialogue
    n laugh "*risos*"
    call pass_time_dialogue
    p laugh "Nem andar sabe, que atrasado! Malta, alguém está a filmar isto para pôr no Com@Viver?"
    jump chat_exit
