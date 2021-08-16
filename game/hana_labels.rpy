############################################################## Hana's Labels ##############################################################

label hana_labels:
    hide room_lights
    hide map1
    $ current_label = "hana"
    scene black
    if not "first" in hana_flags:
        jump hana1
    elif hana_points == 2:
        jump hana2
    elif hana_points == 3:
        jump hana3
    elif hana_points == 4:
        jump hana4
    elif hana_points == 5:
        jump hana5

label hana1:
    hide room_lights
    show bg room night lightoff with dissolve
    "which is precisely where it is most unacceptable."
    "Therefore, we have designed this version of the GPL to prohibit the practice for those products."
    scene black with dis2
    show hana smile with dissolve
    hana "If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL,"
    hana "as needed to protect the freedom of users."
    hana "Finally, every program is threatened constantly by software patents."
    menu:
        "States should not allow patents to restrict development and use of software on general-purpose computers, {image=plus1}":
            p "States should not allow patents to restrict development and use of software on general-purpose computers,"

    hana "but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary."
    hana "To prevent this, the GPL assures that patents cannot be used to render the program non-free."
    hana "The precise terms and conditions for copying, distribution and modification follow."
    hana "\"This License\" refers to version 3 of the GNU General Public License."
    hide hana with dissolve
    $ hana_flags.append("first")
    $ hana_points += 1
    jump day_end

label hana2:
    show bg room night lightoff with dissolve
    scene black with dis2
    show hana smile with dissolve
    hana "Source Code."
    hana "The \"source code\" for a work means the preferred form of the work for making modifications to it."
    hana "\"Object code\" means any non-source form of a work."
    menu:
        "A \"Standard Interface\" means an interface that either is an official standard defined by a recognized standards body, {image=plus1} \"With Glasses\"":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            $ hana_glasses = False
            p "A \"Standard Interface\" means an interface that either is an official standard defined by a recognized standards body,"
        "or, in the case of interfaces specified for a particular programming language, {image=plus1} \"Without Glasses\"":
            $ hana_points += 1
            $ hana_choice_1 = "2"
            $ hana_glasses = True
            p "or, in the case of interfaces specified for a particular programming language,"
        "... {image=minus1}":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "..."
    if hana_choice_1 == "1":
        show hana smile with dissolve
        hana "one that is widely used among developers working in that language."
        hana "The \"System Libraries\" of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component,"
        hide hana with dissolve
        
    if hana_choice_1 == "2":
        show hana smile with dissolve
        hana "one that is widely used among developers working in that language."
        hana "The \"System Libraries\" of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component,"
        hide hana with dissolve

    if hana_choice_1 == "0":
        show hana angry with dissolve
        hana "but which is not part of that Major Component,"
        hana "and (b) serves only to enable use of the work with that Major Component,"
        hana "or to implement a Standard Interface for which an implementation is available to the public in source code form."
        hide hana with dissolve
    jump day_end

label hana3:
    show bg room night lightoff with dissolve
    scene black with dis1
    show hana smile with dissolve
    hana "Conveying Verbatim Copies."
    hana "You may convey verbatim copies of the Program's source code as you receive it,"
    hana "in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice;"
    hana "keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code;"
    hana "keep intact all notices of the absence of any warranty;"
    hana "and give all recipients a copy of this License along with the Program."
    menu:
        "You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee. {image=plus1}":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee."
        "Conveying Modified Source Versions. {image=minus1}":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "Conveying Modified Source Versions."
    if hana_choice_1 == "1":
        show hana smile with dissolve
        hana "You may convey a work based on the Program, or the modifications to produce it from the Program,"
        hana "a) The work must carry prominent notices stating that you modified it,"
        hana "and giving a relevant date."
        hide hana with dissolve
        
    if hana_choice_1 == "0":
        show hana angry with dissolve
        hana " b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7."
        hana "This requirement modifies the requirement in section 4 to \"keep intact all notices\"."
        hana "c) You must license the entire work, as a whole,"
        hana "under this License to anyone who comes into possession of a copy."
        hide hana with dissolve
    jump day_end

label hana4:
    show bg room night lightoff with dissolve
    scene black with dis2
    show hana smile with dissolve
    hana "family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling."
    hana "In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage."
    hana "For a particular product received by a particular user,"
    hana "\"normally used\" refers to a typical or common use of that class of product,"
    hana "regardless of the status of the particular user or of the way in which the particular user actually uses,"
    hana "or expects or is expected to use, the product."
    menu:
        "A product is a consumer product regardless of whether the product has substantial commercial, {image=plus1}":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "A product is a consumer product regardless of whether the product has substantial commercial,"
        "industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product. {image=plus1}":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product."
        "\"Installation Information\" for a User Product means any methods, procedures, {image=minus1}":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "\"Installation Information\" for a User Product means any methods, procedures,"
    if hana_choice_1 == "1":
        show hana smile with dissolve
        hana "authorization keys,"
        hana "or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source."
        hana "The information must suffice to ensure that the continued functioning of the modified object code is in no case prevented or interfered with solely because modification has been made."
        hide hana with dissolve
        
    if hana_choice_1 == "0":
        show hana angry with dissolve
        hana "If you convey an object code work under this section in, or with,"
        hana "or specifically for use in, a User Product,"
        hana "and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term "
        hana "(regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information."
        hide hana with dissolve
    jump day_end

label hana5:
    show bg room night lightoff with dissolve
    scene black with dis2
    show hana smile with dissolve
    hana "you may add to a covered work material governed by the terms of that license document,"
    hana "provided that the further restriction does not survive such relicensing or conveying."
    hana "If you add terms to a covered work in accord with this section, you must place,"
    hana "in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms."
    hana "Additional terms, permissive or non-permissive, may be stated in the form of a separately written license,"
    hana "or stated as exceptions; the above requirements apply either way."
    menu:
        "8. Termination. {image=heart01}":
            $ hana_points += 1
            $ hana_choice_1 = "1"
            p "8. Termination."

        "You may not propagate or modify a covered work except as expressly provided under this License. {image=minus1}":
            $ hana_points -= 1
            $ hana_choice_1 = "0"
            p "You may not propagate or modify a covered work except as expressly provided under this License."
    if hana_choice_1 == "1":
        show hana smile with dissolve
        hana "Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License"
        hana "(including any patent licenses granted under the third paragraph of section 11)."
        hana "However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated"
        hide hana with dissolve
        call screen hana_love_locations with dis1
        scene black with dissolve
        if _return == 1:
            show bg street redux night with dis1
        elif _return == 2:
            show bg classroom 3 night with dis1
        elif _return == 3:
            show bg jungle night with dis1
        elif _return == 4:
            show bg room night lightoff with dis1
        show hana impressed with dissolve
        "This is the end with Nana!"
        show hana concentrate with dis1
        "It's time!"
        show hana smile with dis1
        "I Love You!"
        show hana amused with dis1
        pause
        jump ending

    if hana_choice_1 == "0":
        show hana angry with dissolve
        hana "(a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and"
        hana "(b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation."
        hana "Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means,"
        hana "this is the first time you have received notice of violation of this License (for any work) from that copyright holder,"
        hide hana with dissolve
        jump day_end