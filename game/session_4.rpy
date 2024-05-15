label session_4:

label .ending:
    $ temp_minutes2, temp_seconds2 = divmod(int(renpy.get_game_runtime()), 60) # To record the current gameplay time.
    $ GAME_MINUTES = temp_minutes2 - GAME_MINUTES # To figure out how many minutes the search took.
    if temp_seconds2 >= GAME_SECONDS:
        $ GAME_SECONDS = temp_seconds2 - GAME_SECONDS # To figure out how many seconds the search took.
    else:
        $ GAME_SECONDS = GAME_SECONDS - temp_seconds2 # To figure out how many seconds the search took.
    call platform
    play sound "audio/ping.wav" volume 0.5
    $ score_final = int(score_final) + If(score_final - int(score_final) >= 0.5, 1, 0)
    if score_final < 34:
        $ final_eval = "O seu comportamento foi [score_final]% pró-social. Atenção, deve ajudar a sua escola a obter o certificado de Escola Pró-social."
        $ final_eval_color = "#a00"
    elif score_final < 67:
        $ final_eval = "O seu comportamento foi [score_final]% pró-social. Ajude a sua escola a obter o certificado de Escola Pró-social."
        $ final_eval_color = "#da0"
    else:
        if male:
            $ final_eval = "O seu comportamento foi [score_final]% pró-social. Está mais próximo de ajudar a sua escola a obter o certificado de Escola Pró-social."
        else:
            $ final_eval = "O seu comportamento foi [score_final]% pró-social. Está mais próxima de ajudar a sua escola a obter o certificado de Escola Pró-social."
        $ final_eval_color = "#0a0"
    show screen ending
    $ intervalo = 3
    call screen feedbacklist
    return

label .periodo_aula:
    $ interj_prof = True
    if intervalo == 0:
        $ st_actions[0] += "Aula 1\n"
        call toggle_UI
        scene black_screen with Fade(0.5, 0, 0)
        play sound "audio/bell.mp3"
        scene black_screen with Fade(0, 1.0, 0.5)
        player "{i}Vamos começar mais um dia de aulas.{/i}"
        $ last_room = 4
        $ current_room = 4
        $ floor = 2
        $ intervalo += 1
        $ tasks_discovered[session][2] = True
        $ tasks_discovered[session][6] = True
        #chat classroom
        $ drag_game = True
        $ situation = 110
        call setup_dialogue_class("chat_i0_cr")
        "*À entrada da sala de aula*"
        s normal "Eu percebo que tens boas intenções, mas assim não se resolve nada."
        h angry "O Abel é um otário. E o que eles te fizeram antes não foi justo."
        s sad "Obrigado, a sério, mas só quero que esta história acabe. Está muita gente a ficar magoada."
        i sad "A Patrícia está no hospital e partilhar a foto do Abel só vai piorar tudo!"
        e normal "Eu recebi a foto e apaguei-a. Acho que deviam apagar também antes que chegue a mais pessoas. Não gosto deles, mas não quero fazer parte disto."
        s normal "O melhor é deixar passar uns dias. Isto acaba por se resolver."
        "*a Cármen chega de repente*"
        c angry "Se te voltas a meter com os meus amigos tás lixado!"
        scene periodo_aula with Fade(0.5, 1.0, 0.5)
        play sound "audio/class2.wav"
        scene periodo_aula
        $ renpy.pause(3)
        scene black_screen with Fade(0.5, 1.0, 0.5)
        hide screen clock_UI
        jump leave_conversation
    if intervalo == 1:
        call toggle_UI
        scene black_screen with Fade(0.5, 0, 0)
        play sound "audio/bell.mp3"
        scene black_screen with Fade(0, 1.0, 0.5)
        player "{i}Vou dar a aula agora.{/i}"
        $ last_room = 6
        $ current_room = 6
        $ floor = 2
        $ intervalo += 0.5
        #chat classroom
        $ drag_game = True
        $ situation = 119
        scene periodo_aula with Fade(0.5, 1.0, 0.5)
        play sound "audio/class3.wav"
        scene periodo_aula
        $ renpy.pause(3)
        scene black_screen with Fade(0.5, 1.0, 0.5)
        call setup_dialogue_class("chat_i1_cr")
        "*Depois da aula*"
        aluno "Viste a foto da Patrícia e do Abel?"
        aluna "Bem se fosse eu morria de vergonha..."
        player "Ora bem, quem é que me vai contar o que se passa? Qual fotografia?"
        if male:
            e normal "Professor, eu apaguei, mas andam a enviar uma foto da Patrícia e do Abel... Estou preocupada porque a Patrícia tem problemas de saúde e está no hospital."
        else:
            e normal "Professora, eu apaguei, mas andam a enviar uma foto da Patrícia e do Abel... Estou preocupada porque a Patrícia tem problemas de saúde e está no hospital."
        "*uma professora aproxima-se*"
        prof_luisa "Anda uma fotografia a circular de dois alunos que está a dar muito que falar... O Hélder não é teu aluno? Pelos vistos foi ele que partilhou a fotografia. Houve um aluno que me mostrou isto."
        call set_scene(current_room, True)
        call screen post4
        jogo "algo deu errado; periodo_aula: intervalo = 1"
        #chat classroom
    if intervalo == 1.5:
        $ intervalo = 2
        $ st_actions[1] += "Aula 2\n"
        scene black_screen with Fade(0.5, 1.0, 0.5)
        jump reset_intervalo
    if intervalo == 2:
        $ st_actions[2] += "Reunião \n"
        call toggle_UI
        scene black_screen with Fade(0.5, 0, 0)
        #play sound "audio/bell.mp3"
        scene black_screen with Fade(0, 1.0, 0.5)
        player "{i}A reunião é agora.{/i}"
        scene reuniao with Fade(0.5, 1.0, 0.5)
        play sound "audio/class4.wav"
        scene reuniao
        $ renpy.pause(3)
        scene black_screen with Fade(0.5, 1.0, 0.5)
        player "{i}A reunião durou mais de 2 horas.{/i}"
        call set_daytime
        $ hours = 17
        $ minutes = 30
        $ fakeminutes = 30
        player "{i}Está na hora de acabar o dia.{/i}"
        $ last_room = 8
        $ current_room = 8
        $ floor = 1
        if tasks_state[session][8] == 0:
            $ tasks_state[session][8] = -1
        if tasks_state[session][9] == 0:
            $ tasks_state[session][9] = -1
        if tasks_state[session][10] == 2:
            $ tasks_state[session][10] = -1
        $ tasks_state[session][11] = 1
        call set_scene(8, True)
        call toggle_UI
        $ score_final = 100.0 * pro_social / (8.0+2.0+7.0+12.0)
        $ show_menulist_UI = True
        $ show_feedbacklist_UI = True
        jump session_4.ending

