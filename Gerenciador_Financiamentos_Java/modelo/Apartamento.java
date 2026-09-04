package modelo;

public class Apartamento extends Financiamento{


    private int numeroDeVagasNaGaragem;
    private int numeroAndar;

    public Apartamento(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual, int numeroDeVagasNaGaragem, int numeroAndar) {
        super(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual);
        this.numeroAndar = numeroAndar;
        this.numeroDeVagasNaGaragem = numeroDeVagasNaGaragem;
    }


    public int getNumeroDeVagasNaGaragem() {
        return numeroDeVagasNaGaragem;
    }

    public int getNumeroAndar() {
        return numeroAndar;
    }

    @Override
    public double calcularPagamentoMensal() {
        double total = valorImovel * (1+ (taxaJurosAnual * prazoFinanciamentoAnos));
        return total / (prazoFinanciamentoAnos * 12);
    }

    @Override
    public double calcularTotalPagamento() {
        return calcularPagamentoMensal() * prazoFinanciamentoAnos *12;
    }

    @Override
    public void exibirDadosFinanciamento() {
        super.exibirDadosFinanciamento();
        System.out.println("=========================");
        System.out.println("INFORMAÇÕES ADICIONAIS: ");
        System.out.println("Numero de vagas na garagem: " +  this.numeroDeVagasNaGaragem);
        System.out.println("Andar do apartamento: " + this.numeroAndar);
        System.out.println("=========================");

    }
}
