package model.expression;

import model.exception.MyException;
import model.exception.MyExceptionTypesDontMatch;
import model.exception.MyNotDefinedDictionaryException;
import model.type.RefType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.RefValue;
import model.value.Value;

public class ReadHeapExpression implements Exp{
    Exp expression;
    public ReadHeapExpression(Exp expres)
    {
        expression = expres;
    }
    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Integer,Value> heap) throws MyException {
        Value expression_value = expression.eval(tbl, heap);
        if(!(expression_value instanceof RefValue))
        {
            throw new MyExceptionTypesDontMatch("the expression value must be Ref");
        }
        else
        {
            RefValue value = (RefValue) expression_value;
            int address = value.get_address();
            if(!heap.isDefined(address))
                throw new MyNotDefinedDictionaryException("this key is not defined!");
            else {
                return heap.lookUp(address);
            }


        }
    }

    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        Type typ= expression.typecheck(typeEnv);
        if (typ instanceof RefType) {
            RefType reft =(RefType) typ;
            return reft.getInner();
        } else
            throw new MyException("the ReadHeap argument is not a Ref Type");
    }

    @Override
    public String toString() {
        return "ReadHeap (" +
                 expression +
                ')';
    }
}
