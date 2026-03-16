# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

if __name__ == '__main__':
    mystr = ""
    n = int(input())
    for i in range(n+1):
        if i!=0:
            if i > n:
                break
            else:
                mystr=mystr+(str(i))
    print(int(mystr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
