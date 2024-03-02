#pragma once
#include <vector>
#include <string>
#include "tutorials.h"

class Repository {
private:
    std::vector<Tutorials> tutorials;

public:
    Repository();
    void add_tutorial(const Tutorials& tutorial_to_be_added);
    void delete_tutorial(const Tutorials& tutorial_to_be_deleted);
    void update_tutorial(const Tutorials& tutorial_to_be_updated);
    std::vector<Tutorials> get_presenter_repo(std::string presenter);
    bool check_if_tutorial_exists(const Tutorials& tutorial);
    std::vector<Tutorials> get_all_tutorials() const;
    int get_size() const;
};