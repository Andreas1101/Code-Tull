class Program {
    static String location;
    static DateTime time;
    static void Main() {
        Console.WriteLine(location == null ? "location os null" : location);
        Console.WriteLine(time == null ? "time is null" : time.ToString());
    }
}