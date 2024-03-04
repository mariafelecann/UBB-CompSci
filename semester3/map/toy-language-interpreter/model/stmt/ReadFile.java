package model.stmt;

import model.exception.MyException;
import model.exception.MyExceptionNotDeclared;
import model.exception.MyExceptionTypesDontMatch;
import model.expression.Exp;
import model.program_state.ProgramState;
import model.type.IntType;
import model.type.StringType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Objects;

public class ReadFile implements IStmt{
    Exp expression;
    String variable_name;
    public ReadFile(Exp exp, String s)
    {
        expression = exp;
        variable_name = s;
    }
    @Override
    public ProgramState execute(ProgramState state) throws MyException, IOException {
        MyIDictionary<String, Value> sym_table = state.getSymTable();
        MyIDictionary<StringValue, BufferedReader> fileTable = state.getFileTable();
        MyIHeap<Integer, Value> heap_copy =state.getHeap();
        if(!(sym_table.isDefined(variable_name)))
            throw new MyExceptionNotDeclared("this variable is not defined!");
        if(!Objects.equals(sym_table.lookUp(variable_name).getType(), new IntType()))
        {
            throw new MyExceptionTypesDontMatch("the variable needs to be an int value!");
        }
        Value expression_value = expression.eval(sym_table, heap_copy);
        if(!Objects.equals(expression_value.getType(), new StringType()))
        {
            throw new MyExceptionTypesDontMatch("the name of the file needs to be  string!");
        }

        if(fileTable.isDefined((StringValue) expression_value))
        {
            BufferedReader buffer = fileTable.lookUp((StringValue)expression_value);
                String line = buffer.readLine();
                int value;
                if (line == null)
                    value = 0;
                else {
                    value = Integer.parseInt(line);
                }
                sym_table.update(variable_name, new IntValue(value));
        }
        else throw new MyExceptionNotDeclared("this file does not have a buffer associated!");


        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        Type type_of_variable = typeEnv.lookUp(variable_name);
        Type type_of_expression = expression.typecheck(typeEnv);
        if (Objects.equals(type_of_variable, new IntType()))
        {
            if(Objects.equals(type_of_expression, new StringType()))
                return typeEnv;
            else
                throw new MyException("the file expression needs to be a string!");
        }
        else
            throw new MyException("the file variable needs to be an int value!");
    }

    @Override
    public String toString() {
        return "ReadFile (" +
                "" + expression +
                " var:" + variable_name + '\'' +
                ")\n";
    }
}
