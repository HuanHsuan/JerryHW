
# coding: utf-8

# In[7]:


def calculator():
    def addition(a1,a2):
        return (a1+a2)
    def subtraction(a1,a2):
        return (a1-a2)
    def multiplication(a1,a2):
        return (a1*a2)
    def division(a1,a2):
        return (a1/a2)
    try:
        a=int(input("請輸入數字:"))
        b=int(input("請輸入數字:"))
        calculate=input("請輸入+-*/ ")
        if calculate=="+":
            print (addition(a,b))
        elif calculate=="-":
            print (subtraction(a,b))
        elif calculate=="*":
            print (multiplication(a,b))
        elif calculate=="/":
            print (division(a,b))
        else:
            print("輸入錯誤")
    except:
        print("輸入錯誤")

