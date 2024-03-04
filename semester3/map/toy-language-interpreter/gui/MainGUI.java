package gui;

import model.expression.*;
import model.stmt.*;
import model.type.BoolType;
import model.type.IntType;
import model.type.RefType;
import model.type.Type;
import model.utilis.MyDictionary;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.StringValue;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Pos;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.effect.DropShadow;
import javafx.scene.layout.Background;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Arrays;

public class MainGUI extends Application {
    private ListView<String> list;
    ProgramController guiController;

    public MainGUI() {

    }
    private Button runButton;

    @Override
    public void start(Stage stage) throws IOException {
        this.list = new ListView();
        ObservableList<String> items = FXCollections.observableArrayList();
        IStmt[] list_of_examples = this.getListOfExamples();
        int lenght_examples = list_of_examples.length;

        for(int counter = 0; counter < lenght_examples; ++counter) {
            IStmt stmt = list_of_examples[counter];
            items.add(stmt.toString());
        }

        this.list.setItems(items);
        Label lbl = new Label("Examples List");
        lbl.setFont(Font.font("Times New Roman", FontWeight.BOLD, 27));
        lbl.setTextFill(Color.WHITE);
        lbl.setAlignment(Pos.TOP_CENTER);

        DropShadow dropShadow = new DropShadow();
        dropShadow.setColor(Color.BLACK);
        dropShadow.setRadius(1);
        dropShadow.setOffsetX(0.5);
        dropShadow.setOffsetY(0.5);
        lbl.setEffect(dropShadow);

        this.runButton = new Button("Run Statement");

        Font customFont = Font.font("Times New Roman", 20);

        runButton.setStyle("-fx-background-color: #0a3986; -fx-text-fill: #d0d0d9;");

        runButton.setFont(customFont);

        this.runButton.setOnAction((event) -> {
            String selectedExample = (String)this.list.getSelectionModel().getSelectedItem();
            Integer itemNr = this.list.getSelectionModel().getSelectedIndex();
            if (selectedExample != null) {
                this.guiController = new ProgramController(itemNr, this);
                this.guiController.allSteps();
            } else {
                System.out.println("No example selected.");
            }

        });
        VBox vbox = new VBox(new Node[]{lbl, this.list, this.runButton});
        vbox.setBackground(Background.fill(Color.LIGHTBLUE));
        vbox.setAlignment(Pos.CENTER);
        Scene scene = new Scene(vbox, 700.0, 600.0, Color.GRAY);
        stage.setTitle("Main Page");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(new String[0]);
    }

    public IStmt[] getListOfExamples() {
        IStmt[] statements = new IStmt[0];
        IStmt ex1= new CompStmt(new VarDeclarationStmt("v",new IntType()),
                new CompStmt(new AssigmentStmt("v",new ValueExp(new IntValue(2))), new PrintStmt(new
                        VarExp("v"))));

        try {
            ex1.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[]) Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex1;
            statements = new_statements;
        } catch (Exception var16) {
            System.out.println(var16.getMessage());
        }

