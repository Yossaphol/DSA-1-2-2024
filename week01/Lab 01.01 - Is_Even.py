"""oddeven"""
def main(n):
    """main"""
    if n[-1] in ("0","2","4","6","8"):
        print("True")
    else:
        print("False")
main(input())