import sqlite3
import sys

def delete_new_line(string):
	string=string[0:len(string)-1]
	return string

def create_user_table():
	connection = sqlite3.connect('business_card.db')
	cursor = connection.cursor()

	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS User
			(
			`id` int AUTO_INCREMENT,
			`first_name` varchar(100) NOT NULL,
			`email` varchar(50) NOT NULL,
			`age` int NOT NULL,
			`phone` varchar(15) NOT NULL,
			`additional_info` text,
			PRIMARY KEY (`id`)
			)
		"""
	)

	connection.commit()
	connection.close()

def insert_new_business_card(id, first_name, email, age, phone, additional_info):
	connection = sqlite3.connect('business_card.db')
	cursor = connection.cursor()
	cursor.execute(
		"""
		INSERT INTO User VALUES('{id}', '{first_name}', '{email}', '{age}', '{phone}', '{additional_info}');
		""".format(id=id, first_name=first_name, email=email, age=age, phone=phone, additional_info=additional_info)
	)

	connection.commit()
	connection.close()


def select_business_cards():
	connection = sqlite3.connect('business_card.db')
	cursor = connection.cursor()

	cursor.execute("SELECT id, first_name, email, age, phone, additional_info FROM User")
	users = cursor.fetchall()

	connection.commit()
	connection.close()

	return users

def delete_business_card(id):
	connection = sqlite3.connect('business_card.db')
	cursor = connection.cursor()

	cursor.execute("""DELETE FROM User WHERE id=?;""", (id,))

	connection.commit()
	connection.close()

def get_business_card(id):
	connection = sqlite3.connect('business_card.db')
	cursor = connection.cursor()

	cursor.execute("""SELECT * FROM User WHERE id=?;""", (id,))
	info = cursor.fetchone()

	connection.commit()
	connection.close()

	return info
 

def help():
	print("#############" +'\n'+ "###Options###" + '\n' + "#############" + '\n')
	print("1. `add` - insert new business card")
	print("2. `list` - list all business cards")
	print("3. `delete` - delete a certain business card (`ID` is required)")
	print("4. `get` - display full information for a certain business card (`ID` is required)")
	print("5. `help` - list all available options")

def main():
	create_user_table()
	print("Hello! This is your business card catalog. What would you like? (enter 'help' to list all available options)" + '\n' + ">> Enter command:")
	option = sys.stdin.readline()
	if option == '1\n':
		arg1 = sys.stdin.readline()
		arg1 = delete_new_line(arg1)
		arg2 = sys.stdin.readline()
		arg2 = delete_new_line(arg2)
		arg3 = sys.stdin.readline()
		arg3 = delete_new_line(arg3)
		arg4 = sys.stdin.readline()
		arg4 = delete_new_line(arg4)
		arg5 = sys.stdin.readline()
		arg5 = delete_new_line(arg5)
		arg6 = sys.stdin.readline()
		arg6 = delete_new_line(arg6)
		insert_new_business_card(int(arg1), arg2, arg3, int(arg4), arg5, arg6)
	elif option == '2\n':
		print(select_business_cards())
	elif option == '3\n':
		info = sys.stdin.readline()
		print(info)
		delete_business_card(id=info)
	elif option == '4\n':
		info = sys.stdin.readline()
		print(get_business_card(id=info))
	elif option == '5\n':
		help()

if __name__ == '__main__':
	main()
