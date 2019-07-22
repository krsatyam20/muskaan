#no arguments no return

#create a function 
def hello():
    print("Good Morning")

#call
hello()

hello()

hello()

hello()

#with arguments with No return

def helloName(name):
    print("Hello student %s"%(name))


hello()
helloName('muskaan')


hello()
helloName('muskaan')

hello()
helloName('mohan')

hello()
helloName('monika')

#with argument with return

def addition(a,b):
    c=a+b
    return c
# only one return key use in any function
#more then one value return (value convert into list/tuple/dic)


print(addition(10,20))

x=addition(40,20)

print("Add value of a and b %d"%(x))


n=int(input("First no."))
m=int(input("Second no."))

print(addition(n,m))


#No argument with Return

def basSal(bs):
    hr=bs*.4
    return hr



print(basSal(4000))

basicSalary=int(input("please enter your basic salary"))

print(basSal(basicSalary))


