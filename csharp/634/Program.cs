namespace Example
{
    class Program
    {
        static void Main()
        {
            Stringarr st1 = new Stringarr(5, 12);
            st1.Append("Hello");
            st1.Append("World");
            st1.Append("CSharp");
            st1.Append("Programming");
            st1.Append("Language");
            Stringarr st2 = new Stringarr(5, 10);
            st2.Append("World");
            st2.Append("CSharp");
            st2.Append("Code");
            st2.Append("Example");
            st2.Append("Test");
            Stringarr st3 = new Stringarr(st1, st2);
            for (int i = 0; i < st3.Length; i++)
            {
                Console.WriteLine(st3.Get(i));
            }
            st3.Concatenate(0, "Lol");
            Console.WriteLine(st3.Get(0));

        }
    }
        class Stringarr
    {
        private string[] arr;
        public int Str_Length;
        public int Length;
        public Stringarr(int size, int max_len)
        {
            this.Length = size;
            this.arr = new string[Length];
            this.Str_Length = max_len;
        }
        public Stringarr(Stringarr st1, Stringarr st2)
        {
            Str_Length = Math.Max(st1.Str_Length, st2.Str_Length);
            int not_uniq = 0;
            for (int i = 0; i < st1.Length; i++)
            {
                for (int j = 0; j < st2.Length; j++)
                {
                    if (st1.Get(i) == st2.Get(j))
                    {
                        not_uniq++;
                    }
                }
            }
            this.Length = st1.Length + st2.Length - not_uniq;
            Console.WriteLine("New size: " + this.Length);
            arr = new string[this.Length];
            for (int i = 0; i < st1.Length; i++)
            {
                arr[i] = st1.Get(i);
            }
            for (int i = 0; i < st2.Length; i++)
            {
                bool is_unique = true;
                for (int j = 0; j < st1.Length; j++)
                {
                    if (st2.Get(i) == st1.Get(j))
                    {
                        is_unique = false;
                        break;
                    }
                }
                if (is_unique)
                {
                    arr[st1.Length + i - not_uniq] = st2.Get(i);
                }
            }
        }
        public bool Append(string str)
        {
            if (str.Length <= Str_Length)
            {
                for (int i = 0; i < arr.Length; i++)
                {
                    if (arr[i] == null)
                    {
                        arr[i] = str;
                        return true;
                    }
                }

                Console.WriteLine("Array is full.");
                return false;
            }
            else
            {
                Console.WriteLine("String exceeds maximum length.");
                return false;
            }
        }
        public bool Replace(int index, string str)
        {
            if (index >= 0 && index < arr.Length)
            {
                if (str.Length <= Str_Length)
                {
                    arr[index] = str;
                    return true;
                }
                else
                {
                    Console.WriteLine("String exceeds maximum length.");
                    return false;
                }
            }
            else
            {
                Console.WriteLine("Index out of bounds.");
                return false;
            }
        }
        public string Get(int index)
        {
            if (index >= 0 && index < arr.Length)
            {
                return arr[index];
            }
            else
            {
                Console.WriteLine("Index out of bounds.");
                return null;
            }
        }

        public bool Concatenate(int index, string str)
        {
            if (str.Length + arr[index].Length > Str_Length)
            {
                Console.WriteLine("String size is too big.");
                return false;
            }
            else
            {
                arr[index] = arr[index] + str;
                return true;
            }
        }

    }
}
