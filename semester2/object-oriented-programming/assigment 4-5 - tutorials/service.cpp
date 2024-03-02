#include "service.h"

Service::Service(Repository& _repo): repo {_repo}
{
	this->repo = repo;
}

bool Service::service_add_tutorial(const Tutorials& tutorial)
{
	if (this->repo.check_if_tutorial_exists(tutorial) == false)
	{
		this->repo.add_tutorial(tutorial);
		return true;}
	else
		return false;
}

bool Service::service_delete_tutorial(const Tutorials& tutorial)
{
	if (this->repo.check_if_tutorial_exists(tutorial) == true)
	{
		this->repo.delete_tutorial(tutorial);
		return true;}
	else
		return false;
}

bool Service::service_update_tutorial(const Tutorials& tutorial)
{
	if (this->repo.check_if_tutorial_exists(tutorial) == true)
	{
        this->repo.update_tutorial(tutorial);
		return true;
	}
	return false;
}

int Service::get_size() const
{
	return this->repo.get_size();
}

DynamicVector<Tutorials> Service::get_tutorials_of_presenter(const std::string name)
{
	DynamicVector<Tutorials> list_of_all_tutorials = this->repo.get_all();
	DynamicVector<Tutorials> list_that_user_wants;
	Tutorials tutorial;
	for (int i = 0; i < list_of_all_tutorials.get_size_dynamic_vector(); i++)
	{
		tutorial = list_of_all_tutorials.get_element(i);
		if (tutorial.get_presenter() == name)
		{
			list_that_user_wants.add(tutorial);
		}
	}
	return list_that_user_wants;
}

//Repository Service::get_repo() const
//{
//	return this->repo;
//}

DynamicVector<Tutorials> Service::get_all_tutorials()
{
	Repository repo{};
	repo = this->repo;
	Tutorials tutorial;
	DynamicVector<Tutorials> list = repo.get_all();
	
	return list;
}

//Service Service::create_a_presenter_service()
//{
//	Repository repo_for_presenter{};
//	Service service_for_presenter{ repo_for_presenter };
//	return service_for_presenter;
//}
