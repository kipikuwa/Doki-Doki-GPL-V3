############################################################## Screens ##############################################################

screen map1():
    modal True
    tag map
    add "map_bg"
    style_prefix "map1"
    button:
        focus_mask True
        xysize 94,94
        pos 110,65
        background "map_home_idle"
        hover_background "map_home_hover"
        text "House"
        if not current_label == "house":
            action Function(change_time, 6), Hide("map1"), Jump("house_labels")
    button:
        focus_mask True
        xysize 472,380
        pos 998,185
        background "map_street_idle"
        hover_background "map_street_hover"
        text "Street"
        if not current_label == "nana":
            action Function(change_time, 6), Hide("map1"), Jump("nana_labels")
    button:
        focus_mask True
        xysize 190,158
        pos 1020,629
        background "map_school_idle"
        hover_background "map_school_hover"
        text "School"
        if not current_label == "ayame":
            action Function(change_time, 6), Hide("map1"), Jump("ayame_labels")
    button:
        focus_mask True
        xysize 621,673
        pos 310,743
        background "map_jungle_idle"
        hover_background "map_jungle_hover"
        text "Jungle"
        if not current_label == "mayo":
            action Function(change_time, 6), Hide("map1"), Jump("mayo_labels")

style map1_button:
    hover_sound "audio/re2_coursor.wav"
    activate_sound "audio/re2_decide.wav"

screen hana_love_locations():
    tag map
    add "map_bg"
    style_prefix "hana_love_locations"
    button:
        focus_mask True
        xysize 94,94
        pos 110,65
        background "map_home_idle"
        hover_background "map_home_hover"
        text "House"
        action Return(4)
    button:
        focus_mask True
        xysize 472,380
        pos 998,185
        background "map_street_idle"
        hover_background "map_street_hover"
        text "Street"
        action Return(1)

    button:
        focus_mask True
        xysize 190,158
        pos 1020,629
        background "map_school_idle"
        hover_background "map_school_hover"
        text "School"
        action Return(2)
    button:
        focus_mask True
        xysize 621,673
        pos 310,743
        background "map_jungle_idle"
        hover_background "map_jungle_hover"
        text "Jungle"
        action Return(3)

style hana_love_locations_button:
    hover_sound "audio/re2_coursor.wav"
    activate_sound "audio/re2_decide.wav"

screen show_time():
    text str(time_of_day)

screen show_label_name():
    text str(house_time)

screen room_lights():
    tag map
    button:
        background "lightoffkey" xysize 21,22
        hover_background "lightonkey"
        pos 32,542
        action ToggleVariable("lightswitch", True, False)
    button:
        focus_mask True
        background "bed switch idle" xysize 709,312
        hover_background "bed switch hover"
        pos 372,922
        action Hide("room_lights"), Jump("house_menu")

screen map_icon():
    button:
        background "map_icon_idle" xysize 156,144
        hover_background "map_icon_hover"
        pos 1790,1005
        action Hide("map_icon"), Show("map1")

screen ending():
    text str(credit)