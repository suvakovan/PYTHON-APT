# used when you want to repeat something specfic number of times
for i in range (5):
    print(i)
#  for i in range (start,stop,step):
#     print(i)

for i in range (1,6):
    print(i)

for i in range (1,10,2):
    print (i)
    



item = [10,20,30,40]
for array in item:
    print (array)



    # for index , value in enumerate()

    # for index , value in enumerate (array):
    #     print(index,value)


    arr=['apple','mango','grapes']
    for index , value in enumerate (arr):
        print (index, value)







#  loop through dictionary 
    st = {"name":"ram","age":21}
for key, value in st.items():
    print(key,value)
