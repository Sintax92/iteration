using System;

public partial class Program
{
    public static void ForeachLoopExample()
    {
        int[] numbers = { 1, 2, 3, 4, 5 };
        int sum = 0;

        foreach (int number in numbers)
        {
            sum += number;
        }

        Console.WriteLine($"Sum using foreach loop: {sum}");
    }
}
