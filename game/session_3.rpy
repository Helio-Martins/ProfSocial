label session_3:

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
    $ purge_saves("1-1")
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
        $ situation = 80
        #scene periodo_aula with Fade(0.5, 1.0, 0.5)
        #play sound "audio/class2.wav"
        #scene periodo_aula
        #$ renpy.pause(3)
        scene black_screen with Fade(0.5, 1.0, 0.5)
        #call setup_dialogue_class("chat_i0_cr1")
        call set_scene(current_room, True)
        "*No início da aula*"
        player "Como sabem, hoje a aula vai ser na sala polivalente para prepararmos as atividades para o dia do picnic da escola. Está alguém a faltar?"
        i normal "Falta a Clara que está doente e... o Samuel?"
        player "Alguém viu o Samuel?"
        h normal "Deve estar a chegar. Passei por ele há bocado nas escadas."
        player "Bem, vou pedir à D. Celeste para avisar o Samuel onde estamos. Vamos descer para a sala polivalente."
        #chat classroom
        play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
        scene black_screen with Fade(0.2, 1, 0.2)
        $ last_room = 10
        $ current_room = 10
        $ floor = 1
        call setup_dialogue_class("chat_i0_cr2")
        "*Passado algum tempo, na sala polivalente*"
        e happy "O que é que acham de usarmos estas cores?"
        i happy "Fica top!"
        e happy "Só faltam os recortes para as bandeirolas que o Samuel ia trazer."
        h sad "Bué estranho ele não ter chegado. Ainda há bocado passei por ele lá fora."
        c laugh "*do outro lado da sala* Estrela, desta vez falta-te o cérebro do grupo!"
        e angry "Tens sempre alguma coisa a dizer, Cármen!"
        c disgust "Estou só a gozar. Relaxa."
        i angry "Estás só a gozar, ya… E a tua amiguinha também estava só a gozar com o Samuel quando lhe chamou nomes."
        e sad "Porque é que vocês não deixam o Samuel em paz?"
        c disgust "Foi só uma piada. Sabem o que é humor?"
        h angry "Lembra lá mas é a tua amiguinha o que eu lhe disse que fazia! Ninguém se mete com os meus manos, estou a avisar..."
        c laugh "Ai, és tão bom a contar anedotas, Hélder! *risos* O melhor é não se meterem neste filme, não é com vocês."
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
        $ situation = 89
        call set_scene(current_room, True)
        aluna "O quê? A Patrícia disse isso ao Samuel?"
        player "O que é que a Patrícia disse ao Samuel? Posso saber?"
        if male:
            aluno "Nada stôr!"
        else:
            aluno "Nada stôra!"
        if male:
            aluna "Acho que devíamos mostrar ao stôr!"
        else:
            aluna "Acho que devíamos mostrar à stôra!"
        call screen post3
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
        jump session_3.ending

label .intervalo_0:
    $ interj_prof = True
    $ st_actions[0] += "Intervalo 1\n"
    $ interj_aluno = True
    $ taskNew = True
    $ chats_in_rooms = [99, 99, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    $ active_rooms = [2, 3, 5, 7, 9, 11, 12]
    $ intervalo = 0
    $ chats_i0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    $ chats_i0_rotation = 5
    $ hours = 9
    $ minutes = 45
    $ seconds = 0
    $ fakeminutes = 45
    $ last_room = 8
    $ current_room = 8
    $ floor = 1
    jump leave_conversation
label .intervalo_1:
    $ st_actions[1] += "Intervalo 2\n"
    scene black_screen with Fade(0.5, 1.0, 0.5)
    call set_scene(current_room, True)
    player "{i}Vou ter uma aula agora na sala B às 12:00. Tenho 15 minutos.{/i}"
    player "{i}Posso avançar com algumas das tarefas.{/i}"
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
    jump room_10
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
    $ chats_i2 = [0, -1, 2, 3, 4, 5, 6, 7, 8, -1, 10]
    $ chats_i2_rotation = 5
    $ hours = 14
    $ minutes = 45
    $ seconds = 0
    $ fakeminutes = 45
    $ situation = 90
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
        if chats_in_rooms[1] == 99:
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
    prof_pedro "Olá, bom dia. Natália, por acaso sabes se aconteceu alguma coisa no Com@Viver?"
    prof_natalia "Não faço ideia, não ouvi falar de nada..."
    prof_pedro "Ouvi dois alunos, acho que eram o Rui e o Jorge, a falarem de cyberbullying, e que isso podia acontecer a qualquer um... Achei estranho."
    prof_natalia "Então é mesmo capaz de ter acontecido alguma coisa para o Rui e o Jorge estarem a falar disso. Sabes que o Rui é voluntário na Associação de Apoio à Vítima?"
    prof_pedro "Então e do Jorge sabes alguma coisa?"
    prof_natalia "O Jorge anda sempre com o seu grupinho, o Rui, o Abel e o Samuel, mas costumam ser um grupo pacato."
    prof_pedro "Parece que andaram a insultar alguém mas não percebi quem. Reparei que o Hélder anda irritado, não sei o que se passa com o miúdo."
    prof_maria "Desculpem meter-me na conversa. Conheço bem o Hélder por causa do trabalho dele na Secção de Solidariedade da AE. É um miúdo impecável, mas também se irrita um bocado quando falam mal de alguém! Alguém deve ter feito mal a algum amigo para ele estar assim..."
    player "{i}Hmm...{/i}"
    if (not tasks_discovered[session][2]):
        $ tasks_discovered[session][2] = True
        $ taskNew = True
        $ ping = True
    call toggle_UI
    jump expression "room_"+str(current_room)
label .profs_i1:
    prof_pedro "Oh Natália e Maria, já percebi o que se passa...Andam a ofender o Samuel. Bem tu dizias que o Hélder se irritava com essas coisas. Ainda para mais parece que o Samuel estava na escola e não foi à aula. Que situação."
    prof_natalia "É uma pena, o Samuel é tão inteligente, mas estão sempre a chateá-lo por gostar de estudar sozinho na biblioteca."
    prof_maria "É impressionante, para estes miúdos tudo serve de desculpa para implicar..."
    player "{i}Vou estar atento...{/i}"
    call toggle_UI
    jump expression "room_"+str(current_room)
label .profs_i2:
    prof_paulo "Como é que ficou aquela situação entre o Nando e a Tatiana?"
    colega "Ah pois... isso já tinha história para trás... Afinal os rumores confirmaram-se. A Tatiana vingou-se mesmo da Patrícia. Parece que criou um perfil falso a gozar com ela... Pelo que percebemos, foi isso que motivou a publicação do Nando."
    prof_paulo "Então isto já tem ramificações. O Samuel foi metido ao barulho por causa da Tatiana, acho que tem uma paixoneta por ela, e pelo que me pareceu não vai deixar isto passar em branco."
    colega "Parece que tem uma paixoneta sim...coitado, e por isso está a apanhar por tabela."
    player "{i}É importante refletir sobre este assunto...{/i}"
    call toggle_UI
    jump expression "room_"+str(current_room)
