namespace Example
{
    class Program
    {
        static void Main()
        {
            Compnum c1 = new Compnum(2, 2);
            Compnum c2 = new Compnum(1, 1);
            c1.PrintTrigonometric();
        }
    }
        class Compnum
    {
        private float a;
        private float b;

        public Compnum(float a, float b)
        {
            this.a = a;
            this.b = b;
        }

        public void PrintAlgebraic()
        {
            Console.WriteLine(a.ToString() + "+" + b.ToString() + "i");
        }
        public void PrintTrigonometric()
        {
            float r = (float)Math.Sqrt(a * a + b * b);
            float phi = (float)Math.Atan(b / a);
            Console.WriteLine(r.ToString() + "(cos(" + phi.ToString() + ") + i*sin(" + phi.ToString() + "))");
        }
        public void PrintExponential()
        {
            float r = (float)Math.Sqrt(a * a + b * b);
            float phi = (float)Math.Atan(b / a);
            Console.WriteLine(r.ToString() + "e^(i*" + phi.ToString() + ")");
        }
        
        public Compnum conjugate()
        {
            return new Compnum(a, b * -1);
        }
        
        public static Compnum operator +(Compnum c1, Compnum c2)
        {
            return new Compnum(c1.a + c2.a, c1.b + c2.b);
        }
        public static Compnum operator -(Compnum c1, Compnum c2)
        {
            return new Compnum(c1.a - c2.a, c1.b - c2.b);
        }
        public static Compnum operator *(Compnum c1, Compnum c2)
        {
            return new Compnum(c1.a * c2.a - c1.b * c2.b, c1.b * c2.a + c1.a * c2.b);
        }
        public static Compnum operator /(Compnum c1, Compnum c2)
        {
            float denominator = c2.a * c2.a + c2.b * c2.b;
            return new Compnum((c1.a * c2.a + c1.b * c2.b) / denominator, (c1.b * c2.a - c1.a * c2.b) / denominator);
        }
        public static Compnum operator ^(Compnum c1, int n)
        {
            float r = (float)Math.Sqrt(c1.a * c1.a + c1.b * c1.b);
            float phi = (float)Math.Atan(c1.b / c1.a);
            float newR = (float)Math.Pow(r, n);
            float newPhi = phi * n;
            return new Compnum(newR * (float)Math.Cos(newPhi), newR * (float)Math.Sin(newPhi));
        }
    }
}
