import casbin

CONF = "C:/Users/asish/Desktop/perm/perm/casbin_resolverApp/model.conf"
POLICY = "C:/Users/asish/Desktop/perm/perm/casbin_resolverApp/policy.csv"

e = casbin.Enforcer(CONF, POLICY)


sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.

if e.enforce(sub, obj, act):
    print("permit")
    # permit alice to read data1
else:
    # deny the request, show an error
    print("deny")
