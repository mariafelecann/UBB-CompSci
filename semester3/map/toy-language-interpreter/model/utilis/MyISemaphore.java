package model.utilis;


import model.exception.MyException;
import javafx.util.Pair;

import java.util.HashMap;
import java.util.List;

public interface MyISemaphore {
    void put(int key, Pair<Integer, List<Integer>> value) throws MyException;
    Pair<Integer, List<Integer>> get(int key) throws MyException;
    boolean containsKey(int key);
    int get_free_addr();
    void setFreeAddress(int freeAddress);
    void update(int key, Pair<Integer, List<Integer>> value) throws MyException;
    HashMap<Integer, Pair<Integer, List<Integer>>> getTable_of_semaphores();
    void setTable_of_semaphores(HashMap<Integer, Pair<Integer, List<Integer>>> newSemaphoreTable);
}