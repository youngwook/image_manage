import bcrypt

password = "hello"
 # Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
password1 = "hello"
hashed1 = bcrypt.hashpw(password1, bcrypt.gensalt())
# Check that a unhashed password matches one that has previously been
#   hashed
print hashed
print hashed1
if bcrypt.hashpw(password, hashed) == hashed:
    print("It Matches!")
else:
        print("It Does not Match :(")

if bcrypt.hashpw(password1, hashed) == hashed:
    print("It Matches!")
else:
        print("It Does not Match :(")