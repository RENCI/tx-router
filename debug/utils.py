def dump_args_and_ret(func):
    """This decorator dumps out the arguments passed to a function before calling it"""
    fname = func.__name__

    def echo_func(*args, **kwargs):
        print(f"{fname} args={args} kwargs={kwargs}")
        ret = func(*args, *kwargs)
        print(f"{fname} args={args} kwargs={kwargs} ret={ret}")
        return ret
    return echo_func


def bag_equal(as2, bs):
    bs2 = list(bs)
    for a in as2:
        if a in bs2:
            bs2.remove(a)
        else:
            return False
    return len(bs2) == 0


