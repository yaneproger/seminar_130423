

n = int(input("speed: "))
m = int(input("distance: "))


# res = (m+n-1)//m

temp = int(bool(m % n))
print(temp)
res = m//n + temp

print(res)
