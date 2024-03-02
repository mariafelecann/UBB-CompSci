#pragma once
#include "tutorials.h"

template <typename T>
class DynamicVector
{
private:
	T* elements;
	int capacity, size;

public:
	DynamicVector(int capacity = 20);
	~DynamicVector();

	DynamicVector(const DynamicVector& vector);
	DynamicVector& operator=(const DynamicVector& vector);

	void add(const T& element_to_be_added);
	void delete_(const T& element_to_be_deleted);
	void update(const T& element_to_be_updated);
	void resize();

	T get_element(int i) const;
	int get_size_dynamic_vector() const;
};

template class DynamicVector<Tutorials>;
