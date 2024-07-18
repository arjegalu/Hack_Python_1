"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman".replace('n','N')
    #...
    return result