#personagens
define jogo = Character("Sistema", color="a9a9a9", who_outlines=[(absolute(1), "#000000")])
default player = Character("Jogador", color="a9a9a9", image="player.png", who_outlines=[(absolute(1), "#000000")])
image side player = im.Scale("prof1.png", 400, 400, bilinear=True)

define colega = Character("Professor João", color="a9a9a9", image="colega", who_outlines=[(absolute(1), "#000000")])
image side colega = im.Scale("colega2.png", 300, 300, bilinear=True)
define coordciclo = Character("Coordenador de Ciclo", color="a9a9a9", image="coordciclo", who_outlines=[(absolute(1), "#000000")])
image side coordciclo = im.Scale("coordciclo2.png", 300, 300, bilinear=True)
define aluno = Character("Aluno", color="a9a9a9", image="aluno", who_outlines=[(absolute(1), "#000000")])
image side aluno = im.Scale("aluno.png", 350, 350, bilinear=True)
define aluna = Character("Aluna", color="a9a9a9", image="aluna", who_outlines=[(absolute(1), "#000000")])
image side aluna = im.Scale("aluna.png", 350, 350, bilinear=True)
define grupo_alunos = Character("Grupo de alunos", color="a9a9a9", image="aluna", who_outlines=[(absolute(1), "#000000")])
image side grupo_alunos = im.Scale("aluna.png", 350, 350, bilinear=True)
define auxiliar = Character("Auxiliar", color="a9a9a9", image="auxiliar", who_outlines=[(absolute(1), "#000000")])
image side auxiliar = im.Scale("auxiliar.png", 300, 300, bilinear=True)
define bibliotecaria = Character("Bibliotecária", color="a9a9a9", image="bibliotecaria", who_outlines=[(absolute(1), "#000000")])
image side bibliotecaria = im.Scale("bibliotecaria_face.png", 300, 300, bilinear=True)

define prof_pedro = Character("Professor Pedro", color="a9a9a9", image="prof_pedro", who_outlines=[(absolute(1), "#000000")])
image side prof_pedro = im.Scale("prof3.png", 400, 400, bilinear=True)
define prof_paulo = Character("Professor Paulo", color="a9a9a9", image="prof_paulo", who_outlines=[(absolute(1), "#000000")])
image side prof_paulo = im.Scale("prof6.png", 400, 400, bilinear=True)
define prof_jaime = Character("Professor Pedro", color="a9a9a9", image="prof_jaime", who_outlines=[(absolute(1), "#000000")])
image side prof_jaime = im.Scale("prof7.png", 400, 400, bilinear=True)
define prof_natalia = Character("Professora Natália", color="a9a9a9", image="prof_natalia", who_outlines=[(absolute(1), "#000000")])
image side prof_natalia = im.Scale("prof4.png", 400, 400, bilinear=True)
define prof_luisa = Character("Professora Luísa", color="a9a9a9", image="prof_luisa", who_outlines=[(absolute(1), "#000000")])
image side prof_luisa = im.Scale("prof5.png", 400, 400, bilinear=True)
define prof_maria = Character("Professora Maria", color="a9a9a9", image="prof_maria", who_outlines=[(absolute(1), "#000000")])
image side prof_maria = im.Scale("prof8.png", 400, 400, bilinear=True)

define a = Character("Abel Polido", color="#0e6716", image="abel", who_outlines=[(absolute(1), "#000000")])
#define a = Character("Abel Polido", color="#0e6716", image="abel", who_outlines=[(absolute(1), "#000000")])
image side abel normal = im.Scale("avatars/emotions/abel_normal.png", 350, 350, bilinear=True)
image side abel angry = im.Scale("avatars/emotions/abel_angry.png", 350, 350, bilinear=True)
image side abel happy = im.Scale("avatars/emotions/abel_happy.png", 350, 350, bilinear=True)
image side abel sad = im.Scale("avatars/emotions/abel_sad.png", 350, 350, bilinear=True)
image side abel laugh = im.Scale("avatars/emotions/abel_laugh.png", 350, 350, bilinear=True)
image side abel disgust = im.Scale("avatars/emotions/abel_disgust.png", 350, 350, bilinear=True)
image side abel surprise = im.Scale("avatars/emotions/abel_surprise.png", 350, 350, bilinear=True)
image side abel fear = im.Scale("avatars/emotions/abel_fear.png", 350, 350, bilinear=True)

define c = Character("Cármen Semedo", color="#fb73b4", image="carmen", who_outlines=[(absolute(1), "#000000")])
#define c = Character("Cármen Semedo", color="#ffffff", image="carmen", who_outlines=[(absolute(1), "#000000")])
image side carmen normal = im.Scale("avatars/emotions/carmen_normal.png", 350, 350, bilinear=True)
image side carmen angry = im.Scale("avatars/emotions/carmen_angry.png", 350, 350, bilinear=True)
image side carmen happy = im.Scale("avatars/emotions/carmen_happy.png", 350, 350, bilinear=True)
image side carmen sad = im.Scale("avatars/emotions/carmen_sad.png", 350, 350, bilinear=True)
image side carmen laugh = im.Scale("avatars/emotions/carmen_laugh.png", 350, 350, bilinear=True)
image side carmen disgust = im.Scale("avatars/emotions/carmen_disgust.png", 350, 350, bilinear=True)
image side carmen surprise = im.Scale("avatars/emotions/carmen_surprise.png", 350, 350, bilinear=True)

define e = Character("Estrela Nunes", color="#ffa000", image="estrela", who_outlines=[(absolute(1), "#000000")])
#define e = Character("Estrela Nunes", color="#4363d8", image="estrela", who_outlines=[(absolute(1), "#000000")])
image side estrela normal = im.Scale("avatars/emotions/estrela_normal.png", 350, 350, bilinear=True)
image side estrela angry = im.Scale("avatars/emotions/estrela_angry.png", 350, 350, bilinear=True)
image side estrela happy = im.Scale("avatars/emotions/estrela_happy.png", 350, 350, bilinear=True)
image side estrela sad = im.Scale("avatars/emotions/estrela_sad.png", 350, 350, bilinear=True)
image side estrela laugh = im.Scale("avatars/emotions/estrela_laugh.png", 350, 350, bilinear=True)
image side estrela disgust = im.Scale("avatars/emotions/estrela_disgust.png", 350, 350, bilinear=True)

