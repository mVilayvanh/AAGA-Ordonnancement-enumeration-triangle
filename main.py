import order.order_deg as ODEG
from functools import cmp_to_key

if __name__ == "__main__":
    l = [3, 1, 4, 2]
    l.sort(key=cmp_to_key(ODEG.compare_degree_desc))
    print(l)