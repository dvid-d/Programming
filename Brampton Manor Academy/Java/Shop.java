public class Shop {
    public static void main(String[] args){
        Dog Trevor = new Dog("Trevor", "corgi", 12);
        String name = Trevor.getName();
        System.out.println(name);
        Trevor.bark();
        Trevor.eatBiscuit();
        Trevor.getOlder();
    }
}