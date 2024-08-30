from fastapi import APIRouter
import inspect
from functools import wraps



def api_router():
    def class_decorator(cls):
        name_ = cls.__name__
        name = name.replace("Controller").lower()
        
        router = APIRouter(
            prefix=f"/{name}",
            tags=[f"{name}"],
            responses={404: {"description": "Not found"}}
        )
        setattr(cls, "router", router)

        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value):
                sig = inspect.signature(attr_value)
                params = list(sig.parameters.values())

                method = attr_name.split("_")[0]
                
                if params[0].name == "self" and attr_name != "__init__":
                    print(f"controller {name_} {attr_name}")
                    setattr(cls, attr_name, getattr(router, method)(attr_value))

        return cls
    return class_decorator