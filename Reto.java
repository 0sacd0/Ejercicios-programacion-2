import java.util.Locale;
import java.util.Scanner;

class Calculadora {
    public static float suma(float numero1, float numero2) {
        return numero1 + numero2;
    }

    public static float producto(float numero1, float numero2) {
        return numero1 * numero2;
    }
}

public class Reto {
    private final Scanner entrada = new Scanner(System.in);

    public void run() {
        while (entrada.hasNextFloat()) {
            float numero1 = entrada.nextFloat();
            if (!entrada.hasNextFloat()) {
                break;
            }
            float numero2 = entrada.nextFloat();

            System.out.printf(
                Locale.US,
                "%.1f %.1f%n",
                Calculadora.suma(numero1, numero2),
                Calculadora.producto(numero1, numero2)
            );
        }
    }

    public static void main(String[] args) {
        new Reto().run();
    }
}
