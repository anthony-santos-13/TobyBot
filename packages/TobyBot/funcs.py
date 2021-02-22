import random
import itertools

def rumble_sequence(n):
    """Returns a sequence of numbers from 1 to n in random order."""
    # range starts with 0 and ends with n-1
    seq = list(range(n))
    # but Royal Rumbles start with 1 and ends with n
    incr_seq = [i+1 for i in seq] 
    output_seq = random.sample(incr_seq, n)

    return output_seq

def assign_rumble(members, n):
    """Accepts a list of members and assigns an even amount of random numbers from 1 to n to each member.\n
    Returns a list of formatted message strings."""

    dict_list = []
    # shuffle names
    members = random.sample(members, len(members))
    for member in members:
        dict_list.append({"member": member, "numbers": []})

    # get a random sequence
    rumble_seq = rumble_sequence(n)

    # cycle over names repeatedly
    for d in itertools.cycle(dict_list):
        # break if the sequence is empty (no more numbers to assign)
        if(not len(rumble_seq)):
            break
        
        this_num = rumble_seq.pop()
        d['numbers'].append(this_num)

    # sort the numbers for each name
    [d['numbers'].sort() for d in dict_list]

    messages = get_rumble_messages(dict_list)

    return messages

def get_rumble_messages(dict_list):
    """Accepts a list of dicts, each containing a member and numbers list.\n
    Returns a list of strings representing formatted messages."""
    messages = []
    for d in dict_list:
        # formatted message with the member mentioned
        messages.append(f"<@{d['member'].id}> your numbers are: {', '.join(str(n) for n in d['numbers'])}")

    # transform/pivot the dict_list into single dict where numbers are the key
    transformed_dict = transform_rumble(dict_list)

    # iterate the transformed dict to build formatted message of entire rumble
    formatted_message = "```Here is your ROYAL RUMBLE:\n"
    for k, v in transformed_dict.items():
        formatted_message += f"{k}: {v}\n"
    formatted_message += "```"
    messages.append(formatted_message)

    return messages

def transform_rumble(dict_list):
    """Accepts a list of dicts, each containing a member and numbers list.\n
    Transforms the data into a new dict, listing each number as the key, and member name as the value.\n
    Returns a dict sorted by key (number)."""
    transformed_dict = {}
    for d in dict_list:
        for n in d['numbers']:
            # add item to dict e.g. {1: "JohnSmith"}
            transformed_dict.update({n: d['member'].name})

    # sort the dict by key to get numbers in order
    transformed_dict = dict(sorted(transformed_dict.items()))

    return transformed_dict

def get_toby_clip():
    toby_clips = ["https://www.trueachievements.com/gameclip.aspx?clipid=24880582",
    "https://www.trueachievements.com/gameclip.aspx?clipid=24566232",
    "https://www.trueachievements.com/gameclip.aspx?clipid=39305715",
    "https://www.trueachievements.com/gameclip.aspx?clipid=31552145",
    "https://www.trueachievements.com/gameclip.aspx?clipid=88214325",
    "https://www.trueachievements.com/gameclip.aspx?clipid=169420501",
    "https://www.trueachievements.com/gameclip.aspx?clipid=166655251",
    "https://www.trueachievements.com/gameclip.aspx?clipid=162029530",
    "https://www.trueachievements.com/gameclip.aspx?clipid=162029531",
    "https://www.trueachievements.com/gameclip.aspx?clipid=161712706",
    "https://www.trueachievements.com/gameclip.aspx?clipid=160605008",
    "https://www.trueachievements.com/gameclip.aspx?clipid=160605009",
    "https://www.trueachievements.com/gameclip.aspx?clipid=157112731",
    "https://www.trueachievements.com/gameclip.aspx?clipid=156264376",
    "https://www.trueachievements.com/gameclip.aspx?clipid=148824379",
    "https://www.trueachievements.com/gameclip.aspx?clipid=148741495",
    "https://www.trueachievements.com/gameclip.aspx?clipid=149457306",
    "https://www.trueachievements.com/gameclip.aspx?clipid=149457305",
    "https://www.trueachievements.com/gameclip.aspx?clipid=90283871",
    "https://www.trueachievements.com/gameclip.aspx?clipid=129194622",
    "https://www.trueachievements.com/gameclip.aspx?clipid=128998196",
    "https://www.trueachievements.com/gameclip.aspx?clipid=128962869",
    "https://www.trueachievements.com/gameclip.aspx?clipid=128962868",
    "https://www.trueachievements.com/gameclip.aspx?clipid=82054514",
    "https://www.trueachievements.com/gameclip.aspx?clipid=68835768",
    "https://www.trueachievements.com/gameclip.aspx?clipid=47592202",
    "https://www.trueachievements.com/gameclip.aspx?clipid=24226704",
    "https://www.trueachievements.com/gameclip.aspx?clipid=17018605",
    "https://www.trueachievements.com/gameclip.aspx?clipid=15519789",
    "https://www.trueachievements.com/gameclip.aspx?clipid=2444675",
    "https://www.trueachievements.com/gameclip.aspx?clipid=2444694",
    "https://www.trueachievements.com/gameclip.aspx?clipid=2444687"
    ]

    return random.choice(toby_clips)

def create_poll(message):
    poll_message = ""

    try:
        title = find_title(message)
        options = find_options(message, [])
        if len(options) == 0:
            raise Exception
        poll_message, poll_labels = build_poll_message(title, options)

    except:
        return "<:cena_blep:695734225885855866> Error creating poll. Please check poll syntax: '!poll {title} [option1] [option2] ... [optionN]'", []

    return poll_message, poll_labels

# parses the title, which should be in between curly brackets ('{title}')
def find_title(message):
    # this is the index of the first character of the title
    first = message.find('{') + 1
    # index of the last character of the title
    last = message.find('}')
    if first == 0 or last == -1:
        raise KeyError
    return message[first:last]

# parses the options (recursively), which should be in between square brackets ('[option]')
def find_options(message, options):
    # first index of the first character of the option
    first = message.find('[') + 1
    # index of the last character of the title
    last = message.find(']')
    if (first == 0 or last == -1):
        if len(options) < 2:
            raise KeyError
        else:
            return options
    options.append(message[first:last])
    message = message[last+1:]
    return find_options(message, options)

def build_poll_message(title, options):
    message = f"__**{title}**__\n"
    
    poll_labels = []
    i = 0
    for o in options:
        poll_label = get_poll_label(i, o)
        message += f"{poll_label} {o}\n"

        poll_labels.append(poll_label)
        i += 1
    
    return message, poll_labels

def get_poll_label(index, override):
    default_poll_labels = ['🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯']

    if("orton" in override.lower()):
        return "<:orton_afraid:695734225634328590>"
    if("miz" in override.lower()):
        return "<:miz_nervous:760963180679004200>"


    return default_poll_labels[index]

def get_help_text():
    return """```
Supported commands:
!hello - Say hello to TobyBot!
!tobyclip - Request a cool TobyStamkos gamerclip 😎.
!rumble - Restricted command that only works during a Royal Rumble event. Randomly generates a 30-entrant Royal Rumble pool using the current members of the sender's voice channel.
!poll - Restricted command. Generates a poll of up to 10 options. Requires the following syntax of command and brackets: !poll {Title} [Option1] [Option2] ... [OptionN]
!what - WHAT?

Restricted commands can only be used in the bot channel. The rest can be used anywhere.
```"""

def get_what():
    whats = ["<:austin_happy:696083318818603079>", "<:austin_finger:696083319254941718>"]
    return random.choice(whats)