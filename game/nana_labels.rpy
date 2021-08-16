############################################################## Nana's Labels ##############################################################

label nana_labels:
    hide room_lights
    hide map1
    $ current_label = "nana"
    scene black
    if not "first" in nana_flags:
        jump nana1
    elif "today" in nana_flags and 0 < time_of_day < 12:
        jump nana0
    elif "today" in nana_flags and 11 < time_of_day < 18:
        jump nanae0
    elif "today" in nana_flags and 17 < time_of_day < 24:
        jump nanan0
    elif nana_points == 2:
        jump nana2
    elif nana_points == 3:
        jump nana3
    elif nana_points == 4:
        jump nana4
    elif nana_points == 5:
        jump nana5

label nana0:
    show bg street redux day with dis1
    "Nothing to do here!"
    $ current_label = "nana"
    call screen map1 with dis1

label nanae0:
    show bg street redux evening with dis1
    "Nothing to do here!"
    $ current_label = "nana"
    call screen map1 with dis1

label nanan0:
    show bg street redux night with dis1
    "Nothing to do here!"
    $ current_label = "nana"
    call screen map1 with dis1

label nana1:
    show bg street redux day with dis1
    show nana laugh with dissolve
    nana "The licenses for most software and other practical works are designed to take away your freedom to share and change the works."
    nana "By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users."
    nana "We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors."
    $ p.name = renpy.input("You can apply it to your programs, too.")
    p "When we speak of free software, we are referring to freedom, not price."
    nana "Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software"
    nana "(and charge for them if you wish),"
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "that you receive source code or can get it if you want it,"
    nana "that you can change the software or use pieces of it in new free programs, and that you know you can do these things."
    menu:
        "To protect your rights, ;{image=plus1}":
            p "To protect your rights,"

    show nana smile with dissolve
    nana "we need to prevent others from denying you these rights or asking you to surrender the rights."
    hide nana with dissolve
    $ nana_flags.append("first")
    $ nana_flags.append("today")
    $ nana_points += 1
    jump ayame_labels

label nana2:
    scene bg street redux day with dis1
    show nana laugh with dissolve
    nana " \"Copyright\" also means copyright-like laws that apply to other kinds of works, such as semiconductor masks."
    nana "\"The Program\" refers to any copyrightable work licensed under this License."
    nana "Each licensee is addressed as \"you\".  \"Licensees\" and \"recipients\" may be individuals or organizations."
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "To \"modify\" a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission,"
    menu:
        "other than the making of an exact copy. {image=plus1}":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "other than the making of an exact copy."

        "The resulting work is called a \"modified version\" of the earlier work or a work \"based on\" the earlier work. {image=minus1}":
            $ nana_points -= 1
            $ nana_choice_1 = "0"
            p "The resulting work is called a \"modified version\" of the earlier work or a work \"based on\" the earlier work."
    if nana_choice_1 == "1":
        show nana smile with dissolve
        nana "A \"covered work\" means either the unmodified Program or a work based on the Program."
        hide nana with dissolve
    if nana_choice_1 == "0":
        show nana angry with dissolve
        nana "To \"propagate\" a work means to do anything with it that, without permission,"
        nana "would make you directly or secondarily liable for infringement under applicable copyright law,"
        nana "except executing it on a computer or modifying a private copy."
        hide nana with dissolve
    $ nana_flags.append("today")
    $ current_label = "nana"
    call screen map1 with dis1

label nana3:
    hide room_lights
    scene black
    show bg street redux day with dis1
    "A \"Major Component\", in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs,"
    nana "or a compiler used to produce the work, or an object code interpreter used to run it."
    show nana guilty with dis1
    nana "The \"Corresponding Source\" for a work in object code form means all the source code needed to generate,"
    nana "install, and (for an executable work) run the object code and to modify the work,"
    nana "including scripts to control those activities.  However, it does not include the work's System Libraries,"
    menu:
        "or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work. {image=plus1}":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work."

        "For example, Corresponding Source includes interface definition files associated with source files for the work, {image=minus1}":
            $ nana_points -= 1
            $ nana_choice_1 = "0"
            p "For example, Corresponding Source includes interface definition files associated with source files for the work,"
    if nana_choice_1 == "1":
        show nana smile with dissolve
        nana "and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require,"
        nana "such as by intimate data communication or control flow between those subprograms and other parts of the work."
        hide nana with dissolve
    if nana_choice_1 == "0":
        show nana angry with dissolve
        nana "The Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source."
        nana "The Corresponding Source for a work in source code form is that same work."
        hide nana with dissolve
    $ nana_flags.append("today")
    $ current_label = "nana"
    call screen map1 with dis1

