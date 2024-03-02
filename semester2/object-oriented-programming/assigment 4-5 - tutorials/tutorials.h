#pragma once
#include <string>

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
        void set_minutes(int durationMinutes);
        void set_seconds(int durationSEconds);
        void set_likes(int numberOfLikes);
};