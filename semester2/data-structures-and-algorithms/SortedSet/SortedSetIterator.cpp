#include "SortedSetIterator.h"
#include <exception>

using namespace std;

//worst case, average case, best case: O(1)
SortedSetIterator::SortedSetIterator(const SortedSet& m) : multime(m)
{
	current_element = 0;
}

//worst case, average case, best case: O(1)
void SortedSetIterator::first() {
	current_element = 0;
}

//worst case, average case, best case: O(1)
void SortedSetIterator::next() {
	if (current_element == multime.size())
		throw exception();
	else
	{
		current_element += 1;
	}
}

//worst case, average case, best case: O(1)
TElem SortedSetIterator::getCurrent()
{
	if (current_element == multime.size())
		throw exception();
	else
		return multime.dynamic_array[current_element];
}

//worst case, average case, best case: O(1)
bool SortedSetIterator::valid() const {
	if (current_element < multime.size() && current_element >= 0)
	{
		return true;
	}
	else
		return false;
}

//worst case, average case, best case: O(1)
void SortedSetIterator::previous()
{
	if (!valid())
		throw exception();
	current_element -= 1;
}

