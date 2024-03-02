#include "repository.h"
#include <iostream>
#include <vector>
#include <algorithm>

Repository::Repository() : tutorials(tutorials){
}


void Repository::add_tutorial(const Tutorials& tutorial_to_be_added)
{
	this->tutorials.push_back(tutorial_to_be_added);
}

void Repository::delete_tutorial(const Tutorials& tutorial_to_be_deleted)
{
	auto iterator = std::find(this->tutorials.begin(), this->tutorials.end(), tutorial_to_be_deleted);
	if (iterator != this->tutorials.end()) {
		this->tutorials.erase(iterator);
	}
}

void Repository::update_tutorial(const Tutorials& tutorial_to_be_updated)
{
	auto iterator = std::find_if(this->tutorials.begin(), this->tutorials.end(), [tutorial_to_be_updated](const Tutorials& t) {
		return t.get_title() == tutorial_to_be_updated.get_title();
		});

	if (iterator != this->tutorials.end()) {
		*iterator = tutorial_to_be_updated;
	}
}

bool Repository::check_if_tutorial_exists(const Tutorials& tutorial)
{
	auto iterator = std::find(this->tutorials.begin(), this->tutorials.end(), tutorial);

	if (iterator != this->tutorials.end())
		return true;
	return false;
}

std::vector<Tutorials> Repository::get_presenter_repo(std::string presenter)
{
	std::vector<Tutorials> tutorials_of_a_presenter;
	for (auto tutorial : this->tutorials)
	{
		Tutorials tutorial_to_be_checked = tutorial;
		if (tutorial_to_be_checked.get_presenter() == presenter)
			tutorials_of_a_presenter.push_back(tutorial_to_be_checked);
	}

	return tutorials_of_a_presenter;
}

std::vector<Tutorials> Repository::get_all_tutorials() const
{
	return this->tutorials;
}

int Repository::get_size() const
{
	return static_cast<int>(this->tutorials.size());
}