define h = Character("Hélder Almeida", color="#fffac8", image="helder", who_outlines=[(absolute(1), "#000000")])
#define h = Character("Hélder Almeida", color="#fffac8", image="helder", who_outlines=[(absolute(1), "#000000")])
image side helder normal = im.Scale("avatars/emotions/helder_normal.png", 350, 350, bilinear=True)
image side helder angry = im.Scale("avatars/emotions/helder_angry.png", 350, 350, bilinear=True)
image side helder happy = im.Scale("avatars/emotions/helder_happy.png", 350, 350, bilinear=True)
image side helder sad = im.Scale("avatars/emotions/helder_sad.png", 350, 350, bilinear=True)
image side helder laugh = im.Scale("avatars/emotions/helder_laugh.png", 350, 350, bilinear=True)

define i = Character("Isabel Torres", color="#ff2100", image="isabel", who_outlines=[(absolute(1), "#000000")])
#define i = Character("Isabel Torres", color="#e6194B", image="isabel", who_outlines=[(absolute(1), "#000000")])
image side isabel normal = im.Scale("avatars/emotions/isabel_normal.png", 350, 350, bilinear=True)
image side isabel angry = im.Scale("avatars/emotions/isabel_angry.png", 350, 350, bilinear=True)
image side isabel happy = im.Scale("avatars/emotions/isabel_happy.png", 350, 350, bilinear=True)
image side isabel sad = im.Scale("avatars/emotions/isabel_sad.png", 350, 350, bilinear=True)
image side isabel laugh = im.Scale("avatars/emotions/isabel_laugh.png", 350, 350, bilinear=True)

define j = Character("Jorge Amaral", color="#ff6300", image="jorge", who_outlines=[(absolute(1), "#000000")])
#define j = Character("Jorge Amaral", color="#42d4f4", image="jorge", who_outlines=[(absolute(1), "#000000")])
image side jorge normal = im.Scale("avatars/emotions/jorge_normal.png", 350, 350, bilinear=True)
image side jorge angry = im.Scale("avatars/emotions/jorge_angry.png", 350, 350, bilinear=True)
image side jorge happy = im.Scale("avatars/emotions/jorge_happy.png", 350, 350, bilinear=True)
image side jorge sad = im.Scale("avatars/emotions/jorge_sad.png", 350, 350, bilinear=True)
image side jorge laugh = im.Scale("avatars/emotions/jorge_laugh.png", 350, 350, bilinear=True)
image side jorge surprise = im.Scale("avatars/emotions/jorge_surprise.png", 350, 350, bilinear=True)

define m = Character("Manuela Leitão", color="#00fff2", image="manuela", who_outlines=[(absolute(1), "#000000")])
#define m = Character("Manuela Leitão", color="#911eb4", image="manuela", who_outlines=[(absolute(1), "#000000")])
image side manuela normal = im.Scale("avatars/emotions/manuela_normal.png", 350, 350, bilinear=True)
image side manuela angry = im.Scale("avatars/emotions/manuela_angry.png", 350, 350, bilinear=True)
image side manuela happy = im.Scale("avatars/emotions/manuela_happy.png", 350, 350, bilinear=True)
image side manuela sad = im.Scale("avatars/emotions/manuela_sad.png", 350, 350, bilinear=True)
image side manuela laugh = im.Scale("avatars/emotions/manuela_laugh.png", 350, 350, bilinear=True)
image side manuela disgust = im.Scale("avatars/emotions/manuela_disgust.png", 350, 350, bilinear=True)

define n = Character("Nando Sapina", color="#003cc8", image="nando", who_outlines=[(absolute(1), "#000000")])
#define n = Character("Nando Sapina", color="#bfef45", image="nando", who_outlines=[(absolute(1), "#000000")])
image side nando normal = im.Scale("avatars/emotions/nando_normal.png", 350, 350, bilinear=True)
image side nando angry = im.Scale("avatars/emotions/nando_angry.png", 350, 350, bilinear=True)
image side nando happy = im.Scale("avatars/emotions/nando_happy.png", 350, 350, bilinear=True)
image side nando sad = im.Scale("avatars/emotions/nando_sad.png", 350, 350, bilinear=True)
image side nando laugh = im.Scale("avatars/emotions/nando_laugh.png", 350, 350, bilinear=True)
image side nando mean = im.Scale("avatars/emotions/nando_mean.png", 350, 350, bilinear=True)
image side nando annoyed = im.Scale("avatars/emotions/nando_annoyed.png", 350, 350, bilinear=True)

define p = Character("Patrícia Isidoro", color="#0070c8", image="patricia", who_outlines=[(absolute(1), "#000000")])
#define p = Character("Patrícia Isidoro", color="#f09e38", image="patricia", who_outlines=[(absolute(1), "#000000")])
image side patricia normal = im.Scale("avatars/emotions/patricia_normal.png", 350, 350, bilinear=True)
image side patricia angry = im.Scale("avatars/emotions/patricia_angry.png", 350, 350, bilinear=True)
image side patricia happy = im.Scale("avatars/emotions/patricia_happy.png", 350, 350, bilinear=True)
image side patricia sad = im.Scale("avatars/emotions/patricia_sad.png", 350, 350, bilinear=True)
image side patricia laugh = im.Scale("avatars/emotions/patricia_laugh.png", 350, 350, bilinear=True)
image side patricia disgust = im.Scale("avatars/emotions/patricia_disgust.png", 350, 350, bilinear=True)
image side patricia annoyed = im.Scale("avatars/emotions/patricia_annoyed.png", 350, 350, bilinear=True)
image side patricia surprise = im.Scale("avatars/emotions/patricia_surprise.png", 350, 350, bilinear=True)

define r = Character("Rui Bento", color="#00c38c", image="rui", who_outlines=[(absolute(1), "#000000")])
#define r = Character("Rui Bento", color="#9A6324", image="rui", who_outlines=[(absolute(1), "#000000")])
image side rui normal = im.Scale("avatars/emotions/rui_normal.png", 350, 350, bilinear=True)
image side rui angry = im.Scale("avatars/emotions/rui_angry.png", 350, 350, bilinear=True)
image side rui happy = im.Scale("avatars/emotions/rui_happy.png", 350, 350, bilinear=True)
image side rui sad = im.Scale("avatars/emotions/rui_sad.png", 350, 350, bilinear=True)
image side rui laugh = im.Scale("avatars/emotions/rui_laugh.png", 350, 350, bilinear=True)
image side rui annoyed = im.Scale("avatars/emotions/rui_annoyed.png", 350, 350, bilinear=True)

