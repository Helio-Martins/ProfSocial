label session_1:

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
        player "{i}Está na hora de começar o dia de aulas.{/i}"
        $ last_room = 4
        $ current_room = 4
        $ floor = 2
        $ intervalo += 1
        $ tasks_discovered[session][2] = True
        $ tasks_discovered[session][6] = True
        #chat classroom
        $ drag_game = True
        $ situation = 20
        scene periodo_aula with Fade(0.5, 1.0, 0.5)
        play sound "audio/class2.wav"
        scene periodo_aula
        $ renpy.pause(3)
        scene black_screen with Fade(0.5, 1.0, 0.5)
        call setup_dialogue_class("chat_i0_cr")
        "*No final da aula*"
        i sad "Malta, já sabem o que aconteceu à Tatiana?"
        e normal "O quê? Não sei de nada."
        i angry "Andam a partilhar uma foto dela em biquíni a dizer que ela é feia e gorda."
        s normal "Eu até acho que ela está bem gira. "
        i angry "Isto é bué grave! Ela tem estado fechada na casa de banho."
        c angry "Ela é que leva tudo a sério! Foi só no gozo."
        e angry "Dizes isso porque não é contigo! "
        s angry "Temos de fazer alguma coisa para a ajudar."
        h angry "Epá não sei se me vou meter nesse filme. Ainda sobra para nós!"
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
        $ situation = 29
        call set_scene(current_room, True)
        "*Antes da aula começar*"
        colega "Olá [player_name_dim]. Um aluno enviou-me isto. A Cármen é tua aluna, não é?"
        call screen post1
        #chat classroom
        jogo "algo deu errado; periodo_aula: intervalo = 1"
    if intervalo == 1.5:
        $ intervalo = 2
        $ st_actions[1] += "Aula 2\n"
        scene periodo_aula with Fade(0.5, 1.0, 0.5)
        play sound "audio/class3.wav"
        scene periodo_aula
        $ renpy.pause(3)
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
        player "{i}Vou rever o feedback em relação às minhas escolhas durante o dia de hoje que obtive da equipa Te@ch4SocialGood. Será que as minhas opções colocaram a escola mais perto de obter o certificado de Escola Pró-Social?{/i}"
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
        $ intervalo = 3
        jump session_1.ending

