'''
Created Date: Saturday September 11th 2021 11:50:50 pm
Author: Andrés X. Vargas
-----
Last Modified: Sunday September 12th 2021 12:28:04 am
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''


def morral(cap, weights, values, n):
    if n == 0 or cap == 0:
        return 0
    if weights[n-1] > cap:
        return morral(cap, weights, values, n-1)

    return max(morral(cap, weights, values, n-1),morral(cap-weights[n-1], weights, values, n-1)+values[n-1])

if __name__ == '__main__':
    cap = 50
    values = [60, 100, 120]
    weights = [10, 20, 30]
    n = len(values)

    result = morral(cap, weights, values, n)
    print(result)
