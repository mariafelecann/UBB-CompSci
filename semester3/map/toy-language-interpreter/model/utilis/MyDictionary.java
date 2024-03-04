package model.utilis;

import java.util.*;

public class MyDictionary<K,V> implements MyIDictionary<K,V>{

    Map<K,V> dictionary;
    public MyDictionary() {
        dictionary = new HashMap<>();
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
    public List<String> iterateDictionary() {
        List<String> sym_table_content = new ArrayList<>();
        for (Map.Entry<K, V> entry : dictionary.entrySet()) {
            String new_string = "Key: " + entry.getKey() + ", Value: " + entry.getValue();
            sym_table_content.add(new_string);
        }
        return sym_table_content;
    }

    @Override
    public void remove(K key) {
        dictionary.remove(key);
    }

    public Map<K, V> getContent() {
        return dictionary;
    }

    public void setContent(Map<K, V> content) {
        dictionary = content;
    }
    @Override
    public MyDictionary<K, V> cloneDictionary() {
        MyDictionary<K, V> newDictionary = new MyDictionary<>();
        newDictionary.dictionary.putAll(dictionary);
        return newDictionary;
    }
    public Set<Map.Entry<K, V>> entrySet() {
        return this.dictionary.entrySet();
    }
    @Override
    public boolean isEmpty() {
        return dictionary.isEmpty();
    }
}
