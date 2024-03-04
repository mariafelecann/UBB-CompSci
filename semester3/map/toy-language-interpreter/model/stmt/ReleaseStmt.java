package model.stmt;


import model.exception.MyException;
import javafx.util.Pair;
import model.program_state.ProgramState;
import model.type.IntType;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyISemaphore;
import model.value.IntValue;
import model.value.Value;

import java.util.List;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ReleaseStmt implements IStmt{
    private final String var;
    private static final Lock lock = new ReentrantLock();

    public ReleaseStmt(String var) {
        this.var = var;
    }


    @Override
    public ProgramState execute(ProgramState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symb = state.getSymTable();
        MyISemaphore semaphore_table = state.getSemaphoreTable();
        if (symb.isDefined(var)) {
            if (symb.lookUp(var).getType().equals(new IntType())) {
                IntValue index_val = (IntValue) symb.lookUp(var);
                int foundIndex = index_val.getValue();
                if (semaphore_table.getTable_of_semaphores().containsKey(foundIndex)) {
                    Pair<Integer, List<Integer>> foundSemaphore = semaphore_table.get(foundIndex);
                    if (foundSemaphore.getValue().contains(state.getId()))
                        foundSemaphore.getValue().remove((Integer) state.getId());
                    semaphore_table.update(foundIndex, new Pair<>(foundSemaphore.getKey(), foundSemaphore.getValue()));
                } else {
                    throw new MyException("index not in semaphore table");
                }
            } else {
                throw new MyException("index must be int");
            }
        } else {
            throw new MyException("index not in symbol table");
        }
        lock.unlock();
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookUp(var).equals(new IntType())) {
            return typeEnv;
        } else {
            throw new MyException("var type must be int");
        }
    }

    @Override
    public String toString() {
        return "ReleaseStmt{" +
                "var='" + var + '\'' +
                '}';
    }
}
