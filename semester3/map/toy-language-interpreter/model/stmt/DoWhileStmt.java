package model.stmt;


import model.exception.MyException;
import model.expression.Exp;
import model.program_state.ProgramState;
import model.type.BoolType;
import model.type.Type;
import model.utilis.MyIDictionary;

public class DoWhileStmt implements IStmt{
    private final IStmt statement;
    private final Exp expression;

    public DoWhileStmt(Exp expression, IStmt statement) {
        this.statement = statement;
        this.expression = expression;
    }
    @Override
    public ProgramState execute(ProgramState state) throws MyException {
        IStmt converted = new CompStmt(statement, new WhileStmt(expression, statement));
        state.getExeStack().push(converted);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeExpression = expression.typecheck(typeEnv);
        if (typeExpression.equals(new BoolType())) {
            statement.typecheck(typeEnv.cloneDictionary());
            return typeEnv;
        } else
            throw new MyException("Condition in the do while statement must be bool!");
    }

    @Override
    public String toString() {
        return "DoWhileStmt{" +
                "statement=" + statement +
                ", expression=" + expression +
                '}';
    }
}