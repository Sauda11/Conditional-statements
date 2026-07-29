costprice =int(input("enter the cp: "))  # 50
sellingprice =int(input("enter the sp: ")) #55

if(sellingprice > costprice):  #55>50
  print("profit")  
else :
  print("No profit,but loss")   #45-50=-5

pt=sellingprice-costprice
print(pt)