default s0_state = 0

label session_0:

label .ending:
    $ temp_minutes2, temp_seconds2 = divmod(int(renpy.get_game_runtime()), 60) # To record the current gameplay time.
    $ GAME_MINUTES = temp_minutes2 - GAME_MINUTES # To figure out how many minutes the search took.
    if temp_seconds2 >= GAME_SECONDS:
        $ GAME_SECONDS = temp_seconds2 - GAME_SECONDS # To figure out how many seconds the search took.
    else:
        $ GAME_SECONDS = GAME_SECONDS - temp_seconds2 # To figure out how many seconds the search took.
    call platform
    call screen ending
    return

label .periodo_aula:
    if intervalo == 0:
        $ s0_state = 5
        call toggle_UI
        scene black_screen with Fade(0.5, 0, 0)
        play sound "audio/bell.mp3" volume 0.2
        scene black_screen with Fade(0, 1.0, 0.5)
        if tasks_state[0][1] == 1:
            player "{i}It's already 10am. It's time to start class.{/i}"
            #TRANSLATEplayer "{i}Já são 10h. Está na hora de começar a aula.{/i}"
        else:
            player "{i}It's already 10am. I don't have time to do anything else. I'll go to the classroom.{/i}"
            #TRANSLATEplayer "{i}Já são 10h. Não tenho tempo para fazer mais nada. Vou para a sala de aula.{/i}"
        call set_scene(4, True)

        "*At the beginning of the class, during the attendance call*"
        player "I will make the call according to your numbers."
        player "Hélder Almeida!"
        h normal "Present."
        player "Isabel Torres!"
        i normal "Present!"
        player "Jorge Amaral!"
        j normal "Here."
        player "Cármen Semedo!"
        c normal "Present."
        player "Samuel Andrade!"
        s normal "Yes!"
        player "Estrela Nunes!"
        player "..."
        player "Is Estrela not here?"
        player "..."
        player "Well, it seems not."
        player "{i}Estrela is not here. I will write this down in my notes.{/i}"
        #TRANSLATE"*No início da aula, durante a chamada de presenças*"
        #TRANSLATEplayer "Vou fazer a chamada de acordo com os vossos números."
        #TRANSLATEplayer "Hélder Almeida!"
        #TRANSLATEh normal "Presente."
        #TRANSLATEplayer "Isabel Torres!"
        #TRANSLATEi normal "Presente!"
        #TRANSLATEplayer "Jorge Amaral!"
        #TRANSLATEj normal "Aqui."
        #TRANSLATEplayer "Cármen Semedo!"
        #TRANSLATEc normal "Presente."
        #TRANSLATEplayer "Samuel Andrade!"
        #TRANSLATEs normal "Sim!"
        #TRANSLATEplayer "Estrela Nunes!"
        #TRANSLATEplayer "..."
        #TRANSLATEplayer "A Estrela não está?"
        #TRANSLATEplayer "..."
        #TRANSLATEplayer "Bem, parece que não."
        #TRANSLATEplayer "{i}A Estrela não está cá. Vou apontar isso nas minhas notas."
        
        show screen menulist
        show screen menulist_UI
        $ studentNew = True
        player "{i}I can consult the information I have about my Class Direction through the list of students.{/i}"
        #TRANSLATEplayer "{i}Posso consultar as informações que tenho sobre a minha Direção de Turma através da lista dos alunos.{/i}"
        call toggle_UI
        call toggle_UI
        $ last_room = 4
        $ current_room = 4
        $ floor = 2
        $ intervalo += 1
        scene periodo_aula with Fade(0.5, 1.0, 0.5)
        play sound "audio/class2.wav"
        scene periodo_aula
        $ renpy.pause(3)
        scene black_screen with Fade(0.5, 1.0, 0.5)
        call set_scene(current_room, True)
        "*After class*"
        #TRANSLATE"*Após a aula*"
        show image "chats/session_0/chat_s0_a.png":
            zoom 2
            xalign 0.5
            yalign 0.2

        i normal "Professor, do you have a second?"
        player "Yes, of course. You are Isabel, correct?"
        i normal "Yes, yes. I just wanted to tell you that Estrela is in the courtyard. I just saw her through the window."
        player "With luck I'll still catch her, to give her a class summary form. Thank you very much, Isabel."
        i happy "Your welcome, professor."
        #TRANSLATEif male:
        #TRANSLATE    i normal "Professor, tem um segundo?"
        #TRANSLATE    player "Sim, com certeza. És a Isabel, correto?"
        #TRANSLATE    i normal "Sim, sim. Queria só dizer ao professor que a Estrela está no pátio. Acabei de vê-la pela janela."
        #TRANSLATE    player "Com sorte ainda a apanho, para lhe entregar um formulário de resumo da aula. Muito obrigado Isabel."
        #TRANSLATE    i happy "De nada, professor."
        #TRANSLATEelse:
        #TRANSLATE    i normal "Professora, tem um segundo?"
        #TRANSLATE    player "Sim, com certeza. És a Isabel, correto?"
        #TRANSLATE    i normal "Sim, sim. Queria só dizer à professora que a Estrela está no pátio. Acabei de vê-la pela janela."
        #TRANSLATE    player "Com sorte ainda a apanho, para lhe entregar um formulário de resumo da aula. Muito obrigada, Isabel."
        #TRANSLATE    i happy "De nada, professora."

        $ tasks_state[0][1] = 1
        $ taskNew = True
        $ tasks_discovered[0][2] = True
        call reset_intervalo
        return

