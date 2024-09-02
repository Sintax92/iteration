using System;

public partial class Program
{
    public static void ForLoopExample()
    {
        int[] numbers = { 1, 2, 3, 4, 5 };
        int sum = 0;

        for (int i = 0; i < numbers.Length; i++)
        {
            sum += numbers[i];
        }

        Console.WriteLine($"Sum using for loop: {sum}");
    }
}
