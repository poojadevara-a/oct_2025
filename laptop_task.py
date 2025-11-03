class Laptop():
    def __init__(self,brand_name,processor,storage,ram,os):
        self.brand_name = brand_name
        self.processor = processor
        self.storage = storage
        self.ram = ram
        self.os = os
    def specifications(self,):
        print(f"The Speifications of {self.brand_name} are: \n"
              f"Brand - {self.brand_name}\n"
              f"Processor - {self.processor}\n"
              f"Hard Disk Size - {self.storage}\n"
              f"Ram Memory - {self.ram}\n"
              f"Operating System - {self.os}")
    def gaming(self,):
        print(" ")
        print(f"You are playing Cake Mania on your {self.brand_name} laptop.")
    def browsing(self,browser,site):
        print(" ")
        print(f"You are browsing {site} on {browser} using your {self.brand_name}.")
    def movies(self, mov_name,app_name):
        print(" ")
        print(f"You are watching '{mov_name}' on the {app_name} app using your {self.brand_name}.")
    
HP = Laptop("HP","Intel Core i3","1 TB","32 GB","Windows 11 Pro")
Acer = Laptop("Acer","Core i5","512 GB","16 GB","Windows 11 Home")
ASUS = Laptop("ASUS","Intel Core Ultra 9","2 TB","32 GB","Windows 11 Pro")
Lenovo = Laptop("Lenovo","Core i5 Family","512 GB","16 GB","Windows 11 Pro")
HP.specifications()
Acer.gaming()
Acer.specifications()
ASUS.browsing("Chrome","YouTube")
Lenovo.movies("Coco","Disney")