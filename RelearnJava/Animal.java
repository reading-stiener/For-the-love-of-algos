abstract class Animal {
    public abstract void animalSound();
    public void sleep() { 
        System.out.println("Sleeping... zzz");
    }
}

// Subclass (inherit from Animal)
class Pig extends Animal {
    public void animalSound() {
      // The body of animalSound() is provided here
      System.out.println("The pig says: wee wee");
    }
}
