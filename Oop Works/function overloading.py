# def add(n1,n2):
#     return n1+n2
# def add(n1,n2,n3):
#     return n1+n2+n3
# print(add(100,200,300))
# print(add(100,200))


# def add_numbers(*args):  #  * convert to tuple

#     print(sum(args))

# add_numbers(10,20)
# add_numbers(10,20,30)
# add_numbers(10,20,30,40)
# add_numbers(10,20,30,40,50)


# def get_person(**kwargs):

#     print(kwargs.get("name"))
#     print(kwargs.get("n_place"))

# get_person(name="hari",w_place="tsr",n_place="kakkanad")


 
def flat_list(*args):   # flat_list(1,2,[10,20],[10,[100,200]])
    
    flat=[]

    for arg in args:
        if isinstance(arg,list):
            flat.extend(flat_list(*arg))
        else:
            flat.append(arg)
    return flat
        
print(flat_list((10,20,[100,200],[1000,[2000,3000]])))