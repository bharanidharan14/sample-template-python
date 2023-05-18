from unittest import mock

import pytest

from sample_template.src.dremio_interface import DremioInterface


@pytest.mark.parametrize(
    "query_to_execute,expected_result",
    [
        ("select * from table", ("1", "2")),
    ],
)
@mock.patch("sample_template.src.dremio_interface.DremioInterface.get_connection")
def test_execute_fetch_one_result(mock_conn, query_to_execute, expected_result):
    print("test execute_fetch_one_result function")
    dremio_interface = DremioInterface()
    conn = mock_conn.return_value
    cur = mock.MagicMock(rowcount=0)
    conn.cursor.return_value = cur
    type(cur).fetchone = mock.PropertyMock(side_effect=expected_result)
    result = dremio_interface.execute_fetch_one_result(query_to_execute)
    assert result == expected_result
    cur.close.assert_called()


@mock.patch("sample_template.src.dremio_interface.DremioInterface.get_connection")
def test_is_still_running_value_error(mock_client, query):
    dremio_interface = DremioInterface()
    mock_client.side_effect = ValueError("Test value error")
    with pytest.raises(ValueError):
        dremio_interface.execute_fetch_one_result(query)
