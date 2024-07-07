from func import show_type_menu
from func import show_menu_hotcoffee
from func import show_menu_icedcoffee
from func import show_menu_hotmilk
from func import show_menu_icedmilk
from func import show_menu_hottea
from func import show_menu_icedtea
from func import show_menu_proteinshakes
from func import show_menu_soda
from func import show_menu_smoothie
print("---- WELCOME TO TAO DIN ----", "\n---- คาเฟ่อัตโนมัติ 24 ชั่วโมง ----")

type_menu = show_type_menu()

if type_menu == 1 or type_menu == 2 or type_menu == 3 or type_menu == 4 or type_menu == 5 or type_menu == 6 or type_menu == 7 or type_menu == 8 or type_menu == 9:
    if type_menu ==1:
        menu_hotcoffee= show_menu_hotcoffee()
        if menu_hotcoffee == 1:
            print("--- คุณเลือก เอสเพรสโซ่ร้อน ยอดรวม 40฿ ---")
        elif menu_hotcoffee == 2:
            print("--- คุณเลือก ดับเบิ้ลเอสเพรสโซ่ร้อน ยอดรวม 50฿ ---")
        elif menu_hotcoffee == 3:
            print("--- คุณเลือก กาแฟดำร้อน ยอดรวม 40฿ ---")
        elif menu_hotcoffee == 4:
            print("--- คุณเลือก ลาเต้ร้อน ยอดรวม 45฿ ---")
        elif menu_hotcoffee == 5:
            print("--- คุณเลือก คาปูชิโน่ร้อน ยอดรวม 40฿ ---")
        elif menu_hotcoffee == 6:
            print("--- คุณเลือก มอคค่าร้อน ยอดรวม 40฿ ---")
        elif menu_hotcoffee == 7:
            print("--- คุณเลือก คาราเมลลาเต้ร้อน ยอดรวม 45฿ ---")
        elif menu_hotcoffee == 8:
            print("--- คุณเลือก กาแฟชาไต้หวันร้อน ยอดรวม 50฿ ---")
        elif menu_hotcoffee == 9:
            print("--- คุณเลือก มัทฉะลาเต้ร้อน ยอดรวม 50฿ ---")
        elif menu_hotcoffee == 10:
            print("--- คุณเลือก โคคุโตะลาเต้ร้อน ยอดรวม 55฿ ---")
        elif menu_hotcoffee == 11:
            print("--- คุณเลือก กาแฟชาไทย ยอดรวม 55฿ ---")
        elif menu_hotcoffee == 12:
            print("--- คุณเลือก อเมริกาโน่ลิ้นจี่ร้อน ยอดรวม 55฿ ---")
        else:
            print("--- ไม่พบเมนูที่คุณเลือก ---")
    elif type_menu ==2:
        menu_icedcoffee = show_menu_icedcoffee()
        if menu_icedcoffee == 1:
            print("--- คุณเลือก เต่าบินเกือบเดอร์ตี้ ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 2:
            print("--- คุณเลือก เอสเพรสโซ่เย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 3:
            print("--- คุณเลือก อเมริกาโน่เย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 4:
            print("--- คุณเลือก อเมริกาโน่เย็น(คั่วอ่อน) ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 5:
            print("--- คุณเลือก ลาเต้เย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 6:
            print("--- คุณเลือก คาปูชิโน่เย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 7:
            print("--- คุณเลือก คาราเมลลาเต้เย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 8:
            print("--- คุณเลือก กาแฟชานมไต้หวันเย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 9:
            print("--- คุณเลือก มอคค่าเย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 10:
            print("--- คุณเลือก กาแฟมัทฉะลาเต้เย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 11:
            print("--- คุณเลือก กาแฟบราวน์ชูก้าร์ลาเต้เย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 12:
            print("--- คุณเลือก การแฟชาไทยเย็น ยอดรวม 40฿ ---")
        elif menu_icedcoffee == 13:
            print("--- คุณเลือก อเมริกาโน่ลิ้นจี่เย็น ยอดรวม 40฿ ---")
        else:
            print("--- ไม่พบเมนูที่คุณเลือก ---")
    elif type_menu ==3:
        menu_hotmilk = show_menu_hotmilk()
        if menu_hotmilk ==1:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hotmilk == 2:
            print("--- คุณเลือก นมโคคุโตะร้อน ยอดรวม 40฿ ---")
        elif menu_hotmilk == 3:
            print("--- คุณเลือก โกโก้ร้อน ยอดรวม 40฿ ---")
        elif menu_hotmilk == 4:
            print("--- คุณเลือก คาราเมลโกโก้ร้อน ยอดรวม 40฿ ---")
        elif menu_hotmilk == 5:
            print("--- คุณเลือก นมร้อน ยอดรวม 40฿ ---")
        else:
            print("--- ไม่พบเมนูที่คุณเลือก ---")
    elif type_menu ==4:
        menu_icedmilk=show_menu_icedmilk()
        if menu_icedmilk ==1:
            print("--- คุณเลือก นมคาราเมลเย็น ยอดรวม 40฿ ---")
        elif menu_icedmilk ==2:
            print("--- คุณเลือก นมโคคุโตะเย็น ยอดรวม 40฿ ---")
        elif menu_icedmilk ==3:
            print("--- คุณเลือก โกโก้เย็น ยอดรวม 40฿ ---")
        elif menu_icedmilk ==4:
            print("--- คุณเลือก คาราเมลโกโก้เย็น ยอดรวม 40฿ ---")
        elif menu_icedmilk ==5:
            print("--- คุณเลือก นมชมพูเย็น ยอดรวม 40฿ ---")
        else:
            print("--- ไม่พบเมนูที่คุณเลือก ---")
    elif type_menu ==5:
        menu_hottea = show_menu_hottea()
        if menu_hottea == 1:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hottea == 2:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hottea == 3:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hottea == 4:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hottea == 5:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hottea == 6:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hottea == 7:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hottea == 8:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hottea == 9:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_hottea == 10:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        else:
            print("--- ไม่พบเมนูที่คุณเลือก ---")
    elif type_menu ==6:
        menu_icedtea = show_menu_icedtea()
        if menu_icedtea == 1:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_icedtea == 2:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_icedtea == 3:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_icedtea == 4:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_icedtea == 5:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_icedtea == 6:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_icedtea == 7:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_icedtea == 8:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        else:
            print("--- ไม่พบเมนูที่คุณเลือก ---")
    elif type_menu ==7:
        menu_proteinshakes = show_menu_proteinshakes()
        if menu_proteinshakes == 1:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_proteinshakes == 2:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_proteinshakes == 3:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_proteinshakes == 4:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_proteinshakes == 5:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_proteinshakes == 6:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_proteinshakes == 7:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_proteinshakes == 8:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_proteinshakes == 9:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_proteinshakes == 10:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        else:
            print("--- ไม่พบเมนูที่คุณเลือก ---")
    elif type_menu ==8:
        menu_soda = show_menu_soda()
        if menu_soda == 1:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_soda == 2:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_soda == 3:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_soda == 4:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_soda == 5:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_soda == 6:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_soda == 7:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_soda == 8:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_soda == 9:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_soda == 10:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        else:
            print("--- ไม่พบเมนูที่คุณเลือก ---")
    elif type_menu ==9:
        menu_smoothie = show_menu_smoothie()
        if menu_smoothie == 1:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_smoothie == 2:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_smoothie == 3:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_smoothie == 4:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_smoothie == 5:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_smoothie == 6:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_smoothie == 7:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_smoothie == 8:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        elif menu_smoothie == 9:
            print("--- คุณเลือก นมคาราเมลร้อน ยอดรวม 40฿ ---")
        else:
            print("--- ไม่พบเมนูที่คุณเลือก ---")

else:
    print("--- ไม่พบประเภทที่คุณเลือก ---")