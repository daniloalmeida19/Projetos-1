Algoritmo "Par ou Impar"
Var
   N: inteiro
   R: Caractere

Funcao ParouImpar (V: Inteiro): Caractere
Inicio
   Se (V%2 = 0) entao
      Retorne "Par"

   senao
      Retorne "Impar"
   Fimse
Fimfuncao

Inicio
   Escreva("Digite um numero: ")
   LEIA (N)
   R <- Parouimpar(N)
   Escreva ("O Numero ", N, " e um valor " , R)
Fimalgoritmo