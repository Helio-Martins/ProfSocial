label session_2_dialogues_i0:

# helder, isabel, tatiana
label .chat_i0_cb:
    $ active_rooms = [0, 1, 2, 3, 5, 7, 8, 19]
    $ drag_game = True
    $ situation = 40
    if (not tasks_discovered[session][2]):
        $ tasks_discovered[session][2] = True
        $ taskNew = True
        $ ping = True
    call setup_dialogue("chat_i0_cb_idle")
    call pass_time_dialogue
    i angry "Passou-se! Os meus pais também não me querem deixar ir para o Algarve. Não é por causa disso que vou tentar estragar a viagem de finalistas aos outros."
    call pass_time_dialogue
    h angry "O que merecia depois disto era ficar fora da viagem."
    call pass_time_dialogue
    t angry "Podes crer. E ameaçar que lhe batia e que lhe entrava em casa? Não acho normal!"
    call pass_time_dialogue
    h angry "Não suporto injustiças! O que aconteceu não tem desculpa."
    call pass_time_dialogue
    i angry "Só sei que se voltar a ameaçar que lhe bate, vai arrepender-se a sério!"
    jump chat_exit

# manuela, patricia - sinal 5
label .chat_i0_g0:
    $ chats_i0[0] = 9
    call setup_dialogue("chat_i0_g0_idle")
    call pass_time_dialogue
    p normal "Viste a Cármen?"
    call pass_time_dialogue
    m normal "Entrou agora, mas disse que se ia baldar à 2º aula e ia ao café."
    call pass_time_dialogue
    p sad "Outra vez? Mas ela sempre achou mal que o Nando se baldasse às aulas..."
    call pass_time_dialogue
    m normal "Pois, também não entendo..."
    jump chat_exit

# abel, rui
label .chat_i0_g1:
    $ chats_i0[1] = -1
    call setup_dialogue("chat_i0_g1_idle")
    call pass_time_dialogue
    a normal "Já faltam poucos dias para sair a nova temporada. Estou mesmo ansioso."
    call pass_time_dialogue
    r normal "Yeap, mal posso esperar."
    call pass_time_dialogue
    a normal "Ouvi dizer que uma certa personagem ia deixar de aparecer..."
    call pass_time_dialogue
    r angry "Hey, não digas spoilers!"
    call pass_time_dialogue
    a laugh "*risos*"
    jump chat_exit

# estrela, samuel
label .chat_i0_g3:
    $ chats_i0[3] = -1
    call setup_dialogue("chat_i0_g3_idle")
    call pass_time_dialogue
    e normal "Hoje sempre estamos combinados para trabalhar no projeto?"
    call pass_time_dialogue
    s normal "Mais ou menos, a Tatiana disse que tinha de ir buscar a irmã à escola, por isso não pode vir. Mas nós podemos adiantar progresso à mesma."
    call pass_time_dialogue
    e normal "Tudo bem, aparece na biblioteca depois das aulas."
    call pass_time_dialogue
    s normal "Ok."
    jump chat_exit

# jorge, nando
label .chat_i0_g4:
    $ chats_i0[4] = -1
    call setup_dialogue("chat_i0_g4_idle")
    call pass_time_dialogue
    j normal "Viste o jogo de ontem?"
    call pass_time_dialogue
    n happy "Ya, cheguei a pensar que távamos a jogar sozinhos. A outra equipa parecia que estava a jogar com a equipa B."
    call pass_time_dialogue
    j happy "Curtiste do ponta de lança a levar 3 foras de jogo?"
    call pass_time_dialogue
    n laugh "YA! Ele não deve ter dormido como deve ser."
    call pass_time_dialogue
    j laugh "Pois, só pode!"
    jump chat_exit

