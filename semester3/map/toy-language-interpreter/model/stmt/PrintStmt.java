package model.stmt;

import model.exception.MyException;
import model.expression.Exp;
import model.program_state.ProgramState;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIList;
import model.value.Value;

public class PrintStmt implements IStmt {
    Exp expression;

    public PrintStmt(Exp e)
    {
        expression = e;
    }

    @Override
    public ProgramState execute(ProgramState state) throws MyException
    {
        MyIList<Value> out_list = state.getOut();
        out_list.add(expression.eval(state.getSymTable(), state.getHeap()));
        return null;
    }

    @Override
    public String toString() {
        return "Print( " + expression + ") \n";
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        expression.typecheck(typeEnv.cloneDictionary());
        return typeEnv;
    }
}
