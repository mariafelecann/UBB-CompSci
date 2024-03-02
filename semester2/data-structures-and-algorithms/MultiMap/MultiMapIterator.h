#pragma once
#include "MultiMap.h"

class MultiMap;

class MultiMapIterator
{
	friend class MultiMap;

private:
	const MultiMap& col;
	int current;
	Node* currentElementFromPosition;
	
	//DO NOT CHANGE THIS PART
	MultiMapIterator(const MultiMap& c);
	void findNextValidPosition();
public:
	TElem getCurrent()const;
	bool valid() const;
	void next();
	void first();
	TElem remove();
};

