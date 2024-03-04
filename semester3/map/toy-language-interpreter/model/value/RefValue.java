package model.value;

import model.type.RefType;
import model.type.Type;

public class RefValue implements  Value{
    int heap_address;
    Type type;
    public RefValue(int addr, Type t)
    {
        heap_address = addr;
        type = t;
    }

    public RefValue() {

    }

    @Override
    public Type getType() {
        return new RefType(type);
    }
    public int get_address()
    {
        return heap_address;
    }

    @Override
    public String toString() {
        return "refValue(" +
                "heap_address=" + heap_address +
                ", type=" + type +
                ')';
    }
}
