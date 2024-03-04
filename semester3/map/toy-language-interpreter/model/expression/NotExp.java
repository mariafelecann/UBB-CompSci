package model.expression;

import model.exception.MyException;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.BoolValue;
import model.value.Value;

public class NotExp implements Exp{
    private final Exp expression;

    public NotExp(Exp expression) {
        this.expression = expression;
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return expression.typecheck(typeEnv);
    }

    @Override
    public Value eval(MyIDictionary<String, Value> table, MyIHeap<Integer, Value> heap) throws MyException {
        BoolValue value = (BoolValue) expression.eval(table, heap);
        if (!value.getValue())
            return new BoolValue(true);
        else
            return new BoolValue(false);
    }

    @Override
    public String toString() {
        return String.format("!(%s)", expression);
    }
}