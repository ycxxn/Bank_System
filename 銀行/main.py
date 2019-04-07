from card_2 import *

def main():
    print("================")
    print("====龜龜銀行====")
    print("================")
    print("請選擇以下功能")
    a=int(input("1.創建帳戶 2.登入\n"))
    if a == 1:
        createCard()
    if a == 2:
        loginCard()
        
if __name__ == "__main__":
    main()