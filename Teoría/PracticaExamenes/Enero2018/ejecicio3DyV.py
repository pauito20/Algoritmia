def raiz_cuadrada_entera(n:int):
    def R(num:int) -> int:
        if num*num == n:
            return num
        else:
            if num*num > n:
                return R(num//2)
            elif (num+1) * (num+1) <= n:
                return R(num+1)
            else:
                return R(num-1)

    return R(n//2)


if __name__ == "__main__":
    x = int(input("Introduce un número entero: "))
    print("La raiz cuadrada del número {} es {}".format(x, raiz_cuadrada_entera(x)))