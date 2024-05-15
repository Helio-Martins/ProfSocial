label session_4_dialogues_i1:

# abel, helder - sinal 5
label .chat_i1_g0:
    $ chats_i1[0] = -1
    call setup_dialogue("chat_i1_g0_idle")
    a angry "Dá-me o telemóvel!"
    call pass_time_dialogue
    h angry "Esquece Abel. A foto já não está só comigo. Se fizeres mais alguma coisa eles enviam isso para o Nando e para a escola toda."
    call pass_time_dialogue
    a sad "Se enviares isso ao Nando, estás lixado. Diz para apagarem a foto, já!"
    jump chat_exit

# jorge, samuel - sinal 5
label .chat_i1_g1:
    $ chats_i1[1] = -1
    call setup_dialogue("chat_i1_g1_idle")
    call pass_time_dialogue
    j sad "Samuel, tens de falar com o Hélder e dizer-lhe para parar."
    call pass_time_dialogue
    s angry "Eu já tentei. Mas ele não quer saber porque está a gostar de ser o centro das atenções."
    call pass_time_dialogue
    j sad "Mas como é que ele arranjou a foto?"
    call pass_time_dialogue
    s sad "Conseguimos hackear a conta do Abel, mas nunca imaginei que o Hélder fosse fazer isto."
    jump chat_exit

# carmen, manuela, nando
label .chat_i1_g2:
    $ chats_i1[2] = -1
    call setup_dialogue("chat_i1_g2_idle")
    call pass_time_dialogue
    n sad "E então? Como é que ela está?"
    call pass_time_dialogue
    c normal "Está a repousar, dizem que agora não há muito a fazer a não ser deixá-la descansar."
    call pass_time_dialogue
    m normal "E quando é que ela pode voltar?"
    call pass_time_dialogue
    c normal "Os médicos disseram que em princípio não é nada de muito grave, para a semana deve voltar se tudo correr bem."
    call pass_time_dialogue
    n happy "Ainda bem..."
    jump chat_exit

# estrela, isabel, rui, tatiana
label .chat_i1_g3:
    $ chats_i1[3] = -1
    call setup_dialogue("chat_i1_g3_idle")
    call pass_time_dialogue
    t normal "Amanhã querem ficar a estudar na biblioteca um pouco?"
    call pass_time_dialogue
    i normal "Sim, eu preciso de estudar. Ainda não peguei em nada."
    call pass_time_dialogue
    e normal "Não te preocupes, acho que este exame não vai ser difícil."
    call pass_time_dialogue
    r happy "Se for parecido com o ano passado, vai ser mesmo fácil."
    jump chat_exit

##########

# helder, samuel - sinal 4
label .chat_i1_g4:
    $ chats_i1[4] = -1
    call setup_dialogue("chat_i1_g4_idle")
    call pass_time_dialogue
    h laugh "Olha lá este comentário do MarceloV_14: “O Abel é tão amigo do Nando que não se importa de passar tempo com a namorada dele quando ele não está.” Vou meter like."
    call pass_time_dialogue
    s angry "Hélder, isso não tem piada!"
    call pass_time_dialogue
    h laugh "Relaxa Samuel, não fui eu a escrever isto."
    jump chat_exit

# jorge, rui
label .chat_i1_g5:
    $ chats_i1[5] = -1
    call setup_dialogue("chat_i1_g5_idle")
    call pass_time_dialogue
    r normal "Preparado para o exame de matemática?"
    call pass_time_dialogue
    j normal "Nem por isso... Achas que me consegues ajudar a estudar para o exame de matemática?"
    call pass_time_dialogue
    r normal "Claro que sim, só temos de ver as horas por causa da Associação. Fala com a Estrela, acho que elas queriam ficar a estudar amanhã."
    call pass_time_dialogue
    j happy "Fixe, sem problema."
    jump chat_exit

# carmen, estrela, isabel, manuela, tatiana
label .chat_i1_g6:
    $ chats_i1[6] = -1
    call setup_dialogue("chat_i1_g6_idle")
    call pass_time_dialogue
    i sad "Como está ela?"
    call pass_time_dialogue
    c sad "Está a descansar. Os médicos disseram que ela agora precisa só de descanso."
    call pass_time_dialogue
    e sad "Não era isto que queria que acontecesse, isto foi longe demais pessoal."
    call pass_time_dialogue
    m sad "Pois..."
    call pass_time_dialogue
    t sad "..."
    jump chat_exit

# nando
label .chat_i1_g7:
    $ chats_i1[7] = -1
    call setup_dialogue("chat_i1_g7_idle")
    call pass_time_dialogue
    n annoyed "*a mexer no telemóvel*"
    jump chat_exit

# abel - sinal 4 repetido (pavilhao)
label .chat_i1_g8:
    $ chats_i1[8] = -1
    call setup_dialogue("chat_i1_g8_idle")
    call pass_time_dialogue
    auxiliar "O que é que o menino tá aí a fazer? Conhece as regras. Vou fazer queixa sua!"
    call pass_time_dialogue
    a angry "Deixe-me! Também não quero estar nesta estúpida escola. Vou bazar."
    jump chat_exit
