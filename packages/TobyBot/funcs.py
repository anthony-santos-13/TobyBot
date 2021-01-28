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

def assign_rumble(names, n):
    """Accepts a list of names and assigns an even amount of random numbers from 1 to n to each name.\n
    Return a list of dicts, each containing a name and list of numbers."""

    dict_list = []
    for name in names:
        dict_list.append({"name": name, "numbers": []})

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

    return dict_list
