# Write your solution here
def line(p, q):
    if q == "":
        print("*" * p)

    elif len(q) > 0:
        print(q[0] * p) 

    else:
        print(q * p)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")