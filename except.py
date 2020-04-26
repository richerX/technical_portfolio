try:
    print(1)
except:
    print(2)
else:
    print(3)
finally:
    print(4)
    
print()
print()

try:
    print(1 / 0)
except:
    print(2)
else:
    print(3)
finally:
    print(4)