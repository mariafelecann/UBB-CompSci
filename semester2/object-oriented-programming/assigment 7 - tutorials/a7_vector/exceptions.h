#pragma once

#include <exception>
#include <string>

class RepositoryException : public std::exception {
public:
    RepositoryException(const std::string& message) : message(message) {}
    const char* what() const override {
        return message.c_str();
    }
private:
    std::string message;
};

class DuplicateTutorialException : public RepositoryException {
public:
    DuplicateTutorialException() : RepositoryException("error: tutorial already exists in repository.") {}
};

class TutorialNotFoundException : public RepositoryException {
public:
    TutorialNotFoundException() : RepositoryException("error: tutorial not found in repository.") {}
};
