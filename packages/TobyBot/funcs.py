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
    Returns a list of formatted messages strings."""

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
        d["numbers"].append(this_num)

    # sort the numbers for each name
    [d["numbers"].sort() for d in dict_list]

    messages = get_rumble_messages(dict_list)

    return messages

def get_rumble_messages(dict_list):
    """Accepts a list of dicts, each containing a member and numbers list.\n
    Returns a list of strings representing formatted messages."""
    messages = []
    for d in dict_list:
        messages.append(f"<@{d['member'].id}> your numbers are: {', '.join(str(n) for n in d['numbers'])}")

    return messages

def get_toby_clip():
    toby_clips = ["https://www.trueachievements.com/gameclip.aspx?clipid=24880582",
    "https://www.trueachievements.com/gameclip.aspx?clipid=24566232",
    "https://www.trueachievements.com/gameclip.aspx?clipid=39305715",
    "https://www.trueachievements.com/gameclip.aspx?clipid=31552145",
    "https://www.trueachievements.com/gameclip.aspx?clipid=88214325"]

    return random.choice(toby_clips)