namespace Example
{
    class Program
    {
       static void Main()
        {

       }
    }
    class Animal
    {
        public string Name;
        public int Food_req;
        public string Kind;
        public int ID;
        public Animal(string kind, int id, string name, int food_req)
        {
            this.Name = name;
            this.Food_req = food_req;
            this.Kind = kind;
            this.ID = id;
        }


    }
}