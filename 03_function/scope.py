age = 100

def parent_func():
    age = 30

    def child_func():
        age= 20
        print(age,'local')
    
    child_func()
    print(age,'enclosed')

parent_func()
print(age, 'global')