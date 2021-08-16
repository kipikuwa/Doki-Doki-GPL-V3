
image bg room morning = ConditionSwitch(
    "lightswitch" , "room_morning_light_off",
    "not lightswitch", "room_morning_light_on")

image bg room evening = ConditionSwitch(
    "lightswitch" , "room_dusk_light_off",
    "not lightswitch", "room_dusk_light_on")

image bg room night = ConditionSwitch(
    "lightswitch" , "room_night_light_off",
    "not lightswitch", "room_night_light_on")

image bed morning idle = ConditionSwitch(
    "lightswitch" , "bed_morning_light_off_idle",
    "not lightswitch", "bed_morning_light_on_idle")

image bed morning hover = ConditionSwitch(
    "lightswitch" , "bed_morning_light_off_hover",
    "not lightswitch", "bed_morning_light_on_hover")

image bed evening idle = ConditionSwitch(
    "lightswitch" , "bed_dusk_light_off_idle",
    "not lightswitch", "bed_dusk_light_on_idle")

image bed evening hover = ConditionSwitch(
    "lightswitch" , "bed_dusk_light_off_hover",
    "not lightswitch", "bed_dusk_light_on_hover")

image bed night idle = ConditionSwitch(
    "lightswitch" , "bed_night_light_off_idle",
    "not lightswitch", "bed_night_light_on_idle")

image bed night hover = ConditionSwitch(
    "lightswitch" , "bed_night_light_off_hover",
    "not lightswitch", "bed_night_light_on_hover")

image bg house = ConditionSwitch(
    "0 <= time_of_day < 12" , "bg room morning",
    "11 < time_of_day < 18" , "bg room evening",
    "17 < time_of_day <= 24" , "bg room night")

image bed switch idle = ConditionSwitch(
    "0 <= time_of_day < 12" , "bed morning idle",
    "11 < time_of_day < 18" , "bed evening idle",
    "17 < time_of_day <= 24" , "bed night idle")

image bed switch hover = ConditionSwitch(
    "0 <= time_of_day < 12" , "bed morning hover",
    "11 < time_of_day < 18" , "bed evening hover",
    "17 < time_of_day <= 24" , "bed night hover")

image hana amused = ConditionSwitch(
    "hana_glasses" , "hana_amusedg",
    "not hana_glasses" , "hana_amused")

image hana angry = ConditionSwitch(
    "hana_glasses" , "hana_angryg",
    "not hana_glasses" , "hana_angry")

image hana awkward = ConditionSwitch(
    "hana_glasses" , "hana_awkwardg",
    "not hana_glasses" , "hana_awkward")

image hana concentrate = ConditionSwitch(
    "hana_glasses" , "hana_concentrateg",
    "not hana_glasses" , "hana_concentrate")

image hana dissapointed = ConditionSwitch(
    "hana_glasses" , "hana_dissapointedg",
    "not hana_glasses" , "hana_dissapointed")

image hana impressed = ConditionSwitch(
    "hana_glasses" , "hana_impressedg",
    "not hana_glasses" , "hana_impressed")

image hana noemo = ConditionSwitch(
    "hana_glasses" , "hana_noemog",
    "not hana_glasses" , "hana_noemo")

image hana serious = ConditionSwitch(
    "hana_glasses" , "hana_seriousg",
    "not hana_glasses" , "hana_serious")

image hana smile = ConditionSwitch(
    "hana_glasses" , "hana_smileg",
    "not hana_glasses" , "hana_smile")

image hana talk = ConditionSwitch(
    "hana_glasses" , "hana_talkg",
    "not hana_glasses" , "hana_talk")


############################################################## Character Images ##############################################################

image nana amazed = "images/Nana/amazed.png"
image nana angry = "images/Nana/angry.png"
image nana flustered = "images/Nana/flustered.png"
image nana guilty = "images/Nana/guilty.png"
image nana happy = "images/Nana/happy.png"
image nana sad = "images/Nana/sad.png"
image nana smile = "images/Nana/smile.png"
image nana laugh = "images/Nana/laugh.png"
image nana confident = "images/Nana/confident.png"
image nana talk = "images/Nana/talk.png"

