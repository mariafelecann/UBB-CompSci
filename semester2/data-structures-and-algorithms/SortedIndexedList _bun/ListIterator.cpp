#include "ListIterator.h"
#include "SortedIndexedList.h"
#include <iostream>

using namespace std;

ListIterator::ListIterator(const SortedIndexedList& list) : list(list) {
	this->current_position = 0;
}

//best,worst case: theta(1), overall case: theta(1)
void ListIterator::first(){
	this->current_position = 0;
}

//best,worst case: theta(1), overall case: theta(1)
void ListIterator::next(){
	if (!this->valid())
		throw exception();
	++this->current_position;
}

//best,worst case: theta(1), overall case: theta(1)
bool ListIterator::valid() const{
	return this->current_position < this->list.size();
}

//best,worst case: theta(1), overall case: theta(1)
TComp ListIterator::getCurrent() const{
	if (!this->valid())
		throw exception();
	return list.getElement(this->current_position);
}


