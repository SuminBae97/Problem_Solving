number = "one4seveneight"

a =  {"zero":"0" ,"one":"1" , "two":'2',"three":'3' , "four":'4', "five":'5' , "six":'6', "seven":'7',
      "eight":'8',"nine":'9'}

for key in a.keys():

    while key in number:
        number = number.replace(key,a[key])


#
# while "one" in number:
#     number = number.replace("one",a["one"])
# while "zero" in number:
#     number = number.replace("zero",a["zero"])
#


