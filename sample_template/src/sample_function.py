from sample_template.src.dremio_interface import DremioInterface


def sample_function_1():
    try:
        obj = DremioInterface()
        result = obj.execute_fetch_one_result("select * from test")
        return result
    except Exception as e:
        raise e


def sample_function_2():
    try:
        obj = DremioInterface()
        results = obj.execute_fetch_all_result("select * from test")
        ids = ()
        for res in results:
            ids = ids + res[0]
        query2 = f"select * from test where ids = {ids}"
        return query2
    except Exception as e:
        raise e
