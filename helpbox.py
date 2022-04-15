import random
from traceback import print_exc 

help_0 = """
                 ________________
                |                |_____    __
                |  PythonBox !   |     |__|  |_________
                |________________|     |::|  |        /
   /\**/\       |                \.____|::|__|      <
  ( o_o  )_     |                      \::/  \._______\ 
   (u--u   \_)  |
    (||___   )==\ 
  ,dP"/b/=( /P"/b\ 
  |8 || 8\=== || 8
  `b,  ,P  `b,  ,P
    """     """`   
"""
help_1 = """
.s5SSSs.                                                  .s5SSSs.  .s5SSSs.          
      SS. .s5 s.  .s5SSSSs. .s    s.  .s5SSSs.  .s    s.        SS.       SS. .s5 s.  
sS    S%S     SS.    SSS          SS.       SS.       SS. sS    S%S sS    S%S     SS. 
SS    S%S ssS SSS    S%S    sS    S%S sS    S%S sSs.  S%S SS    S%S SS    S%S ssS SSS 
SS .sS::'  SSSSS     S%S    SSSs. S%S SS    S%S SS `S.S%S SS .sSSS  SS    S%S  SSSSS  
SS          SSS      S%S    SS    S%S SS    S%S SS  `sS%S SS    S%S SS    S%S SSS SSS 
SS          `:;      `:;    SS    `:; SS    `:; SS    `:; SS    `:; SS    `:; SSS `:; 
SS          ;,.      ;,.    SS    ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. SSS ;,. 
`:          ;:'      ;:'    :;    ;:' `:;;;;;:' :;    ;:' `:;;;;;:' `:;;;;;:' `:; ;:' 
                                                                                      
"""
help_2 = """
'########::'##:::'##:'########:'##::::'##::'#######::'##::: ##:'########:::'#######::'##::::'##:
 ##.... ##:. ##:'##::... ##..:: ##:::: ##:'##.... ##: ###:: ##: ##.... ##:'##.... ##:. ##::'##::
 ##:::: ##::. ####:::::: ##:::: ##:::: ##: ##:::: ##: ####: ##: ##:::: ##: ##:::: ##::. ##'##:::
 ########::::. ##::::::: ##:::: #########: ##:::: ##: ## ## ##: ########:: ##:::: ##:::. ###::::
 ##.....:::::: ##::::::: ##:::: ##.... ##: ##:::: ##: ##. ####: ##.... ##: ##:::: ##::: ## ##:::
 ##::::::::::: ##::::::: ##:::: ##:::: ##: ##:::: ##: ##:. ###: ##:::: ##: ##:::: ##:: ##:. ##::
 ##::::::::::: ##::::::: ##:::: ##:::: ##:. #######:: ##::. ##: ########::. #######:: ##:::. ##:
..::::::::::::..::::::::..:::::..:::::..:::.......:::..::::..::........::::.......:::..:::::..::
"""
help_3 = """
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗██████╗  ██████╗ ██╗  ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║██╔══██╗██╔═══██╗╚██╗██╔╝
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║██████╔╝██║   ██║ ╚███╔╝ 
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║██╔══██╗██║   ██║ ██╔██╗ 
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                              
"""
help_4 = """
.-------.  ____     __ ,---------. .---.  .---.     ,-----.    ,---.   .--. _______       ,-----.     _____     __   
\  _(`)_ \ \   \   /  /\          \|   |  |_ _|   .'  .-,  '.  |    \  |  |\  ____  \   .'  .-,  '.   \   _\   /  /  
| (_ o._)|  \  _. /  '  `--.  ,---'|   |  ( ' )  / ,-.|  \ _ \ |  ,  \ |  || |    \ |  / ,-.|  \ _ \  .-./ ). /  '   
|  (_,_) /   _( )_ .'      |   \   |   '-(_{;}_);  \  '_ /  | :|  |\_ \|  || |____/ / ;  \  '_ /  | : \ '_ .') .'    
|   '-.-'___(_ o _)'       :_ _:   |      (_,_) |  _`,/ \ _/  ||  _( )_\  ||   _ _ '. |  _`,/ \ _/  |(_ (_) _) '     
|   |   |   |(_,_)'        (_I_)   | _ _--.   | : (  '\_/ \   ;| (_ o _)  ||  ( ' )  \: (  '\_/ \   ;  /    \   \    
|   |   |   `-'  /        (_(=)_)  |( ' ) |   |  \ `"/  \  ) / |  (_,_)\  || (_{;}_) | \ `"/  \  ) /   `-'`-'    \   
/   )    \      /          (_I_)   (_{;}_)|   |   '. \_/``".'  |  |    |  ||  (_,_)  /  '. \_/``".'   /  /   \    \  
`---'     `-..-'           '---'   '(_,_) '---'     '-----'    '--'    '--'/_______.'     '-----'    '--'     '----' 
                                                                                                                     
"""



def gethelp():
    num = random.randint(0,4)
    if num == 0:
        print(help_0)
    elif num == 1:
        print(help_1)
    elif num == 2:
        print(help_2)
    elif num == 3:
        print(help_3)
    elif num == 4:
        print(help_4)
    
        
    