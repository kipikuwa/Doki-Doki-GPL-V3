############################################################## Mayo's Labels ##############################################################

label mayo_labels:
    hide room_lights
    hide map1
    $ current_label = "mayo"
    scene black
    if not "first" in mayo_flags:
        jump mayo1
    elif mayo_points == 2:
        jump mayo2
    elif mayo_points == 3:
        jump mayo3
    elif mayo_points == 4:
        jump mayo4
    elif mayo_points == 5:
        jump mayo5
    
label mayo1:
    hide room_lights
    scene black with dissolve
    show bg street redux evening with dis1
    "You must make sure that they, too, receive or can get the source code."
    show mayo normal with dissolve
    mayo "And you must show them these terms so they know their rights."
    mayo "Developers that use the GNU GPL protect your rights with two steps:"
    menu:
        "(1) assert copyright on the software, {image=plus1}":
            p "and (2) offer you this License giving you legal permission to copy, distribute and/or modify it."
    show mayo smile with dissolve
    mayo "or the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software.  For both users' and authors' sake,"
    mayo "the GPL requires that modified versions be marked as changed,"
    mayo "so that their problems will not be attributed erroneously to authors of previous versions."
    mayo "Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so."
    hide mayo with dissolve
    "This is fundamentally incompatible with the aim of protecting users' freedom to change the software."
    "The systematic pattern of such abuse occurs in the area of products for individuals to use,"
    $ mayo_flags.append("first")
    $ mayo_points += 1
    jump hana_labels

label mayo2:
    scene black with dissolve
    if 0 < time_of_day < 12:
        show bg jungle day with dis1
    elif 11 < time_of_day < 18:
        show bg jungle afternoon with dis1
    elif 17 < time_of_day < 24:
        show bg jungle night with dis1
    show mayo normal with dissolve
    mayo "Propagation includes copying, distribution (with or without modification),"
    mayo "making available to the public, and in some countries other activities as well."
    mayo "To \"convey\" a work means any kind of propagation that enables other parties to make or receive copies.  Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying."
    menu:
        "An interactive user interface displays \"Appropriate Legal Notices\" {image=plus1}":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "An interactive user interface displays \"Appropriate Legal Notices\""
        "to the extent that it includes a convenient and prominently visible feature that {image=minus1}":
            $ mayo_points -= 1
            $ mayo_choice_1 = "0"
            p "to the extent that it includes a convenient and prominently visible feature that"
    if mayo_choice_1 == "1":
        show mayo smile with dissolve
        mayo "(1) displays an appropriate copyright notice,"
        mayo "and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided),"
    if mayo_choice_1 == "0":
        show mayo angry with dissolve
        mayo "that licensees may convey the work under this License, and how to view a copy of this License."
        mayo "If the interface presents a list of user commands or options,"
        mayo "such as a menu, a prominent item in the list meets this criterion."
    hide mayo with dissolve
    call screen map1 with dis1

label mayo3:
    scene black with dissolve
    if 0 < time_of_day < 12:
        show bg jungle day with dis1
    elif 11 < time_of_day < 18:
        show bg jungle afternoon with dis1
    elif 17 < time_of_day < 24:
        show bg jungle night with dis1
    show mayo normal with dissolve
    mayo "Those thus making or running the covered works for you must do so exclusively on your behalf,"
    mayo "under your direction and control,"
    mayo "on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you."
    menu:
        "Conveying under any other circumstances is permitted solely under the conditions stated below. {image=plus1}":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "Conveying under any other circumstances is permitted solely under the conditions stated below."
        "Sublicensing is not allowed; section 10 makes it unnecessary. {image=minus1}":
            $ mayo_points -= 1
            $ mayo_choice_1 = "0"
            p "Sublicensing is not allowed; section 10 makes it unnecessary."
    if mayo_choice_1 == "1":
        show mayo smile with dissolve
        mayo "Protecting Users' Legal Rights From Anti-Circumvention Law."
        mayo "No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996,"
        mayo "similar laws prohibiting or restricting circumvention of such measures."
        hide mayo with dissolve
    if mayo_choice_1 == "0":
        show mayo angry with dissolve
        mayo "When you convey a covered work,"
        mayo "you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work,"
        mayo "and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work's users,"
        mayo "your or third parties' legal rights to forbid circumvention of technological measures."
        hide mayo with dissolve
    call screen map1 with dis1

