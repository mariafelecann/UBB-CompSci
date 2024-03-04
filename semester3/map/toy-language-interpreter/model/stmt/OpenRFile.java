package model.stmt;

import model.exception.MyException;
import model.exception.MyExceptionTypesDontMatch;
import model.expression.Exp;
import model.program_state.ProgramState;
import model.type.StringType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Objects;

public class OpenRFile implements IStmt{
    Exp expression;
    public OpenRFile(Exp e)
    {
        expression = e;
    }
    /*
    @Override
    public ProgramState execute(ProgramState state) throws MyException, FileNotFoundException {
        MyIDictionary<String, Value> sym_t = state.getSymTable();
        Value exp_value = expression.eval(sym_t);
        if(!Objects.equals(exp_value.getType(), new StringType()))
            throw new MyExceptionTypesDontMatch("the type is not a string!");
        MyIDictionary<StringValue, BufferedReader> file_t = state.getFileTable();
        if(file_t.isDefined((StringValue) exp_value))
        {
            throw new MyException("file already opened!");
        }
        BufferedReader buff = new BufferedReader(new FileReader(((StringValue) exp_value).getValue()));
        file_t.put(new StringValue(((StringValue) exp_value).getValue()), buff);
        return state;
    }

     */
    @Override
    public ProgramState execute(ProgramState state) throws MyException, FileNotFoundException {
        MyIDictionary<String, Value> sym_t = state.getSymTable();
        MyIHeap<Integer, Value> heap_copy =state.getHeap();
        Value exp_value = expression.eval(sym_t, heap_copy);

        // Logging

        if (!Objects.equals(exp_value.getType(), new StringType())) {
            throw new MyExceptionTypesDontMatch("The type is not a string!");
        }

        MyIDictionary<StringValue, BufferedReader> file_t = state.getFileTable();

        if (file_t.isDefined((StringValue) exp_value)) {
            throw new MyException("File already opened!");
        }

        String fileName = ((StringValue) exp_value).getValue();

        System.out.println("opening file: " + fileName);

        BufferedReader buff = new BufferedReader(new FileReader(fileName));
        file_t.put((StringValue)exp_value, buff);

        System.out.println("file opened successfully!");

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        expression.typecheck(typeEnv);
        return typeEnv;
    }

    @Override
    public String toString() {
        return "OpenRFile(" +
                "" + expression +
                ") \n";
    }
}
