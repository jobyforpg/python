class Bank:
    def getdata(self,name,ac_type,ac_num,ac_bal):
        self.name=name
        self.ac_type=ac_type
        self.ac_num=ac_num
        self.ac_bal=ac_bal
        
    def deposit(self,dept):
        self.ac_bal=self.ac_bal+dept

    def witdraw(self,witd):
        if(self.ac_bal<0):
            print("minim balance is requird")
        else:
            self.ac_bal=self.ac_bal-witd
            
    def options(self):
        while True:  
         print("1.Disply balance")
         print("2.withdraw")
         print("3.Deposit")
         print("4. Exit")
         print("____________")
         ch=int(input("choose an option"))
         
         match ch:
             case 1:
                 print("current balance:",self.ac_bal)
                 
             case 2:
               amount=int(input("Enter Amout"))

               if  amount>self.ac_bal:
                         print("insufficient balance")
               elif amount<100 or amount%100!=0:
                    print("withdraw only multiple of 100 ")
              
               else:
                    self.witdraw(amout)
                    print(amount,'withdraw')
                    if(self.ac_bal>=0):
                        
                        print("current balance",  self.ac_bal)
                    else:
                        print(0,"balance")
                        
             case 3:
                 amount=int(input("Enter Amout"))
                 if amount<100 or amount%100!=0:
                    print("deposit only multiple of 100 ")

                 else:
                    self.deposit(amount)
                    print(amount,'Deposit')
                    print("current balance",  self.ac_bal)


             case 4: 
                exit();
B=Bank();
B.getdata("joby","Saving",12345,0)
B.options()


 
                 
                 
                 
