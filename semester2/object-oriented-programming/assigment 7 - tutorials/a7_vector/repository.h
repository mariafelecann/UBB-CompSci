#pragma once
#include "tutorials.h"
#include <vector>

class Repository
{
private:
	std::vector<Tutorials> tutorials;

public:
	Repository();
	void add_tutorial(const Tutorials& tutorial_tp_be_added);
	void delete_tutorial(const Tutorials& tutorial_to_be_deleted);
	void update_tutorial(const Tutorials& tutorial_to_be_updated);
	void Tutorial(const Tutorials& tutorial);
	std::vector<Tutorials> get_all() const;
	int get_size() const;
	bool check_if_tutorial_exists(const Tutorials& t);
	std::vector<Tutorials> get_presenter_repo(std::string presenter);
};

