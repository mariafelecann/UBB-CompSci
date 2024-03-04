package model.expression;

import model.exception.MyException;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.Value;
public interface Exp {
    Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Integer, Value> heap) throws MyException;
    Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException;
}
