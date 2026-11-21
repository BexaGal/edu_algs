namespace Example
{
    class Address
    {
        public string Country
        {
            get {return field; }
            set
            {
                if (string.IsNullOrEmpty(value))
                {
                    throw new ArgumentException("Country cannot be null or empty.");
                }
                field = value;
            }
        }
        public string City
        {
            get {return field; }
            set
            {
                if (string.IsNullOrEmpty(value))
                {
                    throw new ArgumentException("City cannot be null or empty.");
                }
                field = value;
            }
        }
        public string Street
        {
            get {return field; }
            set
            {
                if (string.IsNullOrEmpty(value))
                {
                    throw new ArgumentException("Street cannot be null or empty.");
                }
                field = value;
            }
        }
        public string HouseNumber
        {
            get {return field; }
            set
            {
                if (string.IsNullOrEmpty(value))
                {
                    throw new ArgumentException("House number cannot be null or empty.");
                }
                field = value;
            }
        }
        public string? ApartmentNumber {get; set;}

        public Address(string country, string city, string street, string houseNumber, string? apartmentNumber = null)
        {
            this.Country = country;
            this.City = city;
            this.Street = street;
            this.HouseNumber = houseNumber;
            this.ApartmentNumber = apartmentNumber;
        }
    }

    class Buyer
    {
        public string Name
        {
            get {return field; }
            set
            {
                if (string.IsNullOrEmpty(value))
                {
                    throw new ArgumentException("Name cannot be null or empty.");
                }
                field = value;
            }
        }
        public string Surname
        {
            get {return field; }
            set
            {
                if (string.IsNullOrEmpty(value))
                {
                    throw new ArgumentException("Surname cannot be null or empty.");
                }
                field = value;
            }
        }
        public string? Patronymic {get; set;}
        public string PhoneNumber
        {
            get {return field; }
            set
            {
                if (string.IsNullOrEmpty(value))
                {
                    throw new ArgumentException("Phone number cannot be null or empty.");
                }
                field = value;
            }
        }
        public Address Address {get; set;}

        public Buyer(string name, string surname, string phoneNumber, Address address, string? patronymic = null)
        {
                this.Name = name;
                this.Surname = surname;
                this.PhoneNumber = phoneNumber;
                this.Address = address;
                this.Patronymic = patronymic;

        }
        public void PrintInfo()
        {
            Console.WriteLine($"Name: {Name}");
            Console.WriteLine($"Surname: {Surname}");
            if (!string.IsNullOrEmpty(Patronymic))
            {
                Console.WriteLine($"Patronymic: {Patronymic}");
            }
            Console.WriteLine($"Phone Number: {PhoneNumber}");
            Console.WriteLine($"Address: {Address.Street} {Address.HouseNumber}, Apt. {Address.ApartmentNumber}, {Address.City}, {Address.Country}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Buyer[] buyers =
            {
                new Buyer(
                    "Ivan",
                    "Petrov",
                    "+1-555-0101",
                    new Address("USA", "New York", "Main Street", "12A", "5"),
                    "Sergeevich"
                ),
                new Buyer(
                    "Anna",
                    "Ivanova",
                    "+1-555-0102",
                    new Address("Canada", "Toronto", "Queen Street", "45", "10")
                ),
                new Buyer(
                    "Mikhail",
                    "Sidorov",
                    "+79991642201",
                    new Address("Russia", "Moscow", "Lenina", "7", "12"),
                    "Alexandrovich"
                )
            };

            Array.Sort(buyers, (x, y) => string.Compare(x.Surname, y.Surname, StringComparison.Ordinal));

            foreach (var buyer in buyers)
            {
                buyer.PrintInfo();
                Console.WriteLine();
            }
        }
    }
}