label .intervalo_0:
    $ interj_prof = True
    $ st_actions[0] += "Intervalo 1\n"
    player "{i}A primeira aula começa às 10:00, na sala A. Tenho 15 minutos até lá.{/i}"
    player "{i}Tenho tempo para adiantar algumas tarefas.{/i}"
    $ interj_aluno = True
    $ taskNew = True
    $ chats_in_rooms = [99, 99, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    $ active_rooms = [2, 3, 5, 7, 9, 10]
    $ intervalo = 0
    $ chats_i0 = [0, 1, 2, 3, 4, 5, 6, 7]
    $ chats_i0_rotation = 4
    $ hours = 9
    $ minutes = 45
    $ seconds = 0
    $ fakeminutes = 45
    $ last_room = 8
    $ current_room = 8
    $ floor = 1
    call toggle_UI
    jump expression "room_" + str(current_room)
    ###jump leave_conversation
label .intervalo_1:
    $ st_actions[1] += "Intervalo 2\n"
    scene black_screen with Fade(0.5, 1.0, 0.5)
    call set_scene(current_room, True)
    player "{i}Vou ter uma aula agora na sala B às 12:00. Tenho 15 minutos.{/i}"
    player "{i}Posso avançar com algum trabalho.{/i}"
    player "{i}Sempre que queira ter feedback sobre as minhas opções, posso conversar com a equipa Te@ch4SocialGood no gabinete de trabalho.{/i}"
    $ interj_aluno = True
    $ taskNew = True
    $ ping = True
    $ active_rooms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 19]
    $ intervalo = 1
    $ chats_i1 = [0, 1, 2, 3, 4, 5, 6, 7]
    $ chats_i1_rotation = 4
    $ hours = 11
    $ minutes = 45
    $ seconds = 0
    $ fakeminutes = 45
    if tasks_state[session][0] == 0:
        $ tasks_state[session][0] = -1
    if tasks_state[session][1] == 0:
        $ tasks_state[session][1] = -1
    if tasks_state[session][2] == 2:
        $ tasks_state[session][2] = -1
    $ tasks_state[session][3] = 1
    call toggle_UI
    jump room_4
