#include "tests.h"
#include <assert.h>


void test_service_add()
{
    Repository repo;
    Service service{ repo };

    Tutorials tutorial{ "title", "presenter", "link", 10, 100, 10 };
    assert(service.service_add_tutorial(tutorial) == 0);
    assert(service.service_add_tutorial(tutorial) == 1);
}

void test_delete_service()
{
    Repository repo;
    Service service{ repo };

    Tutorials tutorial{ "title", "presenter", "link", 10, 100, 10 };
    service.service_add_tutorial(tutorial);

    assert(service.service_delete_tutorial(tutorial) == 0);
    assert(service.service_delete_tutorial(tutorial) == 1);
}

void test_update_service()
{
    Repository repo;
    Service service{ repo };

    Tutorials tutorial{ "title", "presenter", "link", 10, 100, 10 };
    service.service_add_tutorial(tutorial);

    Tutorials newTutorial{ "newTitle", "newPresenter", "newLink", 20, 200, 20 };
    assert(service.service_update_tutorial(newTutorial) == 1);

    Tutorials existingTutorial{ "title", "presenter", "newLink", 20, 200, 20 };
    assert(service.service_update_tutorial(existingTutorial) == 0);
}

void test_get_size()
{
    Repository repo;
    Service service{ repo };

    assert(service.get_size() == 0);

    Tutorials tutorial{ "title", "presenter", "link", 10, 100, 10 };
    service.service_add_tutorial(tutorial);

    assert(service.get_size() == 1);
}

void test_get_tutorials_of_presenter()
{
    Repository repo;
    Service service{ repo };

    Tutorials tutorial1{ "title1", "presenter1", "link1", 10, 100, 10 };
    Tutorials tutorial2{ "title2", "presenter2", "link2", 20, 200, 10 };
    Tutorials tutorial3{ "title3", "presenter1", "link3", 30, 300, 10 };

    service.service_add_tutorial(tutorial1);
    service.service_add_tutorial(tutorial2);
    service.service_add_tutorial(tutorial3);

    std::vector<Tutorials> tutorials = service.get_tutorials_of_presenter("presenter1");
    assert(tutorials.size() == 2);

}


void test_get_all_tutorials() {
    Repository repo;
    Service service(repo);

    Tutorials t1{ "Title 1", "Presenter 1", "www.link1.com", 60, 0, 50 };
    Tutorials t2{ "Title 2", "Presenter 2", "www.link2.com", 45, 30, 30 };
    Tutorials t3{ "Title 3", "Presenter 3", "www.link3.com", 90, 15, 20 };
    repo.add_tutorial(t1);
    repo.add_tutorial(t2);
    repo.add_tutorial(t3);

    std::vector<Tutorials> tutorials = service.get_all_tutorials();
    assert(tutorials.size() == 3);

    assert(tutorials[0].get_title() == "Title 1");
    assert(tutorials[1].get_title() == "Title 2");
    assert(tutorials[2].get_title() == "Title 3");

}


void test_tutorials_class()
{
    Tutorials tutorial;
    tutorial.set_presenter("John Smith");
    assert(tutorial.get_presenter() == "John Smith");

    
    tutorial.set_link("https://www.youtube.com/watch?v=123456");
    assert(tutorial.get_link() == "https://www.youtube.com/watch?v=123456");

    
    tutorial.set_minutes(60);
    assert(tutorial.get_minutes() == 60);

   
    tutorial.set_seconds(30);
    assert(tutorial.get_seconds() == 30);


    tutorial.set_likes(1000);
    assert(tutorial.get_likes() == 1000);
}
void run_all_tests()
{


    test_tutorials_class();
    test_service_add();
    test_delete_service();
    test_get_size();
    test_get_tutorials_of_presenter();
    test_update_service();

    
    test_get_all_tutorials();
}
