default tasks_state = [
 [0, 0, 2],                                                                     #s0
 [0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0],                                          #s1
 [0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0],                                          #s2
 [0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0],                                          #s3
 [0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0]                                           #s4
]
default tasks_discovered = [
 [True, True, False],                                                           #s0
 [True, True, False, True, True, False, False, True, True, False, False, True], #s1
 [True, True, False, True, True, False, False, True, True, False, False, True], #s2
 [True, True, False, True, True, False, False, True, True, False, False, True], #s3
 [True, True, False, True, True,  True, False, True, True, False, False, True]  #s4
]
define tasks_description = [
 [                                                                              #s0
 "Finish notes before class (Teacher room)",                                    #0
 "[[10:00] Class (Classroom A)",                                                #1
 "Find out why Estrela was absent (Teacher room)",                              #2
 #TRANSLATE"Acabar os apontamentos antes da aula (Sala de professores)",                  #0
 #TRANSLATE"[[10:00] Aula (Sala de aula A)",                                              #1
 #TRANSLATE"Descobrir o porquê de a Estrela ter faltado (Sala de professores)",           #2
 ], [                                                                           #s1
 "Enviar um e-mail antes da primeira aula (Sala de professores)",               #3
 "Escrever um recado urgente na caderneta do aluno (Sala de aula A)",           #4
 "Perceber quem é o aluno da publicação (Sala de professores)",                 #5
 "[[10:00] Primeira aula (Sala de aula A)",                                     #6
 "Fazer fotocópias das fichas para a segunda aula (Biblioteca)",                #7
 "Ajudar o aluno das aulas de apoio (Sala de aula B)",                          #8
 "Perceber quem publicou a fotografia (Sala de professores)",                   #9
 "[[12:00] Segunda aula (Sala de aula B)",                                      #10
 "Preparar uma atividade antes da reunião (Sala de professores)",               #11
 "Comprar uma rifa dos alunos para apoiar o canil (Pátio)",                     #12
 "Refletir sobre a publicação do Nando (Sala de professores)",                  #13
 "[[15:00] Reunião com os professores (Sala de professores)",                   #14
 ], [                                                                           #s2
 "Preparar material para apresentar numa aula (Sala de professores)",           #15
 "Ajudar alunos a montar uma exposição de trabalhos (Sala polivalente)",        #16
 "Perceber quem é o aluno que ameaçou violência (Sala de professores)",         #17
 "[[10:00] Primeira aula (Sala de aula A)",                                     #18
 "Organizar os trabalhos de grupo dos alunos (Sala de professores)",            #19
 "Tirar uma dúvida a um aluno sobre o teste (Sala de aula B)",                  #20
 "Perceber quem é o aluno que foi ameaçado (Sala de professores)",              #21
 "[[12:00] Segunda aula (Sala de aula B)",                                      #22
 "Reunir com um colega para assinar documentos (Gabinete de trabalho)",         #23
 "Emprestar um livro a um aluno (Biblioteca)",                                  #24
 "Refletir sobre a publicação (Sala de professores)",                           #25
 "[[15:00] Reunião com os professores (Sala de professores)",                   #26
 ], [                                                                           #s3
 "Imprimir a lista de alunos e familiares para o picnic (Biblioteca)",          #27
 "Transportar material para as atividades do picnic (Pátio)",                   #28
 "Perceber quem é o aluno que foi ofendido (Sala de professores)",              #29
 "[[10:00] Primeira aula (Sala de aula A)",                                     #30
 "Entregar a lista de inscrições ao coordenador (Sala de professores)",         #31
 "Tirar uma dúvida a um aluno sobre o teste (Sala de aula B)",                  #32
 "Perceber quem foi a aluna que ofendeu o Samuel (Sala de professores)",        #33
 "[[12:00] Segunda aula (Sala de aula B)",                                      #34
 "Enviar um e-mail aos encarregados de educação (Sala de professores)",         #35
 "Entregar os materiais ao coordenador de ciclo (Sala polivalente)",            #36
 "Refletir sobre a publicação (Sala de professores)",                           #37
 "[[15:00] Reunião com os professores (Sala de professores)",                   #38
 ], [                                                                           #s4
 "Ir buscar um livro para emprestar a um aluno (Biblioteca)",                   #39
 "Tirar dúvidas sobre a matéria a um aluno (Sala de aula B)",                   #40
 "Perceber quem é o aluno que foi ameaçado (Sala de professores)",              #41
 "[[10:00] Primeira aula (Sala de aula A)",                                     #42
 "Dar ao colega a planificação dos projetos (Sala de professores)",             #43
 "Afixar os cartazes do projeto de turma (Pátio)",                              #44
 "Perceber quem foi o aluno que fez a ameaça (Sala de professores)",            #45
 "[[12:00] Segunda aula (Sala de aula B)",                                      #46
 "Atribuir notas aos projetos de turma (Sala de professores)",                  #47
 "Comprar uma rifa para a viagem de finalistas (Pátio)",                        #48
 "Refletir sobre como intervir (Sala de professores)",                          #49
 "[[15:00] Reunião com os professores (Sala de professores)",                   #50
 ]
]

