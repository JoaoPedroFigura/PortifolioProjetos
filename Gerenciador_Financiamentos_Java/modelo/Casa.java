package modelo;

public class Casa extends Financiamento{

    private double areaConstruida;
    private double tamanhoTerreno;

    public Casa(double valorImovel, int prazoFinanciamento, double taxaJurosAnual, double areaConstruida, double tamanhoTerreno) {
        super(valorImovel, prazoFinanciamento, taxaJurosAnual);
        this.areaConstruida = areaConstruida;
        this.tamanhoTerreno = tamanhoTerreno;
    }

    public double getAreaConstruida() {
        return areaConstruida;
    }

    public double getTamanhoTerreno() {
        return tamanhoTerreno;
    }

    @Override
    public double calcularPagamentoMensal() {
        return super.calcularPagamentoMensal() + 240;
    }

    @Override
    public double calcularTotalPagamento() {
        return calcularPagamentoMensal() * prazoFinanciamentoAnos *12;
    }

    @Override
    public void exibirDadosFinanciamento() {
        super.exibirDadosFinanciamento();
        System.out.println("=========================");
        System.out.println("Informações adicionais: ");
        System.out.println("Tamanho do terreno da casa: "  + this.tamanhoTerreno);
        System.out.println("Area construida: "  + this.areaConstruida);
        System.out.println("=========================");

    }
}
