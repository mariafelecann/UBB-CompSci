package model.stmt;

import model.exception.MyException;
import model.program_state.ProgramState;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIStack;
import model.utilis.MyStack;
import model.value.Value;

import java.io.IOException;

public class ForkStatement implements IStmt{
    private IStmt statement;
    public ForkStatement(IStmt new_statement)
    {
        statement = new_statement;
    }
    @Override
    public ProgramState execute(ProgramState state) throws MyException, IOException {
        MyIDictionary<String, Value> clone_symtable = state.getSymTable().cloneDictionary();
        MyIStack<IStmt> new_stack = new MyStack<>();
        ProgramState newState = new ProgramState(
                new_stack,
                clone_symtable,
                state.getOut(),
                statement,
                state.getFileTable(),
                state.getHeap(),
                state.getTypeEnvironment(),
                state.getSemaphoreTable()
        );
        //return new ProgramState(newStack, newSymTable, state.getOut(), state.getFileTable(), state.getHeap(), state.getToySemaphoreTable());
        return newState;
    }
    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        return statement.typecheck(typeEnv.cloneDictionary());
    }

    @Override
    public String toString() {
        return "Fork (" +
                 statement +
                ") \n";
    }
}
