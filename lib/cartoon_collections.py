def roll_call_dwarves(names):
    for i in range(len(names)):
        print(f"{(i + 1)}. {names[i]}");
    return None;

def summon_captain_planet(mcalls):
    if (mcalls == None): return None;
    elif (len(mcalls) < 1): return [];
    else: return [f"{mc.capitalize()}!" for mc in mcalls];

def long_planeteer_calls(mcalls):
    if (mcalls == None or len(mcalls) < 1): return False;
    else: pass;
    for mc in mcalls:
        if (len(mc) > 4): return True;
        else: pass;
    return False;

def find_the_cheese(items):
    if (items == None or len(items) < 1): return None;
    else: pass;
    cheeses = ["cheddar", "gouda", "camembert"];
    for item in items:
        for cheese in cheeses:
            if (item == cheese): return item;
            else: pass;
    return None;
