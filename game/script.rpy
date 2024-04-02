init python:
    def submit_to_google_forms(happy, scare, place, friend, bully, surname, cool, insult, recre, important, confiance, who, hurt, feel, apart, kind, safe):
        js_code = f"submitToGoogleForms('{happy}', '{scare}', '{place}', '{friend}', '{bully}', '{surname}', '{cool}', '{insult}', '{recre}', '{important}', '{confiance}', '{who}', '{hurt}', '{feel}', '{apart}', '{kind}', '{safe}');"
        renpy.emscripten.run_script(js_code)

#Prénom des personnages

define maman = Character('Maman', color="#000000")
define toby = Character('Toby', color="#000000")
define prof = Character('Maîtresse Wouf', color="#000000")
define bella = Character('Bella', color="#000000")
define gazou = Character('Gazou', color="#000000")

#Position des personnages

init:
    $ gazou_position = Position(xpos=0.4, xanchor=0.5, ypos=0.5, yanchor=0.5)
    $ maman_position = Position(xpos=0.6, xanchor=0.5, ypos=0.5, yanchor=0.5)


label start:
    "{color=#000000}Avant de commencer le jeu, comment t'appelles-tu ?"
    $ player_name = renpy.input("Ton prénom :")
    if not player_name:
        $ player_name = "Toi"
    "{color=#000000}Bonjour [player_name], bienvenue dans Trace de Pattes !"

    play music "backgroundmusic.mp3"

    scene chambre with fade
    "{color=#000000}Tu te réveilles dans ta chambre, le soleil éclairant la pièce. Ta mère entre en chantonnant et demande :"
    show maman at left with dissolve
    maman "{color=#000000}Bonjour [player_name], as-tu envie d'aller passer la journée à l'école avec [prof] ?"
    menu:
        "Oui":
            $ happy = "Oui"
        "Non":
            $ happy = "Non"

    scene chemin with fade
    show gazou at gazou_position with dissolve
    "{color=#000000}Sur le chemin de l'école, Gazou vient à ta rencontre et te demande doucement :"
    gazou "{color=#000000}Eh [player_name], je me demandais, tu as déjà ressenti une peur avant de rejoindre [prof] ?"
    menu:
        "Oui":
            $ scare = "Oui"
        "Non":
            $ scare = "Non"
    hide gazou

    scene recre with fade
    show prof_crop with dissolve
    "{color=#000000}Tu arrives à l'école et rejoins la maîtresse dans la cour. Elle te demande :"
    prof "{color=#000000}Quel est le moment que tu préfères quand tu passes la journée avec moi ?"
    menu:
        "La cantine":
            $ place = "La cantine"
        "La classe":
            $ place = "La classe"
        "La récréation":
            $ place = "La récréation"
        "La fin de l'école":
            $ place = "La fin de l'école"
    hide prof

    scene classe with fade
    "{color=#000000}Tu vas en classe, écoute ton cours, puis vient la récréation."
    scene recre with fade

    show toby_crop at right with dissolve
    "{color=#000000}Pendant la récréation, Toby le curieux vient te voir pour te poser une série de questions :"
    toby "{color=#000000}Joues-tu avec les autres animaux de la classe ?"
    menu:
        "Oui":
            $ friend = "Oui"
        "Non":
            $ friend = "Non"

    toby "{color=#000000}T'es-tu déjà fait embêter par les méchants loups ici ?"
    menu:
        "Oui":
            $ bully = "Oui"
        "Non":
            $ bully = "Non"

    toby "{color=#000000}Est-ce qu'on t'a déjà donné un surnom méchant ?"
    menu:
        "Oui":
            $ surname = "Oui"
        "Non":
            $ surname = "Non"

    play sound "cloche.mp3"
    "{color=#000000}La cloche sonne et vous retournez en classe."
    hide toby
    scene classe with fade

    show prof at right with dissolve
    "{color=#000000}En classe, la maîtresse vient te voir et te demande :"
    hide prof 
    show prof_crop at right with dissolve
    prof "{color=#000000}Est-ce que tu t'entends bien avec tes camarades animaux ?"
    menu:
        "Oui":
            $ cool = "Oui"
        "Non":
            $ cool = "Non"

    prof "{color=#000000}Est-ce que les méchants loups se sont déjà moqués de toi ?"
    menu:
        "Oui":
            $ insult = "Oui"
        "Non":
            $ insult = "Non"

    prof "{color=#000000}Par moment, as-tu peur d'aller en récréation avec les animaux ?"
    menu:
        "Oui":
            $ recre = "Oui"
        "Non":
            $ recre = "Non"

    "{color=#000000}La cloche sonne, c'est la fin de la journée."
    scene recre with fade

    show bella_crop at left with dissolve
    "{color=#000000}Après la classe, Bella vient voir comment tu vas :"

    bella "{color=#000000}Te sens-tu à l'écart pendant la journée ?"
    menu:
        "Oui":
            $ apart = "Oui"
        "Non":
            $ apart = "Non"
        "Neutre":
            $ apart = "Neutre"
    
    hide bella

    scene chemin with fade

    show gazou at gazou_position with dissolve
    "{color=#000000}Sur le chemin de la maison, tu es avec Gazou qui te demande :"

    hide gazou
    show gazou_crop at left with dissolve
    gazou "{color=#000000}Tu penses que c'est important d'être gentil avec les autres ? Des fois j'ai envie de l'être, et d'autres fois non."
    menu:
        "Oui":
            $ kind = "Oui"
        "Non":
            $ kind = "Non"
    scene maison with fade
    show gazou_crop at left with dissolve
    gazou "{color=#000000}Bon, tu es arrivé chez toi. Je te laisse, à plus tard !"
    hide gazou_crop
    scene salle_a_manger with fade

    show maman at left with dissolve
    "{color=#000000}Une fois à la maison, tu profites d'un goûter réconfortant préparé par maman et elle te demande :"

    hide maman
    show maman_crop at left with dissolve
    maman "{color=#000000}Si quelqu'un te fait du mal pendant la journée, penses-tu qu'il est important d'en parler ?"
    menu:
        "Oui":
            $ important = "Oui"
        "Non":
            $ important = "Non"

    maman "{color=#000000}Fais-tu confiance aux différents adultes que tu vois pendant la journée ?"
    menu:
        "Oui":
            $ confiance = "Oui"
        "Non":
            $ confiance = "Non"

    maman "{color=#000000}Et si quelqu'un te fait du mal pendant la journée, par exemple les autres animaux ou la maîtresse, qui irais-tu voir en premier ?"
    menu:
        "Mes parents":
            $ who = "Mes parents"
        "Les adultes de l'école":
            $ who = "Les adultes de l'école"
        "Les autres enfants":
            $ who = "Les autres enfants"
        "Personne":
            $ who = "Personne"

    scene salon with fade
    show maman at maman_position with dissolve
    "{color=#000000}Après avoir partagé un délicieux goûter, maman s'assoie confortablement avec toi dans le salon et te pose des questions :"

    hide maman
    show maman_crop at right with dissolve

    maman "{color=#000000}Comment te sens-tu après cette longue journée ?"
    menu:
        "Mal":
            $ feel = "Mal"
        "Bien":
            $ feel = "Bien"
    
    maman "{color=#000000}Est-ce qu'un ou plusieurs animaux te font du mal pendant la journée, quand je ne suis pas là ?"
    menu:
        "Jamais":
            $ hurt = "Jamais"
        "Parfois":
            $ hurt = "Parfois"
        "Souvent":
            $ hurt = "Souvent"
        "Tout le temps":
            $ hurt = "Tout le temps"
    hide maman
    "{color=#000000}Après cette discussion, maman te demande d'aller prendre ta douche puis de la rejoindre dans la salle à manger pour le dîner."
    scene salle_a_manger with fade
    "{color=#000000}Tu es à table avec maman pour le dîner."
    show maman at left with dissolve
    "{color=#000000}Vous commencez à manger et maman te demande :"
    maman "{color=#000000}Est-ce que tu te sens en sécurité quand tu es avec les autres animaux ?"
    menu:
        "Oui":
            $ safe = "Oui"
        "Non":
            $ safe = "Non"
    hide maman

    "{color=#000000}Après avoir fini de manger, tu retournes dans ta chambre pour te préparer à dormir." 
    scene chambre with fade
    "{color=#000000}Maman vient te border et te souhaite une bonne nuit."
    show maman at left with dissolve
    maman "{color=#000000}Bonne nuit [player_name], dors bien."

    # Lorsque toutes les réponses sont collectées, appelle la fonction Python pour soumettre les réponses.
    $ submit_to_google_forms(happy, scare, place, friend, bully, surname, cool, insult, recre, important, confiance, who, hurt, feel, apart, kind, safe)

    "Nous apprécions ton temps et ta participation."

    # Animation de fin avant de quitter
    scene black with fade
    "Fin du jeu. Prends soin de toi !"
    return

