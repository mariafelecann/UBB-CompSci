package model.expression;

import model.exception.MyException;
import model.exception.MyLogicException;
import model.type.BoolType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.BoolValue;
import model.value.Value;

import java.util.Objects;

public class LogicExp implements Exp{

    Exp expression_1;
    Exp expression_2;
    int operation; //1 = or , 2 = and

    @Override
    public String toString() {
        return "logic (" +
                expression_1 +
                " " + operation +
                " " + expression_2 +
                ')';
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Integer, Value> h) throws MyException {
        Value first_value;
        Value second_value;
        first_value = expression_1.eval(tbl,h);
        if(Objects.equals(first_value.getType(), new BoolType()))
        {
            second_value = expression_2.eval(tbl,h);
            if(Objects.equals(second_value.getType(), new BoolType()))
            {
                BoolValue bool_1 = (BoolValue) first_value;
                BoolValue bool_2 = (BoolValue) second_value;

                boolean boolean_1, boolean_2;
                boolean_1 = ((BoolValue)first_value).getValue();
                boolean_2 = ((BoolValue) second_value).getValue();
                if(operation == 1)
                    return new BoolValue(boolean_1 || boolean_2);
                if(operation == 2)
                    return new BoolValue(boolean_1 && boolean_2);

            }
            else
                throw new MyLogicException("");

        }
        else
            throw new MyLogicException("");
        return new BoolValue(false);

    }
    @Override
    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException {
        Type typ1, typ2;
        typ1 = expression_1.typecheck(typeEnv);
        typ2 = expression_2.typecheck(typeEnv);
        if (typ1.equals(new BoolType())) {
            if (typ2.equals(new BoolType())) {
                return new BoolType();
            } else
                throw new MyException("second operand is not boolean");
        } else
            throw new MyException("first operand is not boolean");
    }
}
