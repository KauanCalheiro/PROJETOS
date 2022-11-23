 #include <iostream>

float salario_min, hrs_trab, valor_hrs_trab, salario_mes, hrs_extra, valor_hrs_extra, salario_bruto, salario_liquido, salario_final;
int dependentes_funcionario;

using std::cin;
using std::cout;

int main()
{
    //Entrada_de_Dados:
    printf("dois");
    cout<< "==============================================================";
    cout<< "\nValor do Salário Mínimo: R$ ";
    cin>> salario_min;
    cout<< "--------------------------------------------------------------";
    cout<< "\nQuantidade de horas trabalhadas: ";
    cin>> hrs_trab;
    cout<< "--------------------------------------------------------------";
    cout<< "\nPossui horas extras? ";
    cin>> hrs_extra;
    cout<< "--------------------------------------------------------------";
    cout<< "\nQuantidade de pessoas dependentes: ";
    cin>> dependentes_funcionario;
    if (dependentes_funcionario > 0){
        dependentes_funcionario = (45*dependentes_funcionario);        
    }    

    //Contas:
    valor_hrs_trab = salario_min * 1/20;
    salario_mes = hrs_trab * valor_hrs_trab;
    valor_hrs_extra = (hrs_extra * ((salario_min / 20)*(45 / 100)));
    salario_bruto = salario_mes + dependentes_funcionario + valor_hrs_extra;


    //Script:
    cout<< "==============================================================";
    cout<< "\nO salário bruto é de: R$ " <<salario_bruto;
    cout<< "\n--------------------------------------------------------------";
    if (salario_bruto < 1000){
        cout<<"\nIsento de imposto";
    }
    else if (salario_bruto >= 1000 and salario_bruto <= 3000){
        cout<< "\n15% de imposto";
        salario_liquido = (salario_bruto - (salario_bruto * (15/100)));
     }
    else {
        cout<< "\n25% de imposto";
        salario_liquido = salario_bruto - (salario_bruto * (25/100));
    }
    cout<< "\n--------------------------------------------------------------";
    cout<< "\nSalário líquido é de: R$ "<< salario_liquido;
    cout<< "\n--------------------------------------------------------------";
    if (salario_liquido <= 2500){
        salario_final = salario_liquido + 150;
        cout<< "\nVoce recebeu uma gratificação de R$ 150,00";
    }
    else{
        salario_final = salario_liquido + 55;
        cout<<"\nVoce recebeu uma gratificação de R$ 55,00";
    }
    cout<< "\n--------------------------------------------------------------";
    cout<<"\nSalário final é de: R$ "<< salario_final;
    cout<< "\n==============================================================";
    return 0;
}