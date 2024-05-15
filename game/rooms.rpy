screen ending:
    frame:
        xsize 1100
        xalign 0.5
        yalign 0.9
        image im.Scale("progress.png", 1088, 50)
    frame:
        background "#333"
        xpos (416+1088-int((29-pro_social)*(37.51724138)))
        xsize If((29-pro_social)*(37.51724138) >= 0.5, int((29-pro_social)*(37.51724138))+1, int((29-pro_social)*(37.51724138)))#510
        ysize 50
        ypos 922
    frame:
        xalign 0.5
        xsize 1100
        yalign 0.99
        text final_eval xalign 0.5 #color final_eval_color
    #imagebutton:
    #    xalign 0.99 yalign 0.99 at rot(-90)
    #    idle im.Scale("arrow_idle.png", 100, 100, bilinear=True)
    #    hover im.Scale("arrow_hover.png", 100, 100, bilinear=True)
    #    action Jump("start_session_checker")
    #    focus_mask True

default tooltiper = False
default tooltiperT = False
default tootliperTdesc = ""

screen room_0:#escadas_0
    # tutorial
    if s0_state == 5 or s0_state == 6:
        imagebutton:
            xalign -0.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_s0_3_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_s0_3_hover.png", 1300, 815)
            action If(activeMenu, None, Jump("session_0.chat_3"))
            focus_mask True
    # saida entrada_8
    imagebutton:
        xalign 0.5 yalign 0.99
        if (last_room == 8):
            idle im.Scale("exit_idle_last.png", 100, 100)
        else:
            idle im.Scale("exit_idle.png", 100, 100)
        hover im.Scale("exit_hover.png", 100, 100)
        hovered [SetVariable("tooltiperDesc", "Pátio"), Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_8")])
        focus_mask True
    # saida escadas_1
    imagebutton:
        xalign 0.99 yalign 0.5 at rot(-90)
        if (last_room == 1):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+10), SetVariable("seconds", seconds+10), Jump("room_1")])
        focus_mask True
    # saida escadas_2
    imagebutton:
        xalign 0.5 yalign 0.1 at rot(45+90)
        if (last_room == 2):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_2")])
        focus_mask True
    # saida biblioteca_9
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/escadas_0_saida_biblioteca_9_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/escadas_0_saida_biblioteca_9_hover.png", 1920, 1080)
        hovered [SetVariable("tooltiperDesc", "Biblioteca"), Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_9")])
        focus_mask True

    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring == 99:
        imagebutton:
            xalign -0.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_cb")])
            focus_mask True
        image "chats/bubble01.png":
            xsize 1300
            ysize 815
            xalign -0.2+0.25
            yalign 1.0-1.4
            xzoom 1

    elif chat_occuring != -1:
        imagebutton:
            xalign 1.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [#If(intervalo == 0, SetDict(chats_i0, chat_occuring, -1), None),
             #If(intervalo == 1, SetDict(chats_i1, chat_occuring, -1), None),
             #If(intervalo == 2, SetDict(chats_i2, chat_occuring, -1), None),
             #If(intervalo == 3, SetDict(chats_i3, chat_occuring, -1), None),
             SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 1.2+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    if session == 1 and intervalo == 0 and chats_in_rooms[0] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 0, -1), SetDict(chats_in_rooms, 1, -1), Jump("session_1_dialogues_i0.chat_i0_cb")]
    if session == 2 and intervalo == 0 and chats_in_rooms[0] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 0, -1), SetDict(chats_in_rooms, 1, -1), Jump("session_2_dialogues_i0.chat_i0_cb")]
    if session == 3 and intervalo == 0 and chats_in_rooms[0] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 0, -1), SetDict(chats_in_rooms, 1, -1), Jump("session_3_dialogues_i0.chat_i0_cb")]
    if session == 4 and intervalo == 0 and chats_in_rooms[0] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 0, -1), SetDict(chats_in_rooms, 1, -1), Jump("session_4_dialogues_i0.chat_i0_cb")]

    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text tooltiperDesc

screen room_1:#escadas_1
    # saida entrada_8
    imagebutton:
        xalign 0.5 yalign 0.99
        if (last_room == 8):
            idle im.Scale("exit_idle_last.png", 100, 100)
        else:
            idle im.Scale("exit_idle.png", 100, 100)
        hover im.Scale("exit_hover.png", 100, 100)
        hovered [SetVariable("tooltiperDesc", "Pátio"), Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_8")])
        focus_mask True
    # saida escadas_0
    imagebutton:
        xalign 0.01 yalign 0.5 at rot(90)
        if (last_room == 0):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+10), SetVariable("seconds", seconds+10), Jump("room_0")])
        focus_mask True
    # saida escadas_7
    imagebutton:
        xalign 0.5 yalign 0.1 at rot(-45-90)
        if (last_room == 7):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_7")])
        focus_mask True
    # saida art_10
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/escadas_1_saida_art_10_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/escadas_1_saida_art_10_hover.png", 1920, 1080)
        hovered [SetVariable("tooltiperDesc", "Sala Polivalente"), Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_10")])
        focus_mask True

    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring == 99:
        imagebutton:
            xalign -0.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_cb")])
            focus_mask True
        image "chats/bubble01.png":
            xsize 1300
            ysize 815
            xalign -0.2+0.25
            yalign 1.0-1.4
            xzoom 1

    elif chat_occuring != -1:
        imagebutton:
            xalign -0.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign -0.2+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    if session == 1 and intervalo == 0 and chats_in_rooms[1] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 0, -1), SetDict(chats_in_rooms, 1, -1), Jump("session_1_dialogues_i0.chat_i0_cb")]
    if session == 2 and intervalo == 0 and chats_in_rooms[1] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 0, -1), SetDict(chats_in_rooms, 1, -1), Jump("session_2_dialogues_i0.chat_i0_cb")]
    if session == 3 and intervalo == 0 and chats_in_rooms[1] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 0, -1), SetDict(chats_in_rooms, 1, -1), Jump("session_3_dialogues_i0.chat_i0_cb")]
    if session == 4 and intervalo == 0 and chats_in_rooms[1] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 0, -1), SetDict(chats_in_rooms, 1, -1), Jump("session_4_dialogues_i0.chat_i0_cb")]

    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text tooltiperDesc