image ayame angry = "images/Ayame/angry.png"
image ayame embarrased = "images/Ayame/embarrased.png"
image ayame errkk = "images/Ayame/errkk.png"
image ayame happy = "images/Ayame/happy.png"
image ayame laugh = "images/Ayame/laugh.png"
image ayame lecture = "images/Ayame/lecture.png"
image ayame sad = "images/Ayame/sad.png"
image ayame smile = "images/Ayame/smile.png"
image ayame surprised = "images/Ayame/surprised.png"
image ayame talk = "images/Ayame/talk.png"

image mayo angry = "images/Mayonaise/angry.png"
image mayo awkward = "images/Mayonaise/awkward.png"
image mayo happy = "images/Mayonaise/happy.png"
image mayo emotalk = "images/Mayonaise/emotalk.png"
image mayo noemo = "images/Mayonaise/noemo.png"
image mayo normal = "images/Mayonaise/normal.png"
image mayo sad = "images/Mayonaise/sad.png"
image mayo smile = "images/Mayonaise/smile.png"
image mayo talk = "images/Mayonaise/talk.png"
image mayo wah = "images/Mayonaise/wah.png"

# image hana amused = "images/Hana/noglasses/amused.png"
# image hana angry = "images/Hana/noglasses/angry.png"
# image hana awkward = "images/Hana/noglasses/awkward.png"
# image hana concentrate = "images/Hana/noglasses/concentrate.png"
# image hana dissapointed = "images/Hana/noglasses/dissapointed.png"
# image hana impressed = "images/Hana/noglasses/impressed.png"
# image hana noemo = "images/Hana/noglasses/noemo.png"
# image hana serious = "images/Hana/noglasses/serious.png"
# image hana smile = "images/Hana/noglasses/smile.png"
# image hana talk = "images/Hana/noglasses/talk.png"

# image hana amusedg = "images/Hana/noglasses/amusedg.png"
# image hana angryg = "images/Hana/noglasses/angryg.png"
# image hana awkwardg = "images/Hana/noglasses/awkwardg.png"
# image hana concentrateg = "images/Hana/noglasses/concentrateg.png"
# image hana dissapointedg= "images/Hana/noglasses/dissapointedg.png"
# image hana impressedg = "images/Hana/noglasses/impressedg.png"
# image hana noemog = "images/Hana/noglasses/noemog.png"
# image hana seriousg = "images/Hana/noglasses/seriousg.png"
# image hana smileg = "images/Hana/noglasses/smileg.png"
# image hana talkg = "images/Hana/noglasses/talkg.png"

############################################################## Backgrounds ##############################################################

image bg room morning lightoff = "images/001/room_morning_light_off.jpg"
image bg room morning lighton = "images/001/room_morning_light_off.jpg"
image bg room evening lightoff = "images/001/room_dusk_light_off.jpg"
image bg room evening lighton = "images/001/room_dusk_light_on.jpg"
image bg room night lightoff = "images/001/room_night_light_off.jpg"
image bg room night lighton = "images/001/room_night_light_on.jpg"

image bg street redux day = "images/001/street_redux_day.jpg"
image bg street redux evening = "images/001/street_redux_evening.jpg"
image bg street redux night = "images/001/street_redux_night.jpg"
image bg school gate = "images/001/generic_school_gate.jpg"

image bg classroom 3 day = "images/001/classroom_03_day.jpg"
image bg classroom 3 evening = "images/001/classroom_03_evening.jpg"
image bg classroom 3 night = "images/001/classroom_03_night.jpg"
image bg classroom 4 day = "images/001/classroom_04_day.jpg"

image bg jungle day = "images/001/philippines_003_day.jpg"
image bg jungle afternoon = "images/001/philippines_003_afternoon.jpg"
image bg jungle night = "images/001/philippines_003_night.jpg"

image bg 6hourslater = "images/other/6hourslater.jpg"


############################################################## Other ##############################################################

image heart01 = "images/other/heart01.png"
image plus1 = "images/other/plus1.png"
image minus1 = "images/other/minus1.png"
image lightonkey = "images/other/lighton_key.png"
image lightoffkey = "images/other/lightoff_key.jpg"