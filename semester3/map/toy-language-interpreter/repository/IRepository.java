package repository;

import model.exception.MyException;
import model.program_state.ProgramState;

import java.io.IOException;
import java.util.List;

public interface IRepository {
    //ProgramState getCurrentProgramState();
    void add(ProgramState programState);

    void savePrgStateinLOG(ProgramState state) throws MyException, IOException;

    List<ProgramState> getListOfProgramStates();
    void setProgramStateList(List<ProgramState> newList);
}
