package model.value;

import model.type.BoolType;
import model.type.Type;

public class BoolValue implements Value{
    boolean value;
    public BoolValue(boolean v)
    {
        value = v;
    }

    public boolean getValue()
    {
        return value;
    }
    @Override
    public Type getType() {
        return new BoolType();
    }

    @Override
    public String toString() {
        return "boolVal(" +
                " " + value +
                ')';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        BoolValue boolValue = (BoolValue) o;
        return value == boolValue.value;
    }

}