define tasks_feedback = [
 [                                                                              #s0
 "Discovered why Estrela missed class.",
 "Did not complete the task."
 ], [                                                                           #s1
 "Took time to identify that something serious was going on with a student.",
 "It is important to be attentive to situations involving students at risk.",
 "Took time to identify a student who was mistreating another.",
 "It is important to be attentive to situations involving students at risk.",
 "Took time to reflect on how to intervene in a situation where a student was being mistreated by others.",
 "It is important to reflect on what can be done to intervene in a situation where a student is being mistreated by others."
 ], [                                                                           #s2
 "Took time to identify a student who was mistreating another.",
 "It is important to be attentive to situations involving students at risk.",
 "Took time to identify that something serious was going on with a student.",
 "It is important to be attentive to situations involving students at risk.",
 "Took time to reflect on how to intervene in a situation where a student was being mistreated by others.",
 "It is important to reflect on what can be done to intervene in a situation where a student is being mistreated by others."
 ], [                                                                           #s3
 "Took time to identify a student who was mistreating another.",
 "It is important to be attentive to situations involving students at risk.",
 "Took time to identify that something serious was going on with a student.",
 "It is important to be attentive to situations involving students at risk.",
 "Took time to reflect on how to intervene in a situation where a student was being mistreated by others.",
 "It is important to reflect on what can be done to intervene in a situation where a student is being mistreated by others."
 ], [                                                                           #s4
 "Took time to identify a student who was mistreating another.",
 "It is important to be attentive to situations involving students at risk.",
 "Took time to identify that something serious was going on with a student.",
 "It is important to be attentive to situations involving students at risk.",
 "Took time to reflect on how to intervene in a situation where a student was being mistreated by others.",
 "It is important to reflect on what can be done to intervene in a situation where a student is being mistreated by others."
 ]
]
#TRANSLATEdefine tasks_feedback = [
#TRANSLATE [                                                                              #s0
#TRANSLATE "Descobriu o porquê da Estrela ter faltado à aula.",
#TRANSLATE "Não completou a tarefa."
#TRANSLATE ], [                                                                           #s1
#TRANSLATE "Dedicou tempo a identificar que algo de grave se passava com um aluno.",
#TRANSLATE "É importante estar atento/a a situações de risco envolvendo alunos.",
#TRANSLATE "Dedicou tempo a identificar um aluno que estava a maltratar outro.",
#TRANSLATE "É importante estar atento/a a situações de risco envolvendo alunos.",
#TRANSLATE "Dedicou tempo a refletir sobre como intervir numa situação em que um aluno estava a ser maltratado por outros.",
#TRANSLATE "É importante refletir sobre o que pode fazer para intervir numa situação em que um aluno está a ser maltratado por outros."
#TRANSLATE ], [                                                                           #s2
#TRANSLATE "Dedicou tempo a identificar um aluno que estava a maltratar outro.",
#TRANSLATE "É importante estar atento/a a situações de risco envolvendo alunos.",
#TRANSLATE "Dedicou tempo a identificar que algo de grave se passava com um aluno.",
#TRANSLATE "É importante estar atento/a a situações de risco envolvendo alunos.",
#TRANSLATE "Dedicou tempo a refletir sobre como intervir numa situação em que um aluno estava a ser maltratado por outros.",
#TRANSLATE "É importante refletir sobre o que pode fazer para intervir numa situação em que um aluno está a ser maltratado por outros."
#TRANSLATE ], [                                                                           #s3
#TRANSLATE "Dedicou tempo a identificar um aluno que estava a maltratar outro.",
#TRANSLATE "É importante estar atento/a a situações de risco envolvendo alunos.",
#TRANSLATE "Dedicou tempo a identificar que algo de grave se passava com um aluno.",
#TRANSLATE "É importante estar atento/a a situações de risco envolvendo alunos.",
#TRANSLATE "Dedicou tempo a refletir sobre como intervir numa situação em que um aluno estava a ser maltratado por outros.",
#TRANSLATE "É importante refletir sobre o que pode fazer para intervir numa situação em que um aluno está a ser maltratado por outros."
#TRANSLATE ], [                                                                           #s4
#TRANSLATE "Dedicou tempo a identificar um aluno que estava a maltratar outro.",
#TRANSLATE "É importante estar atento/a a situações de risco envolvendo alunos.",
#TRANSLATE "Dedicou tempo a identificar que algo de grave se passava com um aluno.",
#TRANSLATE "É importante estar atento/a a situações de risco envolvendo alunos.",
#TRANSLATE "Dedicou tempo a refletir sobre como intervir numa situação em que um aluno estava a ser maltratado por outros.",
#TRANSLATE "É importante refletir sobre o que pode fazer para intervir numa situação em que um aluno está a ser maltratado por outros."
#TRANSLATE ]
#TRANSLATE]

default task_num = -1

default student_picked_task = ""

