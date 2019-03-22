"""
a = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
for i in a:
    if i.__contains__("abc"):
        print(i, " is containing")


"""
lande = ["Danmark", "Tyskland", "Sverige", "Holland", "Polen", "Italien", "Norge"]
txtInput = input("Indtast lande navn: ")
for land in lande:
    if land.__contains__(txtInput):
        print("har fundet: " + land)
        #break
    else:
        print("har ikke fundet nogen")
        break

#print(filter(lambda x: txtInput in x, lande))

"""
for land in lande:
    if land.find(x) != -1:
        print(land)
      #  break
    else:
        print("ikke noget match!")

"""
# for land in lande:
#   if sub in land:
##     print("har fundet: " + land)
#    break
# else:
#  print("har ikke fundet nogen")
