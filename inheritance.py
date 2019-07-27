class a:

    def hello(self):
        print("hello")




class b(a):
    @staticmethod
    def stuname(nam):
        print(nam)

class c(b):
    @staticmethod
    def stuadd(add):
        print(add)
    
x=c()

x.hello()
x.stuname('ram')
x.stuadd('delhi')











