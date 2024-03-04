package model.exception;

public class MyNotDefinedDictionaryException extends MyException{
    public MyNotDefinedDictionaryException(String message) {
        super("key not defined in dictionary!");
    }
}
