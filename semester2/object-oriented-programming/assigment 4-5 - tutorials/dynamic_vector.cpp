#include "dynamic_vector.h"
#include "tutorials.h"
#include <iostream>

template <typename T>
DynamicVector<T>::DynamicVector(int capacity): capacity{capacity}, size{0}
{
	this->elements = new T[this->capacity];
}
template <typename T>
DynamicVector<T>::~DynamicVector()
{
	delete[] this->elements;
}

template <typename T>
DynamicVector<T>::DynamicVector(const DynamicVector<T>& vector)
{
	this->size = vector.size;
	this->capacity = vector.capacity;

	this->elements = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elements[i] = vector.elements[i];
}

template <typename T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector<T>& vector)
{
	if (this == &vector)
		return *this;

	this->size = vector.size;
	this->capacity = vector.capacity;

	delete[] this->elements;
	this->elements = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elements[i] = vector.elements[i];

	return *this;
}
template <typename T>
void DynamicVector<T>::resize()
{
	this->capacity *= 2;

	T* new_data = new T[this->capacity];

	for (int i = 0; i < this->size; i++)
		new_data[i] = this->elements[i];

	delete[] this->elements;

	this->elements = new_data;
}
template <typename T>
int DynamicVector<T>::get_size_dynamic_vector() const
{
	return this->size;
}
template <typename T>
T DynamicVector<T>::get_element(int index_of_element) const
{
	return this->elements[index_of_element];
}
template <typename T>
void DynamicVector<T>::add(const T& element_to_be_added)
{

	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size] = element_to_be_added;
	this->size++;

}
template <typename T>
void DynamicVector<T>::delete_(const T& element_to_be_deleted)
{
	int index_of_element_to_be_deleted = -1;
	for (int i = 0; i < this->size; i++)
	{
		if ((element_to_be_deleted.get_title() == this->elements[i].get_title()) && (element_to_be_deleted.get_presenter() == this->elements[i].get_presenter())) {
			index_of_element_to_be_deleted = i;
		}
	}
	if (index_of_element_to_be_deleted != -1) {
		for (int i = index_of_element_to_be_deleted; i < this->size - 1; i++) {
			this->elements[i] = this->elements[i + 1];
		}
		this->size--;
	}
}


template <typename T>
void DynamicVector<T>::update(const T& element_to_be_updated)
{
	for (int i = 0; i < this->size; i++)
		if (this->elements[i].get_title() == element_to_be_updated.get_title())
		{

			std::string temporary_hold_new_presenter = element_to_be_updated.get_presenter();
			this->elements[i].set_presenter(temporary_hold_new_presenter);
			
			std::string temporary_hold_new_link = element_to_be_updated.get_link();
			this->elements[i].set_link(temporary_hold_new_link);
			
			int temporary_hold_duration = element_to_be_updated.get_minutes();
			this->elements[i].set_minutes(temporary_hold_duration);
			
			temporary_hold_duration = element_to_be_updated.get_seconds();
			this->elements[i].set_seconds(temporary_hold_duration);
			
			int temporary_hold_number_of_likes = element_to_be_updated.get_likes();
			this->elements[i].set_likes(temporary_hold_number_of_likes);
			
		}
}
