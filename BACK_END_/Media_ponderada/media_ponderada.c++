#include <stdio.h>
#include <stdlib.h>

int main()
{
    //declaraçao de variaveis    
    float  nota1, nota2, nota3, media;     
    int pesoN1, pesoN2, pesoN3;
    printf("Nota 1: ");     
    scanf("%f",&nota1);    
    printf("Peso Nota 1: ");     
    scanf("%i",&pesoN1);  
    printf("Nota 2: ");     
    scanf("%f",&nota2);     
    printf("Peso Nota 2: ");     
    scanf("%i",&pesoN2);  
    printf("Nota 3: ");     
    scanf("%f",&nota3); 
    printf("Peso Nota 3: ");     
    scanf("%i",&pesoN3);  

    media = ((nota1*pesoN1)+(nota2*pesoN2)+(nota3*pesoN3))/(pesoN1+pesoN2+pesoN3);
    printf("Média final: %f",media);
}