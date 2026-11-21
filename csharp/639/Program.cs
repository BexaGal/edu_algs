namespace Example
{
    class Time
    {
        public int Hours
        {
            get { return field; }
            set
            {
                if (value < 0 || value > 23)
                {
                    throw new ArgumentOutOfRangeException("Hours must be between 0 and 23.");
                }
                field = value;
            }
        }

        public int Minutes
        {
            get { return field; }
            set
            {
                if (value < 0 || value > 59)
                {
                    throw new ArgumentOutOfRangeException("Minutes must be between 0 and 59.");
                }
                field = value;
            }
        }

        public int Seconds
        {
            get { return field; }
            set
            {
                if (value < 0 || value > 59)
                {
                    throw new ArgumentOutOfRangeException("Seconds must be between 0 and 59.");
                }
                field = value;
            }
        }

        public void addMinutes(int minutes)
        {
            int totalMinutes = this.Minutes + minutes;
            int additionalHours = totalMinutes / 60;
            this.Minutes = totalMinutes % 60;
            this.Hours = (this.Hours + additionalHours) % 24;
        }

        public void addSeconds(int seconds)
        {
            int totalSeconds = this.Seconds + seconds;
            int additionalMinutes = totalSeconds / 60;
            this.Seconds = totalSeconds % 60;
            this.addMinutes(additionalMinutes);
        }
        public void addHours(int hours)
        {
            this.Hours = (this.Hours + hours) % 24;
        }

        public Time(int hours, int minutes, int seconds)
        {
            this.Hours = hours;
            this.Minutes = minutes;
            this.Seconds = seconds;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Time time = new Time(23, 59, 50);
            Console.WriteLine($"Initial time: {time.Hours:D2}:{time.Minutes:D2}:{time.Seconds:D2}");

            time.addSeconds(15);
            Console.WriteLine($"After adding 15 seconds: {time.Hours:D2}:{time.Minutes:D2}:{time.Seconds:D2}");

            time.addMinutes(5);
            Console.WriteLine($"After adding 5 minutes: {time.Hours:D2}:{time.Minutes:D2}:{time.Seconds:D2}");

            time.addHours(1);
            Console.WriteLine($"After adding 1 hour: {time.Hours:D2}:{time.Minutes:D2}:{time.Seconds:D2}");
        }
    }
}