default activeMenu = False
default show_toggle_UI = True
default show_menulist_UI = False
default show_tasklist_UI = False
default show_maplist_UI = False
default show_studentlist_UI = False
default show_feedbacklist_UI = False
default taskNew = False
default mapNew = False
default studentNew = False
default feedbackNew = False

label setup_UI:
    show screen menulist
    show screen menulist_UI
    show screen clock_UI
    show screen keymapscreen
    return

label toggle_UI:
    if show_toggle_UI:
        $ show_menulist_UI = False
        $ show_tasklist_UI = False
        $ show_maplist_UI = False
        $ show_studentlist_UI = False
        $ show_feedbacklist_UI = False
        $ activeMenu = False
        hide screen menulist
        hide screen menulist_UI
        hide screen clock_UI
    else:
        show screen menulist
        show screen menulist_UI
        show screen clock_UI
    $ show_toggle_UI = not show_toggle_UI
    return

screen menulist:
    zorder 70
    imagebutton:
        xalign 5*0.001080
        yalign 5*0.001920
        idle If((taskNew or mapNew or studentNew or feedbackNew) and not show_menulist_UI, "menu_new_highlight", im.Scale("menus/menulist_idle.png", 100, 100))
        hover im.Scale("menus/menulist_hover.png", 100, 100)
        action [SetVariable("show_menulist_UI", not show_menulist_UI), SetVariable("show_tasklist_UI", False), SetVariable("show_maplist_UI", False),
         SetVariable("show_studentlist_UI", False), SetVariable("show_feedbacklist_UI", False), SetVariable("activeMenu", False)]
        focus_mask True

    #key "t" action [SetVariable("show_menulist_UI", not show_tasklist_UI), SetVariable("show_tasklist_UI", not show_tasklist_UI), SetVariable("show_maplist_UI", False),
    # SetVariable("show_studentlist_UI", False), SetVariable("show_feedbacklist_UI", False), SetVariable("taskNew", False), SetVariable("activeMenu", not show_tasklist_UI)]
    #key "m" action [SetVariable("show_menulist_UI", not show_maplist_UI), SetVariable("show_tasklist_UI", False), SetVariable("show_maplist_UI", not show_maplist_UI),
    # SetVariable("show_studentlist_UI", False), SetVariable("show_feedbacklist_UI", False), SetVariable("mapfloor", floor), SetVariable("activeMenu", not show_maplist_UI)]
    #key "k" action [SetVariable("show_menulist_UI", not show_studentlist_UI), SetVariable("show_tasklist_UI", False), SetVariable("show_maplist_UI", False),
    # SetVariable("show_studentlist_UI", not show_studentlist_UI), SetVariable("show_feedbacklist_UI", False), SetVariable("activeMenu", not show_studentlist_UI)]
    #key "j" action [SetVariable("show_menulist_UI", not show_feedbacklist_UI), SetVariable("show_tasklist_UI", False), SetVariable("show_maplist_UI", False),
    # SetVariable("show_studentlist_UI", False), SetVariable("show_feedbacklist_UI", not show_feedbacklist_UI), SetVariable("feedbackNew", False), SetVariable("activeMenu", not show_feedbacklist_UI)]
    if show_menulist_UI:
        #tasklist
        imagebutton:
            xalign 5*0.001080
            yalign (5+55)*0.001920
            idle If(taskNew, "task_new_highlight", im.Scale("menus/tasklist_idle.png", 100, 100))
            hover im.Scale("menus/tasklist_hover.png", 100, 100)
            action [SetVariable("show_tasklist_UI", not show_tasklist_UI), SetVariable("show_maplist_UI", False), SetVariable("show_studentlist_UI", False),
             SetVariable("show_feedbacklist_UI", False), SetVariable("taskNew", False), SetVariable("activeMenu", not show_tasklist_UI)]
            focus_mask True
        #maplist
        imagebutton:
            xalign 5*0.001080
            yalign (5+55*2)*0.001920
            idle If(mapNew, "map_new_highlight", im.Scale("menus/maplist_idle.png", 100, 100))
            hover im.Scale("menus/maplist_hover.png", 100, 100)
            action [SetVariable("show_tasklist_UI", False), SetVariable("show_maplist_UI", not show_maplist_UI), SetVariable("show_studentlist_UI", False),
             SetVariable("show_feedbacklist_UI", False), SetVariable("mapNew", False), SetVariable("mapfloor", floor), SetVariable("activeMenu", not show_maplist_UI)]
            focus_mask True
        #studentlist
        if s0_state > 4:
            imagebutton:
                xalign 5*0.001080
                yalign (5+55*3)*0.001920
                idle If(studentNew, "student_new_highlight", im.Scale("menus/studentlist_idle.png", 100, 100))
                hover im.Scale("menus/studentlist_hover.png", 100, 100)
                action [SetVariable("show_tasklist_UI", False), SetVariable("show_maplist_UI", False), SetVariable("show_studentlist_UI", not show_studentlist_UI),
                 SetVariable("show_feedbacklist_UI", False), SetVariable("studentNew", False), SetVariable("activeMenu", not show_studentlist_UI)]
                focus_mask True
        #feedbacklist
        #if s0_state > 6:
        #    imagebutton:
        #        xalign 5*0.001080
        #        yalign (5+55*4)*0.001920
        #        idle If(feedbackNew, "feedback_new_highlight", im.Scale("menus/feedback_idle.png", 100, 100))
        #        hover im.Scale("menus/feedback_hover.png", 100, 100)
        #        action [SetVariable("show_tasklist_UI", False), SetVariable("show_maplist_UI", False), SetVariable("show_studentlist_UI", False),
        #         SetVariable("show_feedbacklist_UI", not show_feedbacklist_UI), SetVariable("feedbackNew", False), SetVariable("activeMenu", not show_feedbacklist_UI)]
        #        focus_mask True

