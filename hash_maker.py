from passlib.context import CryptContext

# 1. Setup the exact same context you used in your main.py file
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. Type whatever you want your test password to be right here
my_hash = pwd_context.hash("getin00")

# 3. Print it out to the terminal!
print(my_hash)