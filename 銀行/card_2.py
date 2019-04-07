def createCard():
    print("創建一個新帳號")
    account=input("請輸入帳號:")
    password=input("請輸入密碼:")
    with open("cardinfo.txt","a",encoding="utf-8") as file:
        a={"account":account,"password":password}
        a=str(a)
        file.write(a)
        file.write("\n")
        file.close()


def readCard():
    with open("cardinfo.txt","r",encoding="utf-8") as file:
        line=file.readline()
        while line:
                line=eval(line)
                print(line["account"])
                line=file.readline()
        file.close()

def length_():
        with open("cardinfo.txt","r",encoding="utf-8") as file:
                x=file.readlines()
                return len(x)
        
        
        
def loginCard():
    num=[]
    with open("cardinfo.txt","r",encoding="utf-8") as file:
        for i in range(length_()):
                line=file.readline()
                line=eval(line)
                num.append(line)
        a=str(input("請輸入帳號:"))
        j=0
        while j < length_():
                
                if num[j]["account"]==a:
                        b=str(input("請輸入密碼:"))
                        if num[j]["password"]==b:
                                print("登入成功")
                        else:
                                print("密碼錯誤")
                        break
                if j==length_():
                        print("此無帳號")
                j+=1
        file.close()

#loginCard()
