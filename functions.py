def multiply_and_greet(*args, **kwargs):
    product=1
    for num in args:
        product*=num
    print(product)
    keys=kwargs.keys()
    if "country" in keys:
        return f"Hello {kwargs['name']} from {kwargs['country']}"
     
    elif "age" in keys:
        return f"Hello {kwargs['name']} you age is {kwargs['age']}"
    
    elif "name" in keys:
        return f"Hello {kwargs['name']} "
    
    else:
        return f"Hello, what's your name?"