image clock_highlight:
    animation
    im.Scale("tasks/clock/clock"+str(hours)+"_"+str(fakeminutes)+".png", 150, 150)
    xalign 0.995
    yalign 0.01
    easeout 0.5 zoom 1.2
    easeout 0.5 zoom 1.0
    repeat

image menu_new_highlight = Animation(im.Scale("menus/menulist_idle_new.png", 100, 100), .5, im.Scale("menus/menulist_idle.png", 100, 100), .5)
image task_new_highlight = Animation(im.Scale("menus/tasklist_idle_new.png", 100, 100), .5, im.Scale("menus/tasklist_idle.png", 100, 100), .5)
image map_new_highlight = Animation(im.Scale("menus/maplist_idle_new.png", 100, 100), .5, im.Scale("menus/maplist_idle.png", 100, 100), .5)
image student_new_highlight = Animation(im.Scale("menus/studentlist_idle_new.png", 100, 100), .5, im.Scale("menus/studentlist_idle.png", 100, 100), .5)
image feedback_new_highlight = Animation(im.Scale("menus/feedback_idle_new.png", 100, 100), .5, im.Scale("menus/feedback_idle.png", 100, 100), .5)

image task_highlight:
    animation
    im.Scale("menus/tasklist_hover.png", 100, 100)
    xalign 5*0.001080
    yalign (5+55)*0.001920
    easeout 0.5 zoom 1.2
    easeout 0.5 zoom 1.0
    repeat
image map_highlight:
    animation
    im.Scale("menus/maplist_hover.png", 100, 100)
    xalign 5*0.001080
    yalign (5+55*2)*0.001920
    easeout 0.5 zoom 1.2
    easein 0.5 zoom 1.0
    repeat
image student_highlight:
    animation
    im.Scale("menus/studentlist_hover.png", 100, 100)
    xalign 5*0.001080
    yalign (5+55*3)*0.001920
    easeout 0.5 zoom 1.2
    easein 0.5 zoom 1.0
    repeat
image feedback_highlight:
    animation
    im.Scale("menus/feedback_hover.png", 100, 100)
    xalign 5*0.001080
    yalign (5+55*4)*0.001920
    easeout 0.5 zoom 1.2
    easein 0.5 zoom 1.0
    repeat
image patio_porta_highlight:
    im.Scale("rooms/dia/entrada_8_saidas_hover.png", 1920, 1080)
    pause 0.5
    im.Scale("rooms/dia/entrada_8_saidas_idle.png", 1920, 1080)
    pause 0.5
    repeat
image escritorio_porta_highlight:
    im.Scale("escadas_13_saida_escritorio_14_hover.png", 1920, 1080)
    pause 0.5
    im.Scale("escadas_13_saida_escritorio_14_idle.png", 1920, 1080)
    pause 0.5
    repeat
image exit_dialogo_highlight:
    animation
    im.Scale("arrow_hover.png", 100, 100)
    rot(90)
    xalign 0.01
    yalign 0.005
    easeout 0.5 zoom 1.2
    easein 0.5 zoom 1.0
    repeat

