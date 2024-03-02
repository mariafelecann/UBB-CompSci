#include "ShortTest.h"
#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <assert.h>
#include <vector>
#include<iostream>

void testAll() {
	MultiMap m;
	m.add(1, 100);
	m.add(2, 200);
	m.add(3, 300);
	m.add(1, 500);
	m.add(2, 600);
	m.add(4, 800);

	assert(m.size() == 6);

	assert(m.remove(5, 600) == false);
	assert(m.remove(1, 500) == true);

	assert(m.size() == 5);

    vector<TValue> v;
	v=m.search(6);
	assert(v.size()==0);

	v=m.search(1);
	assert(v.size()==1);

	assert(m.isEmpty() == false);

	MultiMapIterator im = m.iterator();
	assert(im.valid() == true);
	while (im.valid()) {
		im.getCurrent();
		im.next();
	}
	assert(im.valid() == false);
	im.first();
	assert(im.valid() == true);

	// test for remove from iterator:

	MultiMap map;
	map.add(1, 1);
	map.add(2, 2);
	map.add(1, 3);

	MultiMapIterator iterator = map.iterator();
	iterator.first();
	assert(iterator.valid());
	TElem removedElement = iterator.remove();
	assert(removedElement.first == 1 && removedElement.second == 1);

	iterator.next();
	assert(iterator.valid());
	removedElement = iterator.remove();
	assert(removedElement.first == 1 && removedElement.second == 3);

	iterator.next();
	assert(iterator.valid());
	removedElement = iterator.remove();
	assert(removedElement.first == 2 && removedElement.second == 2);

	assert(!iterator.valid());

	std::cout << "remove() test passed!" << std::endl;
}
