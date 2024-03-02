#pragma once
#include "repository.h"
#include <vector>

class Service
{
private:
	Repository& repo;

public:
	Service(Repository& _repo);
	bool service_add_tutorial(const Tutorials& tutorial);
	bool service_delete_tutorial(const Tutorials& tutorial);
	bool service_update_tutorial(const Tutorials& tutorial);
	std::vector<Tutorials> get_tutorials_of_presenter(const std::string name);
	std::vector<Tutorials> get_all_tutorials();
	int get_size() const;
	//Service create_a_presenter_service();
};



