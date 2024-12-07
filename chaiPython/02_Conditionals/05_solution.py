dict={
    "sunny":"go for a walk",
    "rainy":"read a book",
    "snowy":"build a snowman"
}
print("1.sunny\n2.rainy\n3.snowy")
weather=str(input("Enter the weather of today "))
if(weather=="sunny"):
    print(dict[weather])
elif(weather=="rainy"):
    print(dict[weather])
else:
    print(dict["snowy"])