screen room_2:#escadas_2
    # tutorial
    if s0_state == 3 or s0_state == 3.2:
        imagebutton:
            xalign 0.8 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_s0_11_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_s0_11_hover.png", 1300, 815)
            action If(activeMenu, None, Jump("session_0.chat_11"))
            focus_mask True
    # saida escadas_0
    imagebutton:
        xalign 0.1 yalign 0.7
        if (last_room == 0):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_0")])
        focus_mask True
    # saida corredor_3
    imagebutton:
        xalign 0.99 yalign 0.5 at rot(-90)
        if (last_room == 3):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_3")])
        focus_mask True
    # saida escadas_11
    imagebutton:
        xalign 0.5 yalign 0.1 at rot(45+90)
        if (last_room == 11):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_11")])
        focus_mask True

    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring == 99:
        imagebutton:
            xalign 0.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_cb")])
            focus_mask True
    elif chat_occuring != -1:
        imagebutton:
            xalign 0.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 0.2+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]


screen room_3:#corredor_3
    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring == 99:
        imagebutton:
            xalign 0.99 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_cb")])
            focus_mask True
    elif chat_occuring != -1:
        imagebutton:
            xalign 0.99 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 0.99+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    # saida escadas_2
    imagebutton:
        xalign 0.01 yalign 0.5 at rot(90)
        if (last_room == 2):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_2")])
        focus_mask True
    # saida sala_4
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/corredor_3_saida_sala_4_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/corredor_3_saida_sala_4_hover.png", 1920, 1080)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_4")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text "Sala de Aula A"
    # saida corredor_5
    imagebutton:
        xalign 0.99 yalign 0.5 at rot(-90)
        if (last_room == 5):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+10), SetVariable("seconds", seconds+10), Jump("room_5")])
        focus_mask True

screen room_4:#sala_4
    # saida corredor_3
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/sala_4_saida_corredor_3_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/sala_4_saida_corredor_3_hover.png", 1920, 1080)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_3")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text "Corredor Oeste"

    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring == 99:
        imagebutton:
            xalign 0.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_cb")])
            focus_mask True
    elif chat_occuring != -1:
        imagebutton:
            xalign -0.3 yalign -0.6
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1652*1.4, 1036*1.4)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1652*1.4, 1036*1.4)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize int(1652*1.4)
            ysize int(1036*1.4)
            xalign -0.3-chats_positions[session-1][intervalo][chat_occuring][0]*1.4
            yalign -0.6-chats_positions[session-1][intervalo][chat_occuring][1]*1.3
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    ## saida corredor_3
    #imagebutton:
    #    xalign 0.5 yalign 0.99
    #    idle im.Scale("exit_idle.png", 100, 100)
    #    hover im.Scale("exit_hover.png", 100, 100)
    #    action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_3")])
    #    focus_mask True

    # tutorial
    if session == 0:
        if intervalo == 0:
            if tasks_state[session][1] == 0 and s0_state >= 3 and s0_state < 4:
                imagebutton:
                    idle im.Scale("tasks/task1i.png", 1920, 1080)
                    hover im.Scale("tasks/task1h.png", 1920, 1080)
                    action If(activeMenu, None, Jump("task1"))
                    focus_mask True
    # tasks
    if session == 1:
        if tasks_state[session][3] == 0:
                imagebutton:
                    idle im.Scale("tasks/task6i.png", 1920, 1080)
                    hover im.Scale("tasks/task6h.png", 1920, 1080)
                    action If(activeMenu, None, Jump("task6"))
                    focus_mask True
        if tasks_state[session][1] == 0:
                imagebutton:
                    xalign 0.27 yalign 0.564
                    idle im.Flip(im.Scale("tasks/task4i.png", 215/2.4, 720/2.4), True)
                    hover im.Flip(im.Scale("tasks/task4h.png", 215/1.92, 720/1.92), True)
                    hovered [SetVariable("tooltiperTdesc", "Escrever recado"), Function(get_mouse), SetVariable("tooltiperT", True)]
                    unhovered SetVariable("tooltiperT", False)
                    action If(activeMenu, None, Jump("task4"))
                    focus_mask True
                if tooltiperT:
                    timer 0.03 repeat tooltiperT action Function(get_mouse)
                    frame:
                        xpos mouse_xy[0] ypos mouse_xy[1]-50
                        text tooltiperTdesc
    if session == 2:
        if tasks_state[session][3] == 0:
                imagebutton:
                    idle im.Scale("tasks/task18i.png", 1920, 1080)
                    hover im.Scale("tasks/task18h.png", 1920, 1080)
                    action If(activeMenu, None, Jump("task18"))
                    focus_mask True
    if session == 3:
        if tasks_state[session][3] == 0:
                imagebutton:
                    idle im.Scale("tasks/task30i.png", 1920, 1080)
                    hover im.Scale("tasks/task30h.png", 1920, 1080)
                    action If(activeMenu, None, Jump("task30"))
                    focus_mask True
    if session == 4:
        if tasks_state[session][3] == 0:
                imagebutton:
                    idle im.Scale("tasks/task42i.png", 1920, 1080)
                    hover im.Scale("tasks/task42h.png", 1920, 1080)
                    action If(activeMenu, None, Jump("task42"))
                    focus_mask True

    if s0_state >= 3 and s0_state <= 4:
        timer If(last_room == 3, 2.25, 10) action Jump("session_0.skip_aula")

