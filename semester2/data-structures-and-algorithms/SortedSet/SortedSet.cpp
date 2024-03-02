#include "SortedSet.h"
#include "SortedSetIterator.h"
#include <iostream>

SortedSet::SortedSet(Relation r) {
    relation = r;
    size_of_array = 0;
    capacity = 1;
    dynamic_array = new TComp[1];
}

// worst case: O(n), average case: O(n), best case: O(1)
bool SortedSet::add(TComp elem) {
    if (search(elem))
        return false;

    if (size_of_array == capacity) {
        capacity *= 2;
        TComp* new_array = new TComp[capacity];
        for (int i = 0; i < size_of_array; i++)
            new_array[i] = dynamic_array[i];
        delete[] dynamic_array;
        dynamic_array = new_array;
    }

    int pos = 0;
    for (int i = 0; i < size_of_array; i++)
        if (relation(dynamic_array[i], elem)) {
            pos = i + 1;
        }
        else break;
    for (int i = size_of_array; i > pos; --i)
        dynamic_array[i] = dynamic_array[i - 1];
    dynamic_array[pos] = elem;
    size_of_array += 1;
    return true;
}

// worst case: O(n), average case: O(n), best case: O(1)
bool SortedSet::remove(TComp elem) {
    if (!search(elem))
        return false;
    bool found_check = false;
    for (int i = 0; i < size_of_array - 1; i++) {
        if (dynamic_array[i] == elem)
            found_check = true;
        if (found_check)
            dynamic_array[i] = dynamic_array[i + 1];
    }
    size_of_array -= 1;
    return true;
}

// worst case: O(log(n)) ; average case: O(log(n)); best case: O(1)
bool SortedSet::search(TComp elem) const {
    int left = 0, right = size_of_array - 1, mid;
    while (left <= right)
    {
        mid = (left + right) / 2;
        if (dynamic_array[mid] == elem)
            return true;
        else if (relation(dynamic_array[mid], elem))
            left = mid + 1;
        else right = mid - 1;
    }
    return false;
}

//worst case, average case, best case: O(1)
int SortedSet::size() const {
    return size_of_array;
}


//worst case, average case, best case: O(1)
bool SortedSet::isEmpty() const {
    return size_of_array == 0;
}

SortedSetIterator SortedSet::iterator() const {
    return SortedSetIterator(*this);
}


SortedSet::~SortedSet() {
    delete[] dynamic_array;
}