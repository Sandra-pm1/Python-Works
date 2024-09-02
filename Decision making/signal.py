# read signal from the user
# red => stop
# orange => wait
# green => go


signal=input("Enter the signal ")

if signal=="red":
    print("STOP")

elif signal=="orange":
    print("WAIT")

elif signal=="green":
    print("GO")

else:
    print("INVALID INPUT")