label .intervalo_2:
    $ st_actions[2] += "Intervalo 3\n"
    $ current_room = 8
    $ floor = 1
    scene black_screen with Fade(0.5, 1.0, 0.5)
    call set_scene(current_room, True)
    player "{i}Demorei uma hora a almoçar. Vou ter uma reunião agora às 15:00 na sala dos professores. Tenho 15 minutos.{/i}"
    player "{i}Ainda tenho algumas tarefas por fazer.{/i}"
    $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 99]
    $ taskNew = True
    $ ping = True
    $ active_rooms = [0, 1, 2, 3, 4, 5, 6, 7]
    $ intervalo = 2
    $ chats_i2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    $ chats_i2_rotation = 5
    $ hours = 14
    $ minutes = 45
    $ seconds = 0
    $ fakeminutes = 45
    $ situation = 120
    if tasks_state[session][4] == 0:
        $ tasks_state[session][4] = -1
    if tasks_state[session][5] == 0:
        $ tasks_state[session][5] = -1
    if tasks_state[session][6] == 2:
        $ tasks_state[session][6] = -1
    $ tasks_state[session][7] = 1
    call toggle_UI
    $ first_entry = True
    $ tasks_discovered[session][10] = True
    jump room_8

label .intervalo_3:
    player "{i}A reunião durou quase 2 horas.{/i}"
    $ active_rooms = [0, 1, 2, 3, 5, 8, 19]
    $ intervalo = 3
    $ chats_i3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    $ chats_i3_rotation = 5
    $ seconds = 0
    $ fakeminutes = 45
    jump room_18

label .randomizer:
    if (intervalo == 0):
        if chats_in_rooms[0] == 99:
            $ chats_in_rooms = [99, 99, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        else:
            $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if n_chats % 2 != 0:
            $ shuffled_rooms = active_rooms
            $ renpy.random.shuffle(shuffled_rooms)
            $ x = 0
            while x < chats_i0_rotation:
                if chats_i0[x] != -1 :
                    $ ind = shuffled_rooms[x]
                    $ chats_in_rooms[ind] = chats_i0[x]
                $ x += 1
        else:
            $ shuffled_rooms = active_rooms
            $ renpy.random.shuffle(shuffled_rooms)
            $ x = chats_i0_rotation
            while x < len(chats_i0):
                if chats_i0[x] != -1:
                    $ ind = shuffled_rooms[x - chats_i0_rotation]
                    $ chats_in_rooms[ind] = chats_i0[x]
                $ x += 1
        $ randomize = False
    if (intervalo == 1):
        $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if n_chats % 2 != 0:
            $ shuffled_rooms = active_rooms
            $ renpy.random.shuffle(shuffled_rooms)
            $ x = 0
            while x < chats_i1_rotation:
                if chats_i1[x] != -1 :
                    $ ind = shuffled_rooms[x]
                    $ chats_in_rooms[ind] = chats_i1[x]
                $ x += 1
        else:
            $ shuffled_rooms = active_rooms
            $ renpy.random.shuffle(shuffled_rooms)
            $ x = chats_i1_rotation
            while x < len(chats_i1):
                if chats_i1[x] != -1:
                    $ ind = shuffled_rooms[x - chats_i1_rotation]
                    $ chats_in_rooms[ind] = chats_i1[x]
                $ x += 1
        $ randomize = False
    if (intervalo == 2):
        if chats_in_rooms[19] == 99:
            $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 99]
        else:
            $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if n_chats % 2 != 0:
            $ shuffled_rooms = active_rooms
            $ renpy.random.shuffle(shuffled_rooms)
            $ x = 0
            while x < chats_i2_rotation:
                if chats_i2[x] != -1:
                    $ ind = shuffled_rooms[x]
                    $ chats_in_rooms[ind] = chats_i2[x]
                $ x += 1
        else:
            $ shuffled_rooms = active_rooms
            $ renpy.random.shuffle(shuffled_rooms)
            $ x = chats_i2_rotation
            while x < len(chats_i2):
                if chats_i2[x] != -1:
                    $ ind = shuffled_rooms[x - chats_i2_rotation]
                    $ chats_in_rooms[ind] = chats_i2[x]
                $ x += 1
        $ randomize = False
    if (intervalo == 3):
        jogo "algo deu errado; randomizer: intervalo = 3"
    return

