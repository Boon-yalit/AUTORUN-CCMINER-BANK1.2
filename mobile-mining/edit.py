import os, time, json
from config import banneredit
from multiprocessing import cpu_count


cpu_thread = cpu_count()


def OffMiner():
  
   banneredit()
   try:
       print("ชื่อคนงานขุด เช่น \033[93mMiner01\033[00m")
       name = input("[-n]: ")
       print("\033[35m-----------------------------------------\033[0m")
        
       print(f"จำนวนthread \033[93mค่าที่ใส่ได้คือ 0 ถึง {cpu_thread}\033[00m")
       cpu = int(input("[-t]: "))
       print("\033[35m-----------------------------------------\033[0m")
   except:
            os.system("@cls||clear")
            print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
            time.sleep(3)
            os.system("edit-miner")
   push = {
          'name': name,
          'cpu': cpu
          }
   with open("set-miner/offline.json", "w") as set:
     json.dump(push, set, indent=4)
             
while True:
  banneredit()
  OffMiner()
  os.system("run-miner")     
  break
