import numpy
import random
from collections import OrderedDict

########################################################
########### Skewed Random Number Generator #############
########################################################
# ------------------------------------------------------#
# @author: Yong Chul Yoon
#
# The function takes in 5 different integers greater than 1.
# Each input is responsible for modulating the probability of
# getting certain number in a hard-coded range:
#
# x1 = [1.0. 1.2]; x2 = [1.2, 1.4]; x3 = [1.4, 1.6];
# x4 = [1.6, 1.8]; x5 = [1.8, 2.0].
#
# For example, if you want to generate a number between 1.2 and 1.4
# twice as often as other numbers, then input is:
# [x1, x2, x3, x4, x5] = [1, 2, 1, 1, 1]
# You could easily alter the range by hard-coding if you wish
# but this is probably sufficient for our purpose.
# -------------------------------------------------------#
##########################################################


def skew_random_gen(x1, x2, x3, x4, x5):
    # Generate a random number between 0 and 100
    # with step size of 1
    r = numpy.arange(0, 100, 1)

    # Define probability interval for 100 numbers.
    # x1 = 0~19; x2 = 20~39; x3 = 40~59; x4 = 60~79; x5 = 80~100
    x = ([x1] * 20 + [x2] * 20
         + [x3] * 20 + [x4] * 20
         + [x5] * 20)

    # Normalize the probability to 1.0
    x /= numpy.sum(x)

    # Generate random sample.
    # Divide by 100 and add 1 so the number is between 1 and 2.
    result = numpy.random.choice(r, 1, p=x) / 100 + 1
    return float(result)

# Create Classes for Client, Job, Weapon #


# Client Class
class Client:

    def __init__(self, id, items):
        self.id = id
        self.name = items['Name']
        self.age = items['Age']
        self.occupation = items['Occupation']
        self.flat_modifiers = items['Stats']['flat_modifiers'] if items['Stats']['flat_modifiers'] else None
        self.percentage_modifiers = items['Stats']['percentage_modifiers'] if 'percentage_modifiers' in items['Stats'].keys() else None
        self.stat_text = items['Stats']['text']
        self.bio = items['Bio']

    def print_client(self): # 62
        print(' ________')
        print('| Client | _____')
        print('|________||_____|______________________________________________')
        print('|                                                             |')
        print('| Name: ' + self.name + (' ' * (54 - len(self.name))) + '|')
        print('|                                                             |')
        print('| Age: ' + self.age + (' ' * (55 - len(self.age))) + '|')
        print('|                                                             |')
        print('| Occupation: ' + self.occupation + (' ' * (48 - len(self.occupation))) + '|')
        print('|                                                             |')
        print('| Stats:                                                      |')
        for stat in self.stat_text:
            print('|  - ' + stat + (' ' * (57 - len(stat))) + '|')
        bio_list = self.slice_bio(self.bio)
        print('|                                                             |')
        print('| Bio: ' + bio_list[0])
        for ind in range(1, len(bio_list)):
            print('|      ' + bio_list[ind])
        print('|_____________________________________________________________|')

    def slice_bio(self, bio):
        split_bio = bio.split(" ")
        final_list = []
        count = 0
        tmp = []
        for word in split_bio:
            if count + len(word) + 1 < 56:
                count += len(word) + 1
                tmp.append(word + " ")
            else:
                final_list.append("".join(tmp) + (' ' * (55 - len("".join(tmp)))) + "|")
                count = len(word) + 1
                tmp = [word + " "]
        final_list.append("".join(tmp) + (' ' * (55 - len("".join(tmp)))) + "|")
        return final_list


# Job Class
class Job:

    def __init__(self, id, items):
        self.id = id
        self.title = items['Title']
        self.desc = items['Desc']
        self.restrictions = items['Restrictions']
        self.parameters = items['Parameters']
        self.flat_modifiers = items['Stats']['flat_modifiers'] if 'flat_modifiers' in items['Stats'].keys() else None
        self.percentage_modifiers = items['Stats']['percentage_modifiers'] if 'percentage_modifiers' in items['Stats'].keys() else None
        self.stat_text = items['Stats']['text']

    def print_job(self):
        print('           _____')
        print(' ________ | Job |')
        print('|________||_____|______________________________________________')
        print('|                                                             |')
        print('| Title: ' + self.title + (' ' * (53 - len(self.title))) + '|')
        print('|                                                             |')
        desc_list = self.slice_desc(self.desc)
        print('| Description: ' + desc_list[0])
        for ind in range(1, len(desc_list)):
            print('|              ' + desc_list[ind])
        print('|                                                             |')
        print('| Restrictions:                                               |')
        print('|  - Volume: ' + str(self.restrictions[0]) + (' ' * (49 - len(str(self.restrictions[0])))) + '|')
        print('|  - Weapon Types: ' + ", ".join(self.restrictions[1]) + (' ' * (43 - len(", ".join(self.restrictions[1])))) + '|')
        print('|  - Budget: $' + str(self.restrictions[2]) + (' ' * (48 - len(str(self.restrictions[2])))) + '|')
        print('|                                                             |')
        print('| Stats:                                                      |')
        for stat in self.stat_text:
            print('|  - ' + stat + (' ' * (57 - len(stat))) + '|')
        print('|_____________________________________________________________|')


    def slice_desc(self, desc):
        split_desc = desc.split(" ")
        final_list = []
        count = 0
        tmp = []
        for word in split_desc:
            if count + len(word) + 1 < 49:
                count += len(word) + 1
                tmp.append(word + " ")
            else:
                final_list.append("".join(tmp) + (' ' * (47 - len("".join(tmp)))) + "|")
                count = len(word) + 1
                tmp = [word + " "]
        final_list.append("".join(tmp) + (' ' * (47 - len("".join(tmp)))) + "|")
        return final_list


