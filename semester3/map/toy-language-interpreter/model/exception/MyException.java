package model.exception;

public class MyException extends Exception implements IMyException {
    public MyException(String message)
    {
        super(message);
    }

    @Override
    public void handleMyException()
    {
    }
}
