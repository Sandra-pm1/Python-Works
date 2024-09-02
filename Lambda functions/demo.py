

add=lambda n1,n2:n1+n2
print(add(20,30))

sub=lambda n1,n2:n1-n2
print(sub(30,20))

cube=lambda n:n**3
print(cube(8))

largest=lambda n1,n2:n1 if n1>n2 else n2
print(largest(6,9))

last_digit_max=lambda n1,n2:n1 if n1%10>n2%10 else n2
print(last_digit_max(127,872))