label .intervalo_0:
    $ interj_prof = True
    $ st_actions[0] += "Intervalo 1\n"
    $ interj_aluno = True
    $ taskNew = True
    $ chats_in_rooms = [99, 99, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    $ active_rooms = [2, 3, 5, 7, 8]
    $ intervalo = 0
    $ chats_i0 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    $ chats_i0_rotation = 4
    $ hours = 9
    $ minutes = 45
    $ seconds = 0
    $ fakeminutes = 45
    $ last_room = 8
    $ current_room = 8
    $ floor = 1
    "*aproxima-se uma pessoa*"
    colega "Bom dia! Não sei se estás a par, mas este ano letivo a Comissão Europeia e as Nações Unidas lançaram um desafio às escolas."
    colega "Vamos usar o gabinete de trabalho para a equipa Te@ch4SocialGood conversar sobre este projeto e obter feedback sobre as opções tomadas na escola. Tens aqui o folheto sobre o projeto."
    call screen post0
    jump leave_conversation
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
    $ chats_i1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    $ chats_i1_rotation = 6
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
    $ active_rooms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 19]
    $ intervalo = 2
    $ chats_i2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    $ chats_i2_rotation = 5
    $ hours = 14
    $ minutes = 45
    $ seconds = 0
    $ fakeminutes = 45
    $ situation = 30
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
    label .start:
        if (intervalo == 0):
            $ rng_talk = False
            while not rng_talk:
                if chats_in_rooms[1] == 99:
                    $ chats_in_rooms = [99, 99, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
                else:
                    $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
                if n_chats % 2 == 0:
                    $ rng_talk = False
                    $ shuffled_rooms = active_rooms
                    $ renpy.random.shuffle(shuffled_rooms)
                    $ x = chats_i0_rotation
                    while x < 9:#len(chats_i0):
                        if chats_i0[x] != -1:
                            $ ind = shuffled_rooms[x - chats_i0_rotation]
                            $ chats_in_rooms[ind] = chats_i0[x]
                        $ x += 1
                    if chats_in_rooms[8] != 8 and chats_in_rooms[19] != 8:
                        if chats_i0[8] != 10:
                            $ rng_talk = True
                        elif chats_in_rooms[0] == 10 or chats_in_rooms[1] == 10:
                            $ rng_talk = True
                else:
                    $ rng_talk = True
                    $ shuffled_rooms = active_rooms
                    $ renpy.random.shuffle(shuffled_rooms)
                    $ x = 0
                    while x < chats_i0_rotation:
                        if chats_i0[x] != -1:
                            $ ind = shuffled_rooms[x]
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
                    #jogo "[x] [chats_i1_rotation] [chats_in_rooms]"
            else:
                $ shuffled_rooms = active_rooms
                $ renpy.random.shuffle(shuffled_rooms)
                $ x = chats_i1_rotation
                while x < len(chats_i1):
                    if chats_i1[x] != -1:
                        $ ind = shuffled_rooms[x - chats_i1_rotation]
                        $ chats_in_rooms[ind] = chats_i1[x]
                    $ x += 1
                    #jogo "[x] [chats_i1_rotation] [chats_in_rooms]"
            $ randomize = False
        if (intervalo == 2):
            if chats_in_rooms[19] == 99:
                $ chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 99]
                return
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
    prof_pedro "Bom dia, João. Olha, hoje vi duas alunas da tua Direção a falar mal de outra aluna e achei o que disseram estranho... Há alguma coisa sobre elas que me possas dizer?"
    colega "Bom dia! Como é que eram as alunas?"
    prof_pedro "Uma tem cabelo escuro e comprido e a outra é morena e tem franja."
    colega "A de cabelo comprido é a Manuela e é uma miúda bem-disposta, mas gosta muito de coscuvelhices! A que tem franja é a Patrícia e é muito fofoqueira, mas é das minhas melhores alunas!"
    prof_pedro "Hum...ok. Pareceu-me que estavam a falar de uma foto no Com@Viver... Sabes o que se passa? Achei aqueles risinhos muito estranhos..."
    colega "Não sei de nada... Mas vou estar atento."
    player "{i}Hmm...{/i}"
    if (not tasks_discovered[session][2]):
        $ tasks_discovered[session][2] = True
        $ taskNew = True
        $ ping = True
    call toggle_UI
    jump expression "room_"+str(current_room)
label .profs_i1:
    prof_natalia "Paulo, sabes se se passa alguma coisa com a Tatiana? Ela também é tua aluna, não é?"
    prof_paulo "Não sei de nada, porquê? A Tatiana é uma miúda muito tímida, dá-se pouco..."
    prof_natalia "Ouvi alguns alunos comentarem qualquer coisa que lhe aconteceu, pelos vistos foi uma foto que alguém partilhou no Com@Viver... Tens conhecimento sobre alguma coisa em relação a isto?"
    prof_paulo "Não, não sabia de nada. Estás a contar-me em primeira mão... Mas, pensando agora melhor, por acaso já tenho presenciado a Manuela e a Patrícia de vez em quando gozarem com a Tatiana nas aulas, mas nunca me pareceu nada sério. Será que isso piorou?"
    player "{i}Vou estar atento...{/i}"
    call toggle_UI
    jump expression "room_"+str(current_room)
label .profs_i2:
    prof_natalia "Oh Paulo, apanhei agora uma conversa de miúdos a falar mal da Tatiana."
    prof_paulo "Então isso continua? Pensei que se tinham ficado pela foto no Com@Viver..."
    prof_natalia "Parece que não... Mas sabes se anteriormente se passou alguma coisa entre a Tatiana e a Patrícia?"
    prof_paulo "Parece que houve um problema qualquer entre a Patrícia e a Tatiana, qualquer coisa também no Com@Viver. Nunca percebi bem o que se passou..."
    prof_natalia "Pois, mas tinhas-me dito que a Patrícia e outras alunas gozavam com a Tatiana nas aulas, não era?"
    prof_paulo "Sim, mas pelos rumores que me chegaram, depois disso foi a Tatiana que se andou a meter com a Patrícia, mas não sei detalhes."
    prof_natalia "Ah, estou a ver...então isto tudo que o Nando fez deve estar relacionado com essa história..."
    prof_paulo "Pois, sabes que o Nando é o namorado da Patrícia, não sabes? É capaz de estar a vingar-se de qualquer coisa."
    player "{i}É importante refletir sobre este assunto...{/i}"
    call toggle_UI
    jump expression "room_"+str(current_room)