screen menulist_UI:
    zorder 50
    if show_tasklist_UI:
        button:
            xsize 1920
            ysize 1080
            action NullAction()
        add "menus/tasklist/tasklist.png"
        #if session == 0:
        #    if s0_state > 0:
        #        $ temp_taskcolor = If(tasks_state[session][0] == 0, "#eee", If(tasks_state[session][0] == 1, "#0b0", "#e00"))
        #        frame:
        #            xpos 230
        #            ypos 24+0*65+65*3
        #            xsize 40
        #            ysize 40
        #            background "#eee"
        #            add If(tasks_state[session][0] == 1, "tasks/check.png", If(tasks_state[session][0] == -1, "tasks/cross.png", None)) xsize 70 ysize 70 xalign 0.5 yalign 0.5
        #        text tasks_description[session][0] xoffset 300 yoffset 22+0*65+65*3 color temp_taskcolor size 40
        #    if s0_state > 1:
        #        $ temp_taskcolor = If(tasks_state[session][1] == 0, "#eee", If(tasks_state[session][1] == 1, "#0b0", "#e00"))
        #        frame:
        #            xpos 230
        #            ypos 24+1*65+65*3
        #            xsize 40
        #            ysize 40
        #            background "#eee"
        #            add If(tasks_state[session][1] == 1, "tasks/check.png", If(tasks_state[session][1] == -1, "tasks/cross.png", None)) xsize 70 ysize 70 xalign 0.5 yalign 0.5
        #        text tasks_description[session][1] xoffset 300 yoffset 22+1*65+65*3 color temp_taskcolor size 40
        #    if s0_state > 3:
        #        $ temp_taskcolor = If(tasks_state[session][2] == 0, "#eee", If(tasks_state[session][2] == 1, "#0b0", "#e00"))
        #        frame:
        #            xpos 230
        #            ypos 24+2*65+65*3
        #            xsize 40
        #            ysize 40
        #            background "#eee"
        #            add If(tasks_state[session][2] == 1, "tasks/check.png", If(tasks_state[session][2] == -1, "tasks/cross.png", None)) xsize 70 ysize 70 xalign 0.5 yalign 0.5
        #        text tasks_description[session][2] xoffset 300 yoffset 22+2*65+65*3 color temp_taskcolor size 40
        $ pos_i = -1
        for i in range (0, len(tasks_state[session])):
            if tasks_discovered[session][i]:
                $ pos_i += 1
                $ temp_taskcolor = If(tasks_state[session][i] == -1 or tasks_state[session][i] == 1, "#555", If(tasks_state[session][i] == 2, "#0be", If(((i+1) % 4 == 0) or (session == 0 and i == 1), "#eb0", "#eee")))
                #$ temp_taskcolor = If(tasks_state[session][i] == 0, "#eee", If(tasks_state[session][i] == 1, "#0b0", If(tasks_state[session][i] == -1, "#e00", "#0be")))
                frame:
                    xpos 230
                    ypos 24+pos_i*65+65*3
                    xsize 40
                    ysize 40
                    background "#eee"
                    add If(tasks_state[session][i] == 1, "tasks/check.png", If(tasks_state[session][i] == -1, "tasks/cross.png", None)) xsize 70 ysize 70 xalign 0.5 yalign 0.5
                text tasks_description[session][i] xoffset 300 yoffset 22+pos_i*65+65*3 color temp_taskcolor size 40
        imagebutton:
            xalign 0.9 yalign 0.1
            idle im.Scale("x_idle.png", 75, 75)
            hover im.Scale("x_hover.png", 75, 75)
            action [SetVariable("show_tasklist_UI", not show_tasklist_UI), SetVariable("activeMenu", not show_tasklist_UI)]
            focus_mask True
    if show_maplist_UI:
        button:
            xsize 1920
            ysize 1080
            action NullAction()
        add "menus/maplist/maplist_"+str(mapfloor)+".png"
        if floor == mapfloor:
            add "menus/maplist/here"+str(current_room)+".png" ypos -1
        textbutton "1":
            ypos 900-20
            xpos 200+1350-50
            text_color If(mapfloor == 1, "#fefe00", "#eee")
            text_hover_color "#fefe00"
            text_size 50+20
            action SetVariable("mapfloor", 1)
        textbutton "2":
            ypos 900-20
            xpos 260+1350-30
            text_color If(mapfloor == 2, "#fefe00", "#eee")
            text_hover_color "#fefe00"
            text_size 50+20
            action SetVariable("mapfloor", 2)
        textbutton "3":
            ypos 900-20
            xpos 320+1350-10
            text_color If(mapfloor == 3, "#fefe00", "#eee")
            text_hover_color "#fefe00"
            text_size 50+20
            action SetVariable("mapfloor", 3)
        frame:
            xsize 3
            ysize 60
            background "#eee"
            ypos 915-20
            xpos 251+1350+5-40
        frame:
            xsize 3
            ysize 60
            background "#eee"
            ypos 915-20
            xpos 311+1350+5-20
        imagebutton:
            xalign 0.9 yalign 0.1
            idle im.Scale("x_idle.png", 75, 75)
            hover im.Scale("x_hover.png", 75, 75)
            action [SetVariable("show_maplist_UI", not show_maplist_UI), SetVariable("activeMenu", not show_maplist_UI)]
            focus_mask True
    if show_studentlist_UI:
        button:
            xsize 1920
            ysize 1080
            action NullAction()
        add "menus/studentlist/studentlist.png"
        $ carmen_text = "É alegre e tem um talento especial para cantar. Canta no coro da escola e tem um grupo de fãs. É amiga do seu amigo e não gosta de injustiças. É amiga da Patrícia (9º B) desde criança, mas não gosta da Tatiana (9º B). Os seus pais são muito protetores. Acha que não a vão deixar ir para o Algarve se for esse o destino da viagem de finalistas."
        $ estrela_text = "É responsável. É delegada da turma e está a organizar a viagem de finalistas. Dedica muito tempo à escola e defende sempre os colegas que, no geral, gostam dela. A sua melhor amiga é a Isabel. A Cármen tem implicado com a Estrela por causa do destino da viagem de finalistas. A Estrela normalmente ignora."
        $ helder_text = "É muito popular na escola. Gosta de falar com todas as pessoas e é o diretor da Secção de Solidariedade da Associação de Estudantes. Tem espírito de missionário. Não gosta de intrigas e quando vê alguém a falar mal de outra pessoa, fica agressivo. Na visão dele, só o faz para defender quem ele considera serem os mais fracos da escola."
        $ isabel_text = "É muito extrovertida e popular. Tem algumas dificuldades na escola porque não se consegue concentrar nos estudos. Gosta de estar com os amigos e de viajar. Sempre quis ir ao Algarve com a sua melhor amiga, a Estrela, mas os pais até agora nunca a deixaram. Os seus outros amigos incluem o Samuel e o Hélder e a Tatiana (9º B)."
        $ jorge_text = "Tem muitas dificuldades com os estudos. Apesar de não ter muitos amigos, tem um grupo que o apoia: o Samuel e também o Abel e o Rui (9º B). O Jorge é defensor dos amigos e normalmente apoia as suas decisões. Sabe que o Abel (9º B) não gosta do Hélder, por isso também nunca engraçou muito com ele."
        $ samuel_text = "É muito inteligente, mas pouco popular na escola. Gosta de jogar videojogos e de estar sozinho. Por vezes, é gozado pelos colegas por gostar de estar sozinho a estudar na biblioteca, o que o leva a ter poucos amigos. Tem um fraquinho pela Tatiana do 9º B, mas não sabe como se poderá aproximar dela."
        if session == 0:
            $ carmen_text = "Não tenho informações sobre a Cármen."
            $ estrela_text = "A Estrela faltou à primeira aula."
            $ helder_text = "Não tenho informações sobre o Hélder."
            $ isabel_text = "Não tenho informações sobre a Isabel."
            $ jorge_text = "Não tenho informações sobre o Jorge."
            $ samuel_text = "Não tenho informações sobre o Samuel."
        button:
            xpos 236
            ypos 243
            xsize 250
            ysize 250
            hovered SetVariable("show_hist_c", True)
            unhovered SetVariable("show_hist_c", False)
            action SetVariable("show_hist_c", True)
        if show_hist_c:
            frame:
                xsize 700
                xpos 331
                ypos 238+5+320
                text carmen_text text_align 0.5
        button:
            xpos 236+320
            ypos 243
            xsize 250
            ysize 250
            hovered SetVariable("show_hist_e", True)
            unhovered SetVariable("show_hist_e", False)
            action SetVariable("show_hist_e", True)
        if show_hist_e:
            frame:
                xsize 700
                xpos 331
                ypos 238+5+320
                text estrela_text text_align 0.5
        button:
            xpos 236+320+320
            ypos 243
            xsize 250
            ysize 250
            hovered SetVariable("show_hist_h", True)
            unhovered SetVariable("show_hist_h", False)
            action SetVariable("show_hist_h", True)
        if show_hist_h:
            frame:
                xsize 700
                xpos 331
                ypos 238+5+320
                text helder_text text_align 0.5
        button:
            xpos 236
            ypos 243+350
            xsize 250
            ysize 250
            hovered SetVariable("show_hist_i", True)
            unhovered SetVariable("show_hist_i", False)
            action SetVariable("show_hist_i", True)
        if show_hist_i:
            frame:
                xsize 700
                xpos 331
                ypos 210
                text isabel_text text_align 0.5
        button:
            xpos 236+320
            ypos 243+350
            xsize 250
            ysize 250
            hovered SetVariable("show_hist_j", True)
            unhovered SetVariable("show_hist_j", False)
            action SetVariable("show_hist_j", True)
        if show_hist_j:
            frame:
                xsize 700
                xpos 331
                ypos 210
                text jorge_text text_align 0.5
        button:
            xpos 236+320+320
            ypos 243+350
            xsize 250
            ysize 250
            hovered SetVariable("show_hist_s", True)
            unhovered SetVariable("show_hist_s", False)
            action SetVariable("show_hist_s", True)
        if show_hist_s:
            frame:
                xsize 700
                xpos 331
                ypos 210
                text samuel_text text_align 0.5
        imagebutton:
            xalign 0.596 yalign 0.1
            idle im.Scale("x_idle.png", 75, 75)
            hover im.Scale("x_hover.png", 75, 75)
            action [SetVariable("show_studentlist_UI", not show_studentlist_UI), SetVariable("activeMenu", not show_studentlist_UI)]
            focus_mask True


