namespace Example
{
    abstract class Figure
    {
        public abstract double Area();
        public abstract double Perimeter();
    }

    class Polygon : Figure
    {
        public readonly double[,] Points; // each row is a point: [x, y]

        public Polygon(double[,] points)
        {
            this.Points = points;
        }

        public override double Area()
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

        public override double Perimeter()
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


    class Triangle : Polygon
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

    class Circle : Figure
    {
        public double Radius;
        public double[] Center;

        public Circle(double[] center, double radius)
        {
            this.Center = center;
            this.Radius = radius;
        }

        public override double Area()
        {
            return Math.PI * Radius * Radius;
        }

        public override double Perimeter()
        {
            return 2 * Math.PI * Radius;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Figure[] figures = new Figure[]
            {
                new Polygon(new double[,] { { 0, 0 }, { 4, 0 }, { 4, 3 }, { 0, 3 } }),
                new Triangle(new double[,] { { 0, 0 }, { 3, 0 }, { 0, 4 } }),
                new Circle(new double[] { 0, 0 }, 5)
            };
            Console.WriteLine("Areas and Perimeters of Figures:");
            foreach (var figure in figures)
            {
                Console.WriteLine($"Area: {figure.Area()}, Perimeter: {figure.Perimeter()}");
            }
        }
    }
}