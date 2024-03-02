#include "repository.h"
#include "dynamic_vector.h"
#include <iostream>

void Repository::add_tutorial(const Tutorials& tutorial_to_be_added)
{
    this->tutorials.add(tutorial_to_be_added);
}

void Repository::delete_tutorial(const Tutorials& tutorial_to_be_deleted)
{
    this->tutorials.delete_(tutorial_to_be_deleted);
}

void Repository::update_tutorial(const Tutorials& tutorial_to_be_updated)
{
    this->tutorials.update(tutorial_to_be_updated);
}

DynamicVector<Tutorials> Repository::get_all() const
{
    return this->tutorials;
}

int Repository::get_size() const
{
    return this->tutorials.get_size_dynamic_vector();
}

bool Repository::check_if_tutorial_exists(const Tutorials& tutorial_to_be_checked)
{
    DynamicVector<Tutorials> list = this->tutorials;
    for (int i = 0; i < list.get_size_dynamic_vector(); i++)
    {
        if (list.get_element(i).get_title() == tutorial_to_be_checked.get_title() && list.get_element(i).get_presenter() == tutorial_to_be_checked.get_presenter())
        {
            return true;
        }
    }
    return false;
}