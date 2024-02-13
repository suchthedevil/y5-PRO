beer_content = 500
zelena_content, beer_total, zelena_total = 0, 0, 0

#do lesa
while beer_content > 10:
    zelena_total += 0.2*zelena_content
    beer_total += 0.2*beer_content
    zelena_content = zelena_content - 0.2*zelena_content + 100
    beer_content -= 0.2*beer_content 

#z lesa to iste len opacne hodnoty
    
#dokopy vypite:
print('beer_drunk (ml):',beer_total+zelena_total)
print('zelena_drunk (ml):',zelena_total+beer_total)
    