define s = Character("Samuel Andrade", color="#ffe119", image="samuel", who_outlines=[(absolute(1), "#000000")])
#define s = Character("Samuel Andrade", color="#ffe119", image="samuel", who_outlines=[(absolute(1), "#000000")])
image side samuel normal = im.Scale("avatars/emotions/samuel_normal.png", 350, 350, bilinear=True)
image side samuel angry = im.Scale("avatars/emotions/samuel_angry.png", 350, 350, bilinear=True)
image side samuel happy = im.Scale("avatars/emotions/samuel_happy.png", 350, 350, bilinear=True)
image side samuel sad = im.Scale("avatars/emotions/samuel_sad.png", 350, 350, bilinear=True)
image side samuel laugh = im.Scale("avatars/emotions/samuel_laugh.png", 350, 350, bilinear=True)
image side samuel surprise = im.Scale("avatars/emotions/samuel_surprise.png", 350, 350, bilinear=True)

define t = Character("Tatiana Delgado", color="#79c65d", image="tatiana", who_outlines=[(absolute(1), "#000000")])
#define t = Character("Tatiana Delgado", color="#000000", image="tatiana", who_outlines=[(absolute(1), "#000000")])
image side tatiana normal = im.Scale("avatars/emotions/tatiana_normal.png", 350, 350, bilinear=True)
image side tatiana angry = im.Scale("avatars/emotions/tatiana_angry.png", 350, 350, bilinear=True)
image side tatiana happy = im.Scale("avatars/emotions/tatiana_happy.png", 350, 350, bilinear=True)
image side tatiana sad = im.Scale("avatars/emotions/tatiana_sad.png", 350, 350, bilinear=True)
image side tatiana laugh = im.Scale("avatars/emotions/tatiana_laugh.png", 350, 350, bilinear=True)
image side tatiana cry = im.Scale("avatars/emotions/tatiana_cry.png", 350, 350, bilinear=True)
image side tatiana surprise = im.Scale("avatars/emotions/tatiana_surprise.png", 350, 350, bilinear=True)

# variaveis
default session = 0
default GAME_MINUTES = 0
default GAME_SECONDS = 0

image periodo = "periodo_aula.png"
image reuniao = "reuniao.png"
default n_steps = -1
default n_actions = 0
default n_chats = 0
default active_rooms = [-1]
default chats_in_rooms = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
default randomize = False
default last_room = -1
default current_room = -1
default intervalo = 0
default chats_i0 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
default chats_i0_rotation = 4
default chats_i0_n = [3, 2, 2, 2, 2, 2, 2, 2, 1]
default chats_i1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
default chats_i1_rotation = 5
default chats_i2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
default chats_i2_rotation = 4
default chats_i3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
default chats_i3_rotation = 5
default movement_count = 0
default info = 0
default floor = 1
default mapfloor = 1
default male = True

default sound_rot = 1
default hours = 9
default minutes = 45
default seconds = 0
default fakeminutes = 45
default daytime = "dia"

default lista_personagensActive = False
default score_certeza = 0
default score_situacao = 0
default score_agressores = 0
default score_vitimas = 0

default abel_c = True
default carmen_c = True
default estrela_c = True
default helder_c = True
default isabel_c = True
default jorge_c = True
default manuela_c = True
default nando_c = True
default patricia_c = True
default rui_c = True
default samuel_c = True
default tatiana_c = True
default no_more = True

#########################

default score_final = 0.0
default score_finalx = 0
default change_intervalo = False
default pro_social = 0
default prof = "1"
default first_entry = True
default interj_cb = False
default interj_aluno = False
default interj_prof = False
default final_eval = ""
default final_eval_color = ""
#stats
default st_steps = ""
default st_tasks = ""
default st_chats = ""
default st_info = ""
default st_actions = ["", "", ""]

# inicio e fim
label start:
    init python:
        config.keymap['game_menu'].remove('mouseup_3')
    $ _game_menu_screen = "history"
    call set_scene(num = 8, blurry = True)

    "Welcome to Pro(f)Social!"
    "The game is played with the mouse only. There are some sound effects, the use of headphones is recommended."
    #TRANSLATE"Bem vindo ao jogo Pro(f)Social!"
    #TRANSLATE"O jogo é jogado apenas com o rato. Existem alguns efeitos sonoros, pelo que a utilização de fones é recomendada."

    #"Esta versão é de teste para a sessão 4. Conexão à plataforma desativada."
    call jogar_offline
    #call jogar_online
    #call conetividade
    $ player = Character("[player_name]", color="a9a9a9", image="player", who_outlines=[(absolute(1), "#000000")])
    show screen pick_char
    "Pick your character:"
    #TRANSLATE"Escolha a sua personagem:"

default player_name_dim = "Jogador"
default email_save = ""
default password_save = ""

label jogar_online:
    python:
        email = ""
        password = ""
    label .login:
        python:
            email = renpy.input("Insira o seu email:", default = email, length=100)
            password = renpy.input("Insira a sua password:", default = password,length=50)
            postUrl = 'https://teach4socialgood.com:3000/api/auth/signingame'
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            data = {"email": email, "password": password}
            except_error = False
            try:
                response = requests.post(postUrl, data=json.dumps(data), headers=headers)
            except Exception as exception:
                except_error = True
        if except_error:
            jogo "Falha ao efetuar o login. Clique para tentar novamente. Erro: [exception]"
            jump jogar_online.login
        elif response.status_code == 404:
            jogo "Os dados introduzidos não estão corretos. Clique para tentar novamente. Erro: [response]"
            jump jogar_online.login
        elif response.status_code == 403:
            jogo "A sessão ainda não começou. Clique para tentar novamente. Erro: [response]"
            jump jogar_online.login
        elif response.status_code != 200:
            jogo "Falha ao efetuar o login. Clique para tentar novamente. Erro: [response]"
            jump jogar_online.login
    python:
        player_name = (json.loads(response.content))["user"]["username"]
        player_name_dim = player_name.split()[0]
        session = int((json.loads(response.content))["user"]["session"][7])
    "Nome definido: [player_name]"
    return

