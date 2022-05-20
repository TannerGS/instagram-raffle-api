import os
from dotenv import load_dotenv
load_dotenv() 

user = os.environ.get('ACCESS-TOKEN')
print(user)