label pick_student_task:
    hide screen pick_student_task
    #if tasks_state[session][10] == 1:
    #    $ ses_fb_t[2].append(student_picked_task)
    #    jump task13.pergunta
    if tasks_state[session][6] == 1:
        $ ses_fb_t[1].append(student_picked_task)
        jump task9.pergunta
    if tasks_state[session][2] == 1:
        $ ses_fb_t[0].append(student_picked_task)
        jump task5.pergunta
    jogo "Erro: pick_student_task"
    jump pick_student_task

screen pick_student_task:
    key "mouseup_1" action NullAction()
    grid 6 2:
        area (135, 40, 1920-270, 750)

        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/abel_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Abel":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#0e6716"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Abel"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/carmen_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Cármen":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#fb73b4"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Cármen"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/estrela_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Estrela":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#ffa000"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Estrela"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/helder_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Hélder":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#fffac8"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Hélder"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/isabel_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Isabel":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#ff2100"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Isabel"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/jorge_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Jorge":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#ff6300"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Jorge"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/manuela_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Manuela":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#00fff2"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Manuela"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/nando_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Nando":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#003cc8"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Nando"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/patricia_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Patrícia":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#0070c8"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Patrícia"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/rui_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Rui":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#00c38c"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Rui"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/samuel_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Samuel":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#ffe119"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Samuel"), Jump("pick_student_task")]
        frame:
            xsize 250
            ysize 320
            add im.Scale("avatars/emotions/tatiana_happy.png", 220, 220):
                xalign 0.5
                yalign 0.3
            textbutton "Tatiana":
                xalign 0.5
                ypos 240
                text_size 50
                text_color "#79c65d"
                text_outlines [(absolute(1), "#000000")]
                text_hover_color "#fff"
                action [SetVariable("student_picked_task", "Tatiana"), Jump("pick_student_task")]
label start_aula:
    call toggle_UI
    call set_scene(current_room, True)
    $ next_aula = "aula"
    if intervalo == 2:
        $ next_aula = "reunião"
    menu:
        player "{i}Do I want to wait in the classroom until the next class starts?{/i}"
        #TRANSLATEplayer "{i}Quero esperar nesta sala até à hora da [next_aula] começar?{/i}"

        "Yes":
        #TRANSLATE"Sim":
            $ ping = True
            #player "{i}Vou mais cedo para a [next_aula].{/i}"
            $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][task_num] + '\n'
            $ tasks_state[session][task_num] = 1
            call toggle_UI
            jump periodo_aula
        "No":
        #TRANSLATE"Não":
            player "{i}I still have some time left in the break.{/i}"
            #TRANSLATEplayer "{i}Tenho tempo restante de intervalo.{/i}"
            jump leave_conversation

label task0:
    call toggle_UI
    $ tasks_state[session][0] = 1
    $ minutes += 20
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/pages.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}It took me 20 minutes, but I finished the notes.{/i}"
    #TRANSLATEplayer "{i}Demorei 20 minutos, mas acabei os apontamentos.{/i}"
    $ taskNew = True
    $ ping = True
    $ s0_state = 3
    jump leave_conversation

label task1:
    $ task_num = 1
    jump start_aula

label task2:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Have I completed the investigation to find out why Estrela missed class?{/i}"
        #TRANSLATEplayer "{i}Já concluí a investigação para descobrir a razão pela qual a Estrela faltou à aula?{/i}"

        "Yes":
        #TRANSLATE"Sim":
            jump task2.resposta
        "No":
        #TRANSLATE"Não":
            player "{i}I'll investigate further.{/i}"
            #TRANSLATEplayer "{i}Vou investigar mais um pouco.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][2] = 1
        $ minutes += 2
        $ n_actions += 1

        menu:
            player "{i}Was I able to determine why Estrela didn't go to class?{/i}"

            "Yes":
                $ reason = "What was the reason?"
            "No":
                $ reason = "Why couldn't I?"
                jump .pergunta
        #TRANSLATEmenu:
        #TRANSLATE    player "{i}Consegui determinar a razão da Estrela não ter ido à aula?{/i}"
        #TRANSLATE
        #TRANSLATE    "Sim":
        #TRANSLATE        $ reason = "Qual foi a razão?"
        #TRANSLATE    "Não":
        #TRANSLATE        $ reason = "Porque não consegui?"
        #TRANSLATE        jump .pergunta

        python:
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                resposta = "No answer."
                #TRANSLATEresposta = "Não respondeu."
            reason =  "In this case, is the reason understandable?"
            #TRANSLATEreason =  "Neste caso, a razão é compreensível?"

    label .pergunta:
        python:
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[0][2] + '\n'
        $ s0_state = 10
        $ drag_game = True
        jump leave_conversation

# session 1

label task3:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][0] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/keyboard.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Enviei o e-mail que a diretora me pediu.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][0] + '\n'
    jump leave_conversation

