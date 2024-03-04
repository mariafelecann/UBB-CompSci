package model.stmt;


import model.exception.MyException;
import model.expression.Exp;
import model.expression.RelationEnum;
import model.expression.RelationalExp;
import model.program_state.ProgramState;
import model.type.Type;
import model.utilis.MyIDictionary;
import model.utilis.MyIStack;

public class SwitchStmt implements IStmt{
    private final Exp main_expression;
    private final Exp exp1;
    private final IStmt statement1;
    private final Exp exp2;
    private final IStmt statement2;
    private final IStmt default_statement;

    public SwitchStmt(Exp me, Exp e1, IStmt s1, Exp e2, IStmt s2, IStmt ds) {
        this.main_expression = me;
        this.exp1 = e1;
        this.statement1 = s1;
        this.exp2 = e2;
        this.statement2 = s2;
        this.default_statement = ds;
    }
    @Override
    public ProgramState execute(ProgramState state) throws MyException {
        MyIStack<IStmt> exe_stack = state.getExeStack();
        IStmt switch_statement = new IfStmt(new RelationalExp(main_expression,RelationEnum.EQUAL, exp1), statement1, new IfStmt(new RelationalExp(main_expression,RelationEnum.EQUAL, exp2), statement2, default_statement));
        exe_stack.push(switch_statement);
        state.setExeStack(exe_stack);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type main_expType = main_expression.typecheck(typeEnv);
        Type type1 = exp1.typecheck(typeEnv);
        Type type2 = exp2.typecheck(typeEnv);
        if (main_expType.equals(type1) && main_expType.equals(type2)) {
            statement1.typecheck(typeEnv.cloneDictionary());
            statement2.typecheck(typeEnv.cloneDictionary());
            default_statement.typecheck(typeEnv.cloneDictionary());
            return typeEnv;
        } else
        {
            throw new MyException("the expression types don't match in switch");
        }
    }

    @Override
    public String toString() {
        return "SwitchStmt{" +
                "mainExpression=" + main_expression +
                ", expression1=" + exp1 +
                ", statement1=" + statement1 +
                ", expression2=" + exp2 +
                ", statement2=" + statement2 +
                ", defaultStatement=" + default_statement +
                '}';
    }
}