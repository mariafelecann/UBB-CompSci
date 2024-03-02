#pragma once
#include "Repository.h"

class Service
{
private:
	Repository& repo;
public:
	Service(Repository& _repo);

	bool service_add_tutorial(const Tutorials& tutorial);

	bool service_delete_tutorial(const Tutorials& tutorial);

	bool service_update_tutorial(const Tutorials& tutorial);

	int get_size() const;

	std::vector<Tutorials> get_tutorials_of_presenter(const std::string presenter) const;

	std::vector<Tutorials> get_all_tutorials() const;
};

