package model.exception;

public class MyArithmeticException extends MyException{
    public MyArithmeticException(String message) {
        super("operand not defined correctly!");
    }
}
