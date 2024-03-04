package model.stmt;

import model.exception.MyException;
import model.exception.MyLogicException;
import model.expression.Exp;
import model.program_state.ProgramState;
import model.type.BoolType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.utilis.MyIStack;
import model.value.BoolValue;
import model.value.Value;

import java.util.Objects;

public class IfStmt implements IStmt{
    Exp exp;
    IStmt thenS;
    IStmt elseS;
    public IfStmt(Exp e, IStmt t, IStmt el) {exp=e; thenS=t; elseS=el;}

    @Override
    public String toString()
    {
        return " (if ("+ exp.toString()+") then (" +thenS.toString()+") else (" + elseS.toString() + ") ) \n";
    }

    @Override
    public ProgramState execute(ProgramState state) throws MyException {
        MyIDictionary<String, Value> my_sym_table = state.getSymTable();
        MyIHeap<Integer, Value> heap_copy =state.getHeap();
        Value condition = exp.eval(my_sym_table, heap_copy);
        MyIStack<IStmt> exe_stack = state.getExeStack();
        if(!Objects.equals(condition.getType(), new BoolType()))
            throw new MyLogicException("the type of the condition s not boolean!");
        else
        {
            BoolValue cond = (BoolValue) condition;
            if(cond.getValue())
            {
                exe_stack.push(thenS);
            }
            else
                exe_stack.push(elseS);
        }
        return null;
    }

    @Override
    public MyIDictionary<String,Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        Type typexp=exp.typecheck(typeEnv);
        if (typexp.equals(new BoolType())) {
            thenS.typecheck(typeEnv.cloneDictionary());
            elseS.typecheck(typeEnv.cloneDictionary());
            return typeEnv;
        }
        else
            throw new MyException("The condition of IF has not the type bool");
    }
}
