    # ASSMNT NUMBER 1
""" ========================================================================="""

# Q.1. W.a.p to check Data Quality, input for number of missing values incase if it
# is 0 then print message as ‘cleaned Data’ otherwise print message as ‘Data
# Cleaning Required’

# missing_values = int(input("Enter the number of missing values: "))

# if missing_values == 0:
#     print("Cleaned Data")
# else:
#     print("Data Cleaning Required")

 # =================================================================================

# Q.2  W.a.p to check Data Storage, Read storage used, if it is above 80 then
# display message as ‘Storage almost full’ otherwise display message as
# ‘Storage Okay’

#data_storage = int(input("Read Storage Used: "))
#if data_storage >=80 :
 #       print("Storage Almost Full ")
#else:
  #      print("Storage Okay ")"""
 # ===============================================================================
#3. W.a.p to read username and password then check user is valid user or
# Invalid user
# If user enters username as ‘AVD’ and password as ‘Python’ then valid user
#username = input("Enter Username: ")
#password = input("Enter Password: ")

#if username == "AVD" and password == "Python":
#    print("Valid User")
#else:
#    print("Invalid User")

#========================================================================================
# Q4  Consider customer has Rs:6000 in his account, now read withdraw amount
    # then update his balance. Note: if user enter valid amount then only update
    # balance otherwise display Error message as ‘Sorry...! You have low funds’

balance = 6000

withdraw = int(input("Enter Withdraw Amount: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Sorry...! You have low funds")