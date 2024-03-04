package model.stmt;

import model.exception.MyException;
import model.program_state.ProgramState;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIStack;

public class CompStmt implements IStmt {
    IStmt first;
    IStmt second;
    public CompStmt(IStmt f, IStmt s)
    {
        first = f;
        second = s;
    }

    @Override
    public ProgramState execute(ProgramState state) throws MyException
    {
        MyIStack<IStmt> stk = state.getExeStack();
        stk.push(second);
        stk.push(first);
        return null;
    }

    @Override
    public String toString() {
        return "CompStmt( " +
                " " + first.toString() +
                " " + second.toString()+" ";
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        return second.typecheck(first.typecheck(typeEnv.cloneDictionary()));
    }
}
