pb_global_b=12

def my_fun1():
    pb_a=10
    print(pb_a)
    print(pb_global_b)

def my_fun2():
    print(pb_global_b)

    # print(pb_a)


my_fun1()
print(pb_global_b)
my_fun2()