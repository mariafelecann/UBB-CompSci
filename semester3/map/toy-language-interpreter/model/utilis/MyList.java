package model.utilis;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements MyIList<T> {
    private List<T> items;

    public MyList()
    {
        items = new ArrayList<>();
    }

    @Override
    public void add(T itemToAdd) {
        items.add(itemToAdd);
    }

    @Override
    public int getSize() {
        return items.size();
    }

    @Override
    public boolean isEmpty() {
        return this.items.isEmpty();
    }

    @Override
    public List<T> iterate_list() {
        List<T> iterated = new ArrayList<>();
        for(T item: items)
        {
            iterated.add(item);
        }
        return iterated;
    }

    @Override
    public String toString() {
        return "MyList{" +
                "items=" + items +
                '}';
    }
}