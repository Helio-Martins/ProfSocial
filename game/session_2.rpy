label session_2:

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
        $ situation = 50
        scene periodo_aula with Fade(0.5, 1.0, 0.5)
        play sound "audio/class2.wav"
        scene periodo_aula
        $ renpy.pause(3)
        scene black_screen with Fade(0.5, 1.0, 0.5)
        call setup_dialogue_class("chat_i0_cr1")
        "*A meio da aula*"
        h normal "E esta foi a nossa apresentação do trabalho. Alguma coisa que queiram perguntar, digam."
        c normal "Eu por acaso tenho uma dúvida."
        h normal "Claro, diz."
        c disgust "No vosso grupo quem é que tomou as decisões?"
        i angry "As decisões foram sempre tomadas em conjunto! Há algum problema?"
        c angry "Era só por curiosidade. É que há determinadas pessoas que gostam de decidir o que os outros fazem. Acham que são melhores do que os outros!"
        h normal "Cármen, o que estás a dizer é injusto."
        i laugh "Se tens alguma coisa a dizer, diz na cara! Experimenta só e depois vês o que acontece a seguir."
        c angry "Isto não é contigo, não te metas! É com a tua amiguinha. Ela que responda se tem coragem."
        i angry "Atreve-te a fazer alguma coisa."
        if male:
            s normal "Stôr, não ligue. Elas já se acalmam. Estão só a brincar."
        else:
            s normal "Stôra, não ligue. Elas já se acalmam. Estão só a brincar."
        scene black_screen with Fade(0.5, 1.0, 0.5)
        #scene black_screen with Fade(0.5, 0, 0)
        #play sound "audio/bell.mp3"
        #scene black_screen with Fade(0, 1.0, 0.5)
        call setup_dialogue_class("chat_i0_cr2")
        "*Depois da aula*"
        player "Cármen, gostava de falar contigo."
        if male:
            c normal "Stôr, agora não posso. Preciso mesmo de ir à casa de banho, desculpe. Podemos falar no final da 2ª aula?"
        else:
            c normal "Stôra, agora não posso. Preciso mesmo de ir à casa de banho, desculpe. Podemos falar no final da 2ª aula?"
        player "Está bem, falamos depois."
        #chat classroom
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
        $ situation = 59
        call set_scene(current_room, True)
        "*No início da aula*"
        player "{i}A Cármen está a faltar.{/i}"
        scene periodo_aula with Fade(0.5, 1.0, 0.5)
        play sound "audio/class3.wav"
        scene periodo_aula
        $ renpy.pause(3)
        scene black_screen with Fade(0.5, 1.0, 0.5)
        call setup_dialogue_class("chat_i1_cr1")
        "*No final da aula*"
        player "O que se passa entre ti e a Cármen?"
        if male:
            i normal "Deixe estar professor, não é nada."
        else:
            i normal "Deixe estar professora, não é nada."
        player "Alguma coisa aconteceu."
        i angry "A Cármen está só chateada porque quer ir na viagem de finalistas para a Costa da Caparica e o resto prefere ir para o Algarve."
        player "De certeza que é só isso?"
        i normal "Sim. É só isso. Posso sair?"
        i normal "*sai da sala*"
        call setup_dialogue_class("chat_i1_cr2")
        if male:
            h sad "Stôr, posso falar consigo?"
        else:
            h sad "Stôra, posso falar consigo?"
        player "Claro, Hélder. O que se passa?"
        h sad "Eu não ia dizer nada, mas acho que devia saber o que aconteceu. A Cármen ameaçou a Estrela no Com@Viver. Não diga que fui eu a mostrar-lhe!"
        call screen post2
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
        jump session_2.ending

label .intervalo_0:
    $ interj_prof = True
    $ st_actions[0] += "Intervalo 1\n"
    player "{i}A primeira aula começa às 10:00, na sala A. Tenho 15 minutos até lá.{/i}"
    player "{i}Tenho tempo para adiantar algumas tarefas.{/i}"
    $ interj_aluno = True
    $ taskNew = True
    $ chats_in_rooms = [99, 99, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    $ active_rooms = [2, 3, 5, 7, 8]
    $ intervalo = 0
    $ chats_i0 = [0, 1, -1, 3, 4, 5, 6, 7, 8]
    $ chats_i0_rotation = 5
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
    $ chats_i1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    $ chats_i1_rotation = 5
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
    $ chats_i2 = [0, 1, 2, 3, 4, -1, 6, 7, 8, 9]
    $ chats_i2_rotation = 5
    $ hours = 14
    $ minutes = 45
    $ seconds = 0
    $ fakeminutes = 45
    $ situation = 60
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
    prof_pedro "Olá Luísa. Estás a ajudar na organização da viagem de finalistas, não estás? Parece que já há confusão em relação ao destino da viagem, não é?"
    prof_luisa "Sim, estou. A Estrela é a delegada de turma e tem-se empenhado muito na organização da visita, mas já sabes, há sempre miúdos que nunca estão satisfeitos com nada."
    prof_pedro "Não sei o que se passou mais...mas parece que já houve ameças físicas. Sabes de alguma coisa?"
    prof_luisa "A sério? Não sei de nada! Mas deixa lá que vou estar atenta. Não quero cá mais confusões na viagem de finalistas! Era só o que me faltava..."
    prof_pedro "Pois, acredito... Planear a viagem com tantas turmas já não deve ser fácil, então com problemas destes, nem sei que te diga... Olha, se souber mais alguma coisa digo-te."
    prof_luisa "Ok, obrigada! Tenho de ir andando para a aula."
    player "{i}Hmm...{/i}"
    if (not tasks_discovered[session][2]):
        $ tasks_discovered[session][2] = True
        $ taskNew = True
        $ ping = True
    call toggle_UI
    jump expression "room_"+str(current_room)
label .profs_i1:
    prof_luisa "A Cármen e a Isabel começaram a discutir ontem no meio da aula e a chamarem nomes uma à outra. Mandei as duas para a rua."
    colega "Então, mas o que se passou?"
    prof_luisa "Sinceramente não percebi bem... Por acaso  alguma vez presenciaste algo do género ou algum colega te disse alguma coisa?"
    prof_jaime "Sim...sim, elas desatinam uma com a outra, já se chegaram a ofender nas aulas de outros colegas, mas nunca presenciei nenhuma discussão!"
    player "{i}Vou estar atento...{/i}"
    call toggle_UI
    jump expression "room_"+str(current_room)
label .profs_i2:
    prof_luisa "Oh João, lembras-te de há bocado te ter falado da discussão na minha aula?"
    colega "Então? Aconteceu mais alguma coisa?"
    prof_luisa "Parece-me que isto está a tomar novos contornos... Já soubeste do que a Cármen fez à Estrela no Com@Viver?"
    colega "Sim, já soube... mas parece que isso tem tudo a ver com o destino da viagem. As redes sociais são muito boas, mas depois facilitam este tipo de coisas..."
    prof_luisa "Não sei o que se passa com estes miúdos..."
    colega "Estes miúdos fervem em pouca água! Vamos lá ver se ganham juízo e se deixam de ideias tolas."
    player "{i}É importante refletir sobre este assunto...{/i}"
    call toggle_UI
    jump expression "room_"+str(current_room)