label .chat_11:
    $ s0_state += 0.1
    show screen clock_UI
    call toggle_UI
    show image "chats/session_0/chat_s0_11_idle.png":
        zoom 2
        xalign 0.5
        yalign 0.2
    if minutes < 55:
        $ minutes = 55

    j normal "Excited to start classes?"
    s normal "Ever. Who doesn't love spending their days studying?"
    j laugh "Hahaha, let's see if it's like that this year."
    s normal "Have you joined Com@Viver?"
    j normal "No. What's that?"
    s normal "It is a social network run by AE where students can exchange ideas, post photos, make comments, likes..."
    j normal "And can teachers use Com@Viver? Or is it just for students?"
    s happy "It's just for us!"
    j laugh "Ah, nice!"
    player "{i}If I'm not mistaken, these two boys will be from my Class.{/i}"
    #TRANSLATEj normal "Ansioso para começar as aulas?"
    #TRANSLATEs normal "Sempre. Quem é que não adora passar os dias a estudar?"
    #TRANSLATEj laugh "Hahaha, vamos ver se é assim este ano."
    #TRANSLATEs normal "Já entraste no Com@Viver?"
    #TRANSLATEj normal "Não. O que é isso?"
    #TRANSLATEs normal "É uma rede social dirigida pela AE onde os alunos podem trocar ideias, pôr fotos, fazer comentários, likes..."
    #TRANSLATEj normal "E os professores podem usar o Com@Viver? Ou é só para alunos?"
    #TRANSLATEs happy "É só para nós!"
    #TRANSLATEj laugh "Ah, boa!"
    #TRANSLATEplayer "{i}Se não me engano, estes dois rapazes vão ser da minha Direção de Turma.{/i}"

    #$ show_menulist_UI = True
    #call toggle_UI
    #show student_highlight
    #player "{i}Por agora não tenho nada apontado, mas no futuro poderei consultar as informações que tenho sobre os meus alunos.{/i}"
    #hide student_highlight
    #call toggle_UI

    player "{i}I can listen to conversations between people by clicking to interact with them. I can also consult the dialogues I have witnessed by clicking on the \"History\" button.{/i}"
    player "{i}I could continue listening to their conversation, but it must be almost time for class. I can leave a conversation by clicking the red cross.{/i}"
    call screen chat_exit
    label loop_chat11:
        player "{i}I could continue listening to their conversation, but it must be almost time for class. I can leave a conversation by clicking the red cross.{/i}"
        jump loop_chat11
    #TRANSLATEplayer "{i}Posso escutar conversas entre pessoas ao clicar para interagir com elas. Também posso consultar os diálogos que presenciei ao clicar no botão \"Histórico\".{/i}"
    #TRANSLATEplayer "{i}Podia continuar a ouvir a conversa deles, mas já deve estar quase na altura da aula. Posso sair de uma conversa clicando na cruz vermelha.{/i}"
    #TRANSLATEcall screen chat_exit
    #TRANSLATElabel loop_chat11:
    #TRANSLATE    player "{i}Podia continuar a ouvir a conversa deles, mas já deve estar quase na altura da aula. Posso sair de uma conversa clicando na cruz vermelha.{/i}"
    #TRANSLATE    jump loop_chat11
label .chat_12:
    show screen chat_exit
    $ s0_state += 0.2
    show screen clock_UI
    call toggle_UI
    show image "chats/session_0/chat_s0_12_idle.png":
        zoom 2
        xalign 0.5
        yalign 0.2
        
    i normal "So, is everything OK with you?"
    h normal "Yes, and you? How were the holidays?"
    i happy "They were good. Too short!"
    h laugh "They always are!"
    #TRANSLATEi normal "Então, tudo bem contigo?"
    #TRANSLATEh normal "Sim. E contigo? Como foram as férias?"
    #TRANSLATEi happy "Foram boas. Foram demasiado curtas!"
    #TRANSLATEh laugh "São sempre!"

    #$ show_menulist_UI = True
    #call toggle_UI
    #show student_highlight
    #player "{i}Por agora não tenho nada apontado, mas no futuro poderei consultar as informações que tenho sobre os meus alunos.{/i}"
    #hide student_highlight
    #call toggle_UI
    jump chat_exit
