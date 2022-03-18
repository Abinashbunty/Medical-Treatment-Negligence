print("\nAttaching 2 concepts to the relation.")
r.attach(Concept("C2",1.0))
r.attach(Concept("C3",1.0))
print(r)
input()

print("\nSerialized weights:")
print(r.get())
input()

print("\nPropagate:")
print(r.propagate())
input()

print("\nSetting new weights to:")
print("0.0,1.0,1.0,1.0,1.0,1.0")
r.set("0.0,1.0,1.0,1.0,1.0,1.0")
print(r)
input()

print("\nSetting weights of C2 to:")
print("0.5,0.5")
r.set("C2","0.5,0.5")
print(r)
input()

print("\nRemoveing concept C2")
r.remove(Concept("C2"))
print(r)
input()

while True:
    res=r.propagate()
    print(res)
    error=1.0-res
    r.backprop(error)
    learning_rate=1.0
    r.adapt(error,learning_rate)
    print(r)
    input()