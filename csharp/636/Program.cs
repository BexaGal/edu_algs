using System;
using System.Collections;

namespace Example
{
    class Program
    {
       static void Main()
    {
            Library library = new Library();
            library.AddBook("The Great Gatsby", "F. Scott Fitzgerald", 1925);
            library.AddBook("To Kill a Mockingbird", "Harper Lee", 1960);
            library.AddBook("1984", "George Orwell", 1949);
            Console.WriteLine("Books sorted by title:");
            library.DisplayBooks("title");
            Console.WriteLine("\nBooks sorted by author:");
            library.DisplayBooks("author");
            Console.WriteLine("\nBooks sorted by year:");
            library.DisplayBooks("year");
       }
    }
    class Book
    {
        public string Title;
        public string Author;
        public int Year;

        public Book(string title, string author, int year)
        {
            this.Title = title;
            this.Author = author;
            this.Year = year;
        }
    }
    class Library
    {
        private Hashtable books;
        public Library()
        {
            books = new Hashtable();
        }
        
        public void AddBook(string title, string author, int year)
        {
            books.Add(title, new Book(title, author, year)); 
        }

        public Book GetBookTitle(string title)
        {
            return (Book)books[title];
        }
        public Book GetBookAuthor(string author)
        {
            foreach (Book book in books.Values)
            {
                if (book.Author == author)
                {
                    return book;
                }
            }
            return null;
        }
        public Book GetBookYear(int year)
        {
            foreach (Book book in books.Values)
            {
                if (book.Year == year)
                {
                    return book;
                }
            }
            return null;
        }
        public void RemoveBook(string title, string author, int year)
        {
            books.Remove(title);
        }

        public void DisplayBooks(string sortby = "title")
        {
            if (sortby == "title")
            {
                var sortedEntries = books.Cast<DictionaryEntry>()
                         .OrderBy(entry => ((Book)entry.Value).Title, StringComparer.OrdinalIgnoreCase);
                         
                foreach (DictionaryEntry entry in sortedEntries)
                {
                    Console.WriteLine($"{entry.Key}: {entry.Value.Title}");
                }
            }
            else if (sortby == "author")
            {
                var sortedEntries = books.Cast<DictionaryEntry>()
                         .OrderBy(entry => ((Book)entry.Value).Author, StringComparer.OrdinalIgnoreCase);
                         
                foreach (DictionaryEntry entry in sortedEntries)
                {
                    Console.WriteLine($"{entry.Key}: {entry.Value}");
                }
            }
            else if (sortby == "year")
            {
                var sortedEntries = books.Cast<DictionaryEntry>()
                         .OrderBy(entry => ((Book)entry.Value).Year.ToString(), StringComparer.OrdinalIgnoreCase);
                         
                foreach (DictionaryEntry entry in sortedEntries)
                {
                    Console.WriteLine($"{entry.Key}: {entry.Value}");
                }
            }
        }

    }
}