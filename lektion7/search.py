lande = ["Danmark", "Tyskland", "Sverige", ""]
search = "k"
found = False
matched = ""
if "mark" in "Danmark":
    print("mark er med i Danmark")
for land in lande:
    if search in land:
        matched = land
        found = True
        print("Fandt " + search + " i " + matched)
"""
if found:
    print("Fandt "+search+" i "+matched)
else:
    print("Fandt ikke "+search)"""