screen clock_UI:
    add "tasks/clock/clock"+str(hours)+"_"+str(fakeminutes)+".png" xalign 0.995 yalign 0.01 xsize 150 ysize 150
    zorder 70

screen feedbacklist:
    button:
        xsize 1920
        ysize 1080
        action NullAction()
    frame:
        xpos 181
        ypos 100
        xsize 1558
        ysize 779
        background "#000"
    grid 2 1:
        area (186, 105, 1224, 120)
        frame:
            background "#999"
            xsize 612
            ysize 120
            text "Reflexão" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
        frame:
            background "#999"
            xsize 918+18
            ysize 120
            text "Feedback" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
    vpgrid:
        area (186, 225, 1548, 650)
        cols 3
        draggable False
        mousewheel True

        scrollbars "vertical"

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.5

        if session == 0:
            frame:
                background "#bbb"
                xsize 612
                ysize 120
                text "Tarefas" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
            frame:
                background "#bbb"
                xsize 918
                ysize 120
                text "" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
            frame:
                xsize 0
                background "#bbb"

            frame:
                background "#eee"
                xsize 612
                ysize 130
                text tasks_description[0][2] yalign 0.5 size 26 italic 1 color "#111" xalign 0.5 text_align 0.5
            frame:
                background "#eee"
                xsize 918
                ysize 130
                text tasks_feedback[0][If(tasks_state[session][2] == 1, 2*0, 2*0 + 1)] yalign 0.5 size 23 bold 1 color If(tasks_state[session][2] == 1, "#0b0", "#e00") text_align 0.5 xalign 0.5
            frame:
                xsize 0
                background "#bbb"
        else:
            if tasks_state[session][2] != 0 or tasks_state[session][6] != 0 or tasks_state[session][10] != 0:
                frame:
                    background "#bbb"
                    xsize 612
                    ysize 120
                    text "Tarefas" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
                frame:
                    background "#bbb"
                    xsize 918
                    ysize 120
                    text "" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
                frame:
                    xsize 0
                    background "#bbb"

                $ pos_i = 3
                for i in range (2, -1, -1):#(tasks_state[session][2]**2+tasks_state[session][6]**2+tasks_state[session][10]**2 - 1, -1, -1):
                    if tasks_state[session][2+4*i] != 2:
                        $ pos_i -= 1
                        frame:
                            if pos_i % 2 == 0:
                                background "#eee"
                            else:
                                background "#fff"
                            xsize 612
                            ysize 130
                            text tasks_description[session][2+4*i] yalign 0.5 size 26 italic 1 color "#111" xalign 0.5 text_align 0.5
                        frame:
                            if pos_i % 2 == 0:
                                background "#eee"
                            else:
                                background "#fff"
                            xsize 918
                            ysize 130
                            text tasks_feedback[session][If(tasks_state[session][2+4*i] == 1, 2*i, 2*i + 1)] yalign 0.5 size 23 bold 1 color If(tasks_state[session][2+4*i] == 1, "#0b0", "#e00") text_align 0.5 xalign 0.5
                        frame:
                            xsize 0
                            background "#bbb"

        if session == 0:
            $ len_drag = 3
            frame:
                background "#bbb"
                xsize 612
                ysize 120
                text "Inquérito" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
            frame:
                background "#bbb"
                xsize 918
                ysize 120
                text "" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
            frame:
                xsize 0
                background "#bbb"

            for i in range (len_drag - 1, -1, -1):
                frame:
                    if i % 2 == 0:
                        background "#eee"
                    else:
                        background "#fff"
                    xsize 612
                    ysize 120
                    text "\""+drag_options[i]+"\"" yalign 0.5 size 26 italic 1 color "#111" xalign 0.5 text_align 0.5
                frame:
                    if i % 2 == 0:
                        background "#eee"
                    else:
                        background "#fff"
                    xsize 918
                    ysize 120
                    text drag_feedback[i][0] yalign 0.5 size If(drag_feedback[i][0][:4] == "Numa", 21.5, 23) bold 1 color drag_feedback[i][1] text_align 0.5 xalign 0.5
                frame:
                    xsize 0
                    background "#bbb"
        else:
            for j in range ((situation / 10) - 1 - (session-1)*3, -1, -1):
                $ len_drag = len(drag_feedback[j])
                frame:
                    background "#bbb"
                    xsize 612
                    ysize 120
                    text "Situação "+str(j+1) yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
                frame:
                    background "#bbb"
                    xsize 918
                    ysize 120
                    text "" yalign 0.5 size 35 xalign 0.5 bold 1 color "#111" text_align 0.5
                frame:
                    xsize 0
                    background "#bbb"
                if len_drag - 1 == -1:
                    frame:
                        background "#eee"
                        xsize 612
                        ysize 120
                        text "----------" yalign 0.5 size 28 color "#111" xalign 0.5 text_align 0.5
                    frame:
                        background "#eee"
                        xsize 918
                        ysize 120
                        text "----------" yalign 0.5 size 28 color "#111" xalign 0.5 text_align 0.5
                    frame:
                        xsize 0
                        background "#bbb"
                else:
                    for i in range (len_drag - 1, -1, -1):
                        frame:
                            if i % 2 == 0:
                                background "#eee"
                            else:
                                background "#fff"
                            xsize 612
                            ysize 120
                            text "\""+drag_options[j][i]+"\"" yalign 0.5 size 26 italic 1 color "#111" xalign 0.5 text_align 0.5
                        frame:
                            if i % 2 == 0:
                                background "#eee"
                            else:
                                background "#fff"
                            xsize 918
                            ysize 120
                            text drag_feedback[j][i][0] yalign 0.5 size If(drag_feedback[j][i][0][:4] == "Numa", 21.5, 23) bold 1 color drag_feedback[j][i][1] text_align 0.5 xalign 0.5
                        frame:
                            xsize 0
                            background "#bbb"
    frame:
        xpos 186+612-1
        ypos 105
        xsize 2
        ysize 770
        background "#000"
    frame:
        xpos 186
        ypos 224
        xsize 1548
        ysize 2
        background "#000"

    imagebutton:
        xpos 1666
        ypos 98
        idle im.Scale("x_idle.png", 75, 75)
        hover im.Scale("x_hover.png", 75, 75)
        action If(intervalo != 3, Jump("leave_conversation"), Jump("end_session_checker"))#[Show("clock_UI"), Show("menulist"), SetVariable("show_tasklist_UI", False), SetVariable("show_maplist_UI", False), SetVariable("show_studentlist_UI", False),
         #SetVariable("show_feedbacklist_UI", not show_feedbacklist_UI), SetVariable("feedbackNew", False), SetVariable("activeMenu", not show_feedbacklist_UI), If(session == 0, (SetVariable("s0_state", 12), Jump("room_18")))]
        focus_mask True

