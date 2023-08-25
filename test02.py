#1. ใช้ ม
print("Hallo...",456,'Hi...',True,10+20,"Hey....")
#2. ใช้ + มีข้อแม้ว่าทุกตัวที่เอามาต่อกันต้องเป็น string
print("Hallo... "+str(456)+' Hi... ',str(True)+' '+str(10+20)+" Hey.... ")
#3. ใช้เมธอด format
print('Hallo... {} Hi... {} {} Hey...'.format(456,True,10+20))
print('Hallo... {0} Hi... {1} {2} Hey...'.format(456,True,10+20)) #index number
#4. ใช้ f-string
print(f'Hallo... {456} Hi... {True} {10+20} Hey...')
#5. ใช้ modulas opertor (%) -> %d, %f, %c, %s, .......
print('Hallo.... %d Hi.... %i %d Hey....' %(456,False,10+20))
print('Hallo.... %d Hi.... %s %d Hey....' %(456,True,10+20))