# Weapon Class
class Weapon:

    def __init__(self, id, items):
        self.id = id
        self.name = items['Name']
        self.type = items['Type']
        self.volume = items['Volume']
        self.cost = items['Cost']
        self.parameters = items['Parameters']
        self.flavor_text = items['Flavor_Text']

    def print_weapon(self):
        print(' _________________________________________________________________________')
        print('| *' + self.name + '*' + (' ' * (24-len(self.name))) +
              'Vol: ' + str(self.volume) + (' ' * (9-len(str(self.volume)))) +
              'Cost: ' + str(self.cost) + (' ' * (9-len(str(self.cost)))) +
              'Weight: ' + str(self.parameters[3]) + (' ' * (9-len(str(self.parameters[3])))) + '|')
        print('| ' + 'Type: ' + self.type.upper() + (' ' * (20-len(self.type))) +
              'LTH: ' + str(self.parameters[0]) + (' ' * (9-len(str(self.parameters[0])))) +
              'STL: ' + str(self.parameters[1]) + (' ' * (10-len(str(self.parameters[1])))) +
              'RNG: ' + str(self.parameters[2]) + (' ' * (12-len(str(self.parameters[2])))) + '|')
        print('|_________________________________________________________________________|')

# Initialize all variables #


# Vectors/Variables for Success Calculation
mission_vector = numpy.array([0.0, 0.0, 0.0, 0.0])
target_vector = numpy.array([0.0, 0.0, 0.0, 0.0])
success_vector = numpy.array([0.0, 0.0, 0.0, 0.0])
success_luck = None

# Jobs & Clients
jobs = OrderedDict({
    0: {
        'Title': 'Armstrong',
        'Desc': 'An old friend is back in town. That friend needs to be killed. Quiety.',
        'Restrictions': [7, ['pistol', 'knife'], 700],  # [Volume, [WeaponType/s], Budget]
        'Parameters': numpy.array([10, 5, 2, 2]),  # [Lethality, Stealth, Range, Weight]
        'Stats': {
            'text': ['Pistol Efficiency: +5% Lethality for Pistols', 'Trained Assassin: +2 Stealth',
                     'Job Environment - Dark: -0.5 Range', 'Close Quarters: +10% Stealth for Knives'],
            'percentage_modifiers': {'pistol': [0, 0.05], 'knife': [1, 0.1]},  # [Parameter, Modifier]
            'flat_modifiers': {1: 2, 2: -0.5}  # 1 - stealth, 2 - range
        }
    },
    1: {
        'Title': 'A Requiem for a G',
        'Desc': 'Duty calls for old G, as Senegal calls for his service once more.',
        'Restrictions': [15, ['none'], 2000],  # [Volume, [WeaponType/s], Budget]
        'Parameters': numpy.array([22, 1, 3, 4]),  # [Lethality, Stealth, Range, Weight]
        'Stats': {
            'text': ['Punching Expert: +1 Lethality', 'Clumsy Hands: -1 Range'],
            'flat_modifiers': {0: 1, 2: -1}  # 1 - stealth, 2 - range
        }
    }
})

