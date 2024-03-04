package model.stmt;


import model.exception.MyException;
import javafx.util.Pair;
import model.expression.Exp;
import model.program_state.ProgramState;
import model.type.IntType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.utilis.MyISemaphore;
import model.value.IntValue;
import model.value.Value;

import java.util.ArrayList;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class CreateSemaphoreStmt implements IStmt{
    private String variable;
    private Exp expression;
    private static final Lock lock = new ReentrantLock();

    public CreateSemaphoreStmt(String var, Exp expr) {
        this.variable = var;
        this.expression = expr;
    }
    @Override
    public ProgramState execute(ProgramState state) throws MyException {
        lock.lock();
        MyISemaphore semaphore = state.getSemaphoreTable();
        MyIHeap<Integer, Value> heap = state.getHeap();
        MyIDictionary<String, Value> symb = state.getSymTable();

        IntValue nr_expression = (IntValue) (expression.eval(symb, heap));
        int number_permits = nr_expression.getValue();
        int free_addr = semaphore.get_free_addr();
        semaphore.put(free_addr, new Pair<>(number_permits, new ArrayList<>()));

        if (symb.isDefined(variable) && symb.lookUp(variable).getType().equals(new IntType()))
            symb.update(variable, new IntValue(free_addr));
        else
            throw new MyException("variable of int type not defined");
        lock.unlock();
        return null;
    }


    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookUp(variable).equals(new IntType())) {
            if (expression.typecheck(typeEnv).equals(new IntType()))
                return typeEnv;
            else
                throw new MyException("expression is not int");
        } else {
            throw new MyException("variable needs to be int");
        }
    }

    @Override
    public String toString() {
        return "createSemaphoreStmt{" +
                "var='" + variable + '\'' +
                ", expression=" + expression +
                '}';
    }
}