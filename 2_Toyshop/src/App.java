import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Lottery r = new Lottery();
        try (Scanner scan = new Scanner(System.in)) {
            while (true) {
                System.out.print("""
                        Menu:
                            1 - Add a new toy to the lottery
                            2 - Set drop weight toys
                            3 - Hold a lottery and save results
                            4 - EXIT
                        Enter a number of the command: \s""");
                var selection = scan.next();
                switch (selection) {
                    case "1" -> r.addToy();
                    case "2" -> r.setDrop();
                    case "3" -> r.lottery();
                    case "4" -> {
                        System.out.println("See you soon");
                        System.exit(0);
                    }
                    default -> System.out.println("Incorrect selection. Try again.");
                }
            }
        }catch (Exception e) {
            // TODO: handle exception
        }
    }
}