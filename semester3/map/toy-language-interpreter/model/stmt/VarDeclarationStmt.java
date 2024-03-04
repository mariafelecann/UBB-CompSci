package model.stmt;

import model.exception.MyException;
import model.program_state.ProgramState;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.value.Value;

public class VarDeclarationStmt implements IStmt{
    String name;
    Type type_of_variable;
    public VarDeclarationStmt(String n, Type t)
    {
        name = n;
        type_of_variable = t;
    }
    @Override
    public ProgramState execute(ProgramState state) throws MyException {
        MyIDictionary<String, Value> sym_table = state.getSymTable();
        if(sym_table.isDefined(name))
            throw new MyException("this variable is already declared! ");
        else
        {
            //Value val = null;
            Value value_of_val = type_of_variable.defaultValue();
            sym_table.update(name, value_of_val);
            /*
            if(Objects.equals(type_of_variable, new IntType()))
            {
                Value value_of_var = new IntValue(0);
                sym_table.update(name, value_of_var);
            }
            else
            {
                if(Objects.equals(type_of_variable, new BoolType()))
                {
                    Value value_of_var = new BoolValue(false);
                    sym_table.update(name, value_of_var);
                }
            }
             */
        }
        return null;
    }

    @Override
    public MyIDictionary<String,Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        typeEnv.put(name,type_of_variable);
        return typeEnv;
    }


    @Override
    public String toString() {
        return "(" + type_of_variable.toString() + " "  +  name + ") \n";
    }
}
