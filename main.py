import random
import time
import os
import msvcrt
while True:  
 print("歡迎來到小工具python")   
 選擇 = input("請選擇你要使用工具，(1)整數計算機(2)猜數字(3)擲骰子(4):抽籤(5)小數計算機(6)時鐘(7)離開:")
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
    try:
        a = (int(數字1))
        b = (int(數字2))
        if a == "結束" or 計算符號=="結束" or 數字2=="結束":
          print("計算機已關閉")
          break         
        elif 數字1 == "關於" or 計算符號=="關於" or 數字2=="關於":
          print("整數計算機v1.1")
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
    except ValueError:
          print("請輸入有效的整數")        
 elif 選擇 == "2":
     模式 =input("請選擇模式:(1)1-100模式(2)自定義模式:")
     if 模式 == "1":
      try:
         print("歡迎來到猜數字(按下0退出)")
         亂數 = random.randint(1, 100)
         紀錄次數 = 0
         目標次數=(int(input("請先設定目標次數")))
      except ValueError:
        print("請輸入有效整數")   
      while True: 
       猜數字 = (int(input ("請輸入數字:")))
       if 猜數字 == 0:
        print("已退出")
        break   
       elif 猜數字 == 亂數:
        紀錄次數 += 1
        print(f"恭喜你猜對了，你贏了！{紀錄次數}次猜中")
        break
       elif 猜數字 < 亂數:
        紀錄次數 += 1
        print("你猜的字太小了，請再試一次(按下0退出):")   
        剩下次數 = 目標次數 - 紀錄次數
        print(f"你目前已經猜了{紀錄次數}次，還剩下{剩下次數}次")
        if 紀錄次數 ==目標次數 or 紀錄次數 > 目標次數:
          剩下次數 = 目標次數 - 紀錄次數
          print(f"你輸了。")
          break
       elif 猜數字 > 亂數:
         紀錄次數 += 1
         print("你猜的數字太大了，請再試一次(按下0退出):")
         剩下次數 = 目標次數 - 紀錄次數
         print(f"你目前已經猜了{紀錄次數}次，還剩下{剩下次數}次")
         if 紀錄次數 ==目標次數 or 紀錄次數 > 目標次數:
          剩下次數 = 目標次數 - 紀錄次數
          print(f"你輸了。")
          break
       elif 紀錄次數 ==目標次數 or 紀錄次數 > 目標次數:
        剩下次數 = 目標次數 - 紀錄次數
        print(f"你輸了。")
        break
       else:
        print("無效的輸入，請輸入1-目標次數0的數字或0退出")
        猜數字 = input("請輸入數字按下0退出):")
     if 模式 == "2": 
      try:
        print("歡迎來到猜數字請選擇數字範圍(按下0退出)")
        數字1 =(int(input("請輸入開始的數字(頭)")))
        if 數字1 == "0": 
           print("已退出")
           break
        數字2 =(int(input("請輸入結束的數字(尾)")))
        if 數字2 == "0":
          print("已退出")
          break
          print("歡迎來到猜數字(按下0退出)")
        亂數 = random.randint(數字1, 數字2)
        紀錄次數 = 0
        目標次數=(int(input("請先設定目標次數")))
      except ValueError:
         print("請輸入有效整數")    
      while True: 
         猜數字 = (int(input ("請輸入數字:")))
         if 猜數字 == 0:
          print("已退出")
          break   
         elif 猜數字 == 亂數:
          紀錄次數 += 1
          print(f"恭喜你猜對了，你贏了！{紀錄次數}次猜中")
          break
         elif 猜數字 < 亂數:
          紀錄次數 += 1
          print("你猜的字太小了，請再試一次(按下0退出):")   
          剩下次數 = 目標次數 - 紀錄次數
          print(f"你目前已經猜了{紀錄次數}次，還剩下{剩下次數}次")
          if 紀錄次數 ==目標次數 or 紀錄次數 > 目標次數:
           剩下次數 = 目標次數 - 紀錄次數
           print(f"你輸了。")
           break
         elif 猜數字 > 亂數:
          紀錄次數 += 1
          print("你猜的數字太大了，請再試一次(按下0退出):")
          剩下次數 = 目標次數 - 紀錄次數
          print(f"你目前已經猜了{紀錄次數}次，還剩下{剩下次數}次")
          if 紀錄次數 ==目標次數 or 紀錄次數 > 目標次數:
           剩下次數 = 目標次數 - 紀錄次數
           print(f"你輸了。")
           break
         elif 紀錄次數 ==目標次數 or 紀錄次數 > 目標次數:
            剩下次數 = 目標次數 - 紀錄次數
            print(f"你輸了。")
            break
         else:
           print("無效的輸入")
           猜數字 = input("請再次輸入")   
 elif 選擇 == "3":
    while True:
     開始=input("歡迎來到擲骰子按下y開始，按下n離開").lower()
     if 開始 == "y":
      print("開始擲骰子")
      print("擲骰子結果:", random.randint(1, 6))
     elif 開始 == "n":
      print("已退出")
      break    
     else:
      print("無效的輸入，請輸入y開始或輸入n退出")
 elif 選擇 == "4":
      while True:
        抽籤 = input('請輸入抽籤的內容(以","分隔)(按下0結束):')
        if 抽籤 == "0":
         print("已結束抽籤")  
         break
        else:
          抽籤結果 = random.choice(抽籤.split(","))
          print(f"抽籤結果是: {抽籤結果}")
          while True:
           是否重抽 = input("請問重新再抽一遍還是重新設置(1)重抽(2)重新設置")
           if 是否重抽 == "1":
            print("重新抽籤")
            抽籤結果 = random.choice(抽籤.split(","))
            print(f"抽籤結果是: {抽籤結果}")
           elif 是否重抽 == "2":
            print("已結束抽籤")
            break
           else:
            print("無效的輸入，請輸入1或2")
 elif 選擇 == "5":
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
    try:
        a = (float(數字1))
        b = (float(數字2))
        if a == "結束" or 計算符號=="結束" or 數字2=="結束":
          print("計算機已關閉")
          break         
        elif 數字1 == "關於" or 計算符號=="關於" or 數字2=="關於":
          print("小數計算機v1.0")
        elif 數字1 == "結束" or 計算符號=="結束" or 數字2=="結束":
          print("計算機已關閉")
          break          
        elif  計算符號 == "+":
          print("="+str(float(數字1) + float(數字2)))
        elif 計算符號== "-":   
          print("="+str(float(數字1) - float(數字2)))
        elif 計算符號== "*":
          print("="+str(float(數字1) * float(數字2))) 
        elif 計算符號== "/":
         if 數字2 =="0":
           print("除數不能為零") 
         else:
           print("="+ str(float(數字1) / float(數字2)))        
    except ValueError:
          print("請輸入有效的數")  
 elif 選擇 == "6" :
   print("歡迎來到時鐘(按下q離開，按下enter更新)")
   while True:
      離開 = input(time.ctime(time.time())).lower()
      os.system ('cls')
      if 離開 == "q": 
       print("已退出")
       break
      elif 離開 == "":
       print("正在更新時鐘")
 elif 選擇 == "7":
    print("已退出")
    break
 else:
    print("無效的選擇，請重新輸入")