screen room_5:#corredor_5
    # tutorial
    if s0_state == 3 or s0_state == 3.1:
        imagebutton:
            xalign 0.01 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_s0_12_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_s0_12_hover.png", 1300, 815)
            action If(activeMenu, None, Jump("session_0.chat_12"))
            focus_mask True
    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring == 99:
        imagebutton:
            xalign 0.01 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_cb")])
            focus_mask True
    elif chat_occuring != -1:
        imagebutton:
            xalign 0.01 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 0.01+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    # saida escadas_7
    imagebutton:
        xalign 0.99 yalign 0.5 at rot(-90)
        if (last_room == 7):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_7")])
        focus_mask True
    # saida sala_6
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/corredor_5_saida_sala_6_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/corredor_5_saida_sala_6_hover.png", 1920, 1080)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_6")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text "Sala de Aula B"
    # saida corredor_3
    imagebutton:
        xalign 0.01 yalign 0.5 at rot(90)
        if (last_room == 3):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+10), SetVariable("seconds", seconds+10), Jump("room_3")])
        focus_mask True

screen room_6:#sala_6
    # saida corredor_5
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/sala_6_saida_corredor_5_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/sala_6_saida_corredor_5_hover.png", 1920, 1080)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_5")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0]-240 ypos mouse_xy[1]-50
            text "Corredor Este"


    ## saida corredor_5
    #imagebutton:
    #    xalign 0.5 yalign 0.99
    #    idle im.Scale("exit_idle.png", 100, 100)
    #    hover im.Scale("exit_hover.png", 100, 100)
    #    action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_5")])
    #    focus_mask True

    # tasks
    if session == 1:
        if tasks_state[session][7] == 0 and intervalo == 1:
            imagebutton:
                idle im.Scale("tasks/task10i.png", 1920, 1080)
                hover im.Scale("tasks/task10h.png", 1920, 1080)
                action If(activeMenu, None, Jump("task10"))
                focus_mask True
        if tasks_discovered[session][5] and tasks_state[session][5] == 0 and intervalo == 1:
            imagebutton:
                xalign 0.79 yalign 0.55
                idle im.Flip(im.Scale("tasks/task8i.png", 215/2.4, 720/2.4), True)
                hover im.Flip(im.Scale("tasks/task8h.png", 215/1.92, 720/1.92), True)
                hovered [SetVariable("tooltiperTdesc", "Ajudar aluno"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task8"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
    if session == 2:
        if tasks_state[session][7] == 0 and intervalo == 1:
            imagebutton:
                idle im.Scale("tasks/task22i.png", 1920, 1080)
                hover im.Scale("tasks/task22h.png", 1920, 1080)
                action If(activeMenu, None, Jump("task22"))
                focus_mask True
        if tasks_discovered[session][5] and tasks_state[session][5] == 0 and intervalo == 1:
            imagebutton:
                xalign 0.79 yalign 0.55
                idle im.Flip(im.Scale("tasks/task20i.png", 215/2.4, 720/2.4), True)
                hover im.Flip(im.Scale("tasks/task20h.png", 215/1.92, 720/1.92), True)
                hovered [SetVariable("tooltiperTdesc", "Tirar dúvida"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task20"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
    if session == 3:
        if tasks_discovered[session][5] and tasks_state[session][5] == 0 and intervalo == 1:
            imagebutton:
                xalign 0.79 yalign 0.55
                idle im.Flip(im.Scale("tasks/task32i.png", 215/2.4, 720/2.4), True)
                hover im.Flip(im.Scale("tasks/task32h.png", 215/1.92, 720/1.92), True)
                hovered [SetVariable("tooltiperTdesc", "Tirar dúvida"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task32"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][7] == 0 and intervalo == 1:
            imagebutton:
                idle im.Scale("tasks/task34i.png", 1920, 1080)
                hover im.Scale("tasks/task34h.png", 1920, 1080)
                action If(activeMenu, None, Jump("task34"))
                focus_mask True
    if session == 4:
        if tasks_state[session][1] == 0 and intervalo == 0:
            imagebutton:
                xalign 0.79 yalign 0.55
                idle im.Flip(im.Scale("tasks/task40i.png", 215/2.4, 720/2.4), True)
                hover im.Flip(im.Scale("tasks/task40h.png", 215/1.92, 720/1.92), True)
                hovered [SetVariable("tooltiperTdesc", "Tirar dúvidas"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task40"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][7] == 0 and intervalo == 1:
            imagebutton:
                idle im.Scale("tasks/task46i.png", 1920, 1080)
                hover im.Scale("tasks/task46h.png", 1920, 1080)
                action If(activeMenu, None, Jump("task46"))
                focus_mask True

    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring == 99:
        imagebutton:
            xalign 0.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_cb")])
            focus_mask True
    elif chat_occuring != -1:
        imagebutton:
            xalign 1.2 yalign -0.6
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1652*1.4, 1036*1.4)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1652*1.4, 1036*1.4)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize int(1652*1.4)
            ysize int(1036*1.4)
            xalign 1.2- chats_positions[session-1][intervalo][chat_occuring][0]*1.4
            yalign -0.6-chats_positions[session-1][intervalo][chat_occuring][1]*1.3
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

screen room_7:#escadas_7
    # tutorial
    if s0_state == 3 or s0_state == 3.2:
        imagebutton:
            xalign 0.8 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_s0_11_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_s0_11_hover.png", 1300, 815)
            action If(activeMenu, None, Jump("session_0.chat_11"))
            focus_mask True
    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring == 99:
        imagebutton:
            xalign 0.8 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_cb")])
            focus_mask True
    elif chat_occuring != -1:
        imagebutton:
            xalign 0.8 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 0.8+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    # saida escadas_1
    imagebutton:
        xalign 0.9 yalign 0.7
        if (last_room == 1):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_1")])
        focus_mask True
    # saida corredor_5
    imagebutton:
        xalign 0.01 yalign 0.5 at rot(90)
        if (last_room == 5):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_5")])
        focus_mask True
    # saida escadas_13
    imagebutton:
        xalign 0.5 yalign 0.1 at rot(-45-90)
        if (last_room == 13):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_13")])
        focus_mask True

default tooltiperDesc = ""

screen room_8:#entrada_8
    # saida escadas_0
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/entrada_8_saida_escadas_0_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/entrada_8_saida_escadas_0_hover.png", 1920, 1080)
        hovered [SetVariable("tooltiperDesc", "Entrada Oeste"), Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu or (chats_in_rooms[19] == 99), None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_0")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text tooltiperDesc
    # saida escadas_1
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/entrada_8_saida_escadas_1_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/entrada_8_saida_escadas_1_hover.png", 1920, 1080)
        hovered [SetVariable("tooltiperDesc", "Entrada Este"), Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu or (chats_in_rooms[19] == 99), None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_1")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text tooltiperDesc
    # saida pavilhao
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/saida_pavilhao_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/saida_pavilhao_hover.png", 1920, 1080)
        hovered [SetVariable("tooltiperDesc", "Traseiras"), Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action Jump("pavilhao")
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text tooltiperDesc
    # tasks
    if session == 1:
        if chats_in_rooms[19] != 99:
            if tasks_discovered[session][9] and tasks_state[session][9] == 0 and intervalo == 2:
                imagebutton:
                    xalign 0.54 yalign 0.45
                    idle im.Flip(im.Scale("tasks/task12.png", 215/3.5, 720/3.5), True)
                    hover im.Flip(im.Scale("tasks/task12.png", 215/2.8, 720/2.8), True)
                    hovered [SetVariable("tooltiperTdesc", "Comprar rifa"), Function(get_mouse), SetVariable("tooltiperT", True)]
                    unhovered SetVariable("tooltiperT", False)
                    action If(activeMenu, None, Jump("task12"))
                    focus_mask True
                if tooltiperT:
                    timer 0.03 repeat tooltiperT action Function(get_mouse)
                    frame:
                        xpos mouse_xy[0] ypos mouse_xy[1]-50
                        text tooltiperTdesc
    if session == 3:
        if tasks_state[session][1] == 0 and tasks_discovered[session][1]:
            imagebutton:
                xalign 0.54 yalign 0.45
                idle im.Flip(im.Scale("tasks/task28.png", 215/3.5, 720/3.5), True)
                hover im.Flip(im.Scale("tasks/task28.png", 215/2.8, 720/2.8), True)
                hovered [SetVariable("tooltiperTdesc", "Transportar material"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task28"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
    if session == 4:
        if tasks_state[session][5] == 0 and intervalo < 2:
            imagebutton:
                xalign 0.44 yalign 0.45
                idle im.Scale("tasks/task44.png", 215/3.5, 720/3.5)
                hover im.Scale("tasks/task44.png", 215/2.8, 720/2.8)
                hovered [SetVariable("tooltiperTdesc", "Afixar cartazes"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task44"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][9] == 0 and tasks_discovered[session][9]:
            imagebutton:
                xalign 0.54 yalign 0.45
                idle im.Flip(im.Scale("tasks/task48.png", 215/3.5, 720/3.5), True)
                hover im.Flip(im.Scale("tasks/task48.png", 215/2.8, 720/2.8), True)
                hovered [SetVariable("tooltiperTdesc", "Comprar rifa"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task48"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc

    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring != -1:
        imagebutton:
            xalign 0.95 yalign 0.5
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 600, 376)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 600, 376)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 600
            ysize 376
            xalign 0.95+chats_positions[session-1][intervalo][chat_occuring][0]/5.5
            yalign 0.5+chats_positions[session-1][intervalo][chat_occuring][1]/5.5
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]
    $ chat_occuring = chats_in_rooms[19]
    if chat_occuring == 99:
        imagebutton:
            xalign 0.16 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_cb_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, 19, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_cb")])
            focus_mask True
        image "chats/bubble01.png":
            xsize 1300
            ysize 815
            xalign 0.16-0.1
            yalign 1.0-1.5
            xzoom 1
    elif chat_occuring != -1:
        imagebutton:
            xalign -0.2 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, 19, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign -0.2+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]
    # tutorial
    if s0_state == 5 or s0_state == 7:
        imagebutton:
            xalign 0.16 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_s0_2_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_s0_2_hover.png", 1300, 815)
            action If(activeMenu, None, Jump("session_0.chat_2"))
            focus_mask True

    if session == 1 and intervalo == 2 and chats_in_rooms[19] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 19, -1), Jump("session_1_dialogues_i2.chat_i2_cb")]
    if session == 2 and intervalo == 2 and chats_in_rooms[19] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 19, -1), Jump("session_2_dialogues_i2.chat_i2_cb")]
    if session == 3 and intervalo == 2 and chats_in_rooms[19] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 19, -1), Jump("session_3_dialogues_i2.chat_i2_cb")]
    if session == 4 and intervalo == 2 and chats_in_rooms[19] == 99:
        timer If(last_room == 0, 0.25, 2.25) action [SetDict(chats_in_rooms, 19, -1), Jump("session_4_dialogues_i2.chat_i2_cb")]

label bibliotecaria:
    call set_scene(9, True)
    if session == 1 and tasks_state[session][4] == 0:
        player "Bom dia, por acaso podia-me dizer onde está a impressora?"
        bibliotecaria "Com certeza, professor. Ela está ao fundo do primeiro corredor de livros, ali à direita."
        player "Obrigado."
    else:
        player "Bom dia."
        bibliotecaria "Bom dia, professor."
    jump room_9

screen room_9:#biblioteca_9
    # tutorial
    if s0_state >= 5 and s0_state < 9:
        imagebutton:
            xalign 0.20 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_s0_4_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_s0_4_hover.png", 1300, 815)
            action If(activeMenu, None, Jump("session_0.chat_4"))
            focus_mask True

    # bibliotecaria
    if session != 0:
        imagebutton:
            xalign 0.34 yalign 0.503 at rot(2)
            idle im.Scale("bibliotecaria1.png", 1417/12, 2400/12)
            hover im.Scale("bibliotecaria.png", 1417/9.6, 2400/9.6)
            action If(activeMenu, None, Jump("bibliotecaria"))
            focus_mask True

    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring != -1:
        imagebutton:
            xalign 0.99 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 0.99+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    # saida escadas_1
    imagebutton:
        xalign 0.5 yalign 0.99
        if (last_room == 0):
            idle im.Scale("exit_idle_last.png", 100, 100)
        else:
            idle im.Scale("exit_idle.png", 100, 100)
        hover im.Scale("exit_hover.png", 100, 100)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_0")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text "Escadas Oeste"

    # tasks
    if session == 1:
        if tasks_state[session][4] == 0:
            imagebutton:
                xalign 0.84 yalign 0.5
                idle im.Scale("tasks/task7.png", 1352/9, 1352/9)
                hover im.Scale("tasks/task7.png", 1352/7.2, 1352/7.2)
                hovered [SetVariable("tooltiperTdesc", "Tirar fotocópias"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task7"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
    if session == 2:
        #if chats_in_rooms[19] != 99:
            if tasks_discovered[session][9] and tasks_state[session][9] == 0 and intervalo == 2:
                imagebutton:
                    #xalign 0.54 yalign 0.45
                    xalign 0.44 yalign 0.69
                    idle im.Flip(im.Scale("tasks/task24.png", 215/1.5, 720/1.5), True)
                    hover im.Flip(im.Scale("tasks/task24.png", 215/1.2, 720/1.2), True)
                    hovered [SetVariable("tooltiperTdesc", "Emprestar livro"), Function(get_mouse), SetVariable("tooltiperT", True)]
                    unhovered SetVariable("tooltiperT", False)
                    action If(activeMenu, None, Jump("task24"))
                    focus_mask True
                if tooltiperT:
                    timer 0.03 repeat tooltiperT action Function(get_mouse)
                    frame:
                        xpos mouse_xy[0] ypos mouse_xy[1]-50
                        text tooltiperTdesc
    if session == 3:
        if tasks_state[session][0] == 0:
            imagebutton:
                xalign 0.84 yalign 0.5
                idle im.Scale("tasks/task27.png", 1352/9, 1352/9)
                hover im.Scale("tasks/task27.png", 1352/7.2, 1352/7.2)
                hovered [SetVariable("tooltiperTdesc", "Imprimir lista"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task27"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
    if session == 4:
        if tasks_state[session][0] == 0:
            imagebutton:
                xalign 0.40 yalign 0.56
                idle im.Scale("tasks/task39.png", 800/10, 800/10)
                hover im.Scale("tasks/task39.png", 800/8, 800/8)
                hovered [SetVariable("tooltiperTdesc", "Buscar livro"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task39"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc

screen room_10:#art_10
    # saida escadas_11
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/art_10_saida_escadas_1_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/art_10_saida_escadas_1_hover.png", 1920, 1080)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_1")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text "Escadas Este"
    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring != -1:
        imagebutton:
            xalign 0.99 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 0.99+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    ## saida escadas_0
    #imagebutton:
    #    xalign 0.5 yalign 0.99
    #    idle im.Scale("exit_idle.png", 100, 100)
    #    hover im.Scale("exit_hover.png", 100, 100)
    #    action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_1")])
    #    focus_mask True

    if session == 2:
        if intervalo == 0:
            if tasks_state[session][1] == 0:
                imagebutton:
                    xpos 1200 ypos 400
                    idle im.Flip(im.Scale("tasks/task16.png", 215*1.5, 720*1.5), True)
                    hover im.Flip(im.Scale("tasks/task16.png", 215*1.8, 720*1.8), True)
                    hovered [SetVariable("tooltiperTdesc", "Ajudar alunos"), Function(get_mouse), SetVariable("tooltiperT", True)]
                    unhovered SetVariable("tooltiperT", False)
                    action If(activeMenu, None, Jump("task16"))
                    focus_mask True
                if tooltiperT:
                    timer 0.03 repeat tooltiperT action Function(get_mouse)
                    frame:
                        xpos mouse_xy[0] ypos mouse_xy[1]-50
                        text tooltiperTdesc
    if session == 3:
        if tasks_state[session][9] == 0 and tasks_discovered[session][9]:
            imagebutton:
                xpos 1200 ypos 400
                idle im.Flip(im.Scale("tasks/task36.png", 406*1.5, 972*1.5), True)
                hover im.Flip(im.Scale("tasks/task36.png", 406*1.8, 972*1.8), True)
                hovered [SetVariable("tooltiperTdesc", "Entregar materiais"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task36"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc

screen room_11:#escadas_11
    # saida reunioes_12
    imagebutton:
        idle im.Flip(im.Scale("rooms/"+daytime+"/saida_escadas_p3_idle.png", 1920, 1080), True)
        hover im.Flip(im.Scale("rooms/"+daytime+"/saida_escadas_p3_hover.png", 1920, 1080), True)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_12")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text "Gabinete de Trabalho"
    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring != -1:
        imagebutton:
            xalign 0.99 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 0.99+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    # saida escadas_2
    imagebutton:
        xalign 0.01 yalign 0.80 at rot(45)
        if (last_room == 2):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_2")])
        focus_mask True
    # saida corredor_13
    imagebutton:
        xalign 0.99 yalign 0.5 at rot(-90)
        if (last_room == 13):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_13")])
        focus_mask True

    if interj_prof:
        timer If(last_room == 13, 0.25, 2.25) action Jump("dialog_profs")

screen room_12:#gabinete_12
    # saida escadas_11
    imagebutton:
        xalign 0.5 yalign 0.99
        if (last_room == 11):
            idle im.Scale("exit_idle_last.png", 100, 100)
        else:
            idle im.Scale("exit_idle.png", 100, 100)
        hover im.Scale("exit_hover.png", 100, 100)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_11")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text "Corredor"

    # chats
    if session != 0 or s0_state > 1:
        imagebutton:
            xpos -200 ypos -162 at rot(1)
            idle im.Scale("prof_idle.png", 1300, 815)
            hover im.Scale("prof_hover.png", 1300, 815)
            action Jump("joao_dialogue")
            focus_mask True

    # tasks
    if session == 2:
        if tasks_state[session][8] == 0:
            imagebutton:
                xalign 0.83 ypos 200
                idle im.Scale("tasks/task23.png", 406/0.75, 972/0.75)
                hover im.Scale("tasks/task23.png", 406/0.6, 972/0.6)
                hovered [SetVariable("tooltiperTdesc", "Assinar documentos"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task23"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc

screen room_13:#escadas_13
    # saida professores_14
    imagebutton:
        idle im.Scale("rooms/"+daytime+"/saida_escadas_p3_idle.png", 1920, 1080)
        hover im.Scale("rooms/"+daytime+"/saida_escadas_p3_hover.png", 1920, 1080)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_14")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text "Sala de Professores"

    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring != -1:
        imagebutton:
            xalign 0.99 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 0.99+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]

    # saida escadas_11
    imagebutton:
        xalign 0.01 yalign 0.5 at rot(90)
        if (last_room == 11):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_11")])
        focus_mask True
    # saida escadas_7
    imagebutton:
        xalign 0.99 yalign 0.80 at rot(-45)
        if (last_room == 7):
            idle im.Scale("arrow_idle_last.png", 100, 100)
        else:
            idle im.Scale("arrow_idle.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_7")])
        focus_mask True

    if session == 0 and s0_state == 1:
        timer If(last_room == 11, 0.25, 2.25) action Jump("session_0.joao")
    if interj_prof:
        timer If(last_room == 11, 0.25, 2.25) action Jump("dialog_profs")

screen room_14:#professores_14
    # saida escadas_13
    imagebutton:
        xalign 0.5 yalign 0.99
        if (last_room == 13):
            idle im.Scale("exit_idle_last.png", 100, 100)
        else:
            idle im.Scale("exit_idle.png", 100, 100)
        hover im.Scale("exit_hover.png", 100, 100)
        hovered [Function(get_mouse), SetVariable("tooltiper", True)]
        unhovered SetVariable("tooltiper", False)
        action If(activeMenu, None, [SetVariable("movement_count", movement_count+7), SetVariable("seconds", seconds+7), Jump("room_13")])
        focus_mask True
    if tooltiper:
        timer 0.03 repeat tooltiper action Function(get_mouse)
        frame:
            xpos mouse_xy[0] ypos mouse_xy[1]-50
            text "Corredor"

    # chats
    $ chat_occuring = chats_in_rooms[current_room]
    if chat_occuring != -1:
        imagebutton:
            xalign 0.99 yalign 1.0
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_idle.png", 1300, 815)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chat_occuring)+"_hover.png", 1300, 815)
            action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chat_occuring))])
            focus_mask True
        image "chats/bubble0"+str(chats_positions[session-1][intervalo][chat_occuring][3])+".png":
            xsize 1300
            ysize 815
            xalign 0.99+chats_positions[session-1][intervalo][chat_occuring][0]
            yalign 1.0+chats_positions[session-1][intervalo][chat_occuring][1]
            xzoom chats_positions[session-1][intervalo][chat_occuring][2]
    # tutorial
    if session == 0:
        if intervalo == 0:
            if tasks_state[session][0] == 0:
                imagebutton:
                    xalign 0.52 yalign 0.75
                    idle im.Flip(im.Scale("tasks/task0.png", 800/5/1.1, 800/5/1.1), True)
                    hover im.Flip(im.Scale("tasks/task0.png", 800/4/1.1, 800/4/1.1), True)
                    action If(activeMenu, None, Jump("task0"))
                    focus_mask True
        if intervalo == 1:
            if tasks_discovered[0][2] and tasks_state[0][2] == 2:
                imagebutton:
                    xalign 0.39 yalign 0.74 at rot(18)
                    idle im.Scale("tasks/task2.png", 500/2.5, 500/2.5)
                    hover im.Scale("tasks/task2.png", 500/2, 500/2)
                    action If(activeMenu, None, Jump("task2"))
                    focus_mask True

    # tasks
    if session == 1:
        if tasks_state[session][0] == 0:
            imagebutton:
                xalign 0.34 yalign 0.66# at rot(-3)
                idle im.Flip(im.Scale("tasks/task3.png", 600/2.5/1.2, 525/2.5/1.2), True)
                hover im.Flip(im.Scale("tasks/task3.png", 600/2/1.2, 525/2/1.2), True)
                hovered [SetVariable("tooltiperTdesc", "Escrever e-mail"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task3"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][8] == 0:
            #add im.Scale("tasks/table.png", 1200/3, 511/1) xpos 1200 ypos 800
            imagebutton:
                #xalign 0.77 yalign 0.84
                xalign 0.83 yalign 0.6
                idle im.Scale("tasks/task11.png", 1200/4/2, 1200/4/2)
                hover im.Scale("tasks/task11.png", 1200/3.2/2, 1200/3.2/2)
                hovered [SetVariable("tooltiperTdesc", "Preparar atividade"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task11"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][11] == 0 and intervalo == 2:
                imagebutton:
                    xalign 0.52 yalign 0.74
                    idle im.Flip(im.Scale("tasks/task14.png", 500/2.5, 500/2.5), True)
                    hover im.Flip(im.Scale("tasks/task14.png", 500/2, 500/2), True)
                    hovered [SetVariable("tooltiperTdesc", "Reunião"), Function(get_mouse), SetVariable("tooltiperT", True)]
                    unhovered SetVariable("tooltiperT", False)
                    action If(activeMenu, None, Jump("task14"))
                    focus_mask True
                if tooltiperT:
                    timer 0.03 repeat tooltiperT action Function(get_mouse)
                    frame:
                        xpos mouse_xy[0] ypos mouse_xy[1]-50
                        text tooltiperTdesc
        if tasks_discovered[session][2] and tasks_state[session][2] == 2:
            imagebutton:
                #xalign 0.48 yalign 0.62 at rot(18)
                xalign 0.42 yalign 0.75 at rot(18)
                idle im.Scale("tasks/task5.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task5.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Concluir investigação"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task5"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][6] and tasks_state[session][6] == 2:
            imagebutton:
                xalign 0.42 yalign 0.75 at rot(18)
                idle im.Scale("tasks/task9.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task9.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Concluir investigação"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task9"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][10] and tasks_state[session][10] == 2:
            imagebutton:
                xalign 0.42 yalign 0.75 at rot(18)
                idle im.Scale("tasks/task13.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task13.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Refletir"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task13"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
    if session == 2:
        if tasks_state[session][11] == 0 and intervalo == 2:
            imagebutton:
                xalign 0.52 yalign 0.74
                idle im.Flip(im.Scale("tasks/task26.png", 500/2.5, 500/2.5), True)
                hover im.Flip(im.Scale("tasks/task26.png", 500/2, 500/2), True)
                hovered [SetVariable("tooltiperTdesc", "Reunião"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task26"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][0] == 0:
            imagebutton:
                xalign 0.83 yalign 0.6
                idle im.Scale("tasks/task15.png", 1200/4/2, 1200/4/2)
                hover im.Scale("tasks/task15.png", 1200/3.2/2, 1200/3.2/2)
                hovered [SetVariable("tooltiperTdesc", "Preparar material"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task15"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][4] == 0:
            imagebutton:
                xalign 0.34 yalign 0.66# at rot(-3)
                idle im.Flip(im.Scale("tasks/task19.png", 600/2.5/1.2, 525/2.5/1.2), True)
                hover im.Flip(im.Scale("tasks/task19.png", 600/2/1.2, 525/2/1.2), True)
                hovered [SetVariable("tooltiperTdesc", "Organizar trabalhos"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task19"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][2] and tasks_state[session][2] == 2:
            imagebutton:
                xalign 0.42 yalign 0.75 at rot(18)
                idle im.Scale("tasks/task17.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task17.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Concluir investigação"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task17"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][6] and tasks_state[session][6] == 2:
            imagebutton:
                xalign 0.42 yalign 0.74 at rot(18)
                idle im.Scale("tasks/task21.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task21.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Concluir investigação"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task21"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][10] and tasks_state[session][10] == 2:
            imagebutton:
                xalign 0.42 yalign 0.74 at rot(18)
                idle im.Scale("tasks/task25.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task25.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Refletir"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task25"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
    if session == 3:
        if tasks_state[session][11] == 0 and intervalo == 2:
            imagebutton:
                xalign 0.52 yalign 0.74
                idle im.Flip(im.Scale("tasks/task38.png", 500/2.5, 500/2.5), True)
                hover im.Flip(im.Scale("tasks/task38.png", 500/2, 500/2), True)
                hovered [SetVariable("tooltiperTdesc", "Reunião"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task38"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][4] == 0:
            imagebutton:
                xalign 0.83 ypos 200
                idle im.Scale("tasks/task31.png", 406/0.75, 972/0.75)
                hover im.Scale("tasks/task31.png", 406/0.6, 972/0.6)
                hovered [SetVariable("tooltiperTdesc", "Entregar lista"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task31"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][8] == 0:
            imagebutton:
                xalign 0.34 yalign 0.66
                idle im.Flip(im.Scale("tasks/task35.png", 600/2.5/1.2, 525/2.5/1.2), True)
                hover im.Flip(im.Scale("tasks/task35.png", 600/2/1.2, 525/2/1.2), True)
                hovered [SetVariable("tooltiperTdesc", "Enviar e-mail"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task35"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][2] and tasks_state[session][2] == 2:
            imagebutton:
                xalign 0.42 yalign 0.74 at rot(18)
                idle im.Scale("tasks/task29.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task29.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Concluir investigação"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task29"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][6] and tasks_state[session][6] == 2:
            imagebutton:
                xalign 0.42 yalign 0.74 at rot(18)
                idle im.Scale("tasks/task33.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task33.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Concluir investigação"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task33"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][10] and tasks_state[session][10] == 2:
            imagebutton:
                xalign 0.42 yalign 0.74 at rot(18)
                idle im.Scale("tasks/task37.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task37.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Refletir"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task37"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
    if session == 4:
        if tasks_state[session][11] == 0 and intervalo == 2:
            imagebutton:
                xalign 0.52 yalign 0.74
                idle im.Flip(im.Scale("tasks/task50.png", 500/2.5, 500/2.5), True)
                hover im.Flip(im.Scale("tasks/task50.png", 500/2, 500/2), True)
                hovered [SetVariable("tooltiperTdesc", "Reunião"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task50"))
                focus_mask True
        if tasks_state[session][4] == 0:
            imagebutton:
                xalign 0.83 ypos 200
                idle im.Scale("tasks/task43.png", 406/0.75, 972/0.75)
                hover im.Scale("tasks/task43.png", 406/0.6, 972/0.6)
                hovered [SetVariable("tooltiperTdesc", "Dar planificação"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task43"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_state[session][8] == 0:
            imagebutton:
                xalign 0.34 yalign 0.66
                idle im.Flip(im.Scale("tasks/task47.png", 600/2.5/1.2, 525/2.5/1.2), True)
                hover im.Flip(im.Scale("tasks/task47.png", 600/2/1.2, 525/2/1.2), True)
                hovered [SetVariable("tooltiperTdesc", "Atribuir notas"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task47"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][2] and tasks_state[session][2] == 2:
            imagebutton:
                xalign 0.42 yalign 0.74 at rot(18)
                idle im.Scale("tasks/task41.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task41.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Concluir investigação"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task41"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][6] and tasks_state[session][6] == 2:
            imagebutton:
                xalign 0.42 yalign 0.74 at rot(18)
                idle im.Scale("tasks/task45.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task45.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Concluir investigação"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task45"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc
        if tasks_discovered[session][10] and tasks_state[session][10] == 2:
            imagebutton:
                xalign 0.42 yalign 0.74 at rot(18)
                idle im.Scale("tasks/task49.png", 500/2.5, 500/2.5)
                hover im.Scale("tasks/task49.png", 500/2, 500/2)
                hovered [SetVariable("tooltiperTdesc", "Refletir"), Function(get_mouse), SetVariable("tooltiperT", True)]
                unhovered SetVariable("tooltiperT", False)
                action If(activeMenu, None, Jump("task49"))
                focus_mask True
            if tooltiperT:
                timer 0.03 repeat tooltiperT action Function(get_mouse)
                frame:
                    xpos mouse_xy[0] ypos mouse_xy[1]-50
                    text tooltiperTdesc

    if session == 0 and s0_state == 2:
        timer If(last_room == 13, 2.25, 10) action Jump("session_0.do_task")

label pavilhao:
    call set_scene(20, False)
    call screen pavilhao

screen pavilhao:
    # exit entrada_8
    imagebutton:
        xalign 0.01 yalign 0.5 at rot(90)
        idle im.Scale("arrow_idle_last.png", 100, 100)
        hover im.Scale("arrow_hover.png", 100, 100)
        action Jump("room_8")
        focus_mask True
    if tras_pavilhao and session == 1:
        imagebutton:
            xalign 0.5 yalign 1.5
            idle im.Scale("chats/session_"+str(session)+"/chat_i0_g9_idle.png", 1500, 940)
            hover im.Scale("chats/session_"+str(session)+"/chat_i0_g9_hover.png", 1500, 940)
            action Jump("session_1_dialogues_i0.chat_i0_g11")
            focus_mask True
        image "chats/bubble03.png":
            xsize 1500
            ysize 940
            xalign 0.35
            yalign -1.4
            xzoom 1
    if tras_pavilhao and session == 4:
        imagebutton:
            xalign 0.5 yalign 1.5
            idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g8_idle.png", 1500, 940)
            hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g8_hover.png", 1500, 940)
            action If(intervalo == 0, Jump("session_4_dialogues_i0.chat_i0_g8"), Jump("session_4_dialogues_i1.chat_i1_g8"))
            focus_mask True
        image "chats/bubble03.png":
            xsize 1500
            ysize 940
            xalign 0.35
            yalign -1.4
            xzoom 1

default tras_pavilhao = False
