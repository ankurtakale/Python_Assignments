import math

def Euclidean(P1,P2):
    ans = math.sqrt(((P1['X']-P2['X']) **2) + ((P1['Y']-P2['Y']) **2))
    return ans

def main():
    
    Data = [
            {"point" : 'A', 'X' : 1, 'Y' : 2, "label" : "Red"},
            {"point" : 'B', 'X' : 2, 'Y' : 3, "label" : "Red"},
            {"point" : 'C', 'X' : 3, 'Y' : 1, "label" : "Blue"},
            {"point" : 'D', 'X' : 6, 'Y' : 5, "label" : "Blue"}
            ]
    
    x_coor = int(input("Enter x_coordinate : "))
    y_coor = int(input("Enter y_coordinate : "))
    
    new_data = {'X' : x_coor,'Y' : y_coor}
    
    for i in Data:
        i["distance"] = Euclidean(i,new_data)
        
    print("-"*90)
    print("Euclidean Distances : ")
    print("-"*90)

    for i in Data:
        print(i)

    sort = sorted(Data,key=lambda item : item['distance'])

    print("-"*90)
    print("Sorted Distances : ")
    print("-"*90)

    for i in sort:
        print(i)

    k = 3
    nearest = sort[:k]

    print("-"*90)
    print("Nearest Neighbours : ")
    print("-"*90)

    for i in nearest:
        print(i)

    votes = {}
    for i in nearest:
        label = i["label"]
        votes[label] = votes.get(label,0)+1

    predicted = max(votes,key=votes.get)

    print("-"*90)
    print(f"Predicted class of {x_coor,y_coor} is : ",predicted)
    print("-"*90)

if __name__ == "__main__":
    main()