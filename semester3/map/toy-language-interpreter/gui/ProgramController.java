package gui;

import controller.Controller;
import javafx.util.Pair;
import model.program_state.ProgramState;
import model.stmt.IStmt;
import model.type.Type;
import model.utilis.*;
import model.value.StringValue;
import model.value.Value;
import repository.IRepository;
import repository.Repository;
import javafx.beans.property.SimpleObjectProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.Background;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.io.BufferedReader;
import java.util.List;
import java.util.Map;

public class ProgramController {
    GridPane grid1;
    Stage newStage = new Stage();
    List<ProgramState> program_state_list;
    Integer itemNr;
    Controller controller;
    IStmt statement;
    IRepository repo;
    ProgramState selected_program_state;
    private TableView<Map.Entry<String, Value>> symbolTable;
    private ListView<String> exeStack;
    ListView<String> listProgramStatesViewGui;

    ProgramController(Integer itemNr, MainGUI mainStage){
        this.itemNr=itemNr;
        statement=mainStage.getListOfExamples()[itemNr];

        MyIStack<IStmt> stk1 = new MyStack<>() {};
        MyIDictionary<String, Value> symbol_table1 = new MyDictionary<String, Value>();
        MyIDictionary<StringValue, BufferedReader> file_table_1=new MyDictionary<StringValue, BufferedReader>();
        MyIList<Value> out1 = new MyList<Value>();
        MyIHeap<Integer, Value> heap= new MyHeapTable<>();
        MyIDictionary<String, Type> typeEnvironment = new MyDictionary<String, Type>();
        MyISemaphore semaphore = new MySemaphore();
        ProgramState PrgState1 = new ProgramState(stk1, symbol_table1, out1, statement, file_table_1, heap,typeEnvironment,semaphore);
        selected_program_state=PrgState1;
        itemNr++;
        String logfile="log"+itemNr+".txt";
        repo= new Repository(logfile);
        repo.add(PrgState1);
        controller = new Controller(repo);
    }

