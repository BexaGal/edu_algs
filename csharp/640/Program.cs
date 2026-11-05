namespace Example
{
    class Program
    {
        static void Main()
        {
            Vector v1 = new Vector(1, 2, 3);
            Vector v2 = new Vector(4, 5, 6);
            //Vector v3 = ;
            Console.WriteLine(v1 * v2);
        }
    }
    class Vector 
    {
        private float x;
        private float y;
        private float z;

        public Vector(float x, float y, float z)
        {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        public void Print()
        {
            Console.WriteLine("<" + x.ToString() + ", " + y.ToString() + ", " + z.ToString() + ">");
        }
        public static Vector operator +(Vector v1, Vector v2)
        {
            return new Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z);
        }
        public static Vector operator -(Vector v1, Vector v2)
        {
            return new Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z);
        }
        public static double Cosine(Vector v1, Vector v2)
        {
            double dotProduct = v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
            double magnitudeV1 = Math.Sqrt(v1.x * v1.x + v1.y * v1.y + v1.z * v1.z);
            double magnitudeV2 = Math.Sqrt(v2.x * v2.x + v2.y * v2.y + v2.z * v2.z);
            return dotProduct / (magnitudeV1 * magnitudeV2);
        }    
        public static double operator *(Vector v1, Vector v2)
        {
            return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
        }
    }
       
}
