package model.exception;

public class FullListException extends MyException{
    public FullListException(String message) {
        super("cannot add element into a full list!");
    }
}
