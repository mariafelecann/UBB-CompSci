#include "service.h"
#include <algorithm>

Service::Service(Repository& _repo) : repo{ _repo }
{
}

bool Service::service_add_tutorial(const Tutorials& tutorial)
{

	if (this->repo.check_if_tutorial_exists(tutorial) == false)
		this->repo.add_tutorial(tutorial);
	else
		return false;
	return true;
}

bool Service::service_delete_tutorial(const Tutorials& tutorial)
{
	if (this->repo.check_if_tutorial_exists(tutorial)==true)
		this->repo.delete_tutorial(tutorial);
	else
		return false;
	return true;
}

bool Service::service_update_tutorial(const Tutorials& tutorial)
{
	if (this->repo.check_if_tutorial_exists(tutorial) == true)
		this->repo.update_tutorial(tutorial);
	else
		return false;
	return true;
}

int Service::get_size() const
{
	return this->repo.get_size();
}

std::vector<Tutorials> Service::get_tutorials_of_presenter(const std::string presenter) const
{
	return this->repo.get_presenter_repo(presenter);
}

std::vector<Tutorials> Service::get_all_tutorials() const
{
	return this->repo.get_all_tutorials();
}
