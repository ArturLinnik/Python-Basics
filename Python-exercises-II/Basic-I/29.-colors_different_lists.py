
# Print out a set containing all the colors from color_list_1 which are not present in color_list_2

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def diffColors(list1,list2):
    for color in list1:
        if color not in list2:
            print(color)

diffColors(color_list_1,color_list_2)






