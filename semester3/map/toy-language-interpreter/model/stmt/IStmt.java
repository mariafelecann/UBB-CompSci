package model.stmt;

import model.exception.MyException;
import model.program_state.ProgramState;
import model.type.Type;
import model.utilis.MyIDictionary;

import java.io.IOException;

public interface IStmt {
    ProgramState execute(ProgramState state) throws MyException, IOException;
    MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException;
}