        IStmt ex2 = new CompStmt( new VarDeclarationStmt("a",new IntType()),
                new CompStmt(new VarDeclarationStmt("b",new IntType()),
                        new CompStmt(new AssigmentStmt("a", new ArithExp(1,new ValueExp(new IntValue(2)),new
                                ArithExp(3, new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))) )),
                                new CompStmt(new AssigmentStmt("b",new ArithExp(1,new VarExp("a"), new ValueExp(new
                                        IntValue(1)))), new PrintStmt(new VarExp("b"))))));

        try {
            ex2.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex2;
            statements = new_statements;
        } catch (Exception var15) {
            System.out.println(var15.getMessage());
        }

        IStmt ex3 = new CompStmt(new VarDeclarationStmt("a",new BoolType()),
                new CompStmt(new VarDeclarationStmt("v", new IntType()),
                        new CompStmt(new AssigmentStmt("a", new ValueExp(new BoolValue(false))),
                                new CompStmt(new IfStmt(new VarExp("a"),new AssigmentStmt("v",new ValueExp(new
                                        IntValue(2))), new AssigmentStmt("v", new ValueExp(new IntValue(3)))), new PrintStmt(new VarExp("v"))))));

        try {
            ex3.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex3;
            statements = new_statements;
        } catch (Exception var14) {
            System.out.println(var14.getMessage());
        }

        String varf;
        varf="C:\\Users\\Maria\\Documents\\AAA\\test.txt\\";
        ValueExp e = new ValueExp(new StringValue(varf));

        IStmt ex4 = new CompStmt(new CompStmt(new CompStmt(new CompStmt(                 new CompStmt(
                new OpenRFile(e),
                new VarDeclarationStmt("varc", new IntType())
        ),
                new ReadFile(e, "varc")
        ),
                new ReadFile(e, "varc")
        ),
                new PrintStmt(new VarExp("varc"))
        ),
                new CloseRFile(e)
        );

        try {
            ex4.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex4;
            statements = new_statements;
        } catch (Exception var13) {
            System.out.println(var13.getMessage());
        }

        IStmt ex5  = new CompStmt(
                new VarDeclarationStmt("v", new RefType(new IntType())),
                // Ref int v; new(v, 20);
                new CompStmt(
                        new New("v", new ValueExp(new IntValue(20)))
                        , new CompStmt(
                        // print(rH(v));
                        new PrintStmt(new ReadHeapExpression(new VarExp("v"))),
                        new CompStmt(
                                // wH(v, 30);
                                new WriteToHeap("v", new ValueExp(new IntValue(30))),
                                // print(rH(v) + 5);
                                new PrintStmt(new ArithExp(
                                        1,
                                        new ReadHeapExpression(new VarExp("v")),
                                        new ValueExp(new IntValue(5))
                                ))
                        ))));

        try {
            ex5.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex5;
            statements = new_statements;
        } catch (Exception var12) {
            System.out.println(var12.getMessage());
        }
        IStmt ex6 = new CompStmt(
                new VarDeclarationStmt("v", new RefType(new IntType())),
                new CompStmt(
                        new VarDeclarationStmt("a", new RefType(new RefType(new IntType()))),
                        new CompStmt(
                                new New("v", new ValueExp(new IntValue(20))),
                                new CompStmt(
                                        new New("a", new VarExp("v")),
                                        new CompStmt(
                                                new PrintStmt(new ReadHeapExpression(new VarExp("v"))),
                                                new PrintStmt(new ArithExp(
                                                        1,
                                                        new ReadHeapExpression(new ReadHeapExpression(new VarExp("a"))),
                                                        new ValueExp(new IntValue(5))
                                                ))
                                        )
                                )
                        )
                )
        );
        try {
            ex6.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex6;
            statements = new_statements;
        } catch (Exception var11) {
            System.out.println(var11.getMessage());
        }
        ///ex with While statement: int v; v=4; (while (v>0) print(v);v=v-1);print(v)
        IStmt ex7 = new CompStmt(
                new VarDeclarationStmt("v", new IntType()),
                new CompStmt(
                        new AssigmentStmt("v", new ValueExp(new IntValue(4))),
                        new CompStmt(
                                new WhileStmt(
                                        new RelationalExp(new VarExp("v"), RelationEnum.GREATER_THAN, new ValueExp(new IntValue(0))),
                                        new CompStmt(
                                                new PrintStmt(new VarExp("v")),
                                                new AssigmentStmt("v", new ArithExp(2, new VarExp("v"), new ValueExp(new IntValue(1))))
                                        )
                                ), new PrintStmt(new VarExp("v"))
                        )
                )
        );
        try {
            ex7.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex7;
            statements = new_statements;
        } catch (Exception var10) {
            System.out.println(var10.getMessage());
        }
        ///ex 8: for garbage collector

        IStmt ex8 =
                // Ref int v; new(v, 20);
                new CompStmt(
                        new VarDeclarationStmt("v", new RefType(new IntType())),
                        new CompStmt(
                                new New("v", new ValueExp(new IntValue(20))),

                                // Ref Ref int a; new(a, v);
                                new CompStmt(
                                        new VarDeclarationStmt("a", new RefType(new RefType(new IntType()))),
                                        new CompStmt(
                                                new New("a", new VarExp("v")),
                                                // new(v, 30); print(rH(rH(a)));
                                                new CompStmt(
                                                        new New("v", new ValueExp(new IntValue(30))),
                                                        new PrintStmt(new ReadHeapExpression(new ReadHeapExpression(new VarExp("a"))))
                                                )))));

        try {
            ex8.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex8;
            statements = new_statements;
        } catch (Exception var17) {
            System.out.println(var17.getMessage());
        }

        ///statement 9 : fork
        /// int v; Ref int a; v=10;new(a,22);
        // fork(wH(a,30);v=32;print(v);print(rH(a)));
        // print(v);print(rH(a))

        IStmt ex9 =
                new CompStmt(
                        new VarDeclarationStmt("v", new IntType()), new CompStmt(
                        new VarDeclarationStmt("a", new RefType(new IntType())), new CompStmt(
                        new AssigmentStmt("v", new ValueExp(new IntValue(10))), new CompStmt(
                        new New("a", new ValueExp(new IntValue(22))), new CompStmt(
                        new ForkStatement(new CompStmt(
                                new WriteToHeap("a", new ValueExp(new IntValue(30))), new CompStmt(
                                new AssigmentStmt("v", new ValueExp(new IntValue(32))), new CompStmt(
                                new PrintStmt(new VarExp("v")), new PrintStmt(new ReadHeapExpression(new VarExp("a")))
                        )
                        )
                        )
                        ),
                        new CompStmt(new PrintStmt(new VarExp("v")), new PrintStmt(new ReadHeapExpression(new VarExp("a"))))
                )
                )
                )
                )
                );

        try {
            ex9.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex9;
            statements = new_statements;
        } catch (Exception var18) {
            System.out.println(var18.getMessage());
        }
        
        //semaphore statement

        IStmt ex10 = new CompStmt(
                new VarDeclarationStmt("v1", new RefType(new IntType())),
                new CompStmt(
                        new VarDeclarationStmt("cnt", new IntType()),
                        new CompStmt(
                                new New("v1", new ValueExp(new IntValue(1))),
                                new CompStmt(
                                        new CreateSemaphoreStmt("cnt", new ReadHeapExpression(new VarExp("v1"))),
                                        new CompStmt(
                                                new ForkStatement(
                                                        new CompStmt(
                                                                new AcquireStmt("cnt"),
                                                                new CompStmt(
                                                                        new WriteToHeap("v1", new ArithExp(3, new ReadHeapExpression(new VarExp("v1")), new ValueExp(new IntValue(10)))),
                                                                        new CompStmt(
                                                                                new PrintStmt(new ReadHeapExpression(new VarExp("v1"))),
                                                                                new ReleaseStmt("cnt")
                                                                        )
                                                                )
                                                        )
                                                ),
                                                new CompStmt(
                                                        new ForkStatement(
                                                                new CompStmt(
                                                                        new AcquireStmt("cnt"),
                                                                        new CompStmt(
                                                                                new WriteToHeap("v1", new ArithExp(3,  new ReadHeapExpression(new VarExp("v1")), new ValueExp(new IntValue(10)))),
                                                                                new CompStmt(
                                                                                        new WriteToHeap("v1", new ArithExp(3,  new ReadHeapExpression(new VarExp("v1")), new ValueExp(new IntValue(2)))),
                                                                                        new CompStmt(
                                                                                                new PrintStmt(new ReadHeapExpression(new VarExp("v1"))),
                                                                                                new ReleaseStmt("cnt")
                                                                                        )
                                                                                )
                                                                        )
                                                                )
                                                        ),
                                                        new CompStmt(
                                                                new AcquireStmt("cnt"),
                                                                new CompStmt(
                                                                        new PrintStmt(new ArithExp(2, new ReadHeapExpression(new VarExp("v1")), new ValueExp(new IntValue(1)))),
                                                                        new ReleaseStmt("cnt")
                                                                )
                                                        )
                                                )
                                        )
                                )
                        )
                )
        );

        try {
            ex10.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = ex10;
            statements = new_statements;
        } catch (Exception var19) {
            System.out.println(var19.getMessage());
        }

        //switch statement:

        IStmt e11 = new CompStmt(
                new VarDeclarationStmt("a", new IntType()),
                new CompStmt(
                        new AssigmentStmt("a", new ValueExp(new IntValue(1))),
                        new CompStmt(
                                new VarDeclarationStmt("b", new IntType()),
                                new CompStmt(
                                        new AssigmentStmt("b",new ValueExp(new IntValue(2))),
                                                new CompStmt(
                                                        new VarDeclarationStmt("c", new IntType()),  new CompStmt(
                                                                new AssigmentStmt("c", new ValueExp(new IntValue(5))),
                                                                new CompStmt(
                                                                        new SwitchStmt(new ArithExp(3,new VarExp("a"),new ValueExp(new IntValue(10))),
                                                                                new ArithExp(3, new VarExp("b"),new VarExp("c")),
                                                                                new CompStmt(new PrintStmt(new VarExp("a")), new PrintStmt(new VarExp("b"))),
                                                                                new ValueExp(new IntValue(10)), new CompStmt(new PrintStmt(new ValueExp(new IntValue(100))), new PrintStmt(new ValueExp(new IntValue(200)))),
                                                                                new PrintStmt(new ValueExp(new IntValue(300)))),
                                                                        new PrintStmt(new ValueExp(new IntValue(300)))
                                                                )
                                                                )
                                                        )
                                                )
                                )
                        )
                );

        try
        {
            e11.typecheck(new MyDictionary<String, Type>());
            IStmt[] new_statements = (IStmt[])Arrays.copyOf(statements, statements.length + 1);
            new_statements[new_statements.length - 1] = e11;
            statements = new_statements;
        } catch (Exception var19) {
            System.out.println(var19.getMessage());
        }


        return statements;
    }
}