label nana4:
    scene bg street redux day with dis1
    show nana laugh with dissolve
    nana "This License will therefore apply, along with any applicable section 7 additional terms,"
    nana "to the whole of the work, and all its parts, regardless of how they are packaged."
    nana "This License gives no permission to license the work in any other way,"
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "but it does not invalidate such permission if you have separately received it."
    nana "d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however,"
    nana "if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so."
    menu:
        "A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, {image=plus1}":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work,"

        "and which are not combined with it such as to form a larger program, {image=plus1}":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "and which are not combined with it such as to form a larger program,"
        
        "in or on a volume of a storage or distribution medium, is called an \"aggregate\" {image=plus1}":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "in or on a volume of a storage or distribution medium, is called an \"aggregate\""

        "if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit. {image=minus1}":
            $ nana_points -= 1
            $ nana_choice_1 = "0"
            p "if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit."
        
    if nana_choice_1 == "1":
        show nana smile with dissolve
        nana "Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate."
        nana "Conveying Non-Source Forms."
        hide nana with dissolve
    if nana_choice_1 == "0":
        show nana angry with dissolve
        nana "You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the"
        nana "machine-readable Corresponding Source under the terms of this License, in one of these ways:"
        nana "a) Convey the object code in, or embodied in, a physical product (including a physical distribution medium),"
        hide nana with dissolve
    $ nana_flags.append("today")
    $ current_label = "nana"
    call screen map1 with dis1

label nana5:
    scene bg street redux day with dis1
    show nana laugh with dissolve
    nana "But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product"
    nana "(for example, the work has been installed in ROM)."
    nana "The requirement to provide Installation Information does not include a requirement to continue to provide support service,"
    scene black with dissolve
    show bg school gate with dis1
    show nana confident with dissolve
    nana "warranty, or updates for a work that has been modified or installed by the recipient,"
    nana "or for the User Product in which it has been modified or installed."
    nana "Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network."
    menu:
        "Corresponding Source conveyed, and Installation Information provided, {image=heart01}":
            $ nana_points += 1
            $ nana_choice_1 = "1"
            p "Corresponding Source conveyed, and Installation Information provided,"

        "in accord with this section must be in a format that is publicly documented {image=minus1}":
            $ nana_points -= 1
            $ nana_choice_1 = "0"
            p "in accord with this section must be in a format that is publicly documented"
        
    if nana_choice_1 == "1":
        show nana smile with dissolve
        nana "(and with an implementation available to the public in source code form),"
        nana "and must require no special password or key for unpacking, reading or copying."
        hide nana with dissolve
        jump nana_end
        
    if nana_choice_1 == "0":
        show nana angry with dissolve
        nana "7. Additional Terms."
        nana "\"Additional permissions\" are terms that supplement the terms of this License by making exceptions from one or more of its conditions."
        nana "Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License,"
        hide nana with dissolve
        $ nana_flags.append("today")
        $ current_label = "nana"
        call screen map1 with dis1

label nana_end:
    scene black with dis1
    if 0 < time_of_day < 12:
        show bg street redux day with dis1
    elif 11 < time_of_day < 18:
        show bg street redux evening with dis1
    elif 17 < time_of_day < 24:
        show bg street redux night with dis1
    else:
        show bg street redux day with dis1
    show nana amazed with dissolve
    "This is the end with Nana!"
    show nana happy with dis1
    "It's time!"
    show nana smile with dis1
    "I Love You!"
    show nana laugh with dis1
    pause
    jump ending