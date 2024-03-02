#include "exceptions.h"
#include "service.h"
#include "repository.h"
#include <algorithm>

Service::Service(Repository& _repo) : repo{ _repo }
{
	this->repo = repo;
}

bool Service::service_add_tutorial(const Tutorials& tutorial)
{
	try {
		this->repo.add_tutorial(tutorial);
		return true;
	}
	catch (const DuplicateTutorialException& error) {
		return false;
	}
}

bool Service::service_delete_tutorial(const Tutorials& tutorial)
{
	try {
		this->repo.delete_tutorial(tutorial);
		return true;
	}
	catch (const TutorialNotFoundException& error) {
		return false;
	}
}

bool Service::service_update_tutorial(const Tutorials& tutorial)
{
	try {
		this->repo.update_tutorial(tutorial);
		return true;
	}
	catch (const TutorialNotFoundException& error) {
		return false;
	}
}


int Service::get_size() const
{
	return this->repo.get_size();
}

std::vector<Tutorials> Service::get_tutorials_of_presenter(std::string presenter){

	return this->repo.get_presenter_repo(presenter);
}

std::vector<Tutorials> Service::get_all_tutorials()
{
	return this->repo.get_all();
}