label conetividade:
    python:
        with open(os.path.join(os.path.dirname(renpy.config.gamedir), 'user.txt')) as f:
            player_name = f.readline()
            player_name_dim = player_name.split()[0]
        f.close()
    "Nome definido: [player_name]"
    return

label jogar_offline:
    python:
        #TRANSLATEplayer_name = renpy.input("Insira o seu primeiro nome:", length=20)
        player_name = renpy.input("Insert your first name:", length=20)
        player_name = player_name.strip()
        player_name = player_name.title()

        if not player_name:
            player_name = "Jogador"
        player_name_dim = player_name.split()[0]
    #TRANSLATE"Nome definido: [player_name]"
    "Name set: [player_name]"
    return

label end_session_checker:
    hide screen ending
    if session == 4:
        call toggle_UI
        scene black_screen with Fade(0.5, 1.0, 0.5)
        "Um mês depois..."
        call set_scene(12, True)
        colega "Foi essencial reunirmos em equipa para decidirmos o que fazer em relação a esta história toda entre os alunos."
        colega "A verdade é que, depois de conversarmos individualmente com os alunos e termos falado com os pais, as coisas finalmente ficaram mais calmas."
        colega "Também foi importante a ação de sensibilização sobre o cyberbullying que fizemos em conjunto com o Serviço de Psicologia e Orientação."
        colega "Ah, e antes que me esqueça! A escola sempre conseguiu o certificado de Escola Pró-social. Foi resultado do nosso esforço enquanto equipa. Aqui está o certificado. Estamos todos de parabéns!"
        call screen post5
    else:
        #$ session += 1
        menu:
            "Tem a certeza que quer sair?"

            "Sim":
                #$ session -= 1
                #jump expression "start_session_"+str(session+1)
                call toggle_UI
                scene black_screen with Fade(1.0, 0.5, 1.0)
                $ daytime = "dia"
                jump post_session
                return
            "Não":
                #$ session -= 1
                show screen ending
                call screen feedbacklist
    return

label post_session:
    if session == 0:
        $ renpy.say(jogo,"You finished the tutorial session. You can close the game.", interact=False)
        #TRANSLATE$ renpy.say(jogo,"Terminou o tutorial do jogo. Pode fechar o jogo.", interact=False)
    else:
        $ renpy.say(jogo,"Terminou a sessão de jogo. Pode fechar o jogo e voltar para a plataforma online. Aceda pelo browser usando o seguinte link: {i}{b}https://teach4socialgood.com{/b}{/i}. No site, clique na secção onde diz {b}Pós-Jogo{/b} e siga as instruções do agente social.", interact=False)
    $ renpy.pause(600.0, hard=True)
    jump post_session

label start_session:
    $ _dismiss_pause = False
    $ show_toggle_UI = False
    call setup_UI
    call toggle_UI
    call toggle_UI
    call set_scene(8, True)
    jump expression "start_session_"+str(session)

label start_session_0:
    #call setup_UI
    #call toggle_UI
    scene black_screen with Fade(0.5, 1.0, 0.5)
    player "{i}I remember what I did on the first day at the Golden Fields Middle School... My 9th grade students were in 7th grade, and I was a new teacher at the school who didn't know where to go. Seems like it was yesterday...{/i}"
    #TRANSLATE if male:
        # player "{i}Lembro-me como se fosse hoje o que fiz no 1º dia na Escola Básica e Secundária de Campos Dourados... Os meus alunos de 9º ano estavam no 7º, e eu era um professor novo na escola que não sabia para onde ir. Parece que foi ontem...{/i}"
    #TRANSLATE else:
        # player "{i}Lembro-me como se fosse hoje o que fiz no 1º dia na Escola Básica e Secundária de Campos Dourados... Os meus alunos de 9º ano estavam no 7º, e eu era uma professora nova na escola que não sabia para onde ir. Parece que foi ontem...{/i}"
    scene black_screen with Fade(0.5, 1.0, 0.5)
    call set_scene(8, False)
    jump session_0.intervalo_0

label start_session_1:
    $ s0_state = 12
    scene black_screen with Fade(0.5, 1.0, 0.5)
    $ session = 1
    $ drag_options = [[], [], [], []]
    $ drag_feedback = [[], [], [], []]
    $ randomize = True
    $ daytime = "dia"
    $ pro_social = 0
    call set_scene(8, True)
    player "{i}Incrível como a minha Direção de Turma já está no 9º ano. O tempo passa a voar.{/i}"
    player "{i}No entanto, tenho sentido uma mudança geral de comportamento na minha turma. Será ansiedade por causa da viagem de finalistas? Ou será que se passa algo mais grave?{/i}"
    jump session_1.intervalo_0

label start_session_2:
    $ s0_state = 12
    scene black_screen with Fade(0.5, 1.0, 0.5)
    $ session = 2
    $ drag_options = [[], [], [], []]
    $ drag_feedback = [[], [], [], []]
    $ randomize = True
    $ daytime = "dia"
    $ pro_social = 0
    call set_scene(8, True)
    if male:
        player "{i}Na outra semana houve uma situação entre a Tatiana e o Nando. Vou estar atento ao que se passa entre os alunos.{/i}"
    else:
        player "{i}Na outra semana houve uma situação entre a Tatiana e o Nando. Vou estar atenta ao que se passa entre os alunos.{/i}"
    jump session_2.intervalo_0

label start_session_3:
    $ s0_state = 12
    scene black_screen with Fade(0.5, 1.0, 0.5)
    $ session = 3
    $ drag_options = [[], [], [], []]
    $ drag_feedback = [[], [], [], []]
    $ randomize = True
    $ daytime = "dia"
    $ pro_social = 0
    call set_scene(8, True)
    player "{i}Hoje preciso de organizar as atividades para o picnic da escola. Tenho muito que fazer.{/i}"
    jump session_3.intervalo_0

