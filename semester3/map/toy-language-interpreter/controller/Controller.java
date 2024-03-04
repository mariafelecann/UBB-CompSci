package controller;

import model.exception.*;
import model.program_state.*;
import model.value.RefValue;
import model.value.Value;
import repository.IRepository;

import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller {
    IRepository repo;
    ExecutorService executor;
    public Controller(IRepository repo) {
        this.repo = repo;
    }

    public IRepository getRepository(){return repo;}

    /*

    public void allStep() throws MyException, IOException {
        List<ProgramState> states_from_repo = repo.getListOfProgramStates();
        ProgramState prg = states_from_repo.get(0);
        while (!prg.getExeStack().isEmpty()) {
            System.out.println(prg.toString());
            repo.savePrgStateinLOG(prg);
            try {
                prg.oneStep();
                prg.getHeap().setContent(prg.unsafeGarbageCollector(getAddrFromSymbTable(prg.getSymTable().getContent().values()), getAddrFromSymbTable(prg.getHeap().getContent().values()), prg.getHeap().getContent()));
            } catch (MyException ex) {
                System.out.println(ex.getMessage());
            }

        }

        System.out.println(prg.toString());
        repo.savePrgStateinLOG(prg);
    }

     */

    public List<Integer> getAddrFromSymbTable(Collection<Value> symbTableValues) {
        return symbTableValues.stream().filter(v -> v instanceof RefValue)
                .map(v -> {
                    RefValue v1 = (RefValue) v;
                    return v1.get_address();
                })
                .collect(Collectors.toList());

    }

    public List<ProgramState> removeCompletedProgram(List<ProgramState> inPrgList)
    {
        return inPrgList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());
    }

    public void allStep() throws InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        //remove the completed programs
        List<ProgramState> prgList= removeCompletedProgram(repo.getListOfProgramStates());
        List<ProgramState> states_from_repo = repo.getListOfProgramStates();
        ProgramState prg = states_from_repo.get(0);
        while(prgList.size() > 0){
            prg.getHeap().setContent(prg.unsafeGarbageCollector(getAddrFromSymbTable(prg.getSymTable().getContent().values()), getAddrFromSymbTable(prg.getHeap().getContent().values()), prg.getHeap().getContent()));
            oneStepForAllProgramStates(prgList);
            //remove the completed programs
            prgList=removeCompletedProgram(repo.getListOfProgramStates());
        }
        executor.shutdownNow();
        //HERE the com.example.toylanguagegui.repository still contains at least one Completed Prg
        // and its List<PrgState> is not empty. Note that oneStepForAllPrg calls the method
        //setPrgList of com.example.toylanguagegui.repository in order to change the com.example.toylanguagegui.repository

        // update the com.example.toylanguagegui.repository state
        repo.setProgramStateList(prgList);
    }



    public void oneStepForAllProgramStates(List<ProgramState> prgList) throws InterruptedException {
        if (executor == null) {
            executor = Executors.newFixedThreadPool(2);
        }
        //before the execution, print the PrgState List into the log file
        prgList.forEach(prg -> {
            try {
                System.out.println(prg.toString());
                repo.savePrgStateinLOG(prg);
            } catch (MyException e) {
                throw new RuntimeException(e);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
        List<Callable<ProgramState>> callList = prgList.stream()
                .map((ProgramState p) -> (Callable<ProgramState>)(() -> {return p.oneStep();}))
                .collect(Collectors.toList());

        List<ProgramState> newPrgList = executor.invokeAll(callList). stream()
                . map(future -> {
                    try {
                        return future.get();
                    } catch (Exception ex) {
                        System.out.println(ex.getMessage());
                    }
                    return null;
                }).filter(p -> p!=null)
                            .collect(Collectors.toList());
                    //add the new created threads to the list of existing threads
                    prgList.addAll(newPrgList);

                    prgList.forEach(prg -> {
                        try {
                            repo.savePrgStateinLOG(prg);
                            System.out.println(prg.toString());
                        } catch (MyException e) {
                            throw new RuntimeException(e);
                        } catch (IOException e) {
                            throw new RuntimeException(e);
                        }
                    });
                    repo.setProgramStateList(prgList);
                }



    public void unsafeGarbageCollector(List<ProgramState> prgList) {
        List<Integer> symTableAddr = prgList.stream()
                .flatMap(p -> p.getSymTable().getContent().values().stream())
                .filter(v -> v instanceof RefValue)
                .map(v -> ((RefValue) v).get_address())
                .collect(Collectors.toList());

        List<Integer> heapAddr = getAddrFromSymbTable(prgList.get(0).getHeap().getContent().values());

        Map<Integer, Value> newHeap = prgList.get(0).getHeap().entrySet().stream()
                .filter(e -> symTableAddr.contains(e.getKey()) || heapAddr.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
        for (ProgramState prg : prgList) {
            prg.getHeap().setContent(newHeap);
        }
    }
}
