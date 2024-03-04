package model.stmt;

import model.exception.MyException;
import model.exception.MyExceptionNotDeclared;
import model.exception.MyExceptionTypesDontMatch;
import model.expression.Exp;
import model.program_state.ProgramState;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIHeap;
import model.utilis.MyIStack;
import model.value.Value;

import java.util.Objects;

public class AssigmentStmt implements IStmt{

    String id;
    Exp expression;

    public AssigmentStmt(String v, Exp expres) {
        id = v;
        expression = expres;
    }

    @Override
    public String toString() {
        return "(" + id  +
                " = " + expression + ") \n";
    }

    @Override
    public ProgramState execute(ProgramState state) throws MyException {
        MyIStack<IStmt> exe_stack = state.getExeStack();
        MyIDictionary<String, Value> sym_table = state.getSymTable();
        MyIHeap<Integer, Value> heap_copy =state.getHeap();
        if(sym_table.isDefined(id))
        {
            Value val = expression.eval(sym_table, heap_copy);
            Type type_id = sym_table.lookUp(id).getType();
            if(Objects.equals(val.getType().toString(), type_id.toString()))
            {
                sym_table.update(id, val);
            }
            else
            {
                throw new MyExceptionTypesDontMatch("the types do not match!");}
        }
        else throw new MyExceptionNotDeclared("this variable was not declared!");
        return null;
    }
    @Override
    public MyIDictionary<String,Type> typecheck(MyIDictionary<String,Type> typeEnv) throws
            MyException{
        Type type_of_variable = typeEnv.lookUp(id);
        Type type_of_expression = expression.typecheck(typeEnv.cloneDictionary());
        if (type_of_variable.equals(type_of_expression))
            return typeEnv;
        else
            throw new MyException("Assignment: right hand side and left hand side have different types ");
    }
}
