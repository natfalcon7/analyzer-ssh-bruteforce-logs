import random
from datetime import datetime, timedelta

initial_time = datetime(2026, 2, 19, 0, 0, 0)

users = ["root", "admin", "josipa", "ubuntu", "oracle", "sergio"]
results = ["FAIL", "FAIL", "FAIL", "SUCCESS"]
ips = ["185.220.101.42", "192.168.1.10", "192.168.1.15", "192.168.2.20", "192.168.1.25", "192.255.1.10"]
countries = ["Argentina", "Singapur", "USA", "Croatia"]

with open("ssh_logs.csv", "w") as f:
    
    # header
    f.write("timestamp,ip,user,result,country\n")
    
    # data
    for i in range(10000):
        seconds_random = random.randint(0, 86400)
        moment = initial_time + timedelta(seconds=seconds_random)
        ip = random.choice(ips)
        user = random.choice(users)
        result = random.choice(results)
        country = random.choice(countries)
        
        f.write(f"{moment},{ip},{user},{result},{country}\n")  

