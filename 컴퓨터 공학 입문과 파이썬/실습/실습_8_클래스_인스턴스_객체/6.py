class Phone_Program:
    def __init__(self, user, phone_number, battery):
        self.user = user
        self.phone_number = phone_number
        self.battery = battery
        self.applist = []
    
    def add_app_info(self, appName):
        self.applist.append(appName)
    
    def find_app(self, appName):
        try:
            if self.applist.index(appName) != -1:
                print(f"찾으시는 앱 {appName}이 존재함.")
        except:
            print(f"찾으시는 앱 {appName}이 존재하지 않음.")
    
    def info_abt_user(self):
        print(f"사용자 {self.user}의 전화번호는 {self.phone_number}이며, 배터리 잔량은{self.battery}이다.")

class Phone_Program_Updated(Phone_Program):
    def __init__(self, user, phone_number, battery):
        super().__init__(user, phone_number, battery)
        self.phone_numbers = dict()
    
    def add_phone_number(self, name, number):
        self.phone_numbers[name] = number

    def find_app(self, appName):
        try:
            if self.applist.index(appName) != -1:
                print(f"찾으시는 앱 {appName}이 존재함.")
                self.applist.pop(appName)
                self.applist.append(appName)

        except:
            print(f"찾으시는 앱 {appName}이 존재하지 않음.")
            print('이미 없었던 앱이었으므로 추가만 함.')
            self.applist.append(appName)