label task4:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][1] = 1
    $ minutes += 2
    $ n_actions += 1
    player "Esta foi a terceira vez que faltaste à aula de apoio."
    aluno "Sim, professor. Peço desculpa."
    player "Terei de informar o teu encarregado de educação..."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/writing.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Escrevi o recado na caderneta do aluno.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][1] + '\n'
    jump leave_conversation

label task5:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Já concluí a investigação para descobrir quem era o sujeito da publicação?{/i}"

        "Sim":
            jump task5.resposta
        "Não":
            player "{i}Vou investigar mais um pouco.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][2] = 1
        $ minutes += 2
        $ n_actions += 1
        $ ses_fb_t[0].append("Consegui determinar quem era o aluno que estava na publicação?")
        menu:
            player "{i}Consegui determinar quem era o aluno que estava na publicação?{/i}"

            "Sim":
                $ ses_fb_t[0].append("Sim")
                show screen pick_student_task
                #$ reason = "Quem foi?"
                $ reason =  "Como é que identifiquei?"
            "Não":
                $ ses_fb_t[0].append("Não")
                $ reason = "Porque não consegui identificar?"
                jump .pergunta

        $ ses_fb_t[0].append("Quem foi?")
        "Quem foi?"
        python:
            resposta = renpy.input(reason, length=20)
            resposta = resposta.strip()

            if not resposta:
                resposta = "Não respondeu."
            reason =  "Como é que identifiquei?"

    label .pergunta:
        python:
            ses_fb_t[0].append(reason)
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                resposta = "Não respondeu."
            ses_fb_t[0].append(resposta)

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][2] + '\n'
        jump leave_conversation

label task6:
    $ task_num = 3
    jump start_aula

label task7:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][4] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/printer.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Tirei as fotocópias que precisava.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][4] + '\n'
    jump leave_conversation


label task8:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][5] = 1
    $ minutes += 2
    $ n_actions += 1
    aluno "Professor, poderia então tirar-me uma dúvida rápida?"
    player "Sim, mostra-me o exercício..."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/chalk.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Tirei a dúvida que o meu aluno tinha.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][5] + '\n'
    jump leave_conversation

label task9:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Já concluí a investigação para descobrir quem foi o autor da publicação?{/i}"

        "Sim":
            jump task9.resposta
        "Não":
            player "{i}Vou investigar mais um pouco.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][6] = 1
        $ minutes += 2
        $ n_actions += 1
        $ ses_fb_t[1].append("Consegui determinar quem foi o aluno que publicou a fotografia?")
        menu:
            player "{i}Consegui determinar quem foi o aluno que publicou a fotografia?{/i}"

            "Sim":
                $ ses_fb_t[1].append("Sim")
                show screen pick_student_task
                #$ reason = "Quem foi?"
                $ reason =  "Como é que identifiquei?"
            "Não":
                $ ses_fb_t[1].append("Não")
                $ reason = "Porque não consegui identificar?"
                jump .pergunta

        $ ses_fb_t[1].append("Quem foi?")
        "Quem foi?"
        python:
            resposta = renpy.input(reason, length=20)
            resposta = resposta.strip()

            if not resposta:
                resposta = "Não respondeu."
            reason =  "Como é que identifiquei?"

    label .pergunta:
        python:
            ses_fb_t[1].append(reason)
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                resposta = "Não respondeu."
            ses_fb_t[1].append(resposta)

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][6] + '\n'
        jump leave_conversation

label task10:
    $ task_num = 7
    jump start_aula

label task11:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][8] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/pages.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Preparei a atividade para amanhã.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][8] + '\n'
    jump leave_conversation

label task12:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][9] = 1
    $ minutes += 2
    $ n_actions += 1
    player "Boa tarde, podias-me dar uma rifa?"
    aluno "Sim, professor! Obrigado pelo seu apoio..."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/coins.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Comprei uma rifa para suportar o canil.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][9] + '\n'
    jump leave_conversation

