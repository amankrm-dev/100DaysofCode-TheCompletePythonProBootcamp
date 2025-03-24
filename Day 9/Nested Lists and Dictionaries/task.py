# capitals={
#     "France":"Paris",
#     "Germany":"Berlin"
# }

#Nested List
# travel_log={
#     "France":["Paris","London","UK"],
#
# }
# var=travel_log["France"]
# print(var[1])
# nested_list=["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log={
    "France":{
         "city_visited":["Paris","Lille","Dijon"],
         "Total_Visits":12
     },
    "Germany":{
         "city_visited":["Berlin","Hamburg","Stuttgart"],
         "total_visits":8
    }
}
print(travel_log["Germany"]["city_visited"][2])