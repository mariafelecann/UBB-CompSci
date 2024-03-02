#include "MultiMapIterator.h"
#include "MultiMap.h"
#include <iostream>
#define NULL_TELEM pair<int,int>(-111111, -111111)
using namespace std;

//best case: theta(1)
//worst case: theta(n)
//overall : O(n)
void MultiMapIterator::findNextValidPosition()
{
    while (current < col.capacity && currentElementFromPosition == nullptr)
    {
        currentElementFromPosition = col.hashTable[current];
        if (currentElementFromPosition == nullptr)
            current++;
    }
}

//best case: theta(n)
//worst case: theta(n)
//overall : theta(n)
MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
	current = 0;
	currentElementFromPosition = nullptr;
	findNextValidPosition();
}

//best case: theta(1)
//worst case: theta(1)
//overall : theta(1)
TElem MultiMapIterator::getCurrent() const{
    if (!valid())
        throw std::exception("Invalid iterator state!");

    return currentElementFromPosition->info;
 }

//best case: theta(1)
//worst case: theta(1)
//overall : theta(1)
bool MultiMapIterator::valid() const {
    return current < col.capacity && currentElementFromPosition != nullptr;
}

//best case: theta(1)
//worst case: theta(n)
//overall : O(n)
void MultiMapIterator::next() {
    if (!valid())
        throw std::exception();

    currentElementFromPosition = currentElementFromPosition->next;
    if (currentElementFromPosition == nullptr)
    {
        current++;
        findNextValidPosition();
    }
}

//best case: theta(1)
//worst case: theta(n)
//overall : O(n)
void MultiMapIterator::first() {
    current = 0;
    currentElementFromPosition = nullptr;
    findNextValidPosition();
}

TElem MultiMapIterator::remove()
{
    if (!valid())
        throw std::exception();
    TElem removedElement = currentElementFromPosition->info;
    Node* toRemove = currentElementFromPosition;
    Node* prevNode = nullptr;

    Node* node = col.hashTable[current];
    while (node != nullptr && node != currentElementFromPosition) {
        prevNode = node;
        node = node->next;
    }

    if (prevNode == nullptr) {
        col.hashTable[current] = toRemove->next;
    }
    else {
        prevNode->next = toRemove->next;
    }

    delete toRemove;

    return removedElement;
}


