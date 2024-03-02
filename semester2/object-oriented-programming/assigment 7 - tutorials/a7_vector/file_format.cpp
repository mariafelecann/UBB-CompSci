#include "file_format.h"

void CSV::save(const std::vector<Tutorials>& tutorials)
{
    std::ofstream outfile(filename_);
    for (int i = 0; i < tutorials.size(); i++) {
        Tutorials tutorial;
        tutorial = tutorials[i];
        outfile << tutorial.get_title() << ","
            << tutorial.get_presenter() << ","
            << tutorial.get_link() << ","
            << tutorial.get_minutes() << ","
            << tutorial.get_seconds() << ","
            << tutorial.get_likes() << std::endl;
    }
    outfile.close();
}


void HTML::save(const std::vector<Tutorials>& tutorials)
{
    std::ofstream outfile(filename_);
    outfile << "<html><body><table>" << std::endl;
    outfile << "<tr><th>Title</th><th>Presenter</th><th>Link</th><th>Duration (minutes:seconds)</th><th>Likes</th></tr>" << std::endl;
    for (int i = 0; i < tutorials.size(); i++) {
        Tutorials tutorial;
        tutorial = tutorials[i];
        outfile << "<tr><td>" << tutorial.get_title() << "</td>"
            << "<td>" << tutorial.get_presenter() << "</td>"
            << "<td><a href=\"" << tutorial.get_link() << "\">" << tutorial.get_link() << "</a></td>"
            << "<td>" << tutorial.get_minutes() << ":" << tutorial.get_seconds() << "</td>"
            << "<td>" << tutorial.get_likes() << "</td></tr>" << std::endl;
    }
    outfile << "</table></body></html>" << std::endl;
    outfile.close();
}