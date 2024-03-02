#pragma once
#include <string>

class Tutorials {
private:
	std::string title;
    std::string presenter;
    std::string link;
    int minutes;
    int seconds;
    int likes;

public:
    Tutorials();
    ~Tutorials();
    Tutorials(const std::string& _title, const std::string& _presenter, const std::string& _link, int _minutes, int _seconds, int _likes);

    std::string get_title() const;
    std::string get_presenter() const;
    std::string get_link() const;
    int get_minutes() const;
    int get_seconds() const;
    int get_likes() const;

    void set_title(const std::string& title);
    void set_presenter(const std::string& presenter);
    void set_link(const std::string& link);
    void set_minutes(int minutes);
    void set_seconds(int seconds);
    void set_likes(int likes);

    bool operator==(const Tutorials& other_tutorial) const;

};