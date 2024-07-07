def show_type_menu():
    print("--------------------------------------------------")
    print("1.Hot Coffee")
    print("2.Iced Coffee")
    print("3.Hot Milk")
    print("4.Iced Milk")
    print("5.Hot Tea")
    print("6.Iced Tea")
    print("7.Protein Shakes")
    print("8.Soda")
    print("9.Smoothie")

    customer_choose_type = int(input("Select Type :"))
    return customer_choose_type

def show_menu_hotcoffee():
    print("------------")
    print("1.เอสเพรสโซ่ร้อน 45฿ ")
    print("2.ดับเบิ้ลเอสเพรสโซ่ร้อน ")
    print("3.กาแฟดำร้อน")
    print("4.ลาเต้ร้อน")
    print("5.คาปูชิโน่ร้อน")
    print("6.มอคค่าร้อน ")
    print("7.คาราเมลลาเต้ร้อน")
    print("8.กาแฟชาไต้หวันร้อน ")
    print("9.มัทฉะลาเต้ร้อน ")
    print("10.โคคุโตะลาเต้ร้อน")
    print("11.กาแฟชาไทย")
    print("12.อเมริกาโน่ลิ้นจี่ร้อน")
    customer_choose_hotcoffe = int(input("Select Hot Coffee :"))
    return customer_choose_hotcoffe

def show_menu_icedcoffee():
    print("------------")
    print("1.เต่าบินเกือบเดอร์ตี้")
    print("2.เอสเพรสโซ่เย็น ")
    print("3.อเมริกาโน่เย็น")
    print("4.อเมริกาโน่เย็น(คั่วอ่อน)")
    print("5.ลาเต้เย็น")
    print("6.คาปูชิโน่เย็น ")
    print("7.มอคค่าเย็น")
    print("8.คาราเมลลาเต้เย็น ")
    print("9.กาแฟชานมไต้หวันเย็น ")
    print("10.กาแฟมัทฉะลาเต้เย็น")
    print("11.กาแฟบราวน์ชูก้าร์ลาเต้เย็น")
    print("12.การแฟชาไทยเย็น")
    print("13.อเมริกาโน่ลิ้นจี่เย็น")
    customer_choose_icedcoffee = int(input("Select Iced Coffee :"))
    return customer_choose_icedcoffee

def show_menu_hotmilk():
    print("------------")
    print("1.นมคาราเมลร้อน ")
    print("2.นมโคคุโตะร้อน ")
    print("3.โกโก้ร้อน")
    print("4.คาราเมลโกโก้ร้อน")
    print("5.นมร้อน")
    customer_choose_hotmilk = int(input("Select Hot Milk :"))
    return customer_choose_hotmilk

def show_menu_icedmilk():
    print("------------")
    print("1.นมคาราเมลเย็น ")
    print("2.นมโคคุโตะเย็น ")
    print("3.โกโก้เย็น")
    print("4.คาราเมลโกโก้เย็น")
    print("5.นมชมพูเย็น")
    customer_choose_icedmilk = int(input("Select Iced Milk :"))
    return customer_choose_icedmilk

def show_menu_hottea():
    print("------------")
    print("1.ชาเขียวร้อน")
    print("2.ชาขิงร้อน ")
    print("3.ชาไทยร้อน")
    print("4.ชานมไต้หวันร้อน")
    print("5.มัทฉะลาเต้ร้อน")
    print("6.ชาบราวน์ชูการ์ร้อน")
    print("7.ชามะนาวร้อน")
    print("8.ชาลิ้นจี่ร้อน")
    print("9.ชาสตอเบอร์รี่ร้อน")
    print("10.ชาดำร้อน")
    customer_choose_hottea = int(input("Select Hot Tea :"))
    return customer_choose_hottea

def show_menu_icedtea():
    print("------------")
    print("1.ชาไทยเย็น")
    print("2.ชานมไต้หวัน ")
    print("3.ชาเย็น")
    print("4.ชาสตอเบอร์รี่เย็น")
    print("5.มัทฉะลาเต้เย็น")
    print("6.ชาบราวน์ชูการ์เย็น")
    print("7.ชามะนาวเย็น")
    print("8.ชาลิ้นจี่เย็น")
    customer_choose_icedtea = int(input("Select Iced Tea :"))
    return customer_choose_icedtea

def show_menu_proteinshakes():
    print("------------")
    print("1.มัทฉะโปรตีน")
    print("2.โกโก้โปรตีน")
    print("3.สตอเบอร์รี่โปรตีน")
    print("4.เอสเพรสโซ่โปรตีน")
    print("5.ชานมไทยโปรตีน")
    print("6.บราวน์ชูก้าร์โปรตีน")
    print("7.ชาไต้หวันโปรตีน")
    print("8.คาราเมลโปรตีน")
    print("9.โปรตีนเปล่า")
    print("10.นมโปรตีน")
    customer_choose_proteinshakes = int(input("Select Protein Shakes :"))
    return customer_choose_proteinshakes

def show_menu_soda():
    print("------------")
    print("1.เป๊ปซี่")
    print("2.น้ำมะนาวโซดา ")
    print("3.น้ำลิ้นจี่โซดา")
    print("4.น้ำเมล่อนโซดา")
    print("5.น้ำยูซุโซดา")
    print("6.น้ำบ๊วยโซดา")
    print("7.น้ำขิงโซดา")
    print("8.น้ำสตอเบอร์รี่โซดา")
    print("9.น้ำแดงสละโซดา")
    print("10.น้ำแดงสละมะนาวโซดา")
    customer_choose_sode = int(input("Select Soda :"))
    return customer_choose_sode

def show_menu_smoothie():
    print("------------")
    print("1.โอริโอ้ปั่นภูเขาไฟ")
    print("2.โกโก้สตอเบอร์รี่ปั่น")
    print("3.โอวัลตินปั่น")
    print("4.โกโก้โอวัลตินปั่น")
    print("5.นมสตอเบอร์รี่ปั่น")
    print("6.นมเมล่อนปั่น")
    print("8.นมยูซุปั่น")
    print("9.นมลิ้นจี่ปั่น")
    customer_choose_smoothie = int(input("Select Smoothie :"))
    return customer_choose_smoothie