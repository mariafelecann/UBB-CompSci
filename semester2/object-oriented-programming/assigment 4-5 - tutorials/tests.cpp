#include <cassert>
#include "dynamic_vector.h"
#include "repository.h"
#include "service.h"
#include "tutorials.h"

template <typename Tutorials>
void test_dynamic_vector() {
    DynamicVector<Tutorials> first_vector;
    Tutorials tutorial1{ "title1", "presenter1", "www.link1.com", 30, 15, 10 };
    first_vector.add(tutorial1);

    DynamicVector<Tutorials> second_vector;
    Tutorials tutorial2{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    second_vector.add(tutorial2);

    first_vector = second_vector;

    assert(first_vector.get_size_dynamic_vector() == 1);

    assert(first_vector.get_element(0).get_likes() == 20);

    Tutorials tutorial3{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial4{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial5{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial6{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial7{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial8{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial9{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial10{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial11{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial12{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial13{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial14{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial15{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial16{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial17{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial18{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial19{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial20{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };
    Tutorials tutorial21{ "title2", "presenter2", "www.link2.com", 45, 30, 20 };

    DynamicVector<Tutorials> vector_that_is_tested;
    vector_that_is_tested.add(tutorial1);
    vector_that_is_tested.add(tutorial2);
    vector_that_is_tested.add(tutorial3);
    vector_that_is_tested.add(tutorial4);
    vector_that_is_tested.add(tutorial5);
    vector_that_is_tested.add(tutorial6);
    vector_that_is_tested.add(tutorial7);
    vector_that_is_tested.add(tutorial8);
    vector_that_is_tested.add(tutorial9);
    vector_that_is_tested.add(tutorial10);
    vector_that_is_tested.add(tutorial11);
    vector_that_is_tested.add(tutorial12);
    vector_that_is_tested.add(tutorial13);
    vector_that_is_tested.add(tutorial14);
    vector_that_is_tested.add(tutorial15);
    vector_that_is_tested.add(tutorial16);
    vector_that_is_tested.add(tutorial17);
    vector_that_is_tested.add(tutorial18);
    vector_that_is_tested.add(tutorial19);
    vector_that_is_tested.add(tutorial20);
    vector_that_is_tested.add(tutorial21);

    assert(vector_that_is_tested.get_size_dynamic_vector() == 21);

}

template <typename Tutorials>
void test_resize()
{
    DynamicVector<Tutorials> vector; 
    Tutorials tutorial1{ "title1", "presenter1", "www.link1.com", 30, 15, 10 };
    vector.add(tutorial1);
    assert(vector.get_size_dynamic_vector() == 1); 
    vector.resize();
    assert(vector.get_size_dynamic_vector() == 1); 
    Tutorials tutorial2{ "title2", "presenter2", "www.link2.com", 30, 15, 10 };
    vector.add(tutorial2);
    assert(vector.get_size_dynamic_vector() == 2);
}



void test_service_add_tutorial()
{
    Repository repo;
    Service service{ repo };

    Tutorials tutorial{ "title", "presenter", "link", 10, 100, 10 };
    assert(service.service_add_tutorial(tutorial) == 1);
    assert(service.service_add_tutorial(tutorial) == 0);

}

void test_service_delete_tutorial()
{
    Repository repo;
    Service service{ repo };

    Tutorials tutorial{ "title", "presenter", "link", 10, 100, 10 };
    service.service_add_tutorial(tutorial);

    assert(service.service_delete_tutorial(tutorial) == 1);
    assert(service.service_delete_tutorial(tutorial) == 0);
}

void test_service_update_tutuorial()
{
    Repository repo;
    Service service{ repo };

    Tutorials tutorial{ "title", "presenter", "link", 10, 100, 10 };
    service.service_add_tutorial(tutorial);

    Tutorials newTutorial{ "newTitle", "newPresenter", "newLink", 20, 200, 20 };
    assert(service.service_update_tutorial(newTutorial) == 0);

    Tutorials existingTutorial{ "title", "presenter", "newLink", 20, 200, 20 };
    assert(service.service_update_tutorial(existingTutorial) == 1);
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

    DynamicVector<Tutorials> tutorials = service.get_tutorials_of_presenter("presenter1");

    assert(tutorials.get_size_dynamic_vector() == 2);

}

//void test_get_repo()
//{
//    Repository repo;
//    Service service{ repo };
//
//    assert(service.get_repo().get_size() == 0);
//
//    Tutorials tutorial{ "title", "presenter", "link", 10, 100, 10 };
//    service.service_add_tutorial(tutorial);
//
//    assert(service.get_repo().get_size() == 1);
//}
//testDynamicVector<Tutorials>();

void test_all()
{
    test_service_delete_tutorial();
    test_service_update_tutuorial();
    test_get_size();
    //test_get_repo();
    test_get_tutorials_of_presenter();
    test_service_add_tutorial();
    test_dynamic_vector<Tutorials>();
    test_resize<Tutorials>();
}
