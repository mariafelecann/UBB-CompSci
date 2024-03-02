#include <string>
#include <iostream>
#include "service.h"
#include "tutorials.h"
#include "repository.h"
#include "ui.h"
#include <vector>
#include <cstdlib>

const int MINIMUM_OPTION = 1;
const int MAXIMUM_OPTION = 5;

const int MINIMUM_MODE = 1;
const int MAXIMUM_MODE = 3;

UI::UI(Service& _service, Service& _service_watch_list) :service{ _service }, service_watch_list{ _service_watch_list }
{
}

void UI::add_a_tutorial_ui(const Service& service)
{
	std::string title, presenter, link;
	int duration_minutes, duration_seconds, number_of_likes;
	std::cout << "please write the title, presenter, link, duration and number of likes of the new tutorial" << std::endl;
	getchar();
	std::cout << " title: ";
	getline(std::cin, title);
	std::cout << " presenter: ";
	getline(std::cin, presenter);
	std::cout << " link: ";
	getline(std::cin, link);
	std::cout << " number of minutes:  ";
	std::cin >> duration_minutes;
	std::cout << "number of seconds: ";
	std::cin >> duration_seconds;
	std::cout << " number of likes: ";
	std::cin >> number_of_likes;
	Tutorials t{ title, presenter, link, duration_minutes, duration_seconds, number_of_likes };
	if (this->service.service_add_tutorial(t) == 1)
		std::cout << "tutorial added." << "\n";
	else
		std::cout << "oops! this  tutorial already exists!" << "\n";
}

void UI::delete_a_tutorial_ui(const Service& service)
{
	std::string title, presenter, link;
	int duration_minutes, duration_seconds, number_of_likes;
	std::cout << "please write the tutorial you want to delete: " << std::endl;
	getchar();
	std::cout << " title: ";
	getline(std::cin, title);
	std::cout << " presenter: ";
	getline(std::cin, presenter);
	Tutorials tutorial{ title, presenter, " ", 0, 0, 0 };
	if (this->service.service_delete_tutorial(tutorial) == 1)
		std::cout << "tutorial deleted." << "\n";
	else
		std::cout << "oops! this  tutorial doesn't exists!" << "\n";
}

void UI::update_a_tutorial_ui(const Service& service)
{
	std::string title, presenter, link;
	int duration_minutes, duration_seconds, number_of_likes;
	std::cout << "enter the tutorial you want to update: " << std::endl;
	getchar();
	std::cout << " title: ";
	getline(std::cin, title);
	std::cout << " presenter: ";
	getline(std::cin, presenter);
	std::cout << " new link: ";
	getline(std::cin, link);
	std::cout << " new number of minutes:  ";
	std::cin >> duration_minutes;
	std::cout << "new number of seconds: ";
	std::cin >> duration_seconds;
	std::cout << " new number of likes: ";
	std::cin >> number_of_likes;
	Tutorials t{ title, presenter, link, duration_minutes, duration_seconds, number_of_likes };
	if (this->service.service_update_tutorial(t) == 1)
		std::cout << "tutorial updated" << "\n";
	else
		std::cout << "oops! this  tutorial doesn't exists!" << "\n";
}

