using System;

public partial class Program
{
    public static void WhileLoopExample()
    {
        int[] numbers = { 1, 2, 3, 4, 5 };
        int sum = 0;
        int i = 0;

        while (i < numbers.Length)
        {
            sum += numbers[i];
            i++;
        }

        Console.WriteLine($"Sum using while loop: {sum}");
    }
}
