"""maxminavg"""
import json
def main():
    """main"""
    my_list = json.loads(input())
    avg = 0
    mak = -99999999999999999999
    noi = 99999999999999999999
    for i in my_list:
        i = round(i,2)
        avg += i
        if i > mak:
            mak = i
        if i < noi:
            noi = i
    avg = round(avg / len(my_list), 2)
    print(f"({mak}, {noi}, {avg})")
main()