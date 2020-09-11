class phone:
    os = ""
    cpu = ""
    ram = ""

    def phoneop(self):
        msg = "\n i am a basic phone i can make and recieve calls and text"
        print(msg)
class iphone(phone):
    model= ""
    iosver = ""

    def phoneop(self):
        msg = "\n i am a apple smart phone i can make and recieve calls and text as well as use the apple app store and apple services such as face time and i message"
        print(msg)
        
class android(phone):
    model = ""
    andriodver = ""
    
    def phoneop(self):
        msg = "\n i am a android phone i can make and recieve calls and text as well as use the google play store and other andriod services"
        print(msg)
