#pragma once
#include <iostream>
#include <string>
#include "service.h"
#include "tutorials.h"
#include "repository.h"

class UI
{
private:
	Service& service;
	Service& service_watch_list;
public:
	UI(Service& service, Service& service_watch_list);
	void add_a_tutorial_ui(const Service& service);
	void delete_a_tutorial_ui(const Service& service);
	void update_a_tutorial_ui(const Service& service);
	void see_all_tutorials(const Service& service);

	void see_tutorials_of_a_presenter(const Service& service, const Service& service_watch_list, const std::string presenter);
	void add_tutorial_to_watch_list(const Service& service, const Service& service_watch_list, const std::string mode);
	int see_next_tutorial(const Service& service, const Service& service_watch_list, const std::string name, const int& last_time);
	void delete_tutorial_from_watch_list(const Service& service, const Service& service_watch_list, const std::string mode);
	void see_watch_list(const Service& service, const Service& service_watch_list);

	void print_administrator_mode_options();
	void run_administrator_console(const Service& service);
	void print_user_mode_options();
	void run_user_console(const Service& service, const Service& service_watch_list);
	void choose_user_or_administrator_mode();
	void view_watch_list(const std::string mode);
};



