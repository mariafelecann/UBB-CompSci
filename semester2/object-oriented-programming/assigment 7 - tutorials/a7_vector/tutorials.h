#pragma once
#include <string>
#include <iostream>
class Tutorials
{
private:
    std::string title;
    std::string presenter;
    std::string link;
    int minutes;
    int seconds;
    int number_of_likes;

public:
    Tutorials();
    Tutorials(const std::string& title, const std::string& presenter, const std::string& link, int minutes, int seconds, int number_of_likes);

    std::string get_title() const;
    std::string get_presenter() const;
    std::string get_link() const;
    int get_minutes() const;
    int get_seconds() const;
    int get_likes() const;

    //void set_title(const std::string& title);
    void set_presenter(const std::string& presenter);
    void set_link(const std::string& link);
    void set_minutes(int minutes);
    void set_seconds(int sconds);
    void set_likes(int likes);
    bool operator==(const Tutorials& other) const;

    friend std::ostream& operator<<(std::ostream& os, const Tutorials& tutorial)
    {
        os << tutorial.title << std::endl
            << tutorial.presenter << std::endl
            << tutorial.link << std::endl
            << tutorial.minutes << std::endl
            << tutorial.seconds << std::endl
            << tutorial.number_of_likes << std::endl;
        return os;
    }

    friend std::istream& operator>>(std::istream& is, Tutorials& tutorial)
    {
        std::getline(is >> std::ws, tutorial.title);
        std::getline(is >> std::ws, tutorial.presenter);
        std::getline(is >> std::ws, tutorial.link);
        is >> tutorial.minutes >> tutorial.seconds >> tutorial.number_of_likes;
        return is;
    }
};
