package model.exception;

public class MyFullStackException extends MyException{

    public MyFullStackException(String message) {
        super("cannot push element into full stack!");
    }
}