label .chat_2:
    call toggle_UI
    show image "chats/session_0/chat_s0_2_idle.png":
        zoom 2
        xalign 0.5
        yalign 0.2
    $ minutes += 2

    player "Hello again, have any of you happened to see your colleague Estrela?"
    j normal "Yes, she came through the door on the left a while ago. Was it what, 1 or 2 minutes ago?"
    s normal "Around that, yes."
    player "Ok, thank you."
    j happy "You're welcome, professor."
    #TRANSLATEplayer "Olá novamente, por acaso algum de vocês viu a vossa colega Estrela?"
    #TRANSLATEj normal "Sim, ela entrou pela porta da esquerda há um bocado. Foi há quê, 1 ou 2 minutos?"
    #TRANSLATEs normal "À volta disso, sim."
    #TRANSLATEif male:
    #TRANSLATE    player "Ok, obrigado."
    #TRANSLATE    j happy "De nada, stôr."
    #TRANSLATEelse:
    #TRANSLATE    player "Ok, obrigada."
    #TRANSLATE    j happy "De nada, stôra."

    $ s0_state += 1
    jump leave_conversation
label .chat_3:
    call toggle_UI
    show image "chats/session_0/chat_s0_3_idle.png":
        zoom 2
        xalign 0.5
        yalign 0.2
    $ minutes += 2

    c normal "*listening to music*"
    player "Hello, sorry to interrupt, you're Cármen, aren't you?"
    c normal "Yes. Is something wrong, professor?"
    player "No, I just wanted to know if you saw your colleague Estrela passing by."
    c normal "I think she just entered the library."
    player "Thank you very much, have a good rest of the day."
    #TRANSLATEc normal "*a ouvir música*"
    #TRANSLATEplayer "Olá, desculpa interromper, és a Cármen, não é?"
    #TRANSLATEif male:
    #TRANSLATE    c normal "Sim. Passa-se algo, professor?"
    #TRANSLATE    player "Não, queria só saber se viste a tua colega Estrela a passar por aqui."
    #TRANSLATE    c normal "Acho que ela acabou de entrar na biblioteca."
    #TRANSLATE    player "Muito obrigado, tem um resto de um bom dia."
    #TRANSLATEelse:
    #TRANSLATE    c normal "Sim. Passa-se algo professora?"
    #TRANSLATE    player "Não, queria só saber se viste a tua colega Estrela a passar por aqui."
    #TRANSLATE    c normal "Acho que ela acabou de entrar na biblioteca."
    #TRANSLATE    player "Muito obrigada, tem um resto de um bom dia."
    #TRANSLATEc happy "Igualmente."

    $ s0_state += 2
    jump leave_conversation
label .chat_4:
    call toggle_UI
    show image "chats/session_0/chat_s0_4_idle.png":
        zoom 2
        xalign 0.5
        yalign 0.2
    $ minutes += 2

    player "Good morning, are you Estrela Nunes?"
    e normal "Yes, I am."
    player "I'm the Class A teacher, and I noticed you didn't come to class."
    e sad "I'm really sorry, professor, but there was a problem with my student card, and I was called to deal with it. I just need to make a few more copies of the documents."
    player "OK no problem. I have a form here that summarizes the lesson plan. Read it carefully and talk to me in the next class if you have any questions."
    e happy "Thank you very much, teacher."
    player "You're welcome."  
    #TRANSLATEplayer "Bom dia, és a Estrela Nunes?"
    #TRANSLATEe normal "Sim, sou."
    #TRANSLATEif male:
    #TRANSLATE    player "Eu sou o professor da Turma A, e reparei que não vieste à aula."
    #TRANSLATE    e sad "Peço imensa desculpa professor, mas houve um problema com o meu cartão de aluna, e fui chamada para tratar desse assunto. Só preciso de tirar mais umas cópias dos documentos."
    #TRANSLATE    player "Tudo bem, sem problemas. Eu tenho aqui um formulário que resume o plano das aulas. Lê-o com atenção e fala comigo na próxima aula, se tiveres alguma dúvida."
    #TRANSLATE    e happy "Muito obrigada professor."
    #TRANSLATEelse:
    #TRANSLATE    player "Eu sou a professora da Turma A, e reparei que não vieste à aula."
    #TRANSLATE    e sad "Peço imensa desculpa professora, mas houve um problema com o meu cartão de aluna, e fui chamada para tratar desse assunto. Só preciso de tirar mais umas cópias dos documentos."
    #TRANSLATE    player "Tudo bem, sem problemas. Eu tenho aqui um formulário que resume o plano das aulas. Lê-o com atenção e fala comigo na próxima aula, se tiveres alguma dúvida."
    #TRANSLATE    e happy "Muito obrigada professora."
    #TRANSLATEplayer "Não tens de quê."

    $ s0_state = 9
    jump leave_conversation
