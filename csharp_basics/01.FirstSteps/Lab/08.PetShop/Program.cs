int dogFood = int.Parse(Console.ReadLine());
int catFood = int.Parse(Console.ReadLine());

double dogPrice = dogFood * 2.50;
int catPrice = catFood * 4;
double totalPrice = dogPrice + catPrice;

Console.WriteLine($"{totalPrice} lv.");
