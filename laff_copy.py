def laff_copy(x, y):
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

