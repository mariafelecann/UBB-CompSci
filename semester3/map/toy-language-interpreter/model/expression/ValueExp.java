package model.expression;

import model.exception.MyException;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.Value;

public class ValueExp implements Exp{
    Value e;
    public ValueExp(Value v)
    {
        e = v;
    }
    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Integer,Value> h) throws MyException {
        return e;
    }
    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException{
        return e.getType();
    }

    @Override
    public String toString() {
        return "value " +
                 e +
                ' ';
    }
}