label start_session_4:
    $ s0_state = 12
    scene black_screen with Fade(0.5, 1.0, 0.5)
    $ session = 4
    $ drag_options = [[], [], [], []]
    $ drag_feedback = [[], [], [], []]
    $ randomize = True
    $ daytime = "dia"
    $ pro_social = 0
    call set_scene(8, True)
    player "{i}Como estarão os alunos esta semana?{/i}"
    jump session_4.intervalo_0

screen pick_char:
    key "mouseup_1" action NullAction()
    grid 4 2:
        area (210, 40, 1920-20-400, 750)

        for i in range(1, 9):
            frame:
                xsize 350
                ysize 350
                imagebutton:
                    xsize 350
                    ysize 350
                    ypos -50
                    idle im.Scale("prof"+str(i)+".png", 350, 350)
                    hover im.Scale("prof"+str(i)+"h.png", 350, 350)
                    action [SetVariable("prof", i), If(i==1 or i==3 or i==6 or i==7, SetVariable("male", True), SetVariable("male", False)), Jump("pick_char")]

label pick_char:
    image side player:
        choice (prof == 1):
            im.Scale("prof1.png", 400, 400)
        choice (prof == 2):
            im.Scale("prof2.png", 400, 400)
        choice (prof == 3):
            im.Scale("prof3.png", 400, 400)
        choice (prof == 4):
            im.Scale("prof4.png", 400, 400)
        choice (prof == 5):
            im.Scale("prof5.png", 400, 400)
        choice (prof == 6):
            im.Scale("prof6.png", 400, 400)
        choice (prof == 7):
            im.Scale("prof7.png", 400, 400)
        choice (prof == 8):
            im.Scale("prof8.png", 400, 400)

    image side prof_pedro:
        choice (prof == 1):
            im.Scale("prof3.png", 400, 400, bilinear=True)
        choice (prof == 3):
            im.Scale("prof1.png", 400, 400, bilinear=True)
    image side prof_natalia:
        choice (prof == 2):
            im.Scale("prof4.png", 400, 400, bilinear=True)
        choice (prof == 3):
            im.Scale("prof2.png", 400, 400, bilinear=True)
    image side prof_luisa:
        choice (prof == 2):
            im.Scale("prof5.png", 400, 400, bilinear=True)
        choice (prof == 5):
            im.Scale("prof2.png", 400, 400, bilinear=True)
    image side prof_paulo:
        choice (prof == 1):
            im.Scale("prof6.png", 400, 400, bilinear=True)
        choice (prof == 6):
            im.Scale("prof1.png", 400, 400, bilinear=True)
    image side prof_jaime:
        choice (prof == 1):
            im.Scale("prof7.png", 400, 400, bilinear=True)
        choice (prof == 7):
            im.Scale("prof1.png", 400, 400, bilinear=True)
    image side prof_maria:
        choice (prof == 2):
            im.Scale("prof8.png", 400, 400, bilinear=True)
        choice (prof == 8):
            im.Scale("prof2.png", 400, 400, bilinear=True)

    hide screen pick_char
    jump start_session

label outputlog:
    return
    python:
        with open(os.path.join( renpy.config.gamedir, "tracefile_s"+str(session)+".txt" ), 'w' ) as f:
            #f.write(st_steps)
            #f.write('\n')
            #f.write(st_info)
            #f.write('\n')
            #f.write(st_tasks)
            #f.write('\n')
            for i in range(0, 3):
                f.write(st_actions[i])
                f.write('\n')
        f.close()
    return

default boolvit = True

screen lista_personagens:
    zorder 103
    add im.Scale("avatars/emotions/lista_personagens.png", 1760, 990, bilinear=True) xalign 0.5 yalign -0.9
    if abel_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_a_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_a_hover.png", 1760, 990, bilinear=True)
            action SetVariable("abel_c", not abel_c)
            focus_mask True
    if carmen_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_c_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_c_hover.png", 1760, 990, bilinear=True)
            action SetVariable("carmen_c", not carmen_c)
            focus_mask True
    if estrela_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_e_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_e_hover.png", 1760, 990, bilinear=True)
            action SetVariable("estrela_c", not estrela_c)
            focus_mask True
    if helder_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_h_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_h_hover.png", 1760, 990, bilinear=True)
            action SetVariable("helder_c", not helder_c)
            focus_mask True
    if isabel_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_i_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_i_hover.png", 1760, 990, bilinear=True)
            action SetVariable("isabel_c", not isabel_c)
            focus_mask True
    if jorge_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_j_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_j_hover.png", 1760, 990, bilinear=True)
            action SetVariable("jorge_c", not jorge_c)
            focus_mask True
    if manuela_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_m_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_m_hover.png", 1760, 990, bilinear=True)
            action SetVariable("manuela_c", not manuela_c)
            focus_mask True
    if nando_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_n_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_n_hover.png", 1760, 990, bilinear=True)
            action SetVariable("nando_c", not nando_c)
            focus_mask True
    if patricia_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_p_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_p_hover.png", 1760, 990, bilinear=True)
            action SetVariable("patricia_c", not patricia_c)
            focus_mask True
    if rui_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_r_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_r_hover.png", 1760, 990, bilinear=True)
            action SetVariable("rui_c", not rui_c)
            focus_mask True
    if samuel_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_s_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_s_hover.png", 1760, 990, bilinear=True)
            action SetVariable("samuel_c", not samuel_c)
            focus_mask True
    if tatiana_c:
        imagebutton:
            xalign 0.5 yalign -0.9
            idle im.Scale("avatars/emotions/lista_personagens_t_idle.png", 1760, 990, bilinear=True)
            hover im.Scale("avatars/emotions/lista_personagens_t_hover.png", 1760, 990, bilinear=True)
            action SetVariable("tatiana_c", not tatiana_c)
            focus_mask True
    imagebutton:
        xalign 0.5 yalign -0.9
        idle im.Scale("avatars/emotions/lista_personagens_terminar_idle.png", 1760, 990, bilinear=True)
        hover im.Scale("avatars/emotions/lista_personagens_terminar_hover.png", 1760, 990, bilinear=True)
        action Jump(If(boolvit, "scoring_vitimas", "ending_none"))
        focus_mask True

####################
# INTERVALOS E PERIODOS
####################
label periodo_aula:
    jump expression "session_"+str(session)+".periodo_aula"