label mayo4:
    scene black with dissolve
    if 0 < time_of_day < 12:
        show bg jungle day with dis1
    elif 11 < time_of_day < 18:
        show bg jungle afternoon with dis1
    elif 17 < time_of_day < 24:
        show bg jungle night with dis1
    show mayo normal with dissolve
    mayo "and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge."
    mayo "You need not require recipients to copy the Corresponding Source along with the object code."
    mayo "If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party)"
    menu:
        "that supports equivalent copying facilities, {image=plus1}":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "that supports equivalent copying facilities,"
        "provided you maintain clear directions next to the object code saying where to find the Corresponding Source. {image=plus1}":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "provided you maintain clear directions next to the object code saying where to find the Corresponding Source."
        "Regardless of what server hosts the Corresponding Source, {image=minus1}":
            $ mayo_points -= 1
            $ mayo_choice_1 = "0"
            p "Regardless of what server hosts the Corresponding Source,"

    if mayo_choice_1 == "1":
        show mayo smile with dissolve
        mayo "e) Convey the object code using peer-to-peer transmission,"
        mayo "provided you inform other peers where the object code and Corresponding Source of the work are being offered to the general public at no charge under subsection 6d."
        mayo "A separable portion of the object code,"
        hide mayo with dissolve
    if mayo_choice_1 == "0":
        show mayo angry with dissolve
        mayo "whose source code is excluded from the Corresponding Source as a System Library,"
        mayo "need not be included in conveying the object code work."
        mayo "A \"User Product\" is either (1) a \"consumer product\","
        mayo "which means any tangible personal property which is normally used for personal,"
        hide mayo with dissolve
    call screen map1 with dis1

label mayo5:
    scene black with dissolve
    if 0 < time_of_day < 12:
        show bg jungle day with dis1
    elif 11 < time_of_day < 18:
        show bg jungle afternoon with dis1
    elif 17 < time_of_day < 24:
        show bg jungle night with dis1
    show mayo normal with dissolve
    mayo "b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or"
    mayo "c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or"
    mayo "d) Limiting the use for publicity purposes of names of licensors or authors of the material; or"
    menu:
        "e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or {image=heart01}":
            $ mayo_points += 1
            $ mayo_choice_1 = "1"
            p "e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or"

        "f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material {image=minus1}":
            $ mayo_points -= 1
            $ mayo_choice_1 = "0"
            p "f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material"

    if mayo_choice_1 == "1":
        show mayo smile with dissolve
        mayo "(or modified versions of it) with contractual assumptions of liability to the recipient,"
        mayo "for any liability that these contractual assumptions directly impose on those licensors and authors."
        mayo "All other non-permissive additional terms are considered \"further restrictions\" within the meaning of section 10."
        hide mayo with dissolve
        jump mayo_end

    if mayo_choice_1 == "0":
        show mayo angry with dissolve
        mayo "If the Program as you received it, or any part of it,"
        mayo "contains a notice stating that it isngoverned by this License along with a term that is a further restriction,"
        mayo "you may remove that term."
        mayo "If a license document contains a further restriction but permits relicensing or conveying under this License,"
        hide mayo with dissolve
        call screen map1 with dis1

label mayo_end:
    scene black with dissolve
    if 0 < time_of_day < 12:
        show bg jungle day with dis1
    elif 11 < time_of_day < 18:
        show bg jungle afternoon with dis1
    elif 17 < time_of_day < 24:
        show bg jungle night with dis1
    show mayo emotalk with dissolve
    "This is the end with Nana! [time_of_day] "
    show mayo happy with dis1
    "It's time!"
    show mayo smile with dis1
    "I Love You!"
    show mayo wah with dis1
    pause
    jump ending
