import java.util.Scanner;

public class calculadora {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int R,opcion = 0;
        double N1, N2, resultado, Perimetro , Area;

        do {
            System.out.println("\n--- Menú de Calculadora ---");
            System.out.println("1-Sumar");
            System.out.println("2-Resta");
            System.out.println("3-Multiplicar");
            System.out.println("4-Dividir");
            System.out.println("5-Factorial");
            System.out.println("6-Area de una circunferencia");
            System.out.println("7-Convertir kilómetros a metros y centímetros");
            System.out.println("8-Calcular distancia entre dos puntos");
            System.out.println("9-Salir");
            System.out.print("Seleccione una opción: ");

            if (entrada.hasNextInt()) {
                opcion = entrada.nextInt();

                switch (opcion) {
                    case 1:
                        System.out.print("Ingrese N1: ");
                        N1 = entrada.nextDouble();
                        System.out.print("Ingrese N2: ");
                        N2 = entrada.nextDouble();
                        System.out.println("Resultado Suma: " + (N1 + N2));
                        break;

                    case 2:
                        System.out.print("Ingrese N1: ");
                        N1 = entrada.nextDouble();
                        System.out.print("Ingrese N2: ");
                        N2 = entrada.nextDouble();
                        System.out.println("Resultado Resta: " + (N1 - N2));
                        break;

                    case 3:
                        System.out.print("Ingrese N1: ");
                        N1 = entrada.nextDouble();
                        System.out.print("Ingrese N2: ");
                        N2 = entrada.nextDouble();
                        System.out.println("Resultado Multiplicación: " + (N1 * N2));
                        break;

                    case 4:
                        System.out.print("Ingrese N1: ");
                        N1 = entrada.nextDouble();
                        System.out.print("Ingrese N2: ");
                        N2 = entrada.nextDouble();
                        if (N2 != 0) {
                            System.out.println("Resultado División: " + (N1 / N2));
                        } else {
                            System.out.println("Error: División por cero.");
                        }
                        break;

                    case 5:
                        System.out.print("Ingrese número para Factorial: ");
                        int nFact = entrada.nextInt();
                        if (nFact < 0) {
                            System.out.println("Error: No existen factoriales de negativos.");
                        } else {
                            long fact = 1;
                            for (int i = 1; i <= nFact; i++) {
                                fact *= i; 
                            }
                            System.out.println("Resultado Factorial: " + fact);
                        }
                        break;
                        
                    case 6:
                        System.out.print("Digite radio:");
                        R = entrada.nextInt();
                        System.out.println("El Area de su circunferencia es:" + (3.1416 * R*R));
                            break;

                    case 7:
                        System.out.print("Ingrese la cantidad de kilómetros: ");
                        double kilometros = entrada.nextDouble();
                        System.out.println("Metros: " + (kilometros * 1000));
                        System.out.println("Centímetros: " + (kilometros * 100000));
                        break;

                    case 8:
                        System.out.print("Ingrese la coordenada x del primer punto: ");
                        double x1 = entrada.nextDouble();
                        System.out.print("Ingrese la coordenada y del primer punto: ");
                        double y1 = entrada.nextDouble();
                        System.out.print("Ingrese la coordenada x del segundo punto: ");
                        double x2 = entrada.nextDouble();
                        System.out.print("Ingrese la coordenada y del segundo punto: ");
                        double y2 = entrada.nextDouble();
                        double distancia = Math.hypot(x2 - x1, y2 - y1);
                        System.out.println("La distancia entre los puntos es: " + distancia);
                        break;

                    case 9:
                        System.out.println("Cerrando el sistema...");
                        break;

                    default:
                        System.out.println("Opción inválida.");
                        break;
                }
            } else {
                System.out.println("Error: Ingrese un número entero.");
                entrada.next(); 
            }

        } while (opcion != 9);

        entrada.close();
    }
}