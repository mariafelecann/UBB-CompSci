#include "tutorials.h"

Tutorials::Tutorials():title{""}, presenter{""}, link{""}, minutes{0}, seconds{0}, number_of_likes{0}
{

}
Tutorials::Tutorials(const std::string& _title, const std::string& _presenter, const std::string& _link, int _durationMinutes, int _durationSeconds, int _numberOfLikes): title{_title}, 
                                                                                                                                                                        presenter{_presenter}, 
                                                                                                                                                                        link{_link},  
                                                                                                                                                                        minutes{_durationMinutes}, 
                                                                                                                                                                         seconds{_durationSeconds},
                                                                                                                                                                         number_of_likes{_numberOfLikes}
{
}
std::string Tutorials::get_title()const
{
    return this->title;
}
std::string Tutorials::get_presenter()const
{
    return this->presenter;
}
std::string Tutorials::get_link() const
{
    return this->link;
}
int Tutorials::get_minutes() const
{
    return this->minutes;
}
int Tutorials::get_seconds()const
{
    return this->seconds;
}
int Tutorials::get_likes() const
{
    return this->number_of_likes;
}

void Tutorials::set_presenter(const std::string& presenter)
{
    this->presenter=presenter;
}
void Tutorials::set_link(const std::string& link)
{
    this->link=link;
}
void Tutorials::set_minutes(int durationMinutes)
{
    this->minutes=durationMinutes;
}
void Tutorials::set_seconds(int durationSeconds)
{
    this->seconds=durationSeconds;
}
void Tutorials::set_likes(int numberOfLikes)
{
    this->number_of_likes=numberOfLikes;
}