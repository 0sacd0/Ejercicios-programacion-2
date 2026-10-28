import java.math.BigInteger;
import java.util.Scanner;

public class MenuActividad {
    private static final Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        int opcion;

        do {
            mostrarMenu();
            opcion = leerEntero("Seleccione una opción: ");

            switch (opcion) {
                case 1:
                    ejecutarFactorial();
                    break;
                case 2:
                    ejecutarCalculoIMC();
                    break;
                case 3:
                    ejecutarPausa();
                    break;
                case 4:
                    System.out.println("Programa finalizado.");
                    break;
                default:
                    System.out.println("Opción no válida. Seleccione una opción del 1 al 4.");
            }
        } while (opcion != 4);

        entrada.close();
    }

    private static void mostrarMenu() {
        System.out.println("\n--- Menú de ejercicios ---");
        System.out.println("1. Calcular el factorial de un número");
        System.out.println("2. Calcular el IMC");
        System.out.println("3. Hacer una pausa de 5 segundos");
        System.out.println("4. Salir");
    }

    private static void ejecutarFactorial() {
        int numero;
        do {
            numero = leerEntero("Ingrese un número entero no negativo: ");
            if (numero < 0) {
                System.out.println("El número debe ser no negativo.");
            }
        } while (numero < 0);

        System.out.println("El factorial de " + numero + " es " + calcularFactorial(numero) + ".");
    }

    private static BigInteger calcularFactorial(int numero) {
        BigInteger factorial = BigInteger.ONE;
        for (int i = 2; i <= numero; i++) {
            factorial = factorial.multiply(BigInteger.valueOf(i));
        }
        return factorial;
    }

    private static void ejecutarCalculoIMC() {
        double estatura = leerDecimalPositivo("Ingrese su estatura en centímetros: ");
        double peso = leerDecimalPositivo("Ingrese su peso en kilogramos: ");
        double imc = calcularIMC(peso, estatura);

        System.out.printf("Su IMC es: %.2f%n", imc);
        if (imc <= 18) {
            System.out.println("IMC con valor bajo");
        } else {
            System.out.println("Mantenga su peso controlado");
        }
    }

    private static double calcularIMC(double peso, double estaturaCentimetros) {
        double estaturaMetros = estaturaCentimetros / 100.0;
        return peso / (estaturaMetros * estaturaMetros);
    }

    private static void ejecutarPausa() {
        System.out.println("Haga una pausa de 5 segundos…");
        try {
            Thread.sleep(5000);
            System.out.println("La pausa ha terminado.");
        } catch (InterruptedException exception) {
            Thread.currentThread().interrupt();
            System.out.println("La pausa fue interrumpida.");
        }
    }

    private static int leerEntero(String mensaje) {
        while (true) {
            System.out.print(mensaje);
            String texto = entrada.nextLine().trim();
            try {
                return Integer.parseInt(texto);
            } catch (NumberFormatException exception) {
                System.out.println("Entrada no válida. Ingrese un número entero.");
            }
        }
    }

    private static double leerDecimalPositivo(String mensaje) {
        while (true) {
            System.out.print(mensaje);
            String texto = entrada.nextLine().trim().replace(',', '.');
            try {
                double valor = Double.parseDouble(texto);
                if (Double.isFinite(valor) && valor > 0) {
                    return valor;
                }
            } catch (NumberFormatException exception) {
                // Se informa al usuario en el mensaje común de entrada no válida.
            }
            System.out.println("Ingrese un valor numérico mayor que cero.");
        }
    }
}