label .profs_i0:
    prof_luisa "Cruzei-me com um grupo de alunos teus e as coisas estavam um bocado tensas. Primeiro percebi que a Patrícia está no hospital."
    colega "Ela realmente tem estado a faltar, mas os colegas disseram que estava com gripe..."
    prof_luisa "Pois, mas parece mais grave que isso, pelos vistos está internada."
    colega "Tenho de tirar isso a limpo."
    prof_luisa "Olha e o Nando e o Abel. Eles não são melhores amigos? O que é que se passa agora?"
    colega "Sim, eles são amigos desde que entraram na escola no 5º ano...andam sempre juntos, parecem irmãos! Não sei o que se passa entre eles, mas  deve estar relacionado com a Patrícia."
    prof_luisa "Ouvi falar qualquer coisa de uma foto no Com@Viver... Estará relacionado com a Patrícia estar internada?"
    colega "Sinceramente não sei ainda... Mas tenho de ver isso. A Patrícia não pode continuar a faltar sem ter justificação médica."
    player "{i}Hmm...{/i}"
    if (not tasks_discovered[session][2]):
        $ tasks_discovered[session][2] = True
        $ taskNew = True
        $ ping = True
    call toggle_UI
    jump expression "room_"+str(current_room)
label .profs_i1:
    prof_jaime "Parece que aquela história do Samuel continua..."
    prof_maria "Então? Houve mais confusão?"
    prof_jaime "O Hélder não suporta o Abel e está muito chateado com aquilo que fizeram ao Samuel..."
    prof_maria "Pois, eles são muito amigos mesmo, é normal que fique assim..."
    player "{i}Vou estar atento...{/i}"
    call toggle_UI
    jump expression "room_"+str(current_room)
label .profs_i2:
    colega "Oh Natália, vais agora ter aula com a turma do Nando, não vais?"
    prof_natalia "Sim, vou. Por acaso há bocado fui deixar umas coisas à sala, a turma estava quase toda lá mas não o vi. O que se passa?"
    colega "Soubeste da publicação do Hélder sobre uma foto da Patrícia?"
    prof_natalia "Sim, soube...que confusão."
    colega "Se aquilo for verdade, nem sei o que ele é capaz de fazer... Como ele e o Abel são tão amigos... O que achas do Nando?"
    prof_natalia "Pois é, nunca vi um miúdo tão defensor da sua namorada. Ele é capaz de fazer tudo para se vingar. Espero que não faça nenhuma asneira."
    player "{i}É importante refletir sobre este assunto...{/i}"
    call toggle_UI
    jump expression "room_"+str(current_room)

screen post5:
    imagebutton:
        xalign 0.01 yalign 0.01 at rot(-90)
        idle im.Scale("x_idle.png", 100, 100, bilinear=True)
        hover im.Scale("x_hover.png", 100, 100, bilinear=True)
        action Jump("post5_leave")
        focus_mask True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1360
        ysize 710
        background "#111"
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1350
        ysize 700
        background "#cdf"
        text "ESCOLA PRÓ-SOCIAL":
            xalign 0.5
            yalign 0.1
            text_align 0.5
            size 60
            bold 1
        text "No âmbito dos objetivos para a sustentabilidade 2030 da Comissão Europeia e das Nações Unidas, este certificado comprova que os profissionais educativos deste estabelecimento escolar promoveram uma vida saudável e o bem-estar na comunidade escolar, um ensino de qualidade equitativo para todos os alunos, e um ambiente escolar justo, pacífico e inclusivo.":
            xalign 0.5
            yalign 0.5
            text_align 0.5
            size 40
            xsize 1150
            justify True
        text "Acreditado pelo programa Te@ch4SocialGood":
            xalign 0.5
            yalign 0.9
            text_align 0.5
            size 30
            underline 1
            italic 1
            #color "#111"
        image "comissao.png":
            xalign 0.95
            yalign 0.95
            xsize 1200/6
            ysize 827/6
        image "nacoes.png":
            xalign 0.10
            yalign 0.95
            xsize 1205/(8)
            ysize 1024/(8)

label post5_leave:
    menu:
        "Tem a certeza que quer terminar a sessão?"

        "Sim":
            scene black_screen with Fade(1.0, 0.5, 1.0)
            $ daytime = "dia"
            jump post_session
            return
        "Não":
            call screen post5
    return
