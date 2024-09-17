def laff_copy(x, y):
    # Section 1.5.2, Homework 1.5.2.1
    # Vector-vector COPY routine.

    # vector laff_copy(vector x, vector y)
    # Copies the vector x into the vector y, returning the vector y.
    # Note: we will be using list types here (as opposed to n*1 or 1*n 2D arrays).

    if not ((type(x) == type([])) and (type(y) == type([]))):
        print("laff_copy: incorrect type for argument(s), must be lists")
        return y
    elif (len(x) != len(y)):
        print("laff_copy: argument lengths must be equal")
        return y
    else:
        for i in range(len(x)):
            y[i] = x[i]
        return y

def laff_scal(alpha, x):
    # Section 1.5.3, Homework 1.5.3.1
    # Vector SCAL routine.

    # vector laff_scal(scalar alpha, vector x)
    # Scales the vector x by a factor of alpha, returning the scaled x vector.
    # Note: x should be a list of numbers.

    if not (((type(alpha) == type(1)) or (type(alpha) == type(1.0)))
            and (type(x) == type([]))):
        print("laff_scal: incorrect type for argument(s), must be scalar & list")
        return x
    else:
        for i in range(len(x)):
            x[i] = alpha * x[i]
        return x

