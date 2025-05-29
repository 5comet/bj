def min_sugar_bags(n):
    bag_5kg = n // 5  
    remainder = n % 5 
    
    while bag_5kg >= 0: 
        if remainder % 3 == 0:  
            bag_3kg = remainder // 3
            return bag_5kg + bag_3kg  
        bag_5kg -= 1  
        remainder = n - (bag_5kg * 5)

    return -1  

n = int(input())  
print(min_sugar_bags(n))