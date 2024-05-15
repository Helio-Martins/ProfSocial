default ses_fb = [[1], #SITUAÇÃO 1, 2, 3, P
 [2],
  [3],
   [4]]

default ses_fb_q = [[1,1], #SITUAÇÃO 1, 2, 3, P
 [2,2],
  [3,3],
   [4,4]]

default ses_fb_t = [[], #SITUAÇÃO 1, 2, 3
 [],
  []]

default ses_fb_i = [[0, 1, 2, 3, 12, 13, 14, 15, 4, 5, 6, 7, 8, 9, 10, 11], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5, 6, 7, 8]]

default allGameBoardData = []
default export_success = False

label platform:
    return
    python:
        #import json
        #import requests
        postUrl = 'https://teach4socialgood.com:3000/api/game/finalData'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        list = []

        if session != 0:
            #SIT 1, 2, 3
            for n in range(3):
                list.append({
                    "situation": "SITUACAO_"+str(n+1)+"_Q",
                    "data": {
                        "question": ses_fb_q[n][0],
                        "answer": ses_fb_q[n][1]
                    }
                })
                #for i in range(len(ses_fb[n])):
                #    list.append({
                #        "situation": "SITUACAO_"+str(n+1)+"_"+str(i+1),
                #        "data": {
                #            "question": store.drag_options[n][i],
                #            "answer": ses_fb[n][i]
                #        }
                #    })
                for k in range(len(ses_fb[n])-1):
                    list.append({
                        "situation": "SITUACAO_"+str(n+1)+"_"+str(k+1),
                        "data": {
                            "question": ses_fb[n][len(ses_fb[n])-1][ses_fb_i[n][k]],
                            "answer": ses_fb[n][ses_fb_i[n][k]]
                        }
                    })
            #SIT P
            list.append({
                "situation": "SITUACAO_P_Q",
                "data": {
                    "question": ses_fb_q[3][0],
                    "answer": ses_fb_q[3][1]
                }
            })
            for k in range(len(ses_fb[3])-1):
                list.append({
                    "situation": "SITUACAO_P_"+str(k+1),
                    "data": {
                        "question": ses_fb[3][len(ses_fb[3])-1][k],
                        "answer": ses_fb[3][k]
                    }
                })
            #T
            for n in range(3):
                k = 0
                while k < len(ses_fb_t[n])-1:
                    list.append({
                        "situation": "TAREFA_"+str(n+1)+"_"+str(1+k/2),
                        "data": {
                            "question": ses_fb_t[n][k],
                            "answer": ses_fb_t[n][k+1]
                        }
                    })
                    k = k+2

        allGameBoardData = {
            #"username": "testeProf2",
            "username": player_name,
            "gameTime": {
                "minutes": GAME_MINUTES,
                "seconds": GAME_SECONDS
            },
            "gameBoard": list
        }

        try:
            with open(os.path.join(os.path.dirname(renpy.config.gamedir), "export_manual_sessao_"+str(session)+".txt" ), 'w') as f:
                f.write(json.dumps(allGameBoardData))
            f.close()
        except Exception as exception:
            pass

        #with open(os.path.join(renpy.config.gamedir, "zfeedback_s"+str(session)+".txt" ), 'w' ) as f:
        #    for k in range(len(list)):
        #        a = list[k].values()
        #        f.write(a[0])
        #        f.write("\n")
        #        for b in a[1].values():
        #            f.write(str(b))
        #            f.write("\n")
        #f.close()
    #return
    $ renpy.say(jogo,"A iniciar exportação dos dados para a plataforma...", interact=False)
    $ renpy.pause(1.0, hard=True)
    label .export:
        python:
            except_error = False
            try:
                response = requests.post(postUrl, data=json.dumps(allGameBoardData), headers=headers)
            except Exception as exception:
                except_error = True
        if except_error:
            jogo "Falha ao exportar os dados. Clique para tentar novamente. Erro: [exception]"
        elif response.status_code != 200:
            jogo "Falha ao exportar os dados. Clique para tentar novamente. Erro: [response]"
        else:
            jump platform.sucess
        $ renpy.say(jogo,"A reiniciar exportação dos dados...", interact=False)
        $ renpy.pause(1.0, hard=True)
        jump platform.export

    label .sucess:
        $ renpy.say(jogo,"Exportação dos dados concluída.", interact=False)
        $ renpy.pause(2.0, hard=True)
