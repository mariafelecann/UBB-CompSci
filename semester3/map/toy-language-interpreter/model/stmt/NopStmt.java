package model.stmt;

import model.exception.MyException;
import model.program_state.ProgramState;
import model.type.Type;
import model.utilis.MyIDictionary;

public class NopStmt implements IStmt{
    @Override
    public ProgramState execute(ProgramState state) throws MyException {
        //MyIStack<IStmt> stk = state.getExeStack();
        return null;
    }
    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        return typeEnv;
    }
}
