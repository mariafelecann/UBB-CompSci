package model.program_state;
import model.exception.MyException;
import model.stmt.IStmt;
import model.type.Type;
import model.utilis.*;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class ProgramState {

    private final int id;
    private static int nextAvailableId = 1;
    MyIStack<IStmt> exeStack;
    MyIDictionary<String, Value> symTable;
    MyIList<Value> out;
    MyIDictionary<StringValue, BufferedReader> fileTable;
    IStmt originalProgram;
    MyIHeap<Integer, Value> heap;
    MyISemaphore semaphoreTable;
    MyIDictionary<String, Type> typeEnvironment;

    public int getId()
    {
        return id;
    }

    private static synchronized int getNextId()
    {
        return nextAvailableId++;
    }

    public void setSemaphoreTable(MyISemaphore newSemaphoreTable) {
        this.semaphoreTable = newSemaphoreTable;
    }
    public MyISemaphore getSemaphoreTable() {
        return semaphoreTable;
    }

    public MyIStack<IStmt> getExeStack() {
        return exeStack;
    }

    public void setExeStack(MyIStack<IStmt> exeStack) {
        this.exeStack = exeStack;
    }

    public MyIDictionary<String, Value> getSymTable() {
        return symTable;
    }

    public MyIDictionary<StringValue, BufferedReader> getFileTable() {
        return fileTable;
    }

    public void setSymTable(MyIDictionary<String, Value> symTable) {
        this.symTable = symTable;
    }

    public MyIList<Value> getOut() {
        return out;
    }

    public MyIHeap<Integer, Value> getHeap() {
        return heap;
    }

    public void setOut(MyIList<Value> out) {
        this.out = out;
    }

    public IStmt getOriginalProgram() {
        return originalProgram;
    }

    public void setOriginalProgram(IStmt originalProgram) {
        this.originalProgram = originalProgram;
    }

    /*
    public ProgramState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value>
            ot, IStmt prg, MyIDictionary<StringValue, BufferedReader> ft, MyIHeap<Integer, Value> h) {
        exeStack = stk;
        symTable = symtbl;
        out = ot;
        fileTable = ft;
        heap = h;
        id = getNextId();
        //originalProgram=deepCopy(prg);//recreate the entire original prg
        stk.push(prg);
    }

     */
    public MyIDictionary<String, Type> getTypeEnvironment()
    {
        return typeEnvironment;
    }


    public ProgramState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value>
            ot, IStmt prg, MyIDictionary<StringValue, BufferedReader> ft, MyIHeap<Integer, Value> h, MyIDictionary<String, Type> typeEnv) {
        exeStack = stk;
        symTable = symtbl;
        out = ot;
        fileTable = ft;
        heap = h;
        typeEnvironment = typeEnv;
        id = getNextId();
        //originalProgram=deepCopy(prg);//recreate the entire original prg
        stk.push(prg);
    }

    public ProgramState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value>
            ot, IStmt prg, MyIDictionary<StringValue, BufferedReader> ft, MyIHeap<Integer, Value> h, MyIDictionary<String, Type> typeEnv, MyISemaphore sem) {
        exeStack = stk;
        symTable = symtbl;
        out = ot;
        fileTable = ft;
        heap = h;
        typeEnvironment = typeEnv;
        semaphoreTable = sem;
        id = getNextId();
        //originalProgram=deepCopy(prg);//recreate the entire original prg
        stk.push(prg);
    }


    @Override
    public String toString() {
        return "program state: " +
                "id -> " + id + '\n' +
                "exeStack = " + exeStack.toString() + '\n' +
                "symTable = " + symTable.toString() + '\n' +
                "fileTable = " + fileTable.toString() + '\n' +
                "heap = " + heap.toString() + '\n' +
                "out = " + out.toString() + '\n' +
                "typeEnv = " + typeEnvironment.toString() +
                '\n';
    }

    public Map<Integer,Value> unsafeGarbageCollector(List<Integer> symTableAddr, List<Integer> heapAddr, Map<Integer, Value> heap){
        return heap.entrySet().stream()
                .filter(e->symTableAddr.contains(e.getKey())||heapAddr.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));}


    public boolean isNotCompleted()
    {
        return !exeStack.isEmpty();
    }




    public ProgramState oneStep() throws MyException, IOException {
        if(exeStack.isEmpty())
            throw new MyException("program state:  stack is empty");
        IStmt crtStmt = exeStack.pop();
        MyIDictionary<String, Type> typeEnv = crtStmt.typecheck(typeEnvironment);
        return crtStmt.execute(this);
    }

}