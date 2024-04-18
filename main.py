import time

frames = [
    '****',

    ' ***\n'+
    '   *',

    '  **\n'+
    '   *\n'+
    '   *',

    '   *\n'+
    '   *\n'+
    '  **',

    '    \n'+
    '   *\n'+
    ' ***',

    '    \n'+
    '    \n'+
    '****',

    '    \n'+
    '*   \n'+
    '*** ',

    '*   \n'+
    '*   \n'+
    '**  ',

    '**  \n'+
    '*   \n'+
    '*   ',

    '*** \n'+
    '*   \n'+
    '    ',
]

while True:
    for i in frames:
        print("\x1b[2J\x1b[1;1H")
        print(i)
        time.sleep(0.2)
        
        
        