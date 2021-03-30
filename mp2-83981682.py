import pymysql

db = pymysql.connect(host="127.0.0.1", user='mp2', passwd="eecs116", db="flights", port=3306)
cur = db.cursor()


# Query 1
def query1():
    dep = input("Please enter the airport code for the departure airport:")
    arr = input("Please enter the airport code for the destination airport:")
    date = input("What is the date of the flight in yyyy-mm-dd?")

    sql = "SELECT Flight_number, min(amount) " \
        "FROM fare NATURAL JOIN leg_instance " \
        "WHERE Departure_airport_code = \"" \
        + str(dep) + "\" and Arrival_airport_code = \"" \
        + str(arr) + "\" and Leg_date = \"" + str(date) + "\""

    cur.execute(sql)

    row = cur.fetchone()
    print("The cheapest flight is " + str(row[0]) + ", and the cost is " + str(row[1]) + ".")


# Query 2
def query2():
    name = input("Please enter the customer’s name:")
    sql = "SELECT Flight_number, Seat_number " \
          "FROM seat_reservation " \
          "WHERE Customer_name = \"" + str(name) + "\""
    cur.execute(sql)
    for row in cur.fetchall():
        print("The flight number is " + str(row[0]) + ", and the seat number is " + str(row[1]) + ".")

# Query 3
def query3():
    airline = input("What is the name of the airline?")
    sql = "SELECT Flight_number FROM flight NATURAL JOIN flight_leg " \
          "WHERE Airline = \"" + str(airline) + "\""


    cur.execute(sql)

    print("The non-stop flights are: ")
    for row in cur.fetchall():
        print(str(row[0]))


# Query 4
def query4():
    sql = "SELECT max(Airplane_id) FROM airplane"
    cur.execute(sql)
    idTup = cur.fetchone()
    id = int(idTup[0] + 1)
    numSeats = int(input("Please enter the total number of seats:"))
    planeType = input("Please enter the airplane type:")
    sql = ("""INSERT INTO airplane (Airplane_id, Total_number_of_seats, Airplane_type) VALUES (%s, %s, %s)""")
    val = (id, numSeats, planeType)
    cur.execute(sql, val)
    db.commit()
    print("The new airplane has been added with id: " + str(id))


# Query 5
def query5():
    sql = "SELECT count(Flight_number) FROM fare WHERE Amount < 200"
    cur.execute(sql)
    countTup = cur.fetchone()
    count = countTup[0]
    factor = float(input("Please enter a factor (e.g. 0.2 will increase all fares by 20%):"))
    factor = 1.0 + factor
    sql = "UPDATE fare SET Amount = Amount * %s WHERE Amount < 200"
    cur.execute(sql, str(factor))
    db.commit()
    print(str(count) + " fares are affected")


# Query 6
def query6():
    flight_no = input("Please enter the flight number: ")
    name = input("Please enter the customer name: ")
    sql = "SELECT seat_number FROM seat_reservation WHERE Customer_name = %s AND Flight_number = %s"
    val = (name, flight_no)
    cur.execute(sql, val)
    seatNumTup = cur.fetchone()
    seatNum = seatNumTup[0]
    sql = "DELETE FROM seat_reservation WHERE Customer_name = %s AND Flight_number = %s"
    cur.execute(sql, val)
    db.commit()
    print("Seat " + seatNum + " is released.")


while True:
    i = int(input("\n***Task/Query Info:***\n"
                  "1. Query. Find the cheapest flight given airports and a date.\n"
                  "2. Query. Find the flight and seat information for a customer.\n"
                  "3. Query. Find all non-stop flights for an airline.\n"
                  "4. Task. Add a new airplane.\n"
                  "5. Task. Increase low-cost fares(≤ 200) by a factor.\n"
                  "6. Task. Remove a seat reservation.\n"
                  "Input a task number (1-6) or input 0 to exit:"))
    if i == 0:
        break
    elif i == 1:
        query1()
    elif i == 2:
        query2()
    elif i == 3:
        query3()
    elif i == 4:
        query4()
    elif i == 5:
        query5()
    elif i == 6:
        query6()
db.close()