label reset_intervalo:
    $ change_intervalo = False
    $ st_steps += "\n Intervalo "+str(intervalo)+" - "+str(n_steps)
    $ st_chats += "\n Intervalo "+str(intervalo)+" - "+str(n_chats)
    $ st_info += "\n Intervalo "+str(intervalo)+" - "+str(info)

    $ n_steps = -1
    $ n_chats = 0
    $ n_actions = 0
    $ randomize = True
    $ movement_count = 0
    $ info = 0

    if intervalo == 1:
        call expression "session_"+str(session)+".intervalo_1"
    elif intervalo == 2:
        call expression "session_"+str(session)+".intervalo_2"
    elif intervalo == 3:
        call expression "session_"+str(session)+".intervalo_3"
    else:
        call expression "session_"+str(session)+".ending"
    return

####################
# ROOMS
####################
label time_checker:
    if movement_count > 59:
        $ randomize = True
        $ movement_count = 0
    if seconds > 59:
        $ seconds -= 60
        $ minutes += 1
    if minutes > 59:
        $ minutes -= 60
        $ hours += 1
    if minutes >= 30:
        $ fakeminutes = minutes
    else:
        $ fakeminutes = 60
    if intervalo == 0:
        if hours > 9:
            call periodo_aula
    if intervalo == 1:
        if hours > 11:
            call periodo_aula
    if intervalo == 2:
        if hours > 14:
            call periodo_aula
    if intervalo == 3:
        if hours > 16:
            call periodo_aula
    return

label pre_room_setup(room_n):
    $ tooltiper = False
    $ sound_rot += 1
    if sound_rot == 4:
        $ sound_rot = 1
    call time_checker
    if randomize:
        call expression "session_"+str(session)+".randomizer"
    $ n_steps += 1
    $ last_room = current_room
    $ current_room = room_n
    call set_scene(room_n, False)
    if ping:
        $ ping = False
        play sound "<silence 1.5>"
        play sound "audio/ping.wav" volume 0.5
    return
label room_0:#escadas_0:
    if interj_aluno:
        call set_scene(current_room, True)
        if session == 0:
            $ interj_aluno = False
            player "To access the different spaces, I can look for a door or entrance like I did in the courtyard, or I can follow the arrows. The dark arrows symbolize the direction I came from."
            #TRANSLATEplayer "Para aceder aos diferentes espaços, posso procurar por uma porta ou entrada como fiz no pátio, ou posso seguir as setas. As setas escuras simbolizam a direção de onde vim."
        if session == 2:
            if intervalo == 0:
                $ interj_aluno = False
                if male:
                    aluno "Bom dia professor, depois desta aula seria possível tirar-me uma dúvida do teste exemplo?"
                    player "Sim, eu a seguir vou ter aula na sala B, podes aparecer lá no próximo intervalo."
                    aluno "Obrigado professor."
                else:
                    aluno "Bom dia professora, depois desta aula seria possível tirar-me uma dúvida do teste exemplo?"
                    player "Sim, eu a seguir vou ter aula na sala B, podes aparecer lá no próximo intervalo."
                    aluno "Obrigado professora."
                $ tasks_discovered[session][5] = True
            if intervalo == 1:
                $ interj_aluno = False
                if male:
                    aluno "Olá professor, não sei se se lembra, eu falei-lhe no outro dia sobre um livro que andava à procura."
                    player "Sim, eu lembro-me. Eu tenho-o guardado na sala de professores. No próximo intervalo, vem ao pátio e entrego-to lá."
                    aluno "Muito obrigado professor."
                else:
                    aluno "Olá professora, não sei se se lembra, eu falei-lhe no outro dia sobre um livro que andava à procura."
                    player "Sim, eu lembro-me. Eu tenho-o guardado na sala de professores. No próximo intervalo, vem ao pátio e entrego-to lá."
                    aluno "Muito obrigado professora."
                $ tasks_discovered[session][9] = True
        call set_scene(current_room, False)
    $ floor = 1
    call pre_room_setup(0)
    if last_room == 2:
        play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
        call screen room_0 with Fade(0.5, 1.0, 0.5)
    elif last_room == 9:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_0 with Fade(0.5, 1.0, 0.5)
    elif last_room == 8:
        call screen room_0 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_0
    return
label room_1:#escadas_1:
    if interj_aluno:
        call set_scene(current_room, True)
        if session == 0:
            $ interj_aluno = False
            player "Para aceder aos diferentes espaços, posso procurar por uma porta ou entrada como fiz agora, ou posso seguir as setas. As setas escuras simbolizam a direção de onde vim."
        if session == 2:
            if intervalo == 0:
                $ interj_aluno = False
                if male:
                    aluno "Bom dia professor, depois desta aula seria possível tirar-me uma dúvida do teste exemplo?"
                    player "Sim, eu a seguir vou ter aula na sala B, podes aparecer lá no próximo intervalo."
                    aluno "Obrigado professor."
                else:
                    aluno "Bom dia professora, depois desta aula seria possível tirar-me uma dúvida do teste exemplo?"
                    player "Sim, eu a seguir vou ter aula na sala B, podes aparecer lá no próximo intervalo."
                    aluno "Obrigado professora."
                $ tasks_discovered[session][5] = True
            if intervalo == 1:
                $ interj_aluno = False
                if male:
                    aluno "Olá professor, não sei se se lembra, eu falei-lhe no outro dia sobre um livro que andava à procura."
                    player "Sim, eu lembro-me. Eu tenho-o guardado na sala de professores. No próximo intervalo, vem ao pátio e entrego-to lá."
                    aluno "Muito obrigado professor."
                else:
                    aluno "Olá professora, não sei se se lembra, eu falei-lhe no outro dia sobre um livro que andava à procura."
                    player "Sim, eu lembro-me. Eu tenho-o guardado na sala de professores. No próximo intervalo, vem ao pátio e entrego-to lá."
                    aluno "Muito obrigado professora."
                $ tasks_discovered[session][9] = True
        call set_scene(current_room, False)
    $ floor = 1
    call pre_room_setup(1)
    if last_room == 7:
        play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
        call screen room_1 with Fade(0.5, 1.0, 0.5)
    elif last_room == 10:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_1 with Fade(0.5, 1.0, 0.5)
    elif last_room == 8:
        call screen room_1 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_1
    return
