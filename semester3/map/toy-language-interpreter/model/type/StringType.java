package model.type;

import model.value.StringValue;
import model.value.Value;

public class StringType implements Type{
    public boolean equals(Object another)
    {
        return another instanceof StringType;
    }
    public StringType()
    {

    }
    @Override
    public String toString() {
        return "string";
    }

    @Override
    public Value defaultValue() {
        return new StringValue("");
    }
}
