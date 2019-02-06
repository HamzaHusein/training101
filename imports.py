def calculateLength(name):
    return len(name)

def findGrade(average):
    if average >= 80:
        return "A"
    elif average >=70:
        return "B"
    elif average >=60:
        return "C"
    elif average >=50:
        return "D"
    else:
        return "Fail"

def girl(name):
    name = str(name)
    name = name.lower()
    if name.startswith("h"):
        return "Ruqaiyah is the girl"
    elif name.startswith("I"):
        return "Pure is the girl"
    else:
        return "No girl"