label room_2:#escadas_2:
    if interj_aluno:
        call set_scene(current_room, True)
        if session == 1 or session == 3:
            if intervalo == 0:
                $ interj_aluno = False
                if male:
                    aluno "Bom dia professor, depois desta aula seria possível tirar-me uma dúvida rápida que eu tenho?"
                    player "Sim, eu a seguir vou ter aula na sala B, podes aparecer lá no próximo intervalo."
                    aluno "Obrigado professor."
                else:
                    aluno "Bom dia professora, depois desta aula seria possível tirar-me uma dúvida rápida que eu tenho?"
                    player "Sim, eu a seguir vou ter aula na sala B, podes aparecer lá no próximo intervalo."
                    aluno "Obrigado professora."
                $ tasks_discovered[session][5] = True
            if intervalo == 1 and session == 1:
                $ interj_aluno = False
                if male:
                    aluno "Olá professor, nós estamos a vender rifas para ajudar um canil local. Se estiver interessado estaremos no pátio da escola depois de almoço."
                    player "Vou pensar no assunto, obrigado pelo convite."
                    aluno "Obrigado nós professor."
                else:
                    aluno "Olá professora, nós estamos a vender rifas para ajudar um canil local. Se estiver interessada estaremos no pátio da escola depois de almoço."
                    player "Vou pensar no assunto, obrigada pelo convite."
                    aluno "Obrigado nós professora."
                $ tasks_discovered[session][9] = True
            if intervalo == 1 and session == 3:
                $ interj_aluno = False
                coordciclo "Olá [player_name_dim], no próximo intervalo conseguiria encontrar-se comigo na sala polivalente? Para vermos dos materiais do picnic."
                player "Claro que sim."
                coordciclo "Muito obrigado."
                $ tasks_discovered[session][9] = True
        if session == 4:
            if intervalo == 1:
                $ interj_aluno = False
                if male:
                    aluno "Olá professor, nós estamos a vender rifas para a viagem de finalistas. Se estiver interessado estaremos no pátio da escola depois de almoço."
                    player "Vou pensar no assunto, obrigado pelo convite."
                    aluno "Obrigado nós professor."
                else:
                    aluno "Olá professora, nós estamos a vender rifas para a viagem de finalistas. Se estiver interessado estaremos no pátio da escola depois de almoço."
                    player "Vou pensar no assunto, obrigada pelo convite."
                    aluno "Obrigado nós professora."
                $ tasks_discovered[session][9] = True
        call set_scene(current_room, False)
    $ floor = 2
    call pre_room_setup(2)
    if last_room == 0:
        play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
        call screen room_2 with Fade(0.5, 1.0, 0.5)
    elif last_room == 11:
        play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
        call screen room_2 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_2
    return
label room_3:#corredor_3:
    $ floor = 2
    call pre_room_setup(3)
    if last_room == 4:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_3 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_3
    return
label room_4:#sala_4:
    $ floor = 2
    call pre_room_setup(4)
    if last_room == 3:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_4 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_4
    return
label room_5:#corredor_5:
    $ floor = 2
    call pre_room_setup(5)
    if last_room == 6:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_5 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_5
    return
label room_6:#sala_6:
    $ floor = 2
    call pre_room_setup(6)
    if last_room == 5:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_6 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_6
    return
label room_7:#escadas_7:
    if interj_aluno:
        call set_scene(current_room, True)
        if session == 1 or session == 3:
            if intervalo == 0:
                $ interj_aluno = False
                if male:
                    aluno "Bom dia professor, depois desta aula seria possível tirar-me uma dúvida rápida que eu tenho?"
                    player "Sim, eu a seguir vou ter aula na sala B, podes aparecer lá no próximo intervalo."
                    aluno "Obrigado professor."
                else:
                    aluno "Bom dia professora, depois desta aula seria possível tirar-me uma dúvida rápida que eu tenho?"
                    player "Sim, eu a seguir vou ter aula na sala B, podes aparecer lá no próximo intervalo."
                    aluno "Obrigado professora."
                $ tasks_discovered[session][5] = True
            if intervalo == 1 and session == 1:
                $ interj_aluno = False
                if male:
                    aluno "Olá professor, nós estamos a vender rifas para ajudar um canil local. Se estiver interessado estaremos no pátio da escola depois de almoço."
                    player "Vou pensar no assunto, obrigado pelo convite."
                    aluno "Obrigado nós professor."
                else:
                    aluno "Olá professora, nós estamos a vender rifas para ajudar um canil local. Se estiver interessada estaremos no pátio da escola depois de almoço."
                    player "Vou pensar no assunto, obrigada pelo convite."
                    aluno "Obrigado nós professora."
                $ tasks_discovered[session][9] = True
            if intervalo == 1 and session == 3:
                $ interj_aluno = False
                coordciclo "Olá [player_name_dim], no próximo intervalo conseguiria encontrar-se comigo na sala polivalente? Para vermos dos materiais do picnic."
                player "Claro que sim."
                coordciclo "Muito obrigado."
                $ tasks_discovered[session][9] = True
        call set_scene(current_room, False)
    $ floor = 2
    call pre_room_setup(7)
    if last_room == 1:
        play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
        call screen room_7 with Fade(0.5, 1.0, 0.5)
    elif last_room == 13:
        play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
        call screen room_7 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_7
    return
label room_8:#entrada_8:
    $ purge_saves("1-2")
    $ floor = 1
    call pre_room_setup(8)
    if last_room != 80:
        if first_entry:
            play sound "audio/birds_"+str(6)+".mp3" volume 1 fadein 50 fadeout 50
            $ first_entry = False
        else:
            play sound "audio/birds_"+str(5)+".mp3" volume 1 fadein 50 fadeout 50
        call screen room_8 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_8
    return
label room_9:#biblioteca_9:
    $ floor = 1
    call pre_room_setup(9)
    if session == 0:
        if s0_state == 9:
            player "{i}I think I have all the information about Estrela. I should go to the staff room and write down the justification.{/i}"
            #TRANSLATEplayer "{i}Penso que tenho a informação toda sobre a Estrela. Devia ir à sala de professores anotar a justificação.{/i}"
    if last_room == 0:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_9 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_9
    call screen room_9 with If (last_room in {0}, Fade(0.1, 1, 1), None)
    return
