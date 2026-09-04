package util;

import java.util.Scanner;

public class InterfaceUsuario {
    Scanner sc = new Scanner(System.in);

    /**
     * Solicita o valor do imóvel, verifica se é um valor válido e então o retorna, caso não seja, chama um loop até que o valor inserido seja válido*/
    public double pedirValorImovel(){
        boolean entradaValida = false;
        double valorDoImovel;
        do {
            System.out.print("Digite o valor do Imóvel: R$");
            valorDoImovel = sc.nextDouble();
            if (valorDoImovel <= 0){
                System.out.println("Esse valor não é válido! Tente Novamente");
            } else {
                entradaValida = true;
            }
        } while(!(entradaValida));
        return valorDoImovel;
    }

    /** Solicita o tempo do financiamento, verifica se é um valor válido e então o retorna, caso não seja, chama um loop até que o valor inserido seja válido */
    public int pedirPrazoFinanciamento(){
        boolean prazoEmAnosValido = false;
        int prazoEmAnos;
        do {
            System.out.print("Digite o prazo do finânciamento em anos: ");
             prazoEmAnos = sc.nextInt();
             if (prazoEmAnos < 1 || prazoEmAnos > 35) {
                 System.out.println("O prazo digitado pode ser muito longo (Excede 35 anos) ou muito curto (Menos que 1 ano)");
             } else {
                 prazoEmAnosValido = true;
             }
        } while (!(prazoEmAnosValido));
        return prazoEmAnos;
    }

    /** Solicita a taxa de juros anual, verifica se ela  é válida e então retorna o valor, caso não seja entra em loop até o valor inserido ser válido*/
    public double pedirTaxaJurosAnual(){
        boolean taxaJurosAnualValida = false;
        double taxaDeJurosAnual;
        do {
            System.out.print("Digite a taxa de juros anual: ");
            taxaDeJurosAnual = sc.nextDouble();

            if (taxaDeJurosAnual <=0 || taxaDeJurosAnual > 13  ) {
                System.out.println("A taxa de juros digitada é inválida!");

            } else {
                taxaJurosAnualValida = true;
            }
        } while (!(taxaJurosAnualValida));
        return taxaDeJurosAnual;
    }
}
