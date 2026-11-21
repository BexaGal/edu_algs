namespace Example
{
    class DynamicArray
    {
        Array array;
        int Size { get; set; }
        public DynamicArray(int size)
        {
            if (size <= 0)
            {
                throw new ArgumentException("Size must be greater than zero.");
            }
            this.Size = size;
            this.array = new int[size];
        }
        public void FillRandomly(int minValue, int maxValue)
        {
            Random random = new Random();
            for (int i = 0; i < Size; i++)
            {
                array.SetValue(random.Next(minValue, maxValue), i);
            }
        }

        public void Append(int value)
        {
            if (Size >= array.Length)
            {
                int newSize = array.Length * 2;
                Array newArray = Array.CreateInstance(typeof(int), newSize);
                Array.Copy(array, newArray, array.Length);
                array = newArray;
            }

            array.SetValue(value, Size);
            Size++;
        }

        public void Print()
        {
            for (int i = 0; i < Size; i++)
            {
                Console.Write(array.GetValue(i) + " ");
            }
            Console.WriteLine();
        }
        public void Shuffle()
        {
            Random random = new Random();
            for (int i = Size - 1; i > 0; i--)
            {
                int j = random.Next(0, i + 1);
                object temp = array.GetValue(i);
                array.SetValue(array.GetValue(j), i);
                array.SetValue(temp, j);
            }
        }

        public int DifferentElementsCount()
        {
            HashSet<int> uniqueElements = new HashSet<int>();
            for (int i = 0; i < Size; i++)
            {
                uniqueElements.Add((int)array.GetValue(i));
            }
            return uniqueElements.Count;
        }

    }

    class Program
    {
        static void Main(string[] args)
        {
            DynamicArray dynamicArray = new DynamicArray(5);
            dynamicArray.FillRandomly(1, 10);
            Console.WriteLine("Original array:");
            dynamicArray.Print();

            dynamicArray.Shuffle();
            Console.WriteLine("Shuffled array:");
            dynamicArray.Print();

            dynamicArray.Append(9);
            dynamicArray.Print();

            int differentCount = dynamicArray.DifferentElementsCount();
            Console.WriteLine($"Number of different elements: {differentCount}");
        }
    }
}