label task13:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Estou pronto para refletir sobre a publicação do Nando?{/i}"

        "Sim":
            jump task13.resposta
        "Não":
            player "{i}Tenho de pensar mais sobre o assunto.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][10] = 1
        $ minutes += 2
        $ n_actions += 1
        "Para cada uma das frases, escolha o nível de concordância mais adequado."
        $ ses_fb_t[2].append("Sei o que posso fazer para intervir nestas situações.")
        menu:
            player "{i}Sei o que posso fazer para intervir nestas situações.{/i}"

            "Nada":
                $ reason = "1"
                $ ses_fb_t[2].append(1)
            "Pouco":
                $ reason = "2"
                $ ses_fb_t[2].append(2)
            "Algo":
                $ reason = "3"
                $ ses_fb_t[2].append(3)
            "Muito":
                $ reason = "4"
                $ ses_fb_t[2].append(4)

        $ ses_fb_t[2].append("Sou capaz de ajudar a resolver a situação apesar de ser difícil.")
        menu:
            player "{i}Sou capaz de ajudar a resolver a situação apesar de ser difícil.{/i}"

            "Nada":
                $ reason = "1"
                $ ses_fb_t[2].append(1)
            "Pouco":
                $ reason = "2"
                $ ses_fb_t[2].append(2)
            "Algo":
                $ reason = "3"
                $ ses_fb_t[2].append(3)
            "Muito":
                $ reason = "4"
                $ ses_fb_t[2].append(4)

        $ ses_fb_t[2].append("Quero dedicar-me a resolver esta situação.")
        menu:
            player "{i}Quero dedicar-me a resolver esta situação.{/i}"

            "Nada":
                $ reason = "1"
                $ ses_fb_t[2].append(1)
            "Pouco":
                $ reason = "2"
                $ ses_fb_t[2].append(2)
            "Algo":
                $ reason = "3"
                $ ses_fb_t[2].append(3)
            "Muito":
                $ reason = "4"
                $ ses_fb_t[2].append(4)

        menu:
            player "{i}Quero acrescentar alguma reflexão?{/i}"

            "Sim":
                $ ses_fb_t[2].append("Comentário extra:")
                $ note = ""
                call screen comment
                $ ses_fb_t[2].append(note)
            "Não":
                $ reason = reason

        #python:
        #    reason = "Se quiser, pode acrescentar algum comentário extra."
        #    resposta = renpy.input(reason, length=200)
        #    resposta = resposta.strip()

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][10] + '\n'
        jump leave_conversation

label task14:
    $ task_num = 11
    jump start_aula

# session 2

label task15:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][0] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/pages.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Acabei a preparação da aula.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][0] + '\n'
    jump leave_conversation

label task16:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][1] = 1
    $ minutes += 2
    $ n_actions += 1
    player "Precisavam de ajuda aqui nesta parte?"
    aluno "Sim, professor."
    player "Têm de fazer assim..."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/class4.wav"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Ajudei os alunos com a exposição.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][1] + '\n'
    jump leave_conversation

label task17:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        "{i}Já concluí a investigação para descobrir que aluno ameaçou violência?{/i}"

        "Sim":
            jump task17.resposta
        "Não":
            player "{i}Vou investigar mais um pouco.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][2] = 1
        $ minutes += 2
        $ n_actions += 1
        $ ses_fb_t[0].append("Consegui determinar quem é o aluno que ameaçou bater noutro?")
        menu:
            "{i}Consegui determinar quem é o aluno que ameaçou bater noutro?{/i}"

            "Sim":
                $ ses_fb_t[0].append("Sim")
                show screen pick_student_task
                $ reason =  "Como é que identifiquei?"
            "Não":
                $ ses_fb_t[0].append("Não")
                $ reason = "Porque não consegui identificar?"
                jump .pergunta

        $ ses_fb_t[0].append("Quem foi?")
        "Quem foi?"
        python:
            resposta = renpy.input(reason, length=20)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."
            reason =  "Como é que identifiquei?"

    label .pergunta:
        python:
            ses_fb_t[0].append(reason)
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."
            ses_fb_t[0].append(resposta)

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][2] + '\n'
        jump leave_conversation

label task18:
    $ task_num = 3
    jump start_aula

label task19:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][4] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/keyboard.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Organizei os trabalhos.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][4] + '\n'
    jump leave_conversation

label task20:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][5] = 1
    $ minutes += 2
    $ n_actions += 1
    aluno "Professor, poderia então tirar-me uma dúvida rápida?"
    player "Sim, mostra-me o teste..."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/chalk.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Tirei a dúvida que o meu aluno tinha.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][5] + '\n'
    jump leave_conversation

label task21:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        "{i}Já concluí a investigação para descobrir quem foi ameaçado?{/i}"

        "Sim":
            jump task21.resposta
        "Não":
            player "{i}Vou investigar mais um pouco.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][6] = 1
        $ minutes += 2
        $ n_actions += 1
        $ ses_fb_t[1].append("Consegui determinar quem é o aluno que foi ameaçado?")
        menu:
            "{i}Consegui determinar quem é o aluno que foi ameaçado?{/i}"

            "Sim":
                $ ses_fb_t[1].append("Sim")
                show screen pick_student_task
                $ reason =  "Como é que identifiquei?"
            "Não":
                $ ses_fb_t[1].append("Não")
                $ reason = "Porque não consegui identificar?"
                jump .pergunta

        $ ses_fb_t[1].append("Quem foi?")
        "Quem foi?"
        python:
            resposta = renpy.input(reason, length=20)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."
            reason =  "Como é que identifiquei?"

    label .pergunta:
        python:
            ses_fb_t[1].append(reason)
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."
            ses_fb_t[1].append(resposta)

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][6] + '\n'
        jump leave_conversation

label task22:
    $ task_num = 7
    jump start_aula

label task23:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][8] = 1
    $ minutes += 2
    $ n_actions += 1
    player "Boa tarde, podemos ver dos documentos agora?"
    coordciclo "Sim, vamos."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/writing.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Assinei os documentos.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][8] + '\n'
    jump leave_conversation

