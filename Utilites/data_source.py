from Uitilites import read_utilites

# test_invalid_login_data = [
#     ("saul@gmail", "saul123", "Invalid email or password."),
#     ("kim@gmail", "kim123", "Invalid email or password."),
#     ("john@gmail", "john123", "Invalid email or password.")
# ]

test_add_valid_employee_data = [
    ["princy@jain.com", "padmakshi123", "John Wick", "wick@gmail.com", "Engineer"]]


# test_add_valid_employee_data = read_utilites.get_sheet_as_list("../test_data/selenium.xlsx", "test_add_valid_employee")
# test_invalid_profile_upload_data = read_utilites.get_sheet_as_list("../test_data/selenium.xlsx","test_invalid_profile_upload")
test_invalid_login_data = read_utilites.get_csv_as_list("../test_data/test_invalidLogin.csv")