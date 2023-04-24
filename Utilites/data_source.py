from Uitilites import read_utilites

test_add_valid_employee_data = [
    ["bot@behera.com", "bot123", "John Wick", "wick@gmail.com", "Engineer"]]

test_invalid_login_data = read_utilites.get_csv_as_list("../test_data/test_invalidLogin.csv")