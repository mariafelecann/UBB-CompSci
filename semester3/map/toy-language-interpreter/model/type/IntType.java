package model.type;

import model.value.IntValue;
import model.value.Value;

public class IntType implements Type{
    public boolean equals(Object another)
    {
        return another instanceof IntType;
    }
    public IntType()
    {

    }
    @Override
    public String toString() {
        return "int";
    }

    @Override
    public Value defaultValue() {
        return new IntValue(0);
    }
}
