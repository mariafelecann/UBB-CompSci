package model.expression;

import model.exception.MyException;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.Value;

public class VarExp implements Exp{
    String id;

    public VarExp(String v) {
        id = v;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Integer,Value> h) throws MyException {
        return tbl.lookUp(id);
    }

    @Override
    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        return typeEnv.lookUp(id);
    }

    @Override
    public String toString() {
        return " var " +
                id +
                ' ';
    }
}
