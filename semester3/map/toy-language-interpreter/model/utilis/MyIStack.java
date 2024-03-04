package model.utilis;

import java.util.List;

public interface MyIStack<T> {
        void push(T elem);
        T pop();
        boolean isEmpty();
        List<T> getReverse();
        public MyStack<T> copy();
        public MyStack<T> cloneStack();
}