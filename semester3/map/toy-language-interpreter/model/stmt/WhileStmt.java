package model.stmt;

import model.exception.MyException;
import model.exception.MyExceptionTypesDontMatch;
import model.expression.Exp;
import model.program_state.ProgramState;
import model.type.BoolType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.utilis.MyIStack;
import model.value.BoolValue;
import model.value.Value;

import java.io.IOException;
import java.util.List;

public class WhileStmt implements IStmt{
    Exp expression;
    IStmt statement;
    public WhileStmt(Exp expres, IStmt given)
    {
        expression = expres;
        statement = given;
    }
    /*
    public WhileStmt(Exp expres, List<IStmt> stat)
    {
        expression = expres;
        statements = stat;
    }

     */
    /*
    @Override
    public ProgramState execute(ProgramState state) throws MyException, IOException {
        MyIDictionary<String, Value> symbol_table = state.getSymTable();
        MyIHeap<Integer, Value> heap = state.getHeap();
        Value exp_value = expression.eval(symbol_table, heap);
        if(!(exp_value instanceof BoolValue))
            throw new MyExceptionTypesDontMatch("expression needs to be Bool!");
        else
        {
            while (((BoolValue) expression.eval(symbol_table, heap)).getValue()) {
                for (IStmt statement : statements) {
                    statement.execute(state);
                }
            }
            return null;
        }

    }

     */

    public ProgramState execute(ProgramState state) throws MyException {
        MyIDictionary<String, Value> symTable= state.getSymTable();
        MyIHeap<Integer,Value> heap = state.getHeap();
        MyIStack<IStmt> exeStack= state.getExeStack();

        BoolValue bool= (BoolValue) expression.eval(symTable, heap);
        if (bool.getValue()){
            exeStack.push(this);
            exeStack.push(statement);
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        Type typexp=expression.typecheck(typeEnv);
        if (typexp.equals(new BoolType())) {

            statement.typecheck(typeEnv.cloneDictionary());

            return typeEnv;
        }
        else
            throw new MyException("the condition of WHILE has not the type bool");
    }

    @Override
    public String toString() {
        return "while (" +
                "exp: " + expression +
                ": statement=" + statement +
                ") \n";
    }
}
