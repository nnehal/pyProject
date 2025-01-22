import subprocess

def ping(mysite):
    command = (f"ping -c 1 {mysite}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = process.communicate()[0].decode("utf-8")

    if "0 recieved" in output:
        return False
    else:
        return True
    
with open("sites.txt") as file:
    mysites = file.readlines()

for site in mysites:
    currsite = site.strip()
    mystatus = ping(currsite)
    if mystatus:
        print(f"{currsite} is fine")
    else:
        print("**************************")
        print("vvvvvvvvvvvvvvvvvvvvvvvvvv")
        print(f"{currsite} is down!!!")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("**************************")
    print("--------------")
    