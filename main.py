import random
while True:  
 print("歡迎來到小工具python")   
 選擇 = input("請選擇你要使用工具，(1)計算機(2)猜數字(3)擲骰子(4):退出:")
 if 選擇 == "1":
   while True:
    數字1 = input ("""請輸入你的數字1:
""")
    if 數字1 == "結束":
           print("計算機已關閉")  
           break 
    計算符號= input ("請輸入計算符號:" )
    if 數字1 == "結束" or 計算符號=="結束" :
           print("計算機已關閉")  
           break
    if 計算符號 not in["+","-","*","/","結束","關於"] :
           print("計算符號錯誤請重新輸入")  
           break
    數字2 = input("""請輸入你的數字2:
""")
    if 數字1 == "結束" or 計算符號=="結束" or 數字2=="結束":
           print("計算機已關閉")
           break         
    elif 數字1 == "關於" or 計算符號=="關於" or 數字2=="關於":
       print("計算機v1.0")
    elif 數字1 == "結束" or 計算符號=="結束" or 數字2=="結束":
           print("計算機已關閉")
           break          
    elif  計算符號 == "+":
        print("="+str(int(數字1) + int(數字2)))
    elif 計算符號== "-":   
        print("="+str(int(數字1) - int(數字2)))
    elif 計算符號== "*":
        print("="+str(int(數字1) * int(數字2))) 
    elif 計算符號== "/":
         if 數字2 =="0":
           print("除數不能為零") 
         else:
           print("="+ str(int(數字1) / int(數字2)))
    else:
        print("無效的計算符號或輸入")           
 elif 選擇 == "2":
     print("歡迎來到猜數字(按下0退出)")
     亂數 = random.randint(1, 100)
     紀錄次數 = 0
     目標次數=(int(input("請先設定目標次數")))
     while True: 
      猜數字 = (int(input ("請輸入數字數字:")))
      if 猜數字 == 0:
       print("已退出")
       break   
      elif 猜數字 == 亂數:
       print(f"恭喜你猜對了！{紀錄次數}次猜中")
       break
      elif 猜數字 < 亂數:
        紀錄次數 += 1
        print("你猜的數字小了，請再試一次(按下0退出):")   
        print(f"你目前已經猜了{紀錄次數}次")
        if 紀錄次數 ==目標次數 or 紀錄次數 > 目標次數:
          print(f"你已經猜了{目標次數}次還是猜錯，遊戲結束！正確答案是", 亂數)
          break
      elif 猜數字 > 亂數:
         紀錄次數 += 1
         print("你猜的數字大了，請再試一次(按下0退出):")
         print(f"你目前已經猜了{紀錄次數}次")
         if 紀錄次數 ==目標次數 or 紀錄次數 > 目標次數:
          print(f"你已經猜了{目標次數}次還是猜錯，遊戲結束！正確答案是", 亂數)
          break
      elif 紀錄次數 ==目標次數 or 紀錄次數 > 目標次數:
        print(f"你已經猜了{目標次數}次還是猜錯，遊戲結束！正確答案是", 亂數)
        break
      else:
        print("無效的輸入，請輸入1-目標次數0的數字或0退出")
        猜數字 = input("請輸入1-目標次數0的數字(按下0退出):")
 elif 選擇 == "3":
    while True:
     開始=(int(input("歡迎來到擲骰子(按下0開始，按下7離開)")))
     if 開始 == 0:
      print("開始擲骰子")
      print("擲骰子結果:", random.randint(1, 6))
     elif 開始 == 7:
      print("已退出")
      break    
     else:
      print("無效的輸入，請輸入0開始或7退出")
 elif 選擇 == "4":
    print("已退出")
    break
 else:
    print("無效的選擇，請重新輸入")