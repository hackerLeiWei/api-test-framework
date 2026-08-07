from random import random
import re
from time import sleep
import threading


def digistList(text:str) -> tuple[bool,list[str]]:
    """
    字符串提取连续字符串
    """
    return (text.replace(' ','').isdigit(), re.findall(r'\d+', text))

def rundelay() -> None:
    threading.Timer(3.0, runGame).start()

ll = []
if ll:
    print(f"lll{len(ll)}\n")    
else:
    print(f"ll is empty,ignore\n")    
"""
猜数字游戏
"""
def runGame() -> None:
    score = int(random()*100)
    answerCount = 1
    answer = -1
    while True:
        checkInput = digistList(text:=input(f"请猜分数, 输入 quit 结束游戏{score}:"))
        print(f"checkInput:{checkInput}\n")
        if (text == 'quit'):
            print(f"游戏结束")
            break
        answer = int(digist_list[-1]) if (digist_list:=checkInput[1])  else -1
        if not digist_list or len(digist_list) > 1:
            print(f"输入无效，请重新输入\n")
            continue
        print(f"answer:{answer}\n")
        if score == answer:
            print(f"猜对了\n")
            print(f"\n")
            print(f"3s 后重新开始\n")
            rundelay()
            break
        else :
            if score > answer:
                print(f"偏小，请继续，还有{8 - answerCount}次机会\n")
            else:
                print(f"偏大，请继续，还有{8 - answerCount}次机会\n")
            answerCount += 1
            if answerCount > 8:
                print(f"你已经没有机会了\n")
                print(f"3s 后重新开始\n")
                rundelay()
                break

runGame()