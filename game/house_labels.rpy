############################################################## House Labels ##############################################################

label house_labels:
    hide map1
    $ current_label = "house"
    if not "first" in house_flags:
        jump house1
    else:
        jump house2
label house1:
    show bg room morning with dis1
    pause
    "The GNU General Public License is a free, copyleft license for software and other kinds of works."
    $ house_flags.append("first")
    jump nana_labels

label house2:
    show bg house with dis1
    show screen map_icon
    hide 6hourslater with dis1
    call screen room_lights
    
label house_menu:
    if 17 < time_of_day <= 24:
        jump hana_labels
    else:
        "I can't sleep right now!"
        "Better do something to pass the time."
        menu:
            "Watch TV for 6 hours":
                $ player_choice_1 = "1"
                "I will watch TV for 6 hours"
                show 6hourslater with dis1
                pause
                $ time_of_day += 6
                jump house2

            "Read Some Books for 6 hours":
                $ player_choice_1 = "2"
                "I'm gonna read books for 6 hours"
                show 6hourslater with dis1
                pause
                $ time_of_day += 6
                jump house2

            "Use the computer for 6 hours":
                $ player_choice_1 = "3"
                "I will use the computer for 6 hours"
                show 6hourslater with dis1
                pause
                $ time_of_day += 6
                jump house2