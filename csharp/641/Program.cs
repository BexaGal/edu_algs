namespace Example
{
    class Figure
    {
        public readonly double[,] Points; // each row is a point: [x, y]

        public Figure(double[,] points)
        {
            this.Points = points;
        }

        public double Area()
        {
            double area = 0;
            int n = Points.GetLength(0);
            for (int i = 0; i < n; i++)
            {
                int j = (i + 1) % n;
                area += Points[i, 0] * Points[j, 1];
                area -= Points[j, 0] * Points[i, 1];
            }
            return Math.Abs(area) / 2.0;
        }
        public double Perimeter()
        {
            double perimeter = 0;
            int n = Points.GetLength(0);
            for (int i = 0; i < n; i++)
            {
                int j = (i + 1) % n;
                double dx = Points[j, 0] - Points[i, 0];
                double dy = Points[j, 1] - Points[i, 1];
                perimeter += Math.Sqrt(dx * dx + dy * dy);
            }
            return perimeter;
        }
    }

    class Triangle : Figure
    {
        public Triangle(double[,] points) : base(points)
        {
            if (points.GetLength(0) != 3)
            {
                throw new ArgumentException("A triangle must have exactly 3 points.");
            }
        }
        public double[] MedianIntersection()
        {
            double x1 = Points[0, 0], y1 = Points[0, 1];
            double x2 = Points[1, 0], y2 = Points[1, 1];
            double x3 = Points[2, 0], y3 = Points[2, 1];

            double centroidX = (x1 + x2 + x3) / 3;
            double centroidY = (y1 + y2 + y3) / 3;

            return new double[] { centroidX, centroidY };
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Example usage
            double[,] points = { { 0, 0 }, { 3, 0 }, { 0, 4 } };
            Triangle triangle = new Triangle(points);
            Console.WriteLine($"Area: {triangle.Area()}");
            Console.WriteLine($"Perimeter: {triangle.Perimeter()}");
            Console.WriteLine($"Median Intersection: ({triangle.MedianIntersection()[0]}, {triangle.MedianIntersection()[1]})");
        }
    }
}