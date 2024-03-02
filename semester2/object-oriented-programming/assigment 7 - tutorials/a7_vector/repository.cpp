#include "repository.h"
#include <vector>
#include <iostream>
#include "exceptions.h"


Repository::Repository() : tutorials(tutorials) {
}


void Repository::add_tutorial(const Tutorials& tutorial)
{
	if(check_if_tutorial_exists(tutorial))
		throw DuplicateTutorialException();
	this->tutorials.push_back(tutorial);
}

void Repository::delete_tutorial(const Tutorials& tutorial)
{
	auto it = std::find_if(this->tutorials.begin(), this->tutorials.end(), [tutorial](const Tutorials& t) {
		return t.get_title() == tutorial.get_title();
		});
	if (it != this->tutorials.end()) {
		this->tutorials.erase(it);
	}
	else
	{
		if(!check_if_tutorial_exists(tutorial))
			throw TutorialNotFoundException();
	}
}

void Repository::update_tutorial(const Tutorials& tutorial)
{
	auto it = std::find_if(this->tutorials.begin(), this->tutorials.end(), [tutorial](const Tutorials& t) {
		return t.get_title() == tutorial.get_title();
		});

	if (it != this->tutorials.end()) {
		*it = tutorial;
	}
	else
	{
		if (!check_if_tutorial_exists(tutorial))
			throw TutorialNotFoundException();
	}
}

bool Repository::check_if_tutorial_exists(const Tutorials& tutorial)
{
	auto it = std::find(this->tutorials.begin(), this->tutorials.end(), tutorial);

	if (it != this->tutorials.end())
		return true;
	return false;
}

std::vector<Tutorials> Repository::get_presenter_repo(std::string presenter)
{
	std::vector<Tutorials> tutorials_of_a_presenter;
	for (auto tutorial: tutorials_of_a_presenter)
	{
		Tutorials tutorial_to_be_checked = tutorial;
		if (tutorial_to_be_checked.get_presenter() == presenter)
			tutorials_of_a_presenter.push_back(tutorial_to_be_checked);
	}

	return tutorials_of_a_presenter;
}


std::vector<Tutorials> Repository::get_all() const
{
	return this->tutorials;
}

int Repository::get_size() const
{
	return static_cast<int>(this->tutorials.size());
}
