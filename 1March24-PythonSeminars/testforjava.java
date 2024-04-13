
// import java.util.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class testforjava {

// Заполнить список десятью случайными числами. 
// Отсортировать список методом sort() и вывести его на экран.

    public static void main(String[] args) {

        List<Integer> list = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < 10; i++) {

            list.add(random.nextInt(10));

        }
        System.out.println(list);
        Collections.sort(list);
        System.out.println(list);

    }
}

// Заполнить список названиями планет Солнечной системы в произвольном порядке с повторениями. 
// Вывести название каждой планеты и количество его повторений в списке.