label task24:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][9] = 1
    $ minutes += 2
    $ n_actions += 1
    player "Aqui tens o livro que pediste."
    aluno "Obrigado professor! Eu devolvo-lhe depois na aula de quinta feira."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/pages.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Emprestei o livro ao meu aluno.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][9] + '\n'
    jump leave_conversation

label task25:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        "{i}Estou pronto para refletir sobre como intervir face à publicação?{/i}"

        "Sim":
            jump task25.resposta
        "Não":
            player "{i}Tenho de pensar mais sobre o assunto.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][10] = 1
        $ minutes += 2
        $ n_actions += 1
        $ ses_fb_t[2].append("Sei o que posso fazer para intervir nestas situações.")
        "Para cada uma das frases, escolha o nível de concordância mais adequado."
        menu:
            player "{i}Sei o que posso fazer para intervir nestas situações.{/i}"

            "Nada":
                $ reason = "1"
                $ ses_fb_t[2].append(1)
            "Pouco":
                $ reason = "2"
                $ ses_fb_t[2].append(2)
            "Algo":
                $ reason = "3"
                $ ses_fb_t[2].append(3)
            "Muito":
                $ reason = "4"
                $ ses_fb_t[2].append(4)

        $ ses_fb_t[2].append("Sou capaz de ajudar a resolver a situação apesar de ser difícil.")
        menu:
            player "{i}Sou capaz de ajudar a resolver a situação apesar de ser difícil.{/i}"

            "Nada":
                $ reason = "1"
                $ ses_fb_t[2].append(1)
            "Pouco":
                $ reason = "2"
                $ ses_fb_t[2].append(2)
            "Algo":
                $ reason = "3"
                $ ses_fb_t[2].append(3)
            "Muito":
                $ reason = "4"
                $ ses_fb_t[2].append(4)

        $ ses_fb_t[2].append("Quero dedicar-me a resolver esta situação.")
        menu:
            player "{i}Quero dedicar-me a resolver esta situação.{/i}"

            "Nada":
                $ reason = "1"
                $ ses_fb_t[2].append(1)
            "Pouco":
                $ reason = "2"
                $ ses_fb_t[2].append(2)
            "Algo":
                $ reason = "3"
                $ ses_fb_t[2].append(3)
            "Muito":
                $ reason = "4"
                $ ses_fb_t[2].append(4)

        menu:
            player "{i}Quero acrescentar alguma reflexão?{/i}"

            "Sim":
                $ ses_fb_t[2].append("Comentário extra:")
                $ note = ""
                call screen comment
                $ ses_fb_t[2].append(note)
            "Não":
                $ reason = reason

        #python:
        #    reason = "Se quiser, pode acrescentar algum comentário extra."
        #    resposta = renpy.input(reason, length=200)
        #    resposta = resposta.strip()

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][10] + '\n'
        jump leave_conversation

label task26:
    $ task_num = 11
    jump start_aula

# session 3

label task27:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][0] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/printer.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Imprimi a lista para o picnic da escola.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][0] + '\n'
    jump leave_conversation

label task28:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][1] = 1
    $ minutes += 2
    $ n_actions += 1
    aluna "Podemos levar as coisas professor?"
    player "Levem aqueles cestos, eu levo o resto."
    aluna "Ok."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Levámos os materiais para a sala polivalente.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][1] + '\n'
    $ current_room = 10
    $ last_room = 1
    jump leave_conversation

label task29:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Já concluí a investigação para descobrir quem foi o aluno ofendido?{/i}"

        "Sim":
            jump task29.resposta
        "Não":
            player "{i}Vou investigar mais um pouco.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][2] = 1
        $ minutes += 2
        $ n_actions += 1
        $ ses_fb_t[0].append("Consegui determinar quem era o aluno que estava na publicação?")
        menu:
            player "{i}Consegui determinar quem foi o aluno ofendido?{/i}"

            "Sim":
                $ ses_fb_t[0].append("Sim")
                show screen pick_student_task
                $ reason =  "Como é que identifiquei?"
            "Não":
                $ ses_fb_t[0].append("Não")
                $ reason = "Porque não consegui identificar?"
                jump .pergunta

        $ ses_fb_t[0].append("Quem foi?")
        "Quem foi?"
        python:
            resposta = renpy.input(reason, length=20)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."
            reason =  "Como é que identifiquei?"

    label .pergunta:
        python:
            ses_fb_t[0].append(reason)
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                resposta = "Não respondeu."
            ses_fb_t[0].append(resposta)

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][2] + '\n'
        jump leave_conversation

label task30:
    $ task_num = 3
    jump start_aula

label task31:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][4] = 1
    $ minutes += 2
    $ n_actions += 1
    player "Boa tarde, aqui tem a lista de inscrições que pediu."
    coordciclo "Muito obrigado."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/pages.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Entreguei a lista de inscrições do picnic ao coordenador de ciclo.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][4] + '\n'
    jump leave_conversation

label task32:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][5] = 1
    $ minutes += 2
    $ n_actions += 1
    aluno "Professor, poderia então tirar-me uma dúvida rápida?"
    player "Sim, mostra-me o exercício..."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/chalk.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Tirei a dúvida que o meu aluno tinha.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][5] + '\n'
    jump leave_conversation