label .board:
    scene black_screen with Fade(0.5, 1.0, 0.5)
    call set_scene(14, True)
    player "Está na hora de ir para casa e refletir sobre o primeiro dia."
    $ current_room = 14
    $ feedbackNew = True
    jump setup_dragndrop0

label .intervalo_0:
    $ GAME_MINUTES, GAME_SECONDS = divmod(int(renpy.get_game_runtime()), 60)

    $ randomize = False
    $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    $ intervalo = 0
    $ hours = 9
    $ minutes = 30
    $ seconds = 0
    $ fakeminutes = 30
    $ last_room = 8
    $ current_room = 8
    $ floor = 1
    $ taskNew = True
    $ interj_aluno = True
    player "{i}Today is my first day at this school. I was assigned to be the Class Director of class A, a 7th grade class.{/i}"
    #TRANSLATE if male:
        # player "{i}Hoje é o meu primeiro dia nesta escola. Fui designado para ser o DT da turma A do 7ºano.{/i}"
    #TRANSLATE else:
        # player "{i}Hoje é o meu primeiro dia nesta escola. Fui designada para ser a DT da turma A do 7ºano.{/i}"



    #show image im.Scale("menus/menulist_idle.png", 100, 100):
    #    xalign 5*0.001080
    #    yalign 5*0.001920
    #show image im.Scale("menus/tasklist_idle.png", 100, 100):
    #    xalign 5*0.001080
    #    yalign (5+55)*0.001920
    #show image im.Scale("menus/maplist_idle.png", 100, 100):
    #    xalign 5*0.001080
    #    yalign (5+55*2)*0.001920
    show clock_highlight
    player "{i}I have a class at 10:00, in room A. I can check the clock to see how much time I have until I have to go to class. I have 30 minutes left.{/i}"
    #TRANSLATEplayer "{i}Tenho uma aula às 10:00 com a minha Direção de Turma, na sala A. Posso consultar o relógio para saber quanto tempo tenho até ter de ir para a aula. Neste momento, faltam 30 minutos.{/i}"
    hide clock_highlight
    show image im.Scale("tasks/clock/clock"+str(hours)+"_"+str(fakeminutes)+".png", 150, 150):
        xalign 0.995
        yalign 0.01
    show screen menulist
    show screen menulist_UI
    player "{i}I should stop by the teacher room to finish notes for the class I'm going to teach. I can check my to-do list so I don't forget what I have to do.{/i}"
    player "{i}The tasks I have to do are marked in white. My scheduled classes appear in yellow.{/i}"
    #TRANSLATEplayer "{i}Devia passar pela sala de professores para terminar os apontamentos da aula que vou dar. Posso consultar a minha lista de tarefas para não me esquecer do que tenho a fazer.{/i}"
    #TRANSLATEplayer "{i}As tarefas que tenho para fazer aparecem marcadas a branco. O horário das minhas aulas aparecem a amarelo.{/i}"
    $ mapNew = True
    player "{i}I don't know where the teacher room is, I should check the map. I can click on the floor number to switch between different floors of the school.{/i}"
    #TRANSLATEplayer "{i}Não sei onde fica a sala de professores, devia consultar o mapa. Posso clicar no número dos pisos para alternar entre os diferentes andares da escola.{/i}"
    show patio_porta_highlight
    player "{i}To enter the school, I can go through any of the entrances.{/i}"
    #TRANSLATEplayer "{i}Para entrar na escola, posso passar por qualquer uma das entradas.{/i}"
    hide patio_porta_highlight
    call toggle_UI
    call toggle_UI
    $ s0_state = 1
    jump leave_conversation

default point_coords = 0
screen point_arrow:
    add Animation(im.Scale("images/arrow_hover.png", 100, 100), .5, im.Scale("images/arrow_idle.png", 100, 100), .5):
        xysize(100, 100)
        xalign 0.06
        ypos point_coords
        at rot(90)

