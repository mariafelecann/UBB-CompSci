package model.utilis;

import model.exception.MyException;
import javafx.util.Pair;
import model.stmt.IStmt;

import java.util.*;

public interface MyIProc {
    boolean isDefined(String key);
    void put(String key, Pair<List<String>, IStmt> value);
    Pair<List<String>, IStmt> lookUp(String key) throws MyException;
    void update(String key,  Pair<List<String>, IStmt> value) throws MyException;
    Collection< Pair<List<String>, IStmt>> values();
    void remove(String key) throws MyException;
    Set<String> keySet();
    HashMap<String,  Pair<List<String>, IStmt>> getContent();
    MyIDictionary<String, Pair<List<String>, IStmt>> deepCopy() throws MyException;
}