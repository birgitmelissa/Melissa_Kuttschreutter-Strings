# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer1 = 'Ruud Gullit'
scorer2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer1  + ' ' + str(goal_0) + ',' + ' ' + scorer2  + ' ' + str(goal_1)

report = f"{scorer1} scored in the {int(goal_0)}nd minute\n{scorer2} scored in the {int(goal_1)}th minute"

player = 'Ronald Koeman'
first_name = player[0:player.find(" ")]
last_name_len = len(player[player.find(" ")+1:])
name_short = player[0:1] + "." + player[player.find(" "):]
chant1 = (first_name + "!" + " ") * len(first_name)
chant = chant1[:-1]
good_chant = (chant != " ")