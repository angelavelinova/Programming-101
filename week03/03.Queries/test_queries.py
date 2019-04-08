import unittest
from queries import *
filename="data.csv"
class TestReversedPolishNotation(unittest.TestCase):

	def test_if_all_data_is_returned_by_salary(self):
		s = "4550"
		expected_result = ['Mary Powell,gray,Wright-Hoover,dglover@yahoo.com,02870375047,4550\n']
		self.assertEqual(filter(filename,salary=s),expected_result)

	def test_if_all_data_is_returned_by_full_name(self):
		n = "Teresa Nelson"
		expected_result = ['Teresa Nelson,silver,Smith-Kelly,taylorapril@gmail.com,753-792-5034x06814,2485\n']
		self.assertEqual(filter(filename,full_name=n),expected_result)

	def test_if_all_data_is_returned_by_favourite_color(self):
		c = "maroon"
		expected_result = ['Amanda Hughes,maroon,"Franco, Harvey and Payne",wilkinsonjason@hotmail.com,1-366-403-5794x0781,3779\n', 'Frank Mcdonald,maroon,"Gonzales, Jones and Clark",operkins@hotmail.com,(084)057-7479x38393,5694\n', 'Karl Anderson,maroon,Greer-Brown,zanderson@hotmail.com,530.581.9790x927,8157\n', 'Taylor Smith,maroon,"Vargas, Johnston and Wilson",brookskayla@hotmail.com,361-050-8073,1877\n', 'Meredith Williams,maroon,Thomas-Barnes,mckayjennifer@hotmail.com,985.240.5856x7832,4461\n', 'Patricia Salas,maroon,Bowman Ltd,flara@gmail.com,(045)068-2028x4528,8837\n', 'Nicolas Arellano,maroon,"Martinez, Meyers and Foley",brownvincent@gmail.com,+31(7)4922109880,9705\n', 'Sandra Clark,maroon,Hopkins-Reyes,cesarmason@yahoo.com,(728)483-3602x255,5971\n', 'Sarah Spencer,maroon,"Mcintyre, Rodriguez and House",vhughes@yahoo.com,(405)158-4692x0532,9926\n', 'Mark Drake,maroon,Myers-Brown,richard83@gmail.com,+09(5)2782023228,2622\n', 'Kimberly Williams,maroon,"Ruiz, Williams and Schultz",idavidson@hotmail.com,009.146.6877,2351\n', 'Hunter Vargas,maroon,Anderson-Ramirez,nixonjonathan@gmail.com,602.911.5067,3687\n', 'Victoria White,maroon,Nelson-Chavez,moralesashley@hotmail.com,1-343-009-7512x70680,9938\n', 'Bobby Jones,maroon,Peterson Ltd,wallsheather@hotmail.com,(318)090-5241x441,5563\n', 'Lori Johnson,maroon,Johnson and Sons,kellymatthew@gmail.com,(020)023-5361,8075\n', 'Jared Peterson,maroon,"Lee, Jones and Gill",jerryknight@hotmail.com,899.524.4170x5792,9165\n', 'Christopher Chavez,maroon,"Perkins, Cochran and Powell",cdaniels@gmail.com,1-692-749-7750x142,7989\n', 'Lance Miller,maroon,Reid-Norris,ramseybrian@yahoo.com,06424198416,3948\n', 'Ryan Johnson,maroon,"Robinson, Smith and Haynes",kjones@gmail.com,246.544.4636,7062\n', 'Andrea Shepherd,maroon,Simon-Buchanan,huffmanelizabeth@gmail.com,07207058593,3666\n', 'Maxwell Johnson,maroon,"Garcia, Gonzalez and Davis",xmatthews@yahoo.com,710-194-3657x37680,6733\n', 'Theresa Ramos,maroon,Williams-Todd,jeffery40@hotmail.com,042-484-0427x13915,3392\n', 'Charles Fisher,maroon,Huerta-Garcia,conradmichael@gmail.com,970-850-0000,3090\n', 'Denise Martin,maroon,Stephens-Silva,christinawarren@yahoo.com,+68(2)9737587237,2599\n', 'Alan Rangel,maroon,Lee LLC,cmartinez@hotmail.com,(485)723-6325x7701,1121\n', 'Andrew Chase,maroon,Gonzalez Group,lucasbrian@yahoo.com,1-324-009-8104,1774\n', 'Thomas Warren,maroon,Flores-Mitchell,lucasnelson@gmail.com,+18(2)0883465044,1872\n', 'John Johnson,maroon,Ford PLC,larrymcdaniel@yahoo.com,1-260-106-1019,9690\n', 'Jennifer Zamora,maroon,Miller-Bowers,ijackson@hotmail.com,970.613.2310x740,2567\n', 'Lisa Ayala,maroon,"Smith, Robinson and Arnold",cody19@hotmail.com,(700)406-7305x99054,3888\n']
		self.assertEqual(filter(filename,favourite_color=c),expected_result)
	def test_if_all_data_is_returned_by_email(self):
		e = "hortiz@hotmail.com"
		expected_result = ['Angela Smith,olive,"Bowman, Miller and Brown",hortiz@hotmail.com,654-892-0237x2715,2290\n']
		self.assertEqual(filter(filename,email=e),expected_result)

	def test_if_all_data_is_returned_by_phone_number(self):
		n = "654-892-0237x2715"
		expected_result = ['Angela Smith,olive,"Bowman, Miller and Brown",hortiz@hotmail.com,654-892-0237x2715,2290\n']
		self.assertEqual(filter(filename,phone_number=n),expected_result)

	def test_if_all_data_is_returned_by_full_name_and_favourite_color(self):
		n = 'Diana Harris'
		c = 'lime'
		expected_result = ['Diana Harris,lime,Martin-Barnes,timothy81@gmail.com,1-860-251-9980x6941,5354\n']
		self.assertEqual(filter(filename,full_name=n, favourite_color=c),expected_result)

	def test_if_all_data_is_returned_by_full_name__startswith_and_email__contains(self):
		fs="Diana"
		ec="@gmail"
		expected_result = ['Diana Harris,lime,Martin-Barnes,timothy81@gmail.com,1-860-251-9980x6941,5354\n']
		self.assertEqual(filter(filename,full_name__startswith=fs, email__contains=ec),expected_result)

	def test_when_returns_all_data_for_people_with_salary_gt_and_lt_something_ordered_by_salary(self):
		expected_result = [['Keith Smith', 'fuchsia', 'Castro-Ingram', 'mcleanbrian@yahoo.com', '+11(4)0692238929', '9005\n'], ['Lisa Wagner', 'teal', 'Smith and Sons', 'kevinmiller@gmail.com', '05934705632', '9104\n'], ['Diane White', 'purple', 'Richardson Ltd', 'nicole00@yahoo.com', '(742)341-5158', '9135\n'], ['Jared Peterson', 'maroon', '"Lee Jones and Gill"', 'jerryknight@hotmail.com', '899.524.4170x5792', '9165\n']]
		self.assertEqual(filter(filename,salary__gt=9000,salary__lt=9190,order_by="salary"),expected_result)

	def test_if_count_right_number_of_returned_rows(self):
		expected_result = 4
		self.assertEqual(count(filename,salary__gt=9000,salary__lt=9190,order_by="salary"),expected_result)

	def test_if_first_returns_first_element_from_filter(self):
		expected_result = ['Keith Smith', 'fuchsia', 'Castro-Ingram', 'mcleanbrian@yahoo.com', '+11(4)0692238929', '9005\n']
		self.assertEqual(first(filename,salary__gt=9000,salary__lt=9190,order_by="salary"),expected_result)

	def test_if_first_returns_last_element_from_filter(self):
		expected_result = ['Jared Peterson', 'maroon', '"Lee Jones and Gill"', 'jerryknight@hotmail.com', '899.524.4170x5792', '9165\n']
		self.assertEqual(last(filename,salary__gt=9000,salary__lt=9190,order_by="salary"),expected_result)


if __name__ == '__main__':
	unittest.main()