    void allSteps() {
        program_state_list = controller.getRepository().getListOfProgramStates();
        Button next_button = new Button("Next Step");
        next_button.autosize();
        HBox hbox = new HBox(5);
        hbox.setPadding(new Insets(20));
        hbox.setAlignment(Pos.BASELINE_RIGHT);
        Button button_program_state=new Button("See Program State");
        program_state_list = controller.removeCompletedProgram(repo.getListOfProgramStates());
        repo.setProgramStateList(program_state_list);
        hbox.getChildren().addAll(next_button);

        Label nrProgramStates = new Label("The Number of Program States: ");
        listProgramStatesViewGui=getProgramStates();
        button_program_state.setOnAction(actionEvent ->
        {
            String selectedExample = listProgramStatesViewGui.getSelectionModel().getSelectedItem();
            Integer itemNr=listProgramStatesViewGui.getSelectionModel().getSelectedIndex()+1;
            if (selectedExample != null) {
                if (!program_state_list.isEmpty()) {
                    for (ProgramState pstate : program_state_list) {
                        if(pstate.getId()==itemNr) {
                            selected_program_state = pstate;
                            grid1 = updateProgramState(selected_program_state);
                        }
                    }
                }
                hbox.getChildren().remove(3);
                hbox.getChildren().add(grid1);
            };
        });
        HBox buttonsHBox = new HBox(next_button, button_program_state);
        VBox vbox = new VBox(buttonsHBox, nrProgramStates, listProgramStatesViewGui);

        try {
            if (!program_state_list.isEmpty()) {
                selected_program_state.unsafeGarbageCollector(controller.getAddrFromSymbTable(selected_program_state.getSymTable().getContent().values()), controller.getAddrFromSymbTable(selected_program_state.getHeap().getContent().values()), selected_program_state.getHeap().getContent());
                grid1= oneStepInGui(selected_program_state);
                hbox.getChildren().clear();
                hbox.getChildren().addAll(vbox, grid1);
                controller.unsafeGarbageCollector(program_state_list);
            }
            program_state_list = controller.removeCompletedProgram(repo.getListOfProgramStates());
            repo.setProgramStateList(program_state_list);

        } catch (Exception e) {
            Label exceptionLabel = new Label(e.getMessage());
            Scene newScene = new Scene(exceptionLabel);
            newStage.setScene(newScene);
            newStage.setTitle("exception has been caught ! :( ");
            newStage.show();
        }

        next_button.setOnAction(event -> {
            listProgramStatesViewGui=getProgramStates();
            button_program_state.setOnAction(actionEvent ->
            {
                String selectedExample = listProgramStatesViewGui.getSelectionModel().getSelectedItem();
                Integer itemNr=listProgramStatesViewGui.getSelectionModel().getSelectedIndex()+1;
                if (selectedExample != null) {
                    if (!program_state_list.isEmpty()) {
                        for (ProgramState ProgramState : program_state_list) {
                            if(ProgramState.getId()==itemNr) {
                                selected_program_state = ProgramState;
                                grid1 = updateProgramState(selected_program_state);
                            }
                        }
                    }
                    hbox.getChildren().remove(3);
                    hbox.getChildren().add(grid1);
                };
            });
            try {
                if (!program_state_list.isEmpty()) {
                    selected_program_state.unsafeGarbageCollector(controller.getAddrFromSymbTable(selected_program_state.getSymTable().getContent().values()), controller.getAddrFromSymbTable(selected_program_state.getHeap().getContent().values()), selected_program_state.getHeap().getContent());
                    grid1= oneStepInGui(selected_program_state);
                    hbox.getChildren().clear();
                    hbox.getChildren().addAll(vbox, grid1);
                    controller.unsafeGarbageCollector(program_state_list);
                }
                program_state_list = controller.removeCompletedProgram(repo.getListOfProgramStates());
                repo.setProgramStateList(program_state_list);

            } catch (Exception e) {
                Label exceptionLabel = new Label(e.getMessage());
                Scene newScene = new Scene(exceptionLabel);
                newStage.setScene(newScene);
                newStage.setTitle("exception has been caught ! :( ");
                newStage.show();
            }
        });

        hbox.setBackground(Background.fill(Color.LIGHTBLUE));
        Scene newScene = new Scene(hbox, 800, 600);
        newStage.getMaxHeight();
        newStage.getMaxWidth();
        newStage.setScene(newScene);
        newStage.show();
    }

    private GridPane oneStepInGui(ProgramState prg) throws Exception {
        controller.oneStepForAllProgramStates(program_state_list);
        program_state_list = repo.getListOfProgramStates();
        return updateProgramState(prg);
    }
    private GridPane updateProgramState(ProgramState prg) {
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);

        TitledPane exeStackPane = new TitledPane("Execution Stack", getExecutionStack(prg));
        grid.add(exeStackPane, 0, 0);

        TitledPane symbolTablePane = new TitledPane("Symbol Table", getSymbolTable(prg));
        grid.add(symbolTablePane, 0, 1);

        TitledPane heapTablePane = new TitledPane("Heap Table", getHeapTable(prg));
        grid.add(heapTablePane, 1, 0);

        TitledPane fileTablePane = new TitledPane("File Table", getFileTable(prg));
        grid.add(fileTablePane, 1, 1);

        TitledPane outputPane = new TitledPane("Output", getOutput(prg));
        grid.add(outputPane, 0, 2, 2, 1);

