package main;

import modelo.Financiamento;
import util.InterfaceUsuario;

import java.util.ArrayList;

public class Main {
    static void main() {
        InterfaceUsuario interfaceDoUsuario = new InterfaceUsuario();

        ArrayList<Financiamento> financiamentos = new ArrayList<>();


        //Editar o valor da comparação com i para adicionar mais financiamentos
        for (int i = 0; i <=0; i++) {

            System.out.println("==========");
            double valorImovel = interfaceDoUsuario.pedirValorImovel();
            System.out.println("==========");
            int prazoFinanciamentoAnos = interfaceDoUsuario.pedirPrazoFinanciamento();
            System.out.println("==========");
            double taxaJurosAnual = interfaceDoUsuario.pedirTaxaJurosAnual();
            System.out.println("==========");

            Financiamento financiamento = new modelo.Terreno(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual, "Urbana");

            System.out.printf("O financiamento %d foi criado \n", i+1);

            financiamentos.add(financiamento);
        }

        financiamentos.add(new modelo.Casa(500000, 10, 10, 16, 32));
        financiamentos.add(new modelo.Apartamento(500000, 10, 10, 1, 2));
        financiamentos.add(new modelo.Terreno(500000, 10, 10, "Rural"));


        for (Financiamento f : financiamentos) {
           f.exibirDadosFinanciamento();
        }

        double valorTotaldosImoveis = 0;
        double valorTotalDosFinanciamentos = 0;


        for (Financiamento f : financiamentos) {
            valorTotaldosImoveis+= f.getValorImovel();
            valorTotalDosFinanciamentos+= f.calcularTotalPagamento();
        }

        System.out.println("Total de todos os imóveis: R$" + String.format("%.2f", valorTotaldosImoveis));
        System.out.println("Total de todos os Financiamentos R$:" + String.format("%.2f", valorTotalDosFinanciamentos));


    }
}
