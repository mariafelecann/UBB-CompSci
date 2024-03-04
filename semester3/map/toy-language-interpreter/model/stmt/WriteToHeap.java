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

public class WriteToHeap implements IStmt{
    String variable_name;
    Exp expression;
    public WriteToHeap(String name, Exp given_expression)
    {
        variable_name = name;
        expression = given_expression;
    }
    @Override
    public ProgramState execute(ProgramState state) throws MyException, IOException {
        MyIDictionary<String, Value> symbol_table = state.getSymTable();
        MyIHeap<Integer, Value> heap = state.getHeap();
        if(!symbol_table.isDefined(variable_name))
            throw new MyNotDefinedDictionaryException("variable ot defined!");
        else
        {
            Value var_value = symbol_table.lookUp(variable_name);
            if(!(var_value.getType() instanceof RefType)){
                throw new MyExceptionTypesDontMatch("the type needs to be Ref");}
            else {
                RefValue r =(RefValue) var_value;
                int address = r.get_address();
                if (!heap.isDefined(address)) {
                    throw new MyNotDefinedDictionaryException("not defined in heap!");

                } else {
                    Value exp_value = expression.eval(symbol_table,heap);
                    heap.update(address, exp_value);

                }
            }
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        Type varType = typeEnv.lookUp(variable_name);
        if (varType == null) {
            throw new MyException("variable not defined!");
        }
        if (!(varType instanceof RefType)) {
            throw new MyExceptionTypesDontMatch("variable must have RefType!");
        }

        RefType refType = (RefType) varType;

        Type expType = expression.typecheck(typeEnv);

        if (!expType.equals(refType.getInner())) {
            throw new MyExceptionTypesDontMatch("expression type does not match the pointed type in heap!");
        }

        return typeEnv;
    }

    @Override
    public String toString() {
        return "WriteToHeap(" +
                "variable='" + variable_name + '\'' +
                " value=" + expression +
                ") \n";
    }
}
