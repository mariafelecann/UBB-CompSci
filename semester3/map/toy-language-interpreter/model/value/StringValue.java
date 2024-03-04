package model.value;

import model.type.StringType;
import model.type.Type;

import java.util.Objects;

public class StringValue implements Value{
    String value;

    public StringValue(String v)
    {
        value = v;
    }
    public String getValue()
    {
        return value;
    }

    @Override
    public Type getType() {
        return new StringType();
    }

    @Override
    public String toString() {
        return "stringVal(" +
                 value + '\'' +
                ')';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        StringValue that = (StringValue) o;
        return Objects.equals(value, that.value);
    }
}
