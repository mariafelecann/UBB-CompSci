package model.utilis;

import model.exception.MyException;
import javafx.util.Pair;

import java.util.HashMap;
import java.util.List;

public class MySemaphore implements MyISemaphore{
    private HashMap<Integer, Pair<Integer, List<Integer>>> table_of_semaphores;
    private int next_free_location = 0;

    public MySemaphore() {
        this.table_of_semaphores = new HashMap<>();
    }

    @Override
    public void put(int key, Pair<Integer, List<Integer>> value) throws MyException {
        synchronized (this) {
            if (!table_of_semaphores.containsKey(key)) {
                table_of_semaphores.put(key, value);
            } else {
                throw new MyException("this semaphore already exists");
            }
        }
    }

    @Override
    public HashMap<Integer, Pair<Integer, List<Integer>>> getTable_of_semaphores() {
        synchronized (this) {
            return table_of_semaphores;
        }
    }

    @Override
    public int get_free_addr() {
        synchronized (this) {
            next_free_location++;
            return next_free_location;
        }
    }

    @Override
    public Pair<Integer, List<Integer>> get(int key) throws MyException {
        synchronized (this) {
            if (table_of_semaphores.containsKey(key)) {
                return table_of_semaphores.get(key);
            } else {
                throw new MyException("this semaphore doesnt exist in the table");
            }
        }
    }
    @Override
    public void setTable_of_semaphores(HashMap<Integer, Pair<Integer, List<Integer>>> new_table_s) {
        synchronized (this) {
            this.table_of_semaphores = new_table_s;
        }
    }

    @Override
    public boolean containsKey(int key) {
        synchronized (this) {
            return table_of_semaphores.containsKey(key);
        }
    }

    @Override
    public void setFreeAddress(int freeaddr) {
        synchronized (this) {
            this.next_free_location = freeaddr;
        }
    }

    @Override
    public void update(int key, Pair<Integer, List<Integer>> value) throws MyException {
        synchronized (this) {
            if (table_of_semaphores.containsKey(key))
            {
                table_of_semaphores.replace(key, value);
            }
            else {
                throw new MyException("semaphore doesnt contain this key");
            }
        }
    }

    @Override
    public String toString() {
        return "MySemaphore{" +
                "semaphoreTable=" + table_of_semaphores +
                ", freeLocation=" + next_free_location +
                '}';
    }
}