        TitledPane semaphorePane = new TitledPane("Semaphore", getSemaphoreTableView(prg));
        grid.add(semaphorePane, 1,3);
        return grid;
    }

    private TableView<Map.Entry<String, Value>> getSymbolTable(ProgramState prg) {
        MyIDictionary<String, Value> smbltable = prg.getSymTable();
        ObservableList<Map.Entry<String, Value>> items = FXCollections.observableArrayList();

        if (smbltable != null && !smbltable.isEmpty()) {
            for (Map.Entry<String, Value> entry : smbltable.entrySet()) {
                items.add(entry);
            }
        }

        TableView<Map.Entry<String, Value>> tableView = new TableView<>();
        tableView.setEditable(true);

        TableColumn<Map.Entry<String, Value>, String> nameColumn = new TableColumn<>("Variable");
        nameColumn.setCellValueFactory(param -> new SimpleObjectProperty<>(param.getValue().getKey()));

        TableColumn<Map.Entry<String, Value>, Value> valueColumn = new TableColumn<>("Value");
        valueColumn.setCellValueFactory(param -> new SimpleObjectProperty<>(param.getValue().getValue()));

        tableView.getColumns().addAll(nameColumn, valueColumn);
        tableView.setItems(items);

        return tableView;
    }


    private TableView<Map.Entry<Integer, Value>> getHeapTable(ProgramState prg) {
        MyIHeap<Integer, Value> heap = prg.getHeap();
        ObservableList<Map.Entry<Integer, Value>> items = FXCollections.observableArrayList();
        if (heap != null && !heap.isEmpty()) {
            items.addAll(heap.entrySet());
        }
        TableView<Map.Entry<Integer, Value>> tableView = new TableView<>();

        TableColumn<Map.Entry<Integer, Value>, Integer> addressColumn = new TableColumn<>("Address");
        addressColumn.setCellValueFactory(param -> new SimpleObjectProperty<>(param.getValue().getKey()));
        TableColumn<Map.Entry<Integer, Value>, Value> valueColumn = new TableColumn<>("Value");
        valueColumn.setCellValueFactory(param -> new SimpleObjectProperty<>(param.getValue().getValue()));

        tableView.getColumns().addAll(addressColumn, valueColumn);
        tableView.setItems(items);
        return tableView;
    }

    private ListView<String> getFileTable(ProgramState prg) {
        ObservableList<String> items = FXCollections.observableArrayList();
        MyIDictionary<StringValue, BufferedReader> fileTable = prg.getFileTable();
        for (Map.Entry<StringValue, BufferedReader> entry : fileTable.entrySet()) {
            items.add(entry.getKey().toString() + " " + entry.getValue().toString());
        }
        ListView<String> list = new ListView<>();
        list.setItems(items);
        return list;
    }

    private ListView<String> getOutput(ProgramState prg) {
        ObservableList<String> items = FXCollections.observableArrayList();
        MyIList<Value> listoutput = prg.getOut();
        if (!listoutput.isEmpty()) {
            items.addAll(listoutput.toString());
        }
        ListView<String> list = new ListView<>();
        list.setItems(items);
        return list;
    }


    private ListView getExecutionStack(ProgramState prg){
        ListView<String> list=new ListView<>();
        MyIStack<IStmt> stack = prg.getExeStack();
        MyIStack<IStmt> tempStack = new MyStack<IStmt>() {};
        while (!stack.isEmpty()) {
            tempStack.push(stack.pop());
        }
        ObservableList<String> items = FXCollections.observableArrayList();
        while (!tempStack.isEmpty()) {
            IStmt statement = tempStack.pop();
            items.add(statement.toString());
            stack.push(statement);
        }
        list.setItems(items);
        return list;
    }

    private ListView getSemaphoreTableView(ProgramState programState) {
        ListView<String> semaphoreListView = new ListView<>();
        MyISemaphore semaphore = programState.getSemaphoreTable();

        ObservableList<String> semaphoreList = FXCollections.observableArrayList();

        for (Map.Entry<Integer, javafx.util.Pair<Integer, List<Integer>>> entry : semaphore.getTable_of_semaphores().entrySet()) {
            int key = entry.getKey();
            int value1 = entry.getValue().getKey();
            List<Integer> value2 = entry.getValue().getValue();

            String item = "Key: " + key + ", Value1: " + value1 + ", Value2: " + value2;
            semaphoreList.add(item);
        }

        semaphoreListView.setItems(semaphoreList);
        return semaphoreListView;
    }



    ObservableList<String> items = FXCollections.observableArrayList();

    private ListView<String> getProgramStates() {
        listProgramStatesViewGui = new ListView<>();
        System.out.println(controller.getRepository().getListOfProgramStates());
        items.clear();
        for (ProgramState p : program_state_list) {
            if (!items.contains(String.valueOf(p.getId())) && !p.getExeStack().isEmpty())
                items.add(String.valueOf(p.getId()));
        }
        listProgramStatesViewGui.setItems(items);
        return listProgramStatesViewGui;

    }

}