label task33:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Já concluí a investigação para descobrir quem foi a aluna que ofendeu o Samuel?{/i}"

        "Sim":
            jump task33.resposta
        "Não":
            player "{i}Vou investigar mais um pouco.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][6] = 1
        $ minutes += 2
        $ n_actions += 1
        $ ses_fb_t[1].append("Consegui determinar quem foi o aluno que publicou a fotografia?")
        menu:
            player "{i}Consegui determinar quem foi a aluna?{/i}"

            "Sim":
                $ ses_fb_t[1].append("Sim")
                show screen pick_student_task
                $ reason =  "Como é que identifiquei?"
            "Não":
                $ ses_fb_t[1].append("Não")
                $ reason = "Porque não consegui identificar?"
                jump .pergunta

        $ ses_fb_t[1].append("Quem foi?")
        "Quem foi?"
        python:
            resposta = renpy.input(reason, length=20)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."
            reason =  "Como é que identifiquei?"

    label .pergunta:
        python:
            ses_fb_t[1].append(reason)
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                resposta = "Não respondeu."
            ses_fb_t[1].append(resposta)

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][6] + '\n'
        jump leave_conversation

label task34:
    $ task_num = 7
    jump start_aula

label task35:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][8] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/keyboard.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Enviei um e-mail a relembrar o picnic da escola aos encarregados de educação.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][8] + '\n'
    jump leave_conversation

label task36:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][9] = 1
    $ minutes += 2
    $ n_actions += 1
    player "Boa tarde, aqui estão os materiais que pediu."
    coordciclo "Obrigado pela ajuda, [player_name_dim]."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/folder.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Entreguei os materiais do picnic ao coordenador de ciclo.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][9] + '\n'
    jump leave_conversation

label task37:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Estou pronto para refletir sobre a publicação?{/i}"

        "Sim":
            jump task13.resposta
        "Não":
            player "{i}Tenho de pensar mais sobre o assunto.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][10] = 1
        $ minutes += 2
        $ n_actions += 1
        "Para cada uma das frases, escolha o nível de concordância mais adequado."
        $ ses_fb_t[2].append("Sei o que posso fazer para intervir nestas situações.")
        menu:
            player "{i}Sei o que posso fazer para intervir nestas situações.{/i}"

            "Nada":
                $ reason = "1"
                $ ses_fb_t[2].append(1)
            "Pouco":
                $ reason = "2"
                $ ses_fb_t[2].append(2)
            "Algo":
                $ reason = "3"
                $ ses_fb_t[2].append(3)
            "Muito":
                $ reason = "4"
                $ ses_fb_t[2].append(4)

        $ ses_fb_t[2].append("Sou capaz de ajudar a resolver a situação apesar de ser difícil.")
        menu:
            player "{i}Sou capaz de ajudar a resolver a situação apesar de ser difícil.{/i}"

            "Nada":
                $ reason = "1"
                $ ses_fb_t[2].append(1)
            "Pouco":
                $ reason = "2"
                $ ses_fb_t[2].append(2)
            "Algo":
                $ reason = "3"
                $ ses_fb_t[2].append(3)
            "Muito":
                $ reason = "4"
                $ ses_fb_t[2].append(4)

        $ ses_fb_t[2].append("Quero dedicar-me a resolver esta situação.")
        menu:
            player "{i}Quero dedicar-me a resolver esta situação.{/i}"

            "Nada":
                $ reason = "1"
                $ ses_fb_t[2].append(1)
            "Pouco":
                $ reason = "2"
                $ ses_fb_t[2].append(2)
            "Algo":
                $ reason = "3"
                $ ses_fb_t[2].append(3)
            "Muito":
                $ reason = "4"
                $ ses_fb_t[2].append(4)

        menu:
            player "{i}Quero acrescentar alguma reflexão?{/i}"

            "Sim":
                $ ses_fb_t[2].append("Comentário extra:")
                $ note = ""
                call screen comment
            "Não":
                $ reason = reason

        #python:
        #    reason = "Se quiser, pode acrescentar algum comentário extra."
        #    resposta = renpy.input(reason, length=200)
        #    resposta = resposta.strip()

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][10] + '\n'
        jump leave_conversation

label task38:
    $ task_num = 11
    jump start_aula

# session 4

label task39:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][0] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/pages.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Tenho o livro que irei emprestar ao aluno.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][0] + '\n'
    jump leave_conversation

label task40:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][1] = 1
    $ minutes += 2
    $ n_actions += 1
    aluno "Tinha dúvidas nesta parte professor."
    player "Vamos lá a ver..."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/chalk.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Ajudei o aluno a tirar as dúvidas que tinha.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][1] + '\n'
    jump leave_conversation

