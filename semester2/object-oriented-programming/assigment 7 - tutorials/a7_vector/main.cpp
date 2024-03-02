
#include "header.h"
#include <iostream>
#include <crtdbg.h>
#include "service.h"
#include <assert.h>
#include "ui.h"
#include "tests.h"
#include <fstream>

using namespace std;

int main()
{
	{
		std::ifstream fileIn("tutorials.txt");
		if (!fileIn)
		{
			std::cerr << "error opening file for reading!\n";
			return 1;
		}

		Repository repo{};
		Tutorials tutorial;
		while (fileIn >> tutorial)
		{
			//std::cout << "Read tutorial from file: " << tutorial.get_title() << std::endl;
			repo.add_tutorial(tutorial);
		}
		fileIn.close();

		/*Tutorials t1{ "Introduction to C++", "test", "https://www.youtube.com/watch?v=ZzaPdXTrSb8", 120, 0, 500 };
		Tutorials t2{ "Understanding Object-Oriented Programming", "Taylor S.", "https://www.youtube.com/watch?v=JjY9U9lu37I", 90, 20, 800 };
		Tutorials t3{ "Advanced Concepts in C++", "John S.", "https://www.youtube.com/watch?v=GQp1zzTwrIg", 60, 50, 400 };
		Tutorials t4{ "C++ Data Structures and Algorithms Explained", "Sara K.", "https://www.youtube.com/watch?v=q1ZmFc-sqNc", 150, 15, 600 };
		Tutorials t5{ "Managing Memory in C++ Programs", "Mike C.", "https://www.youtube.com/watch?v=FkCB5ooKozU", 45, 30, 300 };
		Tutorials t6{ "Exploring STL Containers in C++", "Lisa W.", "https://www.youtube.com/watch?v=gJ6XpGpjQqU", 80, 10, 700 };
		Tutorials t7{ "Best Practices for C++ Programming", "test", "https://www.youtube.com/watch?v=aT5qO-FkHO8", 120, 45, 900 };
		Tutorials t8{ "Functional Programming Techniques in C++", "Dan K.", "https://www.youtube.com/watch?v=EXLgZZE072g", 60, 0, 550 };
		Tutorials t9{ "Parallel Programming with C++", "Sophie L.", "https://www.youtube.com/watch?v=hP6QpMeSG6s", 100, 5, 750 };
		Tutorials t10{ "Debugging C++ Programs: Tips and Tricks", "test", "https://www.youtube.com/watch?v=qU9mHegkTc4", 45, 15, 350 };
		repo.add_tutorial(t1);
		repo.add_tutorial(t2);
		repo.add_tutorial(t3);
		repo.add_tutorial(t4);
		repo.add_tutorial(t5);
		repo.add_tutorial(t6);
		repo.add_tutorial(t7);
		repo.add_tutorial(t8);
		repo.add_tutorial(t9);
		repo.add_tutorial(t10);*/

		Service service{ repo };

		Repository repo_watch_list{};
		Service service_watch_list{ repo_watch_list };

		//run_all_tests();
		//std::cout << "tests done!";

		UI ui(service, service_watch_list);
		ui.choose_user_or_administrator_mode(); }
	_CrtDumpMemoryLeaks();

	return 0;
}