clients = OrderedDict({
    0: {
        'Name': 'Y O N C E',
        'Age': 'unknown',
        'Occupation': 'Singer',
        'Stats': {
            'text': ['Pistol Efficiency: +5% Lethality for Pistols', 'Trained Assassin: +2 Stealth'],
            'percentage_modifiers': {'pistol': 0.05},
            'flat_modifiers': {2: 2}
        },
        'Bio': 'Y O N C E is an immortal singer/songwriter from the world famous band SUCHMOS. After sacrificing his '
               'old band-mates in 2020 and drinking their blood, he gained eternal life and youth. Y O N C E normally '
               'spends his days staring at mirrors and writing new songs, but rumours are that an old band mate '
               'survived the ritual and is back to take revenge on him.'
    },
    1: {
        'Name': 'G',
        'Age': 'unknown',
        'Occupation': 'unknown',
        'Stats': {
            'text': ['Punching Expert: +1 Lethality', 'Clumsy Hands: -1 Range'],
            'flat_modifiers': {0: 1, 2: -1}
        },
        'Bio': 'G is an enigma. No one knows very much about his past, except for the fact that he wears an old '
               'orange uniform. Rumours are, he never takes it off.'
    }
})

# Weapons
weapons = OrderedDict({
    0: {
        'Name': 'AK-47',
        'Type': 'rifle',
        'Volume': 5,
        'Cost': 3600,
        'Parameters': numpy.array([15, -2, 5, 3.6]),  # [Lethality, Stealth, Range, Weight]
        'Flavor_Text': 'As reliable as they come. The tried and true AK-47 is still used today, decades after it\'s inception.'
    },
    1: {
        'Name': 'Glock 19',
        'Type': 'pistol',
        'Volume': 1,
        'Cost': 455,
        'Parameters': numpy.array([6, 1, 2, 0.59]),  # [Lethality, Stealth, Range, Weight]
        'Flavor_Text': 'No modern pistol is more iconic than the Glock. Smart, effective, and lethal, the Glock is a '
                       'go to weapon for any mercenary.'
    },
    2: {
        'Name': 'HK P30',
        'Type': 'pistol',
        'Volume': 0.8,
        'Cost': 915,
        'Parameters': numpy.array([9, 2, 2, 0.65]),  # [Lethality, Stealth, Range, Weight]
        'Flavor_Text': 'Chambered in .40 S&W, the P30 packs peak German efficiency into a deadly pistol.'
    },
    3: {
        'Name': 'S35VN Combat Knife',
        'Type': 'knife',
        'Volume': 0.5,
        'Cost': 325,
        'Parameters': numpy.array([12, 4, 0, 0.32]),  # [Lethality, Stealth, Range, Weight]
        'Flavor_Text': 'When it\'s time to get up close and personal, you want a reliable knife. Meet the S35VN.'
    },
    4: {
        'Name': 'KRISS Vector',
        'Type': 'smg',
        'Volume': 1.6,
        'Cost': 1349,
        'Parameters': numpy.array([9, 3, 4, 2.7]),  # [Lethality, Stealth, Range, Weight]
        'Flavor_Text': 'Expensive but compact, the Vector is the prime gun for stealthiness and lethality.'
    },
    5: {
        'Name': 'Cheytac M300',
        'Type': 'sniper',
        'Volume': 4,
        'Cost': 9135,
        'Parameters': numpy.array([20, 0, 10, 9.5]),  # [Lethality, Stealth, Range, Weight]
        'Flavor_Text': 'The lighter variant of the M200, the M300 still provides the same range and accuracy; '
                       'guaranteed to blow the minds of your enemies.'
    }
})

# Instantiate arrays of objects
all_clients = [Client(i, clients[i]) for i in range(len(clients.keys()))]
all_jobs = [Job(j, jobs[j]) for j in range(len(jobs.keys()))]
all_weapons = [Weapon(k, weapons[k]) for k in range(len(weapons.keys()))]

# Helper Methods #


# For printing
def print_weapon_list():
    print("Here are the weapons in your inventory:\n")
    for i in range(len(all_weapons)):
        print("[" + str(i) + "]")
        all_weapons[i].print_weapon()
        print("\n")


def print_sell_list():
    print("--- Selected ---\n")
    for i in range(len(weapons_to_sell)):
        print("[" + str(i) + "]")
        print(weapons_to_sell[i].print_weapon())
        print("\n")


def print_parameter_status(job):
    print("Current Status: ")
    print("--Restrictions--")
    print("Volume: " + str(sum([w.volume for w in weapons_to_sell])) + "/" + str(job.restrictions[0]))
    print("Weapon Types: " + ", ".join([w.type for w in weapons_to_sell]))
    print("Budget: " + str(sum([w.cost for w in weapons_to_sell])) + "/" + str(job.restrictions[2]))
    print("--Parameters--")
    print("Weight: " + str(sum([w.parameters[3] for w in weapons_to_sell])) + "/" + str(target_vector[3]))
    print("Lethality: " + str(sum([w.parameters[0] for w in weapons_to_sell])) + "/" + str(target_vector[0]))
    print("Stealth: " + str(sum([w.parameters[1] for w in weapons_to_sell])) + "/" + str(target_vector[1]))
    print("Range: " + str(max([w.parameters[2] for w in weapons_to_sell])) + "/" + str(target_vector[2]))


