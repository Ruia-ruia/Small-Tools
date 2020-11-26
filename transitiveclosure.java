import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class War {

    // store for loops
    public static ArrayList<Integer> starts = new ArrayList<Integer>(); 
    public static boolean[][] newM;

    public static void printMatrix(boolean[][] matrix, int size) {
        if (matrix == null) {
            return;
        }
        System.out.println();
        for (int y = 0; y < size; y++) {
            for (int x = 0; x < size; x++) {
                if (matrix[y][x]) {
                    System.out.print("1 ");
                } else {
                    System.out.print("0 ");
                }
            }
            System.out.println();
        } 
    }

    public static void nodeContext(boolean[][] matrix, int context, int size) {
        if (matrix == null || context < 0 || context >= size || size < 1) {
            return; 
        }

        for (int x = 0; x < size; x++) {
            if (matrix[context][x]) {
                if (! starts.contains(x)) {
                    System.out.println("Adding: " + x);
                    starts.add(x);
                    nodeContext(matrix, x, size);
                }
            }
        }
    }

    public static void transitive(boolean[][] matrix, int size) {
        if (matrix == null ){
             return; 
        }

        for (int y = 0; y < size; y++) {
            System.out.println("---");
            System.out.println("In context: " + y);
            starts = new ArrayList<Integer>();
            nodeContext(matrix, y, size);
            for (int x = 0; x < starts.size(); x++) {
                newM[y][starts.get(x)] = true;
            }
            System.out.println("---");
        }
    }

    public static void main(String[] args) {
        Scanner scanin = new Scanner(System.in);

        // get the size of the matrix n by n
        System.out.print("Enter the size of the matrix: ");
        int n = scanin.nextInt();
        boolean[][] m = new boolean[n][n];
        newM = new boolean[n][n];

        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                System.out.print("Enter for " + y + " to " + x + ": ");
                if (scanin.nextInt() == 1) {
                    m[y][x] = true;
                } else {
                    m[y][x] = false; 
                }
            }
        }
        transitive(m, n);
        printMatrix(newM, n);        
    }
}