default show_hist_c = False
default show_hist_e = False
default show_hist_h = False
default show_hist_i = False
default show_hist_j = False
default show_hist_s = False

default show_hist_a = False
default show_hist_m = False
default show_hist_n = False
default show_hist_p = False
default show_hist_r = False
default show_hist_t = False

# BACKUP
#
#for i in range (0, If(tasks_discovered[session][2], 4 + intervalo*4, 4 + intervalo*4 - 1)):
#    $ temp_taskcolor = If(tasks_state[session][i] == 0, "#eee", If(tasks_state[session][i] == 1, "#0b0", "#e00"))
#    frame:
#        xpos 230
#        ypos 24+i*65+65*3
#        xsize 40
#        ysize 40
#        background "#eee"
#        add If(tasks_state[session][i] == 1, "tasks/check.png", If(tasks_state[session][i] == -1, "tasks/cross.png", None)) xsize 70 ysize 70 xalign 0.5 yalign 0.5
#    #text If(tasks_discovered[session][i], tasks_description[session][i], tasks_description[0][0]) xoffset 300 yoffset 22+i*65+65*3 color temp_taskcolor size 40
#    if i != 11:
#        text If(tasks_discovered[session][i], tasks_description[session][i], tasks_description[session][i+1]) xoffset 300 yoffset 22+i*65+65*3 color temp_taskcolor size 40
#    else:
#        text tasks_description[session][i] xoffset 300 yoffset 22+i*65+65*3 color temp_taskcolor size 40
#if session == 1:
#if tasks_discovered[session][2]:
#    if tasks_state[session][2] == 0:
#        frame:
#            xpos 1550
#            ypos 20+5*65
#            xsize 220-45
#            ysize 50
#            background "#eee"
#            textbutton "Concluir":
#                xsize 212-45
#                ysize 42
#                background "#000"
#                xalign 0.5
#                yalign 0.5
#                text_bold 1
#                text_color "#eee"
#                text_hover_color "#fefe00"
#                action Jump("task"+str(session*12-12+5))
#if tasks_discovered[session][6]:
#    if tasks_state[session][6] == 0 and intervalo > 0:
#        frame:
#            xpos 1550
#            ypos 20+9*65
#            xsize 220-45
#            ysize 50
#            background "#eee"
#            textbutton "Concluir":
#                xsize 212-45
#                ysize 42
#                background "#000"
#                xalign 0.5
#                yalign 0.5
#                text_bold 1
#                text_color "#eee"
#                text_hover_color "#fefe00"
#                action Jump("task"+str(session*12-12+9))
#if tasks_discovered[session][10]:
#    if tasks_state[session][10] == 0 and intervalo > 1:
#        frame:
#            xpos 1550
#            ypos 20+13*65
#            xsize 220-45
#            ysize 50
#            background "#eee"
#            textbutton "Concluir":
#                xsize 212-45
#                ysize 42
#                background "#000"
#                xalign 0.5
#                yalign 0.5
#                text_bold 1
#                text_color "#eee"
#                text_hover_color "#fefe00"
#                action Jump("task"+str(session*12-12+13))
