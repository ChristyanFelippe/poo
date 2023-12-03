public class App{
    
    public static void main(String[] args) {
        System.out.println("hello world");
        Pessoa pessoa1 = new Pessoa();
        pessoa1.setNome("Chris");
        pessoa1.setIdade(21);
        System.out.println(pessoa1.getNome());
        System.out.println(pessoa1.getIdade());
    }
}

