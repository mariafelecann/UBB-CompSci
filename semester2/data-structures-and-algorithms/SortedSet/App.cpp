#include "ShortTest.h"
#include "ExtendedTest.h"
#include "SortedSet.h"
#include "SortedSetIterator.h"
#include <iostream>

using namespace std;

bool relation(TComp e1, TComp e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

int main() {
	testAll();
	testAllExtended();
	SortedSet set(relation);
	SortedSetIterator iterator = set.iterator();
	set.add(0);
	set.add(1);
	set.add(2);
	TComp current = iterator.getCurrent();
	iterator.next();
	iterator.previous();
	TComp new_current = iterator.getCurrent();
	if (new_current == current)
		cout << "previous works" << endl;
	else
		cout << "previous failed" << endl;
	cout << "Test end" << endl;
	system("pause");
}