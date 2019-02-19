def switch_demo(x):
    return {
        1: "mandag",
        2: "tirsdag",
        3: "onsdag",
        4: "torsdag",
        5: "fridag",
        6: "lørdag",
        7: "søndag"
    }.get(x, 1)
    print(" jjj " + switch_demo(x))