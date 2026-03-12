ap1_n1 = float(input("digite a nota da sua primeira avaliação da n1:"))
ap2_n1 = float(input("digite a nota da sua primeira avaliação da n1:"))
media_n1 = (ap1_n1+ap2_n1)/2
print("Sua média da n1 é: ", media_n1)

ap1_n2 = float(input("digite a nota da sua primeira avaliação da n2:"))
ap2_n2 = float(input("digite a nota da sua primeira avaliação da n2:"))
media_n2 = (ap1_n2+ap2_n2)/2
print("Sua média da n2 é: ", media_n2)

media_final = ((media_n1)*2+(media_n2)*3)/5
print("Sua média final é: ", media_final)

if media_final >= 6.0:
    {
        print("Parabéns, você foi aprovado com média:", media_final)
    }
elif media_final >= 3.0 and media_final <= 5.9:
    {
        print("Sua média é:", media_final, "você está de AF!")
    }
else:
    {
        print("Sua média é:", media_final, "você foi reprovado!")
    }