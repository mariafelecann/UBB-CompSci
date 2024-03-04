package repository;

import model.exception.MyException;
import model.program_state.ProgramState;
import model.stmt.IStmt;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.utilis.MyIList;
import model.utilis.MyIStack;
import model.value.StringValue;
import model.value.Value;

import java.io.*;
import java.util.ArrayList;
import java.util.List;


public class Repository implements IRepository{

    String logFilePath;
    public Repository(String l) {
        programStateList = new ArrayList<>();
        logFilePath = l;
    }
    List<ProgramState> programStateList;

    /*
    @Override
    public ProgramState getCurrentProgramState() {
        try {
            return programStateList.get(0);
        } catch (IndexOutOfBoundsException indexOutOfBoundsException) {
            return null;
        }
    }

     */

    @Override
    public String toString() {
        return "Repository{" +
                "programStateList=" + programStateList +
                '}';
    }

    @Override
    public void add(ProgramState programState) {
        programStateList.add(programState);
    }

    @Override
    public void savePrgStateinLOG(ProgramState prg) throws MyException, IOException {
        PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        logFile.println("");
        logFile.println(" -- program state -- ");
        logFile.println("");
        logFile.println("id : ");
        logFile.println(prg.getId());
        logFile.println();
        logFile.println();
        logFile.println("exe stack: ");
        MyIStack<IStmt> stack_copy = prg.getExeStack().copy();
        while(!stack_copy.isEmpty())
        {
            logFile.println(stack_copy.pop().toString());
        }
        logFile.println();
        logFile.println("sym table: ");
        MyIDictionary<String, Value> copy_sym = prg.getSymTable();
        List<String> sym_table_content = copy_sym.iterateDictionary();
        for(String item: sym_table_content)
        {
            logFile.println(item);
        }
        logFile.println();
        logFile.println("file table: ");
        MyIDictionary<StringValue, BufferedReader> copy = prg.getFileTable();
        List<String> file_table_content = copy.iterateDictionary();
        for(String item: sym_table_content)
        {
            logFile.println(item);
        }

        MyIHeap<Integer, Value> heap_copy =prg.getHeap();
        logFile.println();
        if(heap_copy!=null) {
            logFile.println("heap : ");
            List<String> heap_content = heap_copy.iterateHeap();
            for (String item : heap_content) {
                logFile.println(item);
            }
            logFile.println("out: ");
            MyIList<Value> out_copy = prg.getOut();
            List<Value> out_content = out_copy.iterate_list();
            for (Value item : out_content) {
                logFile.println(item.toString());
            }
        }
        logFile.println();
        logFile.flush();
        logFile.close();
    }

    @Override
    public List<ProgramState> getListOfProgramStates() {
        return programStateList;
    }

    @Override
    public void setProgramStateList(List<ProgramState> newList) {
        programStateList = newList;
    }
}
