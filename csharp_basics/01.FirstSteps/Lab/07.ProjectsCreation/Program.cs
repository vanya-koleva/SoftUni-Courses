string name = Console.ReadLine();
int numberOfProjects = int.Parse(Console.ReadLine());
int hoursPerProject = 3;
int hours = numberOfProjects * hoursPerProject;

Console.WriteLine($"The architect {name} will need {hours} hours to complete {numberOfProjects} project/s.");
