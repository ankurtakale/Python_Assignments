#===================================================================================================
#
#   Problem Statement : Use KNN to predict whether a student passes or fails based on study hours and attendance.
                            
#                           Dataset

#                           Study Hours         Attendance              Result
#                               2                   60                  Fail
#                               5                   80                  Pass
#                               6                   85                  Pass
#                               1                   50                  Fail

#                           Tasks:
#                           1. Accept input from user:
#                                       Study hours
#                                       Attendance percentage

#                            2. Apply KNN algorithm

#                            3. Predict whether the student Passes or Fails

#                           Input Example:
#                           Enter Study Hours: 4
#                           Enter Attendance: 70

#                            Expected Output:

#                            Predicted Result: Pass
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

import math

def Euclidean(P1,P2):

    ans = math.sqrt((P1["Study_hours"] - P2["Study_hours"]) **2 + ((P1["Attendance"] - P2["Attendance"]) **2))

    return ans

def main():
    
    Data = [
            {"Study_hours" : 2, "Attendance" : 60, "Result" : "Fail"},
            {"Study_hours" : 5, "Attendance" : 80, "Result" : "Pass"},
            {"Study_hours" : 6, "Attendance" : 85, "Result" : "Pass"},
            {"Study_hours" : 1, "Attendance" : 50, "Result" : "Fail"}
            ]

    study_hr = int(input("Enter study hours : "))
    attendance = int(input("Enter attendace percentage : "))

    new_data = {"Study_hours" : study_hr, "Attendance" : attendance}

    for i in Data:
        i["distance"] = Euclidean(i,new_data)

    sort = sorted(Data,key=lambda item : item["distance"])

    k = 3
    nearest = sort[:k]

    votes = {}
    for i in nearest:
        label = i["Result"]
        votes[label] = votes.get(label,0)+1

    predicted = max(votes,key=votes.get)

    print("Predicted Result : ",predicted)

if __name__ == "__main__":
    main()