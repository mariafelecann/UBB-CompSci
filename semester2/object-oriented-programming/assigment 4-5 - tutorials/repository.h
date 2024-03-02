#pragma once
#include "tutorials.h"
#include "dynamic_vector.h"

class Repository
{
private:
	DynamicVector<Tutorials> tutorials;

public:
	void add_tutorial(const Tutorials& tutorial_tp_be_added);
	void delete_tutorial(const Tutorials& tutorial_to_be_deleted);
	void update_tutorial(const Tutorials& tutorial_to_be_updated);
	void Tutorial(const Tutorials& tutorial);
	DynamicVector<Tutorials> get_all() const;
	int get_size() const;
	bool Repository::check_if_tutorial_exists(const Tutorials& tutorial);
};

