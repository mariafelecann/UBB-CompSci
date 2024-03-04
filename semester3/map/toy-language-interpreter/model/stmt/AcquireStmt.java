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

public class AcquireStmt implements IStmt{
    private String semaphore_name;
    private static final Lock lock = new ReentrantLock();

    public AcquireStmt(String var) {
        this.semaphore_name = var;
    }

    @Override
    public ProgramState execute(ProgramState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symb_table = state.getSymTable();
        MyISemaphore semaphore_table = state.getSemaphoreTable();

        if (symb_table.isDefined(semaphore_name)) {

            if (symb_table.lookUp(semaphore_name).getType().equals(new IntType())){

                IntValue int_val = (IntValue) symb_table.lookUp(semaphore_name);
                int foundIndex = int_val.getValue();

                if (semaphore_table.getTable_of_semaphores().containsKey(foundIndex)) {
                    Pair<Integer, List<Integer>> found_semaphore = semaphore_table.get(foundIndex);
                    int NL = found_semaphore.getValue().size();
                    int N1 = found_semaphore.getKey();
                    if (N1 > NL) {
                        if (!found_semaphore.getValue().contains(state.getId())) {
                            found_semaphore.getValue().add(state.getId());
                            semaphore_table.update(foundIndex, new Pair<>(N1, found_semaphore.getValue()));
                        }
                    } else {
                        state.getExeStack().push(this);
                    }
                } else {
                    throw new MyException("index is not a key in the semaphore");
                }
            } else {
                throw new MyException("index must be int");
            }
        } else {
            throw new MyException("index not found");
        }
        lock.unlock();
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookUp(semaphore_name).equals(new IntType())) {
            return typeEnv;
        } else {
            throw new MyException("variable is not int");
        }
    }

    @Override
    public String toString() {
        return "AcquireStmt{" +
                "var='" + semaphore_name + '\'' +
                '}';
    }
}
