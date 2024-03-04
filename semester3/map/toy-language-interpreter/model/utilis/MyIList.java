package model.utilis;

import java.util.List;

public interface MyIList<T> {
    void add(T itemToAdd);
    int getSize();

    boolean isEmpty();

    List<T> iterate_list();
}
