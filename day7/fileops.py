path = input("Enter the file path:")
key = input("Enter the key:")
var = input("Enter the desired value:")

def update_server_conf(path, key, var):
    with open(path, 'r') as x:
        lines = x.readlines()

    with open(path, 'w') as x:
        for i in lines:
            if key in i:
                x.write(key + "=" + var)
            else:
                x.write(i)

print(path)
print(key)
print(var)

update_server_conf(path, key, var)