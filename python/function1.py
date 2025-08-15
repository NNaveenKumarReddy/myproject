def outer_fun():
    outer_var=10
    def inner_func():
        inner_var=20
        print("outer variable=",outer_var)
        print("inner variable",inner_var)
    inner_func()
    
    print("outer variable=",outer_var)
    print("inner varaible=",inner_var)
outer_fun()