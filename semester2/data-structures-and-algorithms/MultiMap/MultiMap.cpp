#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;

//best case: theta(1)
//worst case: theta(1)
//overall : theta(1)
MultiMap::MultiMap() {
	capacity = 10;
	count = 0;
	hashTable = new Node * [capacity];
	for (int i = 0; i < capacity; i++)
		hashTable[i] = nullptr;
}

//best case: theta(1)
//worst case: theta(1)
//overall : theta(1)
int MultiMap::hash(TKey key) const
{
	return abs(key) % this->capacity;
}

//best case: theta(n)
//worst case: theta(n)
//overall : theta(n)
void MultiMap::resizeHashTable()
{
	int newCapacity = 2 * capacity;
	Node** newHashTable = new Node * [newCapacity];
	for (int i = 0; i < newCapacity; i++)
		newHashTable[i] = nullptr;

	for (int i = 0; i < capacity; i++)
	{
		Node* current = hashTable[i];
		while (current != nullptr)
		{
			Node* next = current->next;
			int hashValue = abs(current->info.first) % newCapacity;
			current->next = newHashTable[hashValue];
			newHashTable[hashValue] = current;

			current = next;
		}
	}

	delete[] hashTable;
	hashTable = newHashTable;
	capacity = newCapacity;
}

//best case: theta(1)
//worst case: theta(n)
//overall : O(n)
Node* MultiMap::searchNode(TKey key) const
{
	int hashValue = hash(key);
	Node* current = hashTable[hashValue];
	while (current != nullptr)
	{
		if (current->info.first == key)
			return current;
		current = current->next;
	}
	return nullptr;
}

//best case: theta(1)
//worst case: theta(n)
//overall : O(n)
void MultiMap::add(TKey c, TValue v) {
	if (count == capacity)
		resizeHashTable();

	int hashValue = hash(c);
	Node* newNode = new Node(make_pair(c, v), nullptr);
	if (hashTable[hashValue] == nullptr) {
		hashTable[hashValue] = newNode;
	}
	else {
		Node* current = hashTable[hashValue];
		while (current->next != nullptr) {
			current = current->next;
		}
		current->next = newNode;
	}

	count++;
}

//best case: theta(1)
//worst case: theta(n)
//overall : O(n)
bool MultiMap::remove(TKey c, TValue v) {
	int hashValue = hash(c);
	Node* current = hashTable[hashValue];
	Node* prev = nullptr;

	while (current != nullptr)
	{
		if (current->info.first == c && current->info.second == v)
		{
			if (prev == nullptr)
				hashTable[hashValue] = current->next;
			else {
				prev->next = current->next;
			}
			delete current;
			count--;
			return true;

		}

		prev = current;
		current = current->next;
	}

	return false;
}

//best case: theta(1)
//worst case: theta(n)
//overall : O(n)
vector<TValue> MultiMap::search(TKey c) const {
	int hashValue = hash(c);
	Node* current = hashTable[hashValue];

	vector<TValue> values;
	while (current != nullptr) {
		if (current->info.first == c) {
			values.push_back(current->info.second);
		}
		current = current->next;
	}

	return values;
}

//best case: theta(1)
//worst case: theta(1)
//overall : theta(1)
int MultiMap::size() const {
	return count;
}

//best case: theta(1)
//worst case: theta(1)
//overall : theta(1)
bool MultiMap::isEmpty() const {
	return (count == 0);
}

//best case: theta(1)
//worst case: theta(1)
//overall : theta(1)
MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}

//best case: theta(n)
//worst case: theta(n)
//overall : theta(n)
MultiMap::~MultiMap() {
	for (int i = 0; i < capacity; i++)
	{
		Node* current = hashTable[i];
		while (current != nullptr)
		{
			Node* next = current->next;
			delete current;
			current = next;
		}
	}
	delete[] hashTable;
}