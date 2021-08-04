# closure

def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of  # 返回值是exponent_of函数