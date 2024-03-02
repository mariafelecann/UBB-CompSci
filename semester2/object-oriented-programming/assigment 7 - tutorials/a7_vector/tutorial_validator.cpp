#include "tutorial_validator.h"
bool TutorialValidator::validate(const Tutorials& tutorial) const
{
    if (tutorial.get_title().empty()) {
        return false;
    }
    if (tutorial.get_presenter().empty()) {
        return false;
    }
    if (tutorial.get_link().empty()) {
        return false;
    }
    if (tutorial.get_minutes() < 0) {
        return false;
    }
    if (tutorial.get_seconds() < 0 || tutorial.get_seconds() >= 60) {
        return false;
    }
    if (tutorial.get_likes() < 0) {
        return false;
    }
    return true;
}