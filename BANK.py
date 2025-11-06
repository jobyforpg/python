class Bank:
    def getdata(self,name,ac_type,ac_num,ac_bal):
        selef.name=name
        self.ac_type=ac_type
        self.ac_num=ac_num
        self.ac_bal=ac_bal
        
    def deposit(self,dept):
        self.ac_bal=self.ac_bal+dept

    def witdraw(self,witd):
        if(self.ac_bal<0):
            print("minim balance is requird")
        else:
            
            self.ac_bal=self.ac-witd
            
     def options(self):
         print("1.Disply balance")
         print("2.withdraw")
         print("3.Deposit")
         print("____________")
         ch=int(input("choose an option"))
         switch(ch):
             case 1:
                 print("current balance:",self.ac_bal)
             case 2:
                self.witd=int(print("Enter Amout"))
                if(self.witd<100 and self.witd%=!100):
                    print("withdraw only multiple of 100 ")
                
                 
                 
