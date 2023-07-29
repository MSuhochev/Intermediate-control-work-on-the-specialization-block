import java.util.Objects;

public class Toys implements Comparable<Toys> {  

    private int toyId;
    private String toyName;
    private int toyVictoryDrop;

    public Toys(int toyId, String toyName, int toyVictoryDrop) {  // Constructor class Toys
        this.toyId = toyId;
        this.toyName = toyName;
        this.toyVictoryDrop = toyVictoryDrop;
    }

    /**
     *Getters and setters
     */
    public int getToyId() {
        return toyId;
    }

    public String getToyName() {
        return toyName;
    }

    public int getToyVictoryDrop() {
        return toyVictoryDrop;
    }

    public void setToyVictoryDrop(int toyVictoryDrop) {
        this.toyVictoryDrop = toyVictoryDrop;
    }

    public String getInfo() {
        return String.format("ID: %d, Name: %s", toyId, toyName);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;
        Toys toy = (Toys) o;
        return toyName.equals(toy.toyName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(toyName);
    }

    @Override
    public int compareTo(Toys o) {
        return Integer.compare(this.toyVictoryDrop, o.toyVictoryDrop);
    }
}