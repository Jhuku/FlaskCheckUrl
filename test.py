
# print 'enteredUrl type=',type(enteredUrl.encode('utf-8'))
# print '\n Safe Urls'




search = "ele\n"
with open("dummy.txt") as file:
    if any(line == search for line in file):
        print("Found it!")
    else:
        print("Move along.")