void UI::see_all_tutorials(const Service& service)
{
	std::vector<Tutorials> list = this->service.get_all_tutorials();
	Tutorials tutorial;
	for (int i = 0; i < list.size(); i++)
	{
		tutorial = list[i];
		std::cout << "title: " << tutorial.get_title() << "  presenter: " << tutorial.get_presenter() << "  link: " << tutorial.get_link() << "  duration: " << tutorial.get_minutes() << " : " << tutorial.get_seconds() << "  likes: " << tutorial.get_likes() << std::endl;
	}

}
void UI::see_tutorials_of_a_presenter(const Service& service, const Service& service_watch_list, const std::string presenter)
{
	std::vector<Tutorials> list = this->service.get_tutorials_of_presenter(presenter);
	Tutorials tutorial;
	std::string command;
	if (!presenter.empty())
		for (int i = 0; i < list.size(); i++)
		{
			tutorial = list[i];
			if (tutorial.get_presenter() == presenter)
			{
				std::cout << " " << tutorial.get_title() << "  " << tutorial.get_presenter() << "  " << tutorial.get_link() << "  " << tutorial.get_minutes() << "  " << tutorial.get_seconds() << "  " << tutorial.get_likes() << std::endl;
				command = "start " + tutorial.get_link();
				std::system(command.c_str());
				break;
			}
		}
	else
	{
		tutorial = list[0];
		std::cout << " " << tutorial.get_title() << "  " << tutorial.get_presenter() << "  " << tutorial.get_link() << "  " << tutorial.get_minutes() << "  " << tutorial.get_seconds() << "  " << tutorial.get_likes() << std::endl;
		command = "start " + tutorial.get_link();
		std::system(command.c_str());
	}

}
void UI::add_tutorial_to_watch_list(const Service& service, const Service& service_watch_list)
{
	std::string title, presenter, link;
	int duration_minutes, duration_seconds, number_of_likes;
	std::cout << "please write the new tutorial" << std::endl;
	getchar();
	std::cout << " title: ";
	getline(std::cin, title);
	std::cout << " presenter: ";
	getline(std::cin, presenter);
	std::cout << " link: ";
	getline(std::cin, link);
	std::cout << " number of minutes:  ";
	std::cin >> duration_minutes;
	std::cout << "number of seconds: ";
	std::cin >> duration_seconds;
	std::cout << " number of likes: ";
	std::cin >> number_of_likes;
	Tutorials t{ title, presenter, link, duration_minutes, duration_seconds, number_of_likes };
	if (this->service_watch_list.service_add_tutorial(t) == 1)
		std::cout << "tutorial added to watch list." << "\n";
	else
		std::cout << "oops! This  tutorial already exists!" << "\n";
}

int UI::see_next_tutorial(const Service& service, const Service& service_watch_list, const std::string name, const int& last_time)
{
	std::string command;

	std::vector<Tutorials> list = this->service.get_all_tutorials();
	Tutorials tutorial;
	if (last_time < list.size())
	{
		tutorial = list[last_time];
		std::cout << " " << tutorial.get_title() << "  " << tutorial.get_presenter() << "  " << tutorial.get_link() << "  " << tutorial.get_minutes() << "  " << tutorial.get_seconds() << "  " << tutorial.get_likes() << std::endl;
		command = "start " + tutorial.get_link();
		std::system(command.c_str());
		return 1;
	}
	else
		return 0;
}

void UI::delete_tutorial_from_watch_list(const Service& service, const Service& service_watch_list)
{
	std::string title, presenter, link;
	int duration_minutes, duration_seconds, number_of_likes;
	std::cout << "please write the title and presenter of the tutorial you want to delete" << std::endl;
	getchar();
	std::cout << " title: ";
	getline(std::cin, title);
	std::cout << " presenter: ";
	getline(std::cin, presenter);
	std::cout << " link: ";
	getline(std::cin, link);
	std::cout << " number of minutes:  ";
	std::cin >> duration_minutes;
	std::cout << "number of seconds: ";
	std::cin >> duration_seconds;
	std::cout << " number of likes: ";
	std::cin >> number_of_likes;
	Tutorials tutorial{ title, presenter, link, duration_minutes, duration_seconds, number_of_likes };
	if (this->service_watch_list.service_delete_tutorial(tutorial) == 1)
		std::cout << "tutorial deleted from watch list." << "\n";
	else
		std::cout << "oops! this  tutorial doesn't exists!" << "\n";
}
void UI::see_watch_list(const Service& service, const Service& service_watch_list)
{

	std::vector<Tutorials> list = this->service_watch_list.get_all_tutorials();
	Tutorials tutorial;
	for (int i = 0; i < list.size(); i++)
	{
		tutorial = list[i];
		std::cout << "title: " << tutorial.get_title() << "  presenter: " << tutorial.get_presenter() << "  link: " << tutorial.get_link() << "  duration: " << tutorial.get_minutes() << ":" << tutorial.get_seconds() << "  likes: " << tutorial.get_likes() << std::endl;
	}

}
void UI::print_administrator_mode_options()
{
	std::cout << "administrator options: " << std::endl;
	std::cout << " 1. add a tutorial " << std::endl;
	std::cout << " 2. delete a tutorial " << std::endl;
	std::cout << " 3. update a tutorial " << std::endl;
	std::cout << " 4. list all tutorials" << std::endl;
	std::cout << " 5. choose another mode" << std::endl;

	std::cout << " enter your choice: " << std::endl << " --> ";
}