# carmen, nando, patricia - sinal 3
label .chat_i0_g5:
    $ chats_i0[5] = 10
    call setup_dialogue("chat_i0_g5_idle")
    call pass_time_dialogue
    n normal "Logo à tarde vou ao canil e precisava de uma ajuda. Alguém pode vir comigo?"
    call pass_time_dialogue
    p sad "Desculpa amor, hoje não posso! Tenho de estudar para o teste. Mas vou contigo para a semana, prometo."
    call pass_time_dialogue
    n normal "E tu, Cármen?"
    call pass_time_dialogue
    c disgust "Isso não é cena para mim. Esquece! Fico a cheirar a xixi de cão, nem pensar!"
    call pass_time_dialogue
    n sad "Era pouco tempo. Precisava mesmo de alguém hoje para me ajudar."
    call pass_time_dialogue
    c disgust "Não percebo como é que consegues gastar tantas horas a fazer esse tipo de coisas. Tenho cenas mais úteis para fazer com a minha vida!"
    jump chat_exit

# estrela, jorge
label .chat_i0_g6:
    $ chats_i0[6] = -1
    call setup_dialogue("chat_i0_g6_idle")
    call pass_time_dialogue
    j normal "Já sabes se vamos para o Algarve ou como é?"
    call pass_time_dialogue
    e angry "Honestamente Samuel, não faço ideia e neste momento não quero saber."
    call pass_time_dialogue
    j sad "Então? Que agressividade é essa?"
    call pass_time_dialogue
    e disgust "Desculpa, mas tou com um stress enorme. A Cármen anda-me a chatear a cabeça e francamente tou a ficar farta."
    call pass_time_dialogue
    j sad "Calma. Não vale a pena stressar. Isto vai a votos de qualquer das formas, até sabermos o resultado só temos de esperar."
    call pass_time_dialogue
    e disgust "E é suposto eu ignorar o que ela disse no Com@Viver?"
    call pass_time_dialogue
    j sad "Nisso tens razão, mas achas mesmo que ela faria isso? Ignora só."
    call pass_time_dialogue
    e disgust "Veremos."
    jump chat_exit

# abel, rui, samuel
label .chat_i0_g7:
    $ chats_i0[7] = -1
    call setup_dialogue("chat_i0_g7_idle")
    call pass_time_dialogue
    a happy "Ontem estávamos a jogar fixe! Quase que chegávamos a 5 vitórias seguidas."
    call pass_time_dialogue
    s happy "Sim, começo a achar que consigo ir para profissional."
    call pass_time_dialogue
    a happy "Calma mano, primeiro acaba a escola, depois pensa nos jogos."
    call pass_time_dialogue
    s happy "Óbvio, estava a gozar, mas quem sabe um dia vais me ver lá no palco a representar o país."
    call pass_time_dialogue
    r happy "Quando acordares desse sonho avisa-me!"
    jump chat_exit

# manuela
label .chat_i0_g8:
    $ chats_i0[8] = -1
    call setup_dialogue("chat_i0_g8_idle")
    call pass_time_dialogue
    m normal "*a mexer no telemóvel*"
    jump chat_exit

# sinais de alerta, substituem chats 0 e 5

# carmen, manuela, patricia - sinal 1
label .chat_i0_g9:
    $ chats_i0[0] = 11
    call setup_dialogue("chat_i0_g9_idle")
    call pass_time_dialogue
    p surprise "Ela canta super bem!"
    call pass_time_dialogue
    c normal "Eu canto muito melhor do que ela. Não percebo como é que ela tem tantos seguidores. Já viram o vídeo que publiquei?"
    call pass_time_dialogue
    m happy "Claro! Tu estás top, babe!"
    call pass_time_dialogue
    c normal "Não se esqueçam de pôr like e partilhar só o meu vídeo para ser viral. Vou concorrer ao próximo The Voice, sabiam?"
    jump chat_exit

# carmen - sinal 2
label .chat_i0_g11:
    $ chats_i0[0] = -1
    call setup_dialogue("chat_i0_g2_idle")
    call pass_time_dialogue
    c angry "*concentrada no telemóvel*"
    jump chat_exit

# carmen - sinal 4
label .chat_i0_g10:
    $ chats_i0[5] = -1
    call setup_dialogue("chat_i0_g2_idle")
    call pass_time_dialogue
    c normal "*a andar enquanto olha para o telemóvel*"
    call pass_time_dialogue
    c surprise "*tropeça nos atacadores e cai*"
    call pass_time_dialogue
    c angry "..."
    call pass_time_dialogue
    c angry "*dá um pontapé na parede e vai-se embora*"
    jump chat_exit
