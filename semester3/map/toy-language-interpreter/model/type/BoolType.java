package model.type;

import model.value.BoolValue;
import model.value.Value;

public class BoolType implements Type{
    public boolean equals(Object another)
    {
        return another instanceof BoolType;
    }
    public BoolType()
    {

    }
    @Override
    public String toString() {
        return "bool";
    }

    @Override
    public Value defaultValue() {
        return new BoolValue(false);
    }
}
