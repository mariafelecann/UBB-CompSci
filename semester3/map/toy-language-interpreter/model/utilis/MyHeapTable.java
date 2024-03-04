package model.utilis;

import java.util.*;

public class MyHeapTable<K,V> implements MyIHeap<K,V>{

    Map<K,V> dictionary;
    int last_address;
    public void default_first_address()
    {
        last_address = 0;
    }
    public int getLastAddress()
    {
        return last_address;
    }
    @Override
    public void updateLastAddress(int new_addr)
    {
        last_address = new_addr;
    }
    public MyHeapTable() {
        dictionary = new HashMap<>();
        last_address = 0;
    }
    @Override
    public boolean isDefined(K key) {
        return dictionary.containsKey(key);
    }

    @Override
    public void put(K key, V value) {
        dictionary.put(key, value);
    }

    @Override
    public V lookUp(K key) {
        try
        {
            return dictionary.get(key);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
    @Override
    public void update(K key, V value) {
        dictionary.put(key, value);
    }

    @Override
    public String toString() {
        return "MyDictionary{" +
                "dictionary=" + dictionary +
                '}';
    }
    @Override
    public List<String> iterateHeap() {
        List<String> heap_table_content = new ArrayList<>();
        for (Map.Entry<K, V> entry : dictionary.entrySet()) {
            String new_string = "Key: " + entry.getKey() + ", Value: " + entry.getValue();
            heap_table_content.add(new_string);
        }
        return heap_table_content;
    }

    @Override
    public void remove(K key) {
        dictionary.remove(key);
    }


    public Map<K, V> getContent() {
        return dictionary;
    }

    @Override
    public boolean isEmpty() {
        return dictionary.isEmpty();
    }
    public Set<Map.Entry<K, V>> entrySet() {
        return this.dictionary.entrySet();
    }

    public void setContent(Map<K, V> content) {
        dictionary = content;
    }
}
