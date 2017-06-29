import re
file = open("html_list_archived.txt", 'r')

userIdSet = set()
groupIdSet = set()

#row_header_id_thread:1406269782734629
#row_header_id_user:100002197983451

for line in file:
    user = re.findall('user:(.+?)"', line)
    group = re.findall('thread:(.+?)"', line)

    for id in user:
        userIdSet.add(id)

    for id in group:
        groupIdSet.add(id)

output = open("output.txt", 'w')

print("User:")
output.write("User:\n")
for id in userIdSet:
    print(id)
    output.write(id + "\n")

print("Group:")
output.write("Group:\n")
for id in groupIdSet:
    print(id)
    output.write(id + "\n")

output.close()
