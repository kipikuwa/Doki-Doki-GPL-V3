############################################################## Ayame's Labels ##############################################################

label ayame_labels:
    hide room_lights
    hide map1
    $ current_label = "ayame"
    scene black
    if not "first" in ayame_flags:
        jump ayame1
    elif "today" in ayame_flags and 0 < time_of_day < 12:
        jump ayame0
    elif "today" in ayame_flags and 11 < time_of_day < 18:
        jump ayamee0
    elif "today" in ayame_flags and 17 < time_of_day < 24:
        jump ayamen0
    elif ayame_points == 2:
        jump ayame2
    elif ayame_points == 3:
        jump ayame3
    elif ayame_points == 4:
        jump ayame4
    elif ayame_points == 5:
        jump ayame5


label ayame0:
    show bg classroom 3 day with dis1
    "Nothing to do here!"
    call screen map1 with dis1

label ayamee0:
    show bg classroom 3 evening with dis1
    "Nothing to do here!"
    call screen map1 with dis1

label ayamen0:
    show bg classroom 3 night with dis1
    "Nothing to do here!"
    call screen map1 with dis1

label ayame1:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "Therefore, you have certain responsibilities if you distribute copies of the software,"
    menu:
        "or if you modify it: responsibilities to respect the freedom of others. {image=plus1}":
            p "or if you modify it: responsibilities to respect the freedom of others."

    show ayame smile with dissolve
    ayame "For example, if you distribute copies of such a program, whether gratis or for a fee,"
    ayame "you must pass on to the recipients the same freedoms that you received."
    hide ayame with dissolve
    $ ayame_flags.append("first")
    $ ayame_points += 1
    jump mayo_labels

label ayame2:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "Propagation includes copying, distribution (with or without modification),"
    ayame "making available to the public, and in some countries other activities as well."
    ayame "To \"convey\" a work means any kind of propagation that enables other parties to make or receive copies.  Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying."
    menu:
        "An interactive user interface displays \"Appropriate Legal Notices\" {image=plus1}":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "An interactive user interface displays \"Appropriate Legal Notices\""
        "to the extent that it includes a convenient and prominently visible feature that {image=minus1}":
            $ ayame_points -= 1
            $ ayame_choice_1 = "0"
            p "to the extent that it includes a convenient and prominently visible feature that"
    if ayame_choice_1 == "1":
        show ayame smile with dissolve
        ayame "(1) displays an appropriate copyright notice,"
        ayame "and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided),"
        hide ayame with dissolve

    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame "that licensees may convey the work under this License, and how to view a copy of this License."
        ayame "If the interface presents a list of user commands or options,"
        ayame "such as a menu, a prominent item in the list meets this criterion."
        hide ayame with dissolve
    $ ayame_flags.append("today")
    call screen map1 with dis1

label ayame3:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "Basic Permissions."
    ayame "All rights granted under this License are granted for the term of copyright on the Program,"
    ayame "and are irrevocable provided the stated conditions are met."
    ayame "This License explicitly affirms your unlimited permission to run the unmodified Program."
    menu:
        "The output from running a covered work is covered by this License only if the output, {image=plus1}":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "The output from running a covered work is covered by this License only if the output,"
        "given its content, constitutes a covered work. {image=minus1}":
            $ ayame_points -= 1
            $ ayame_choice_1 = "0"
            p "given its content, constitutes a covered work."
    if ayame_choice_1 == "1":
        show ayame smile with dissolve
        ayame "This License acknowledges your rights of fair use or other equivalent,"
        ayame "as provided by copyright law."
        ayame "You may make, run and propagate covered works that you do not convey,"
        ayame "without conditions so long as your license otherwise remains in force."
        ayame "You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works,"
        hide ayame with dissolve
    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame "provided that you comply with the terms of this License in conveying all material for which you do not control copyright."
        hide ayame with dissolve
    $ ayame_flags.append("today")
    call screen map1 with dis1

label ayame4:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange."
    ayame "b) Convey the object code in, or embodied in, a physical product (including a physical distribution medium),"
    ayame "accompanied by a written offer,"
    ayame "valid for at least three years and valid for as long as you offer spare parts or customer support for that product model,."
    menu:
        "to give anyone who possesses the object code either {image=plus1}":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "to give anyone who possesses the object code either"

        "(1) a copy of the Corresponding Source for all the software in the product that is covered by this License, {image=plus1}":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "(1) a copy of the Corresponding Source for all the software in the product that is covered by this License,"

        "on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or {image=minus1}":
            $ ayame_points -= 1
            $ ayame_choice_1 = "0"
            p "on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or"

    if ayame_choice_1 == "1":
        show ayame smile with dissolve
        ayame "(2) access to copy the Corresponding Source from a network server at no charge."
        ayame "c) Convey individual copies of the object code with a copy of the written offer to provide the Corresponding Source."
        ayame "This alternative is allowed only occasionally and noncommercially,"
        hide ayame with dissolve
    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame "and only if you received the object code with such an offer, in accord with subsection 6b."
        ayame "d) Convey the object code by offering access from a designated place"
        ayame "(gratis or for a charge),"
        hide ayame with dissolve
    $ ayame_flags.append("today")
    call screen map1 with dis1

label ayame5:
    scene black with dissolve
    show bg classroom 3 day with dis1
    show ayame talk with dissolve
    ayame "to the extent that they are valid under applicable law.  If additional permissions apply only to part of the Program,"
    ayame "that part may be used separately under those permissions,"
    ayame "but the entire Program remains governed by this License without regard to the additional permissions."
    ayame "When you convey a copy of a covered work,"
    menu:
        "you may at your option remove any additional permissions from that copy, {image=heart01}":
            $ ayame_points += 1
            $ ayame_choice_1 = "1"
            p "you may at your option remove any additional permissions from that copy,"

        "or from any part of it. {image=minus1}":
            $ ayame_points -= 1
            $ ayame_choice_1 = "0"
            p "or from any part of it."

    if ayame_choice_1 == "1":
        show ayame smile with dissolve
        ayame "(Additional permissions may be written to require their own removal in certain cases when you modify the work.)"
        ayame "You may place additional permissions on material,"
        ayame "added by you to a covered work, for which you have or can give appropriate copyright permission."
        hide ayame with dissolve
        jump ayame_end

    if ayame_choice_1 == "0":
        show ayame angry with dissolve
        ayame " Notwithstanding any other provision of this License, for material you add to a covered work,"
        ayame "you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:"
        ayame "a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or"
        hide ayame with dissolve
        $ ayame_flags.append("today")
        call screen map1 with dis1

label ayame_end:
    scene black with dis1
    if 0 < time_of_day < 12:
        show bg street redux day with dis1
    elif 11 < time_of_day < 18:
        show bg street redux evening with dis1
    elif 17 < time_of_day < 24:
        show bg street redux night with dis1
    show ayame embarrased with dissolve
    "This is the end with Nana!"
    show ayame happy with dis1
    "It's time!"
    show ayame smile with dis1
    "I Love You!"
    show ayame laugh with dis1
    pause
    jump ending