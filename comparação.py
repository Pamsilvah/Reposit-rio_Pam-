#comparação
´´´
n1 = int(input('digite um número'))
def comparar(n1):
    return n1 % 2 == 0
print(comparar(n1))
´´´
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")