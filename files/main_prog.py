from prettytable import PrettyTable


def main_program(cur):

    cmd = """create table mobile_data ( Sl_No integer,
            Brand varchar,	Model varchar,	Announced varchar,	Audio_jack varchar,	Battery varchar,
            Bluetooth varchar,	CPU varchar,	Chipset varchar, Colors varchar, Dimensions varchar,Display_type varchar,
            GPU varchar,	Internal_memory varchar,	Loud_speaker varchar,	Memory_card varchar,	Network varchar,	Operating_System varchar,
            Primary_camera varchar,	RAM varchar,	Radio varchar,	SIM varchar,	Secondary_camera varchar,	Sensors varchar,
            Status varchar,	USB varchar );"""
    cur.execute(cmd)
    conn.commit()
    cur.execute("copy mobile_data from '/home/android/Programs/sql/access_sql/upload1.csv' delimiter ',' csv header")
    conn.commit()
    # cur.execute("select * from mobile_data")

    # comment the above code if youre running the code seccond time or the database is already created
    # now we have uploded data now we need to perform task from the stored data

    while True:
        try:
            print("""select which of the mobile you want information for
                1.  Apple
                2.  Asus
                3.  Coolpad
                4.  Google
                5.  Lenovo
                6.  Microsoft
                7.  Motorola
                8.  Nokia
                9.  One plus
                10. Oppo
                11. Samsung
                12. Vivo
                13. Xiaomi
            """)
            choice = int(input())

        except:
            print("select the valid number from list")
            continue
        if 0 < int(choice) < 14:
            break
        else:
            print("please select the number between the provided")

    dt = {1: 'Apple', 2: 'Asus', 3: 'Coolpad', 4: 'Google', 5: 'Lenovo', 6: 'Microsoft', 7: "Motorola", 8: "Nokia", 9: 'One plus', 10: 'Oppo', 11: 'Samsung', 12: 'Vivo', 13: 'Xiaomi'}

    st = f"""select sl_no, brand, model from mobile_data where brand = '{dt[choice]}';"""
    cur.execute(st)
    rows = cur.fetchall()

    table = PrettyTable(['Serial Number', 'Brand', 'Model'])
    for row in rows:
        table.add_row([row[0], row[1], row[2]])
    print(table)

    numb = input("select the corresponding serial_number of the model you want the information of: \nNote if you need multiple model info enter numbers with separted by comma \n")
    st1 = f"""select * from mobile_data where sl_no in ({numb});"""
    cur.execute(st1)
    row = cur.fetchone()
    table1 = PrettyTable(['Sl_No', 'Brand', 'Model', 'Announced', 'Audio_jack', 'Battery', 'Bluetooth', 'CPU', 'Chipset', 'Colors', 'Dimensions', 'Display_type', 'GPU', 'Internal_memory', 'Loud_speaker', 'Memory_card', 'Network', 'Operating_System', 'Primary_camera', 'RAM', 'Radio', 'SIM', 'Secondary_camera', 'Sensors', 'Status', 'USB'])
    while row:
        # edit here
        table1.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25]])
        row = cur.fetchone()

    print(table1)