label task41:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Já concluí a investigação para descobrir quem foi ameaçado?{/i}"

        "Sim":
            jump task41.resposta
        "Não":
            player "{i}Vou investigar mais um pouco.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][2] = 1
        $ minutes += 2
        $ n_actions += 1
        menu:
            player "{i}Consegui determinar quem era o aluno que foi ameaçado?{/i}"

            "Sim":
                $ reason = "Quem era?"
            "Não":
                $ reason = "Porque não consegui identificar?"
                jump .pergunta

        python:
            resposta = renpy.input(reason, length=20)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."
            reason =  "Como é que identifiquei?"

    label .pergunta:
        python:
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][2] + '\n'
        jump leave_conversation

label task42:
    $ task_num = 3
    jump start_aula

label task43:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][4] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/folder.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Dei a planificação dos projetos de turma.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][4] + '\n'
    jump leave_conversation


label task44:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][5] = 1
    $ minutes += 2
    $ n_actions += 1
    player "Ok pessoal, vamos pendurar os cartazes. Sigam-me."
    aluno "Sim, professor."
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/pages.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Afixámos os cartazes.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][5] + '\n'
    jump leave_conversation

label task45:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Já concluí a investigação para descobrir quem estava a ameaçar partilhar a fotografia?{/i}"

        "Sim":
            jump task45.resposta
        "Não":
            player "{i}Vou investigar mais um pouco.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][6] = 1
        $ minutes += 2
        $ n_actions += 1
        menu:
            player "{i}Consegui determinar quem foi o aluno que ameaçou partilhar a fotografia?{/i}"

            "Sim":
                $ reason = "Quem foi?"
            "Não":
                $ reason = "Porque não consegui identificar?"
                jump .pergunta

        python:
            resposta = renpy.input(reason, length=20)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."
            reason =  "Como é que identifiquei?"

    label .pergunta:
        python:
            resposta = renpy.input(reason, length=250)
            resposta = resposta.strip()

            if not resposta:
                 resposta = "Não respondeu."

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][6] + '\n'
        jump leave_conversation

label task46:
    $ task_num = 7
    jump start_aula

label task47:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][8] = 1
    $ minutes += 2
    $ n_actions += 1
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/keyboard.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Atribuí as notas aos projetos.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][8] + '\n'
    jump leave_conversation

label task48:
    call toggle_UI
    $ pro_social += 1
    $ tasks_state[session][9] = 1
    $ minutes += 2
    $ n_actions += 1
    player "Boa tarde, podias-me dar uma rifa?"
    aluno "Sim, professor!"
    scene black_screen with Fade(0.5, 0, 0)
    play sound "audio/coins.mp3"
    scene black_screen with Fade(0, 1.0, 0.5)
    player "{i}Comprei uma rifa da viagem de finalistas.{/i}"
    $ taskNew = True
    $ ping = True
    $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][9] + '\n'
    jump leave_conversation

label task49:
    call toggle_UI
    call set_scene(current_room, True)
    menu:
        player "{i}Estou pronto para refletir sobre como intervir?{/i}"

        "Sim":
            jump task49.resposta
        "Não":
            player "{i}Tenho de pensar mais sobre o assunto.{/i}"
            jump leave_conversation

    label .resposta:
        $ pro_social += 1
        $ tasks_state[session][10] = 1
        $ minutes += 2
        $ n_actions += 1
        "Para cada uma das frases, escolha o nível de concordância mais adequado."
        menu:
            player "{i}Sei o que posso fazer para intervir nestas situações.{/i}"

            "Nada":
                $ reason = "1"
            "Pouco":
                $ reason = "2"
            "Algo":
                $ reason = "3"
            "Muito":
                $ reason = "4"

        menu:
            player "{i}Sou capaz de ajudar a resolver a situação apesar de ser difícil.{/i}"

            "Nada":
                $ reason = "1"
            "Pouco":
                $ reason = "2"
            "Algo":
                $ reason = "3"
            "Muito":
                $ reason = "4"

        menu:
            player "{i}Quero dedicar-me a resolver esta situação.{/i}"

            "Nada":
                $ reason = "1"
            "Pouco":
                $ reason = "2"
            "Algo":
                $ reason = "3"
            "Muito":
                $ reason = "4"

        menu:
            player "{i}Quero acrescentar alguma reflexão?{/i}"

            "Sim":
                $ note = ""
                call screen comment
            "Não":
                $ reason = reason

        #python:
        #    reason = "Se quiser, pode acrescentar algum comentário extra."
        #    resposta = renpy.input(reason, length=200)
        #    resposta = resposta.strip()

        #$ feedbackNew = True
        $ taskNew = True
        $ ping = True
        $ st_actions[intervalo] += "Tarefa: " + tasks_description[session][10] + '\n'
        jump leave_conversation

label task50:
    $ task_num = 11
    jump start_aula

# functions

screen comment:
    vbox:
        yalign 0.5
        xalign 0.5
        frame:
            background "#eee"
            xsize 1000
            ysize 400
            has vbox
            label "Comentário Extra"
            input:
                default ""
                value VariableInputValue('note')
                length 300
            textbutton "Terminar" action Return()

default note = ""