# Calculations
def calculate_weapon_modifiers(job):
    if not job.percentage_modifiers:
        return
    modifier_list = job.percentage_modifiers
    for weapon in weapons_to_sell:
        if weapon.type in modifier_list.keys():
            modifier = modifier_list[weapon.type]
            weapon.parameters[modifier[0]] += (weapon.parameters[modifier[0]] * modifier[1])


def check_restrictions(job):
    job_restrictions = job.restrictions
    volume_restriction = job_restrictions[0]
    type_restrictions = job_restrictions[1]
    budget_restriction = job_restrictions[2]
    type_flag = True
    volume_flag = True
    budget_flag = True
    if sum([w.volume for w in weapons_to_sell]) > volume_restriction: # check volume
        volume_flag = False
        print("Volume restriction not met.")
    for t in [w.type for w in weapons_to_sell]: # check weapon types
        if t not in type_restrictions and 'none' not in type_restrictions:
            type_flag = False
            print("Type restriction not met.")
            break
    if sum([w.cost for w in weapons_to_sell]) > budget_restriction:
        budget_flag = False
        print("Budget restriction not met.")
    # If all flags are True, restrictions passed. Else failed.
    if type_flag and volume_flag and budget_flag:
        return True
    else:
        return False


def check_continue():
    global mission_vector
    global success_vector
    global target_vector
    if check_restrictions(current_job):
        calculate_weapon_modifiers(current_job)
        for weapon in weapons_to_sell:
            mission_vector += weapon.parameters
        success_vector = mission_vector - target_vector
        print("Success vector: ", success_vector)
        print("Mission vector: ", mission_vector)
        return True
    else:
        print("Mission failed. We'll get em\' next time.")
        return False


# Inventory
def pick_weapons():
    while True:
        print("-------------------------------------------")

        # Pick a weapon to add
        print_weapon_list()
        print("Pick a weapon to sell using the ID above each weapon. (Enter -1 to not pick a weapon)")
        weapon_id = int(input("Enter ID: "))
        if weapon_id != -1:
            weapons_to_sell.append(all_weapons.pop(weapon_id))
        print("-------------------------------------------")
        print_parameter_status(current_job)
        print("-------------------------------------------")

        # Add more?
        add_more = input("Would you like to add more weapons? [Y/N]")
        if add_more in ["Y", "y", "Yes", "yes", "YES"]:
            continue

        # Edit inventory?
        edit_input = input("Would you like to edit your inventory? [Y/N]")
        if edit_input in ["Y", "y", "Yes", "yes", "YES"]:
            edit_inventory()

        # Finalize?
        finish = input("Finalize your choices? [Y/N]")
        print(type(finish))
        if finish in ["Y", "y", "Yes", "yes", "YES"]:
            return


def edit_inventory():
    print_sell_list()
    print("Enter ID of weapon you want to remove.")
    edit_id = int(input("Enter ID: "))
    all_weapons.append(weapons_to_sell.pop(edit_id))


# ------------------------------------------------ #

# Misc Initialization
weapons_to_sell = []

# Game Loop
if __name__ == "__main__":
    #job_picker = random.randint(0, 1)

    current_job = all_jobs[0]
    current_client = all_clients[0]

    target_vector = current_job.parameters

    print("Welcome to the Basic Mechanics Game Demo.")
    print("A job and client has been assigned to you. See below for details:")
    current_client.print_client()
    current_job.print_job()

    # Pick Weapons to Sell #

    print("Please supply the client with the appropriate weapons.")

    # Core game loop: pick weapons -> check if restrictions are met -> if so, calculate / if not, re-pick
    while True:
        pick_weapons()
        print("-------------------------------------------")
        print("SELECTED WEAPONS:")
        print_sell_list()
        if check_continue():
            # Calculate success from here
            success_luck = skew_random_gen(500, 100, 20, 10, 5)
            # [ high, low ]
            lethality_success_range = numpy.array([target_vector[0] * success_luck, target_vector[0] -
                                            ((target_vector[0] * success_luck) - target_vector[0])])
            stealth_success_rate = numpy.array([target_vector[1] * success_luck, target_vector[1] -
                                            ((target_vector[1] * success_luck) - target_vector[1])])
            print("lethality ", lethality_success_range)
            print("stealth ", stealth_success_rate)
            print("luck: " + str(success_luck))
            break
        else:
            # Give choice to abandon job.
            print("-------------------------------------------")
            if input("Abandon job?[Y/N]") in ["Y", "y", "Yes", "yes", "YES"]:
                exit(0)
            # Go back to picking weapons
            else:
                continue




