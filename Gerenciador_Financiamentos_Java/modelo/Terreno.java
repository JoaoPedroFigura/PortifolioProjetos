package modelo;

public class Terreno extends Financiamento{

    private final String tipoDeZona;

    public Terreno(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual, String tipoDeZona) {
        super(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual);
        this.tipoDeZona = tipoDeZona;
    }

    public String getTipoDeZona() {
        return tipoDeZona;
    }

    @Override
    public double calcularPagamentoMensal() {
        return super.calcularPagamentoMensal() * 1.02;
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
        System.out.println("O terreno fica localizado na zona: " + this.tipoDeZona);
    }
}
