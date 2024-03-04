package model.stmt;

import model.exception.MyException;
import model.exception.MyExceptionTypesDontMatch;
import model.exception.MyNotDefinedDictionaryException;
import model.expression.Exp;
import model.program_state.ProgramState;
import model.type.RefType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.RefValue;
import model.value.Value;

import java.io.IOException;

public class New implements IStmt{
    String var_name;
    Exp expression;
    public New(String name, Exp exp)
    {
        var_name = name;
        expression = exp;
    }
    @Override
    public ProgramState execute(ProgramState state) throws MyException, IOException {
        MyIDictionary<String, Value> symtable = state.getSymTable();
        MyIHeap<Integer, Value> heap = state.getHeap();
        if(!symtable.isDefined(var_name))
            throw new MyNotDefinedDictionaryException("variable not defined");
        else
        {
            Value value_associated = symtable.lookUp(var_name);
            if(!(value_associated instanceof RefValue))
            {
                throw new MyExceptionTypesDontMatch("the value is not Ref!");
            }
            Value expression_value = expression.eval(symtable, heap);
            RefType type_associated = (RefType) value_associated.getType();
            Type expres_type;
            expres_type = ((RefType) value_associated.getType()).getInner();
            //System.out.println(expres_type);
            //System.out.println(type_associated.getInner());
            if(!(expres_type.equals(type_associated.getInner())))
            {
                throw new MyExceptionTypesDontMatch("the types dont match");
            }
            RefValue value_made_ref = (RefValue) value_associated;

            int current_address = heap.getLastAddress();
            current_address ++;

            RefType new_refType = new RefType(expression_value.getType());
            RefValue new_refValue = new RefValue(current_address, new_refType);

            symtable.update(var_name, new_refValue);
            heap.put(current_address, expression_value);
            heap.updateLastAddress(current_address);}

        return null;
    }

    @Override
    public MyIDictionary<String,Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        Type typevar = typeEnv.lookUp(var_name);
        Type typexp = expression.typecheck(typeEnv);
        if (typevar.equals(new RefType(typexp)))
            return typeEnv;
        else
            throw new MyException("NEW stmt: right hand side and left hand side have different types ");
    }

    @Override
    public String toString() {
        return "New (" +
                "" + var_name + '\'' +
                "= " + expression +
                ") \n";
    }
}
