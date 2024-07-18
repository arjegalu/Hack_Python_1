"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman".replace('i','1').replace('a','@').replace('o','0')
    #...
    return result  