from time import sleep

def getInput():
    """讀取使用者的輸入資訊，並依規格讀取Command及參數。

    Returns:
        str: Command
        array: parameters
    """
    inputstr = input('#### 請輸入指令:')
    while (len(inputstr)<1):   
        inputstr = input('*** 請輸入指令:')
    args = inputstr.split(',')
    command = args[0].upper()
    return command, args

def run_cmd(cmd):
    print(f"執行指令: {cmd}")

def start():
    """程式的控制區，負責分派使用者的指令
    """
    while (True):
        sleep(1)
        command, args = getInput()
        if command == 'EXIT' or command == 'LOGOUT':
            # 登出
            run_cmd(command)            
            break
        elif command == 'LOGIN':
            run_cmd(command)
        elif command == 'QUERY':
            run_cmd(command)
        else:
            run_cmd('Unknown Command')
            print(f"未知的指令: {command}, 請重新輸入。")

if __name__ == "__main__":
    start()