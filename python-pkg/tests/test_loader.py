from city_macro_data import data_version, get_metadata, load_data, validate_data


def test_load_data_not_empty():
    df = load_data()
    assert not df.empty


def test_metadata_has_version():
    meta = get_metadata()
    assert "data_version" in meta
    assert data_version() == meta["data_version"]


def test_validate_data_default_columns():
    assert validate_data() is True
