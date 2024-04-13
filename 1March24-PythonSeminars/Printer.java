
// //     public static LocalDateTime getCurrentDateTime() {
// //         return LocalDateTime.now()
// //     }

// //     public static void getUserDataFromConsole() {
// //         System.out.println("введите данные: ")
// //         Scanner sc = new Scanner(System. in )
// //         // экземпляр класса Scanner
// //         //, который вызывает спец. класс для ввода данных в системную консоль
// //         // System. in
// //         String userData = sc.nextLine()
// //         //
// //         System.out.printf("%s: %s%n", "Вы ввели", userData)
// //     }
// // }

// // public static int getSumElemsFromArray(int[][] arr) {
// //         int sum = 0;

// //     //    for (int i = 0; i < arr.length; i++) {
// // //            for (int j = 0; j < arr[i].length; j++) {
// // //                sum += arr[i][j];
// // //            }
// // //        }
// //         for (int[] ints : arr) {
// //             for (int anInt : ints) {
// //                 sum += anInt;
// //             }
// //         }

// //         return sum;
// //     }

// // public static String reverse(String str) {
// //         String[] arr = str.split(" ");
// // //        [Добро,пожаловать,на ,курс, по ,Java]
// //         StringBuilder sb = new StringBuilder();
// //         for (String s : arr) {
// //             sb.append(s).append(" ");
// //         }
// // //        sb.append(str);
// //         sb.reverse();
// // //        for (int i = arr.length - 1; i >=0 ; i--) {
// // //            sb.append(arr[i]).append(" ");
// // //        }
// //         return sb.toString();
// //     }

class Calculator {
    public int calculate(char op, int a, int b) {
        // Введите свое решение ниже
        if (op == '+') {
            return a + b;
        } else if (op == '-') {
            return a - b;
        } else if (op == '*') {
            return a * b;
        } else if (op == '/') {
            return a / b;
        } else
            System.out.printf("Некорректный оператор: '{op}'");

        return a;
    }

}

// Не удаляйте этот класс - он нужен для вывода результатов на экран и проверки
public class Printer {
    public static void main(String[] args) {
        int a = 0;
        char op = ' ';
        int b = 0;

        if (args.length == 0) {
            // При отправке кода на Выполнение, вы можете варьировать эти параметры
            a = 3;
            op = '+';
            b = 7;
        } else {
            a = Integer.parseInt(args[0]);
            op = args[1].charAt(0);
            b = Integer.parseInt(args[2]);
        }

        Calculator calculator = new Calculator();
        double result = calculator.calculate(op, a, b);
        System.out.println(result);
    }
}

// class Answer {
//     public void printPrimeNums() {
//         // Напишите свое решение ниже
//         int[] arr = new int[1000];
//         int[] arr2 = new int[] { 2, 3, 5, 7 };
//         int[] arr3 = new int[1000];
//         for (int i = 2; i <= 1000; i++)
//             // if(i/i==1 && i/1==i)
//             if (i > 1 && i % i == 0 && i % 1 == 0 && i % 2 != 0 && i % 3 != 0 && i % 5 != 0 && i % 7 != 0
//                     && i % 9 != 0) {
//                 // arr.append(i);

//                 System.out.println(i);

//             }
//         // arr3=arr2+arr;

//     }
// }

// // Не удаляйте этот класс - он нужен для вывода результатов на экран и проверки
// public class Printer {
//     public static void main(String[] args) {

//         Answer ans = new Answer();
//         ans.printPrimeNums();
//     }
// }
