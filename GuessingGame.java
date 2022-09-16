import java.util.Scanner;

// Generate a gueressing game
class GuessingGame {
    public static void main(String[] args) {
        int number = (int) (Math.random() * 100);
        // Write input
        Scanner input = new Scanner(System.in);
         System.out.println("Guess a magic number between 0 and 100");
        int guess = -1;
        while (guess != number) {
            System.out.print("Enter your guess: ");
            guess = input.nextInt();
            if (guess == number)
                System.out.println("Yes, the number is " + number);
            else if (guess > number)
                System.out.println("Your guess is too high");
            else
                System.out.println("Your guess is too low");
        
    }

// Generate a random number that is the answer 
if (guess == number) {
    System.out.println("Yes, the number is " + number);
} else if (guess > number) {
    System.out.println("Your guess is too high");
} else {
    System.out.println("Your guess is too low");
 

// After 3 trys say sorry you failed
if (guess == number)
    System.out.println("Yes, the number is " + number);
else if (guess > number)
    System.out.println("Your guess is too high");
else
    System.out.println("Your guess is too low");
}
}
}

/// GuessingGame.java
/// [c]  - Flames San
