#include "tutorials.h"

Tutorials::Tutorials() :title{ "" }, presenter{ "" }, link{ "" }, minutes{ 0 }, seconds{ 0 }, likes{ 0 }
{

}

Tutorials::~Tutorials()
{
}

Tutorials::Tutorials(const std::string& _title, const std::string& _presenter, const std::string& _link, int _minutes, int _seconds, int _likes) : title{ _title },
presenter{ _presenter },
link{ _link },
minutes{ _minutes },
seconds{ _seconds },
likes{ _likes }
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
    return this->likes;
}


void Tutorials::set_title(const std::string& title)
{
    this->title = title;
}

void Tutorials::set_presenter(const std::string& presenter)
{
    this->presenter = presenter;
}

void Tutorials::set_link(const std::string& link)
{
    this->link = link;
}

void Tutorials::set_minutes(int durationMinutes)
{
    this->minutes = durationMinutes;
}

void Tutorials::set_seconds(int durationSeconds)
{
    this->seconds = durationSeconds;
}

void Tutorials::set_likes(int numberOfLikes)
{
    this->likes = numberOfLikes;
}

bool Tutorials::operator==(const Tutorials& other) const
{
    return this->title == other.title;
 
}