label .intervalo_1:
    scene black_screen with Fade(0.5, 1.0, 0.5)
    call set_scene(current_room, True)
    player "{i}I don't have any more classes for today. I should go look for Estrela to give her the form.{/i}"
    #TRANSLATEplayer "{i}Por hoje não tenho mais aulas. Devia ir procurar a Estrela para lhe entregar o formulário.{/i}"
    show screen menulist
    show screen menulist_UI
    player "{i}Tasks that involve investigation appear blue in the task list. I only consider the task complete after writing down my conclusions and thoughts in my notebook in the staff room.{/i}"
    player "{i}These tasks are very important and should be done as soon as possible, as they can affect the well-being of the school community and the school environment.{/i}"
    #TRANSLATEplayer "{i}Tarefas que envolvem investigação aparecem com uma cor azul na lista de tarefas. Só considero a tarefa completa depois de anotar as minhas conclusões e pensamentos no meu bloco de notas, na sala de professores.{/i}"
    #TRANSLATEplayer "{i}Estas tarefas são muito importantes e devem ser feitas assim que possível, pois podem afetar o bem-estar da comunidade escolar e o ambiente da escola.{/i}"
    call toggle_UI
    call toggle_UI
    $ intervalo = 1
    $ hours = 11
    $ minutes = 45
    $ seconds = 0
    $ fakeminutes = 45
    call toggle_UI
    jump room_4

label .randomizer:
    $ randomize = False
    return

label .joao:
    call toggle_UI

    colega "Good morning [player_name_dim]! So, how are you getting used to school?"
    player "Good morning João. It's going well, the school looks bigger from the outside."
    colega "Yes, it's a small school. We have around 250 students and most people know each other, including students, teachers and guardians. There is a platform for teachers to plan and manage daily activities. I'll help you with that later."
    colega "As I recall, today is your first class. You became CD of class A, didn't you?"
    player "Yes and you?"
    colega "This year I became DT of class B. If you need anything, you can come and talk to me in the office. And don't worry, you'll adapt well!"
    player "Thank you, I'll take that into account. See you later."
    colega "See you later."
    colega "*goes towards the office*"
    player "{i}João is a good colleague and friend; We've known each other for a few years now. He is the school coordinator, and is a teacher with more experience. If I need to know information about his class, I can visit him in his office.{/i}"
    #TRANSLATEcolega "Bom dia [player_name_dim]! Então, como te estás a ambientar à escola?"
    #TRANSLATEplayer "Bom dia João. Está a correr bem, a escola parece maior vista de fora."
    #TRANSLATEcolega "Sim, é uma escola pequena. Nós temos cerca de 250 alunos e a maior parte das pessoas conhece-se, incluindo alunos, professores e encarregados de educação. Existe uma plataforma para os professores planificarem e gerirem as atividades diárias. Depois ajudo-te com isso."
    #TRANSLATEif male:
    #TRANSLATE    colega "Pelo que me lembro, hoje é a tua primeira aula. Tu ficaste DT da turma A, não foi?"
    #TRANSLATEelse:
    #TRANSLATE    colega "Pelo que me lembro, hoje é a tua primeira aula. Tu ficaste DT da turma A, não foi?"
    #TRANSLATEplayer "Sim, e tu?"
    #TRANSLATEcolega "Este ano fiquei DT da turma B. Se precisares de alguma coisa, podes vir falar comigo ao gabinete. E não te preocupes, vais-te adaptar bem!"
    #TRANSLATEif male:
    #TRANSLATE    player "Obrigado, vou ter isso em conta. Vemo-nos mais tarde."
    #TRANSLATEelse:
    #TRANSLATE    player "Obrigada, vou ter isso em conta. Vemo-nos mais tarde."
    #TRANSLATEcolega "Até logo."
    #TRANSLATEcolega "*vai em direção ao gabinete*"
    #TRANSLATEplayer "{i}O João é um bom colega e amigo; já nos conhecemos há alguns anos. Ele é o coordenador da escola, e é um professor com mais experiência. Se precisar de saber informação sobre a turma dele, posso visitá-lo no gabinete.{/i}"
    
    $ s0_state = 2
    call toggle_UI
    jump room_13

label .skip_aula:
    player "{i}I can click on the blackboard to pass the waiting time until class.{/i}"
    #TRANSLATEplayer "{i}Posso clicar no quadro para passar o tempo de espera até à aula.{/i}"
    jump room_4

label .do_task:
    player "{i}To complete a task, I need to click on the corresponding object. In this case, to finish the notes, I need to interact with the book on the table.{/i}"
    #TRANSLATEplayer "{i}Para completar uma tarefa, preciso de clicar no objeto correspondente. Neste caso, para acabar os apontamentos, preciso de interagir com o livro em cima da mesa.{/i}"
    jump room_14
