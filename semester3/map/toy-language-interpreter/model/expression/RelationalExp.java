package model.expression;

import model.exception.MyException;
import model.type.BoolType;
import model.type.IntType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.Value;

public class RelationalExp implements Exp{
    RelationEnum relation;
    Exp e1;
    Exp e2;
    public RelationalExp(Exp expr1, RelationEnum rel, Exp expr2){
        e1=expr1;
        e2=expr2;
        relation=rel;
    }

    @Override
    public String toString() {
        return e1.toString()+" "+relation+" "+e2.toString();
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Integer, Value> h) throws MyException {
        Value v1 = e1.eval(tbl,h);
        Value v2 = e2.eval(tbl,h);
        int n1, n2;
        if (v1.getType().equals(new IntType())) {
            if (v2.getType().equals(new IntType())) {
                n1 = ((IntValue) v1).getValue();
                n2 = ((IntValue) v2).getValue();
            } else if (v2 instanceof IntValue) {
                n1 = ((IntValue) v1).getValue();
                n2 = ((IntValue) v2).getValue();
            } else {
                throw new MyException("Second operand is not an int");
            }
        } else if (v1 instanceof IntValue) {
            if (v2.getType().equals(new IntType())) {
                n1 = ((IntValue) v1).getValue();
                n2 = ((IntValue) v2).getValue();
            } else if (v2 instanceof IntValue) {
                n1 = ((IntValue) v1).getValue();
                n2 = ((IntValue) v2).getValue();
            } else {
                throw new MyException("Second operand is not an int");
            }
        } else {
            throw new MyException("First operand is not an int");
        }
        switch (relation) {
            case EQUAL:
                return new BoolValue(n1==n2);
            case LESS_THAN:
                return new BoolValue(n1<n2);
            case GREATER_THAN:
                return new BoolValue(n1>n2);
            case LESS_OR_EQUAL:
                return new BoolValue(n1<=n2);
            case GREATER_OR_EQUAL:
                return new BoolValue(n1>=n2);
            case NOT_EQUAL:
                return new BoolValue(n1!=n2);
            default:
                throw new MyException("Relation isn't valid");

        }
    }

    @Override
    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException {
        Type typ1, typ2;
        typ1 = e1.typecheck(typeEnv);
        typ2 = e2.typecheck(typeEnv);
        if (typ1.equals(new IntType())) {
            if (typ2.equals(new IntType())) {
                return new BoolType();
            } else
                throw new MyException("second operand is not an integer");
        } else
            throw new MyException("first operand is not an integer");
    }

}
