#รับค่า/ป้อนทางแป้นพิมพ์ ใช้ฟังก์ชัน input() โดยสิ่งที่ป้นทั้งหมดเป็น String

#ตัวแปร variable เป็น indenifier มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรแกรม ข้อมูลที่เก็บจะอยู่ใน RAM
#indentifier คือ ชื่อที่ dev. ตั้งขึ้นมาเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn = input('ป้อนปีเกิด : ') #สิ่งที่ป้อนทั้งหมดเป็น String
print('............................')
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
stdAge =2023 -int (stdYearBorn) #ต้องแปร String เป็น number -> int( ), float( )
print(f'คุณเกิดปี {stdYearBorn} อายุ {stdAge}')
print('............................')
print("ยินดีต้อนรับ",std_id,"ชื่อ",std_name)#ใช้ , 
print("คุณเกิดปี",stdYearBorn,"อายุ",stdAge)
print('............................')
print("ยินดีต้อนรับ"+str(std_id)+" ชื่อ "+str(std_name))#ใช้ +
print("คุณเกิดปี "+str(stdYearBorn)+" อายุ "+str(stdAge))
print('............................')
print("ยินดีต้อนรับ {} ชื่อ {} ".format(std_id,std_name))#ใช้ เมธอด format
print("คุณเกิดปี {} ชื่อ {} ".format(stdYearBorn,stdAge))
print('............................')
print("ยินดีต้อนรับ %s ชื่อ %s" %(std_id,std_name))#ใช้ %
print("คุณเกิดปี %s อายุ %s" %(stdYearBorn,stdAge))