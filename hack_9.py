"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    #...
    i = 0
    while i < 3:
        result.insert((i*2)+1,'@')
        i += 1
        
    return result  