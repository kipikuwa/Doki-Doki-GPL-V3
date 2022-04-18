
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

image nana amazed = "images/Nana/amazed.webp"
image nana angry = "images/Nana/angry.webp"
image nana flustered = "images/Nana/flustered.webp"
image nana guilty = "images/Nana/guilty.webp"
image nana happy = "images/Nana/happy.webp"
image nana sad = "images/Nana/sad.webp"
image nana smile = "images/Nana/smile.webp"
image nana laugh = "images/Nana/laugh.webp"
image nana confident = "images/Nana/confident.webp"
image nana talk = "images/Nana/talk.webp"

image ayame angry = "images/Ayame/angry.webp"
image ayame embarrased = "images/Ayame/embarrased.webp"
image ayame errkk = "images/Ayame/errkk.webp"
image ayame happy = "images/Ayame/happy.webp"
image ayame laugh = "images/Ayame/laugh.webp"
image ayame lecture = "images/Ayame/lecture.webp"
image ayame sad = "images/Ayame/sad.webp"
image ayame smile = "images/Ayame/smile.webp"
image ayame surprised = "images/Ayame/surprised.webp"
image ayame talk = "images/Ayame/talk.webp"

image mayo angry = "images/Mayonaise/angry.webp"
image mayo awkward = "images/Mayonaise/awkward.webp"
image mayo happy = "images/Mayonaise/happy.webp"
image mayo emotalk = "images/Mayonaise/emotalk.webp"
image mayo noemo = "images/Mayonaise/noemo.webp"
image mayo normal = "images/Mayonaise/normal.webp"
image mayo sad = "images/Mayonaise/sad.webp"
image mayo smile = "images/Mayonaise/smile.webp"
image mayo talk = "images/Mayonaise/talk.webp"
image mayo wah = "images/Mayonaise/wah.webp"

# image hana amused = "images/Hana/noglasses/amused.webp"
# image hana angry = "images/Hana/noglasses/angry.webp"
# image hana awkward = "images/Hana/noglasses/awkward.webp"
# image hana concentrate = "images/Hana/noglasses/concentrate.webp"
# image hana dissapointed = "images/Hana/noglasses/dissapointed.webp"
# image hana impressed = "images/Hana/noglasses/impressed.webp"
# image hana noemo = "images/Hana/noglasses/noemo.webp"
# image hana serious = "images/Hana/noglasses/serious.webp"
# image hana smile = "images/Hana/noglasses/smile.webp"
# image hana talk = "images/Hana/noglasses/talk.webp"

# image hana amusedg = "images/Hana/noglasses/amusedg.webp"
# image hana angryg = "images/Hana/noglasses/angryg.webp"
# image hana awkwardg = "images/Hana/noglasses/awkwardg.webp"
# image hana concentrateg = "images/Hana/noglasses/concentrateg.webp"
# image hana dissapointedg= "images/Hana/noglasses/dissapointedg.webp"
# image hana impressedg = "images/Hana/noglasses/impressedg.webp"
# image hana noemog = "images/Hana/noglasses/noemog.webp"
# image hana seriousg = "images/Hana/noglasses/seriousg.webp"
# image hana smileg = "images/Hana/noglasses/smileg.webp"
# image hana talkg = "images/Hana/noglasses/talkg.webp"

############################################################## Backgrounds ##############################################################

image bg room morning lightoff = "images/001/room_morning_light_off.webp"
image bg room morning lighton = "images/001/room_morning_light_off.webp"
image bg room evening lightoff = "images/001/room_dusk_light_off.webp"
image bg room evening lighton = "images/001/room_dusk_light_on.webp"
image bg room night lightoff = "images/001/room_night_light_off.webp"
image bg room night lighton = "images/001/room_night_light_on.webp"

image bg street redux day = "images/001/street_redux_day.webp"
image bg street redux evening = "images/001/street_redux_evening.webp"
image bg street redux night = "images/001/street_redux_night.webp"
image bg school gate = "images/001/generic_school_gate.webp"

image bg classroom 3 day = "images/001/classroom_03_day.webp"
image bg classroom 3 evening = "images/001/classroom_03_evening.webp"
image bg classroom 3 night = "images/001/classroom_03_night.webp"
image bg classroom 4 day = "images/001/classroom_04_day.webp"

image bg jungle day = "images/001/philippines_003_day.webp"
image bg jungle afternoon = "images/001/philippines_003_afternoon.webp"
image bg jungle night = "images/001/philippines_003_night.webp"

image bg 6hourslater = "images/other/6hourslater.webp"


############################################################## Other ##############################################################

image heart01 = "images/other/heart01.webp"
image plus1 = "images/other/plus1.webp"
image minus1 = "images/other/minus1.webp"
image lightonkey = "images/other/lighton_key.webp"
image lightoffkey = "images/other/lightoff_key.webp"