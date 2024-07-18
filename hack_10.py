"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman".upper()    #...    
    result = list(result.replace('I','1').replace('A','@').replace('O','0'))
    return result  