package model.value;

import model.type.IntType;
import model.type.Type;

public class IntValue implements Value{
    int value;
    public IntValue(int i)
    {
        value = i;
    }


    public int getValue()
    {
        return value;
    }
    @Override
    public Type getType() {
        return new IntType();
    }

    @Override
    public String toString() {
        return "intVal(" +
                " " + value +
                ')';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        IntValue intValue = (IntValue) o;
        return value == intValue.value;
    }

}
