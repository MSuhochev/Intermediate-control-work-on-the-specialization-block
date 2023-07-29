import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class Lottery {

    private static ArrayList<Toys> toyses = new ArrayList<>();
    private static PriorityQueue<Toys> winnings = new PriorityQueue<>();

    private static int idCounter = 0;

    public void addToy() {
        
        String title;
        int drop;
        while (true) {
            Scanner scan = new Scanner(System.in);
            System.out.print("Input toy name: ");
            title = scan.nextLine();
            if (title.isEmpty()) {
                System.out.println("Incorrected Name.");
                break;
            }
            System.out.print("Enter the drop weight of the toy: ");
            String value = scan.nextLine();
            if (isDigit(value)) {
                drop = Integer.parseInt(value);
                if (drop <= 0) {
                    System.out.println("Incorrected input.");
                } else {
                    Toys toy = new Toys(idCounter, title, drop);
                    if (!toyses.contains(toy) || toyses.size() == 0) {
                        idCounter++;
                        toyses.add(toy);
                        System.out.println("New toy was added");
                    } else {
                        System.out.println("This toy is already in the prize fund.");
                    }
                }
            } else {
                System.out.println("The command not exist - select 1, 2, 3 or 4");
            }
            break;
        }
    }

    public void setDrop() {
        try (Scanner scan = new Scanner(System.in)) {
            System.out.print("Enter Toy ID: ");
            String digit = scan.nextLine();
            if (isDigit(digit)) {
                int selectedId = Integer.parseInt(digit);
                if (selectedId >= 0 && selectedId < toyses.size()) {
                    System.out.println("Toy " + toyses.get(selectedId).getToyName() +
                            " has drop of victory " + toyses.get(selectedId).getToyVictoryDrop());
                    System.out.print("Enter new drop of dropping out: ");
                    digit = scan.nextLine();
                    if (isDigit(digit)) {
                        int newDrop = Integer.parseInt(digit);
                        toyses.get(selectedId).setToyVictoryDrop(newDrop);
                        System.out.println("Drop was changed.");
                    } else {
                        System.out.println("Incorrected input. Input drop in percent from 1 to 100.");
                    }
                } else {
                    System.out.println("There is not toy with such ID in toys list.");
                }
            } else {
                System.out.println("Incorrected input.");
            }
        } catch (NumberFormatException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    private static boolean isDigit(String s) throws NumberFormatException {
        try {
            Integer.parseInt(s);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public Toys getWinning() {
        if (winnings.size() == 0) {
            Random rand = new Random();
            for (Toys toy : toyses) {
                for (int i = 0; i < toy.getToyVictoryDrop(); i++) {
                    Toys tmp = new Toys(toy.getToyId(), toy.getToyName(), rand.nextInt(1, 10));
                    winnings.add(tmp);
                }
            }
        }
        return winnings.poll();
    }

    public void lottery() {
        if (toyses.size() >= 2) {
            Toys win = getWinning();
            System.out.println("Win: " + win.getToyName());
            saveResult(win.getInfo());
        } else {
            System.out.println("The winning fund cannot contain less than two toys.");
        }
    }

    private void saveResult(String text) {
        File resultFile = new File("winlist.txt");
        try {
            resultFile.createNewFile();
        } catch (Exception ignored) {
            throw new RuntimeException();
        }
        try (FileWriter fw = new FileWriter("winlist.txt", true)) {
            fw.write(text + "\n");
        } catch (IOException o) {
            System.out.println(o.getMessage());
        }
    }
}