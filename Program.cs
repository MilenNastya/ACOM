using System;
using System.Collections.Generic;

class GaussianBlur
{
    public static void Main(string[] args)
    {
        var image = new List<List<int>>()
        {
            new List<int> { 50, 50, 50, 60, 60, 10, 60, 60, 50, 50, 50 },
            new List<int> { 50, 50, 50, 60, 60, 10, 60, 60, 50, 50, 50 },
            new List<int> { 50, 50, 50, 60, 60, 10, 60, 60, 50, 50, 50 },
            new List<int> { 50, 50, 50, 60, 60, 10, 60, 60, 50, 50, 50 },
            new List<int> { 50, 50, 50, 60, 60, 10, 60, 60, 50, 50, 50 },
            new List<int> { 50, 50, 50, 60, 60, 10, 60, 60, 50, 50, 50 },
            new List<int> { 50, 50, 50, 60, 60, 10, 60, 60, 50, 50, 50 },
            new List<int> { 50, 50, 50, 60, 60, 10, 60, 60, 50, 50, 50 }
        };

        var blurredImage = MyGaussianBlur(image, kernelSize: 3, standardDeviation: 100);

        // Вывод результата
        foreach (var row in blurredImage)
        {
            Console.WriteLine(string.Join(", ", row));
        }
    }

    public static List<List<int>> MyGaussianBlur(List<List<int>> img,
                                                  int kernelSize,
                                                  double standardDeviation)
    {
        var kernel = new double[kernelSize][];
        for (int i = 0; i < kernelSize; i++)
        {
            kernel[i] = new double[kernelSize];
        }

        int a = (kernelSize + 1) / 2;
        int b = a;

        // Генерация ядра Гаусса
        for (int i = 0; i < kernelSize; i++)
        {
            for (int j = 0; j < kernelSize; j++)
            {
                kernel[i][j] = Gauss(i - a + 1, j - b + 1, standardDeviation, a, b);
            }
        }

        // Нормализация ядра
        double sum = 0;
        for (int i = 0; i < kernelSize; i++)
        {
            for (int j = 0; j < kernelSize; j++)
            {
                sum += kernel[i][j];
            }
        }

        for (int i = 0; i < kernelSize; i++)
        {
            for (int j = 0; j < kernelSize; j++)
            {
                kernel[i][j] /= sum;
            }
        }

        int xStart = kernelSize / 2;
        int yStart = kernelSize / 2;

        // Применение размытия по Гауссу
        for (int i = xStart; i < img.Count - xStart; i++)
        {
            for (int j = yStart; j < img[i].Count - yStart; j++)
            {
                double val = 0;
                for (int k = -(kernelSize / 2); k <= kernelSize / 2; k++)
                {
                    for (int l = -(kernelSize / 2); l <= kernelSize / 2; l++)
                    {
                        val += img[i + k][j + l] * kernel[k + (kernelSize / 2)][l + (kernelSize / 2)];
                    }
                }
                img[i][j] = (int)val;
            }
        }

        return img;
    }

    public static double Gauss(double x,
                                double y,
                                double omega,
                                double a,
                                double b)
    {
        double omegaIn2 = 2 * Math.Pow(omega, 2);
        double m1 = 1 / (Math.PI * omegaIn2);
        double m2 = Math.Exp(-(Math.Pow((x - a), 2) + Math.Pow((y - b), 2)) / omegaIn2);

        return m1 * m2;
    }
}