default blurry = False

label set_scene(num, blurry):
    if num < 8:
        if num == 0:
            scene expression "escadas_0[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 1:
            scene expression "escadas_1[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 2:
            scene expression "escadas_2[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 3:
            scene expression "corredor_3[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 4:
            scene expression "sala_4[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 5:
            scene expression "corredor_5[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 6:
            scene expression "sala_6[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 7:
            scene expression "escadas_7[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
    else:
        if num == 8:
            scene expression "entrada_8[daytime]":
                size (1920, 1080) blur (10 if blurry else 0)
        if num == 9:
            scene expression "biblioteca_9[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 10:
            scene expression "art_10[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 11:
            scene expression "escadas_11[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 12:
            scene expression "gabinete_12[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 13:
            scene expression "escadas_13[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        if num == 14:
            scene expression "professores_14[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)
        #if num == 15:
        #    scene expression "corredor_15[daytime]":
        #        size(1920, 1080) blur (10 if blurry else 0)
        #if num == 16:
        #    scene expression "gabjoao_16[daytime]":
        #        size(1920, 1080) blur (10 if blurry else 0)
        #if num == 17:
        #    scene expression "escadas_17[daytime]":
        #        size(1920, 1080) blur (10 if blurry else 0)
        #if num == 18:
        #    scene expression "gabinete_18[daytime]":
        #        size(1920, 1080) blur (10 if blurry else 0)
        if num == 20:
            scene expression "pavilhao_20[daytime]":
                size(1920, 1080) blur (10 if blurry else 0)

    return

label set_daytime:
    $ daytime = "tarde"
    return
