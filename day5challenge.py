n=int(input("enter no.of weights:"))
weights=[0]*n
for i in range(n):
    weights[i]=int(input("enter the weight:"))
print(weights)

very_light=[0]*n
normal_load=[0]*n
heavy_load=[0]*n
overload=[0]*n
invalid_entries=[0]*n
v_index=0
n_index=0
h_index=0
o_index=0
i_index=0
valid_entries=0
for i in weights:
    if i<0:
        invalid_entries[i_index]=i
        i_index=i_index+1
    elif i<=5:
        very_light[v_index]=i
        v_index=v_index+1
        valid_entries=valid_entries+1
    elif i<=25:
       normal_load[n_index]=i
       n_index=n_index+1
       valid_entries=valid_entries+1
    elif i<=60:
        heavy_load[h_index]=i
        h_index=h_index+1
        valid_entries=valid_entries+1
    else:
        overload[o_index]=i
        o_index=o_index+1
        valid_entries=valid_entries+1


