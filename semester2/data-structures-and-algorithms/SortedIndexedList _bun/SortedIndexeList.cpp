#include "ListIterator.h"
#include "SortedIndexedList.h"
#include <iostream>
using namespace std;
#include <exception>

SortedIndexedList::SortedIndexedList(Relation r) {
	this->r = r;
	this->head = nullptr;
	this->size_of_list = 0;
}

//best,worst case: theta(1), overall case: theta(1)
int SortedIndexedList::size() const {
	if (head == nullptr)
		return 0;
	return this->size_of_list;
}

//best,worst case: theta(1), overall case: theta(1)
bool SortedIndexedList::isEmpty() const {
	return this->size_of_list == 0;
}

//best case: theta(1), worst case:theta(n), overall case: o(n)
TComp SortedIndexedList::getElement(int i) const{
    if (i < 0 || i >= this->size_of_list)
    {
        throw exception();
    }
    node* current = this->head;
    int position = 0;
    while (current != nullptr)
    {
        if (i == position)
            return current->element;
        else
        {
            position = position + 1;
            current = current->next_element;
        }
    }
}

//best case: theta(1) , worst case: theta(n), overall case: o(n)
TComp SortedIndexedList::remove(int i) {
	if (i <0 || i >= size()) {
		throw std::exception();
	}

	node* previous_node = nullptr;
	node* current_node = this->head;

	int current_position = 0;
	while (current_position < i && current_node != nullptr) {
		previous_node = current_node;
		current_node = current_node->next_element;
		current_position++;
	}

	if (previous_node == nullptr && current_node != nullptr) {
		this->head = current_node->next_element;
		this->size_of_list = this->size_of_list - 1;
	}
	else if (current_node != nullptr) {
		previous_node->next_element = current_node->next_element;
		current_node->next_element = nullptr;
		this->size_of_list = this->size_of_list - 1;
	}
	return current_node->element;
}

//best case: theta(1), worst case: theta(n), overall case: o(n)
int SortedIndexedList::search(TComp e) const {
	node* current = this->head;
	int position = 0;
	while (current != nullptr)
	{
		if (current->element == e)
			return position;
		else
		{
			position = position + 1;
			current = current->next_element;
		}
	}
	return -1;
}

//best case: theta(1), worst case: theta(n), overall case: o(n)
void SortedIndexedList::add(TComp e) {
	node* current = this->head;

	int position = 0;
	while (current != nullptr && !this->r(e, current->element)) {
		current = current->next_element;
		position++;
	}

	if (position == 0) {
		node* new_node = new node();
		new_node->element = e;
		new_node->next_element = this->head;

		this->head = new_node;
		this->size_of_list = this->size_of_list + 1;
	}
	else {
		node* current_node = this->head;

		int current_position = 0;
		while (current_position < (position - 1) && current_node != nullptr) {
			current_node = current_node->next_element;
			current_position++;
		}
		if (current_node != nullptr) {
			node* new_node = new node();
			new_node->element = e;
			new_node->next_element = current_node->next_element;

			current_node->next_element = new_node;
			this->size_of_list = this->size_of_list + 1;
		}
	}
}

ListIterator SortedIndexedList::iterator() {
	return ListIterator(*this);
}

SortedIndexedList::~SortedIndexedList() {
	while (!this->isEmpty())
		this->remove(0);
}

//best case: theta(1), worst case: theta(n), overall case: o(n)
void SortedIndexedList::removeBetween(int start, int end) {
	if (start < 0 || end >= this->size_of_list || start > end) {
		throw std::exception();
	}

	node* previous_node = nullptr;
	node* current_node = this->head;

	int current_position = 0;
	while (current_position < start && current_node != nullptr) {
		previous_node = current_node;
		current_node = current_node->next_element;
		current_position++;
	}

	while (current_position <= end && current_node != nullptr) {
		node* next_node = current_node->next_element;
		delete current_node;
		current_node = next_node;
		current_position++;
		this->size_of_list--;
	}

	if (previous_node == nullptr && current_node != nullptr) {
		this->head = current_node;
	}

	else if (current_node != nullptr) {
		previous_node->next_element = current_node;
	}
}
