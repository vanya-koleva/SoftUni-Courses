double squareMeters = double.Parse(Console.ReadLine());
double pricePerSquareMeter = 7.61;

double price = squareMeters * pricePerSquareMeter;
double discount = price * 0.18;

Console.WriteLine($"The final price is: {price - discount} lv.");
Console.WriteLine($"The discount is: {discount} lv.");
