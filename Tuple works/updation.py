# add 150 to the tuple
# expected output 
#           numbers=[1,2,[3,4,(100,150,200,300)],5,6]

numbers=[1,2,[3,(100,200,300),4],5,6]
num=numbers[2]
poped_ele=num.pop()
num.insert(1,poped_ele)
num2=numbers[2][2]
new_num=list(num2)
new_num.insert(1,150)
new_num1=tuple(new_num)
numbers[2][2]=new_num1
print(numbers)
