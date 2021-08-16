############################################################## Variables ##############################################################

default nana_points = 1
default nana_flags = []
default ayame_points = 1
default ayame_flags = []
default mayo_points = 1
default mayo_flags = []
default hana_points = 1
default hana_flags = []
default house_flags = []
default day_counter = 1
default time_of_day = 0
default hana_loc_choice = 0
default hana_glasses = True
default lightswitch = True
default current_label = None
default house_time = None
define credit = """Heart icon by ina el-kadhi:
{a=https://www.flickr.com/people/139807577@N08/}https://www.flickr.com/people/139807577@N08{/a}
{a=https://www.flickr.com/photos/139807577@N08/25508799373}https://www.flickr.com/photos/139807577@N08/25508799373{/a}

Fonts:
Piazzolla Family

0GUI by kiaazad:
{a=https://github.com/Kiaazad/0GUI}https://github.com/Kiaazad/0GUI{/a}

Backgrounds by Uncle Mugen:
{a=https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=17302}https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=17302{/a}

Characters by MUGかぶり:
{a=https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=39049}https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=39049{/a}

Musics:
Daydream by MJ7

Story:
GPL V3

Sound Effects:
From Resident Evil 2TM Capcom
And Thanks for playing [p.name]!"""

############################################################## Transitions ##############################################################

define dis1 = Dissolve(1.0)
define dis2 = Dissolve(2.0)

############################################################## Characters ##############################################################

define nana = Character("Nana", who_color="#cb8872", what_color="#FFF") 
define ayame = Character("Ayame", who_color="#746060", what_color="#FFF")
define mayo = Character("Mayonaise", who_color="#957372", what_color="#FFF")
define hana = Character("Hana", who_color="#d7cbc4", what_color="#FFF")
default p = Character("Unknown", who_color="#1f4eff", what_color="#FFF")

############################################################## Start Label ##############################################################

label start:
    jump day_loop

label day_loop:
    
    play sound daydream
    scene black
    "{cps=5} Day [day_counter] {cps=5}"
    jump house_labels

label day_end:
    
    if "today" in nana_flags:
        $ nana_flags.remove("today")
    if "today" in ayame_flags:
        $ ayame_flags.remove("today")
    if "today" in mayo_flags:
        $ mayo_flags.remove("today")
    if "today" in hana_flags:
        $ hana_flags.remove("today")
    $ day_counter += 1
    $ time_of_day = 0
    jump day_loop

label ending:
    scene black with dis1
    show screen ending with dissolve
    pause
    return   