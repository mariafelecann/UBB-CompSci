package model.utilis;

import java.util.List;
import java.util.Map;
import java.util.Set;

public interface MyIDictionary<K, V> {
    boolean isDefined(K key);

    void put(K key, V value);

    V lookUp(K key);

    void update(K key, V value);
    public List<String> iterateDictionary();
    void remove(K key);
    public void setContent(Map<K, V> content);
    public Map<K, V> getContent();
    public MyDictionary<K, V> cloneDictionary();
    public Set<Map.Entry<K, V>> entrySet();

    public boolean isEmpty();
}
