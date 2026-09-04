package modelo;

public abstract class Financiamento {

    protected double valorImovel;
    protected int prazoFinanciamentoAnos;
    protected double taxaJurosAnual;



    // Construtor da classe
    public Financiamento(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual) {
        this.valorImovel = valorImovel;
        this.prazoFinanciamentoAnos = prazoFinanciamentoAnos;
        this.taxaJurosAnual = taxaJurosAnual /100.0;
    }

    //Métodos:


    public double getValorImovel() {
        return this.valorImovel;
    }

    public int getPrazoFinanciamentoAnos() {
        return this.prazoFinanciamentoAnos;
    }

    public double getTaxaJurosAnual() {
        return this.taxaJurosAnual;
    }

    public double calcularPagamentoMensal(){
        return (this.valorImovel / (this.prazoFinanciamentoAnos * 12)) * (1+ (this.taxaJurosAnual / 12));
    }

    public abstract double calcularTotalPagamento();

    public void exibirDadosFinanciamento(){

        System.out.println("=========================");
        System.out.println("INFORMAÇÕES BÁSICAS SOBRE O FINANCIAMENTO: ");
        System.out.println("TIPO DO FINANCIAMENTO: " + getClass().getSimpleName());
        System.out.println("VALOR DO IMOVEL: " + getValorImovel());
        System.out.println("PRAZO DO FINANCIAMENTO EM ANOS: " + getPrazoFinanciamentoAnos());
        System.out.println("A TAXA DE JUROS ANUAL É DE: " + getTaxaJurosAnual() + "%" );
        System.out.println("O PAGAMENTO MENSAL DO FINCANCIAMENTO SERA DE: R$" + calcularPagamentoMensal());
        System.out.println("O PAGAMENTO TOTAL DO FINANCIAMENTO SERA DE: R$" + String.format("%.2f", calcularTotalPagamento()));
    }

}