void UI::run_administrator_console(const Service& service)
{

	print_administrator_mode_options();
	int option;
	std::cin >> option;

	while (option != MAXIMUM_OPTION)
	{
		if (option == MINIMUM_OPTION)
			add_a_tutorial_ui(service);
		else
			if (option == MINIMUM_OPTION + 1)
				delete_a_tutorial_ui(service);
			else
				if (option == MINIMUM_OPTION + 2)
					update_a_tutorial_ui(service);
				else
					if (option == MINIMUM_OPTION + 3)
						see_all_tutorials(service);
					else
						std::cout << "invalid input" << std::endl;
		print_administrator_mode_options();
		std::cin >> option;

	}
}

void UI::print_user_mode_options()
{
	std::cout << "user options" << std::endl;
	std::cout << "1. show next tutorial" << std::endl;
	std::cout << "2. add tutorial to watchlist" << std::endl;
	std::cout << "3. delete a tutorial from the watchlist" << std::endl;
	std::cout << "4. see the watchlist" << std::endl;
	std::cout << "5. choose another mode" << std::endl;
	std::cout << "your option is?";
}
void UI::run_user_console(const Service& service, const Service& service_watch_list)
{
	std::string presenter;
	std::cout << "the presenter you wish to explore the videos of is? ";
	getchar();
	getline(std::cin, presenter);
	Repository repo_for_presenter{};
	Service service_for_presenter{ repo_for_presenter };

	std::vector<Tutorials> list = this->service.get_all_tutorials();
	Tutorials tutorial;

	if (!presenter.empty())
		for (int i = 0; i < list.size(); i++)
		{
			if (list[i].get_presenter() == presenter)
			{
				tutorial = list[i];
				service_for_presenter.service_add_tutorial(tutorial);
			}
		}
	else
	{
		for (int i = 0; i < list.size(); i++)
		{
			tutorial = list[i];
			service_for_presenter.service_add_tutorial(tutorial);
		}
	}

	print_user_mode_options();
	int option, number_of_times_see_next_tutorial_was_called = 0;
	std::cin >> option;
	int last_time = 0;
	while (option != MAXIMUM_OPTION)
	{
		if (option == MINIMUM_OPTION)
		{
			if (see_next_tutorial(service_for_presenter, service_watch_list, presenter, last_time) == 0)
			{
				last_time = 0;
				int a = see_next_tutorial(service_for_presenter, service_watch_list, presenter, last_time);
			}
			number_of_times_see_next_tutorial_was_called++;
			last_time++;
		}

		else
			if (option == MINIMUM_OPTION + 1)
				add_tutorial_to_watch_list(service, service_watch_list);
			else
				if (option == MINIMUM_OPTION + 2)
				{
					delete_tutorial_from_watch_list(service, service_watch_list);
				}
				else
					if (option == MINIMUM_OPTION + 3)
						see_watch_list(service, service_watch_list);

					else
						std::cout << "invalid input" << std::endl;

		print_user_mode_options();
		std::cin >> option;

	}
}

void UI::choose_user_or_administrator_mode()
{
	std::cout << " ~~ WELCOME! ~~" << std::endl;
	std::cout << "which mode would you like to use? " << std::endl;
	std::cout << "1. administrator " << std::endl;
	std::cout << "2. user " << std::endl;
	std::cout << "3. exit " << std::endl;
	int mode;
	std::cout << " --> ";
	std::cin >> mode;
	while (mode != MAXIMUM_MODE)
	{
		if (mode == MINIMUM_MODE)
			run_administrator_console(service);
		else
			if (mode == MINIMUM_MODE + 1)
				run_user_console(service, service_watch_list);
			else
				std::cout << "oops! invalid option" << std::endl;
		std::cout << "which mode would you like to use? " << std::endl;
		std::cout << "1. administrator " << std::endl;
		std::cout << "2. user " << std::endl;
		std::cout << "3. exit " << std::endl;
		std::cout << " --> ";
		std::cin >> mode;
	}

}