label room_10:#art_10:
    $ floor = 1
    call pre_room_setup(10)
    if last_room == 1:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_10 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_10
    return
label room_11:#escadas_11:
    $ floor = 3
    call pre_room_setup(11)
    if last_room == 2:
        play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
        call screen room_11 with Fade(0.5, 1.0, 0.5)
    elif last_room == 12:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_11 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_11
    return
label room_12:#gabinete_12:
    $ floor = 3
    call pre_room_setup(12)
    if session == 0:
        if s0_state == 12:

            player "{i}Feedback on my decisions helps me understand how to be more prosocial with my decisions.{/i}"
            player "{i}As a teacher, I must fulfill my school tasks, but also help students to adopt pro-social behaviors.{/i}"
            player "{i}Well, it seems I got lost in my memories... It's time to return to the present.{/i}"
            #TRANSLATEif male:
            #TRANSLATE    player "{i}O feedback das minhas decisões ajuda-me a perceber como ser mais pró-social com as minhas decisões.{/i}"
            #TRANSLATE    player "{i}Enquanto professor devo cumprir as minhas tarefas escolares, mas também ajudar os alunos a adotarem comportamentos pró-sociais.{/i}"
            #TRANSLATE    player "{i}Bem, parece que fiquei perdido nas minhas recordações... Está na hora de voltar ao presente.{/i}"
            #TRANSLATEelse:
            #TRANSLATE    player "{i}O feedback das minhas decisões ajuda-me a perceber como ser mais pró-social com as minhas decisões.{/i}"
            #TRANSLATE    player "{i}Enquanto professora devo cumprir as minhas tarefas escolares, mas também ajudar os alunos a adotarem comportamentos pró-sociais.{/i}"
            #TRANSLATE    player "{i}Bem, parece que fiquei perdida nas minhas recordações... Está na hora de voltar ao presente.{/i}"
            
            scene black_screen with Fade(0.2, 1, 0.2)
            call toggle_UI
            call platform
            jump post_session
            return
    if last_room == 11:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_12 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_12
    return
label room_13:#escadas_13:
    $ floor = 3
    call pre_room_setup(13)
    if last_room == 7:
        play sound "audio/steps_"+str(sound_rot)+".mp3" volume 5.0
        call screen room_13 with Fade(0.5, 1.0, 0.5)
    elif last_room == 14:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_13 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_13
    return
label room_14:#professores_14:
    $ floor = 3
    call pre_room_setup(14)
    if session == 0:
        if s0_state == 3:
            show screen menulist
            show screen menulist_UI
            player "{i}When I complete a task, I receive a visual and audible warning, and the task list is updated. I can go to class early or I can explore the school a little.{/i}"
            #TRANSLATEplayer "{i}Quando completo uma tarefa, recebo um aviso visual e sonoro, e a lista de tarefas é atualizada. Posso ir para a sala de aula mais cedo ou então posso explorar a escola um pouco.{/i}"
        if s0_state == 11:
            player "{i}I need to go to the work office next door and talk to João.{/i}"
            #TRANSLATEplayer "{i}Preciso de ir ao gabinete de trabalho falar com o João.{/i}"
    if last_room == 13:
        play sound "audio/door_"+str(sound_rot)+".mp3" volume 0.5
        call screen room_14 with Fade(0.5, 1.0, 0.5)
    else:
        call screen room_14
    return

####################
# DIALOGOS
####################
default fade = True
default ping = False

label leave_conversation:
    $ purge_saves("1-3")
    $ tooltiper = False
    $ tooltiperT = False
    if fade:
        scene black_screen with Fade(0.2, 1, 0.2)
    $ fade = True
    if drag_game:
        call set_scene(current_room, True)
        jump setup_dragndrop
    call toggle_UI
    $ movement_count = 59
    jump expression "room_" + str(current_room)
    return

label dialog_profs:
    call set_scene(current_room, True)
    call toggle_UI
    $ interj_prof = False
    jump expression "session_"+str(session)+".profs_i"+str(intervalo)

####################
# FUNCTIONS
####################

default chatnum = 0

screen keymapscreen:
    zorder 1200
    #key "p" action SetVariable("minutes", 59)
    #key "p" action SetVariable("tasks_discovered", [[True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True, True]])
    #key "p" action Jump("testscreen")
    #key "m" action Show("pick_student_task")
    #key "l" action ShowMenu("load")

label testscreen:
    $ chatnum += 1
    jump room_10
screen debugscreen:
    imagebutton:
        xalign 0.99 yalign 1.0
        idle im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chatnum)+"_idle.png", 1300, 815)
        hover im.Scale("chats/session_"+str(session)+"/chat_i"+str(intervalo)+"_g"+str(chatnum)+"_hover.png", 1300, 815)
        action If(activeMenu, None, [SetDict(chats_in_rooms, current_room, -1), Jump("session_"+str(session)+"_dialogues_i"+str(intervalo)+".chat_i"+str(intervalo)+"_g"+str(chatnum))])
        focus_mask True
    image "chats/bubble0"+str(chats_positions[session-1][intervalo][chatnum][3])+".png":
        xsize 1300
        ysize 815
        xalign 0.99+chats_positions[session-1][intervalo][chatnum][0]
        yalign 1.0+chats_positions[session-1][intervalo][chatnum][1]
        xzoom chats_positions[session-1][intervalo][chatnum][2]

define gui.choice_button_text_idle_color = '#000000'
define gui.choice_button_width = 750

transform rot(rotation):
    rotate rotation

transform hmove(amount):
    on hover:
        xpos amount

transform change_transform(old, new):
    contains:
        old
        yalign 1.0
        xpos 0.0 xanchor 0.0
        linear 0.2 xanchor 1.0
    contains:
        new
        yalign 1.0
        xpos 0.0 xanchor 1.0
        linear 0.2 xanchor 0.0

define config.side_image_change_transform = change_transform

style window:
    left_padding 0

default mouse_xy = (0, 0)

init python:
    import requests
    import json
    def get_mouse():
        global mouse_xy
        mouse_xy = renpy.get_mouse_pos()
    def purge_saves(savefile_slot):
        #saves = renpy.list_slots()
        #for save in saves:
        #    renpy.unlink_save(save)
        renpy.take_screenshot()
        renpy.save(savefile_slot, save_name)
        return
