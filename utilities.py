import traceback

def safe_index(dict_obj, key, returnOnError, printObject=False):
    try:
        return dict_obj[key]
    except Exception:
        print("function utilities.safe_index() caught error")
        traceback.print_exc()
        print(f"\nreturning {returnOnError}\n")
        if printObject:
            print(f"problematic dict_obj:\n{dict_obj}\n")
        return returnOnError
        