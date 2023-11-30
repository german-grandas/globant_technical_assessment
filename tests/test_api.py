def test_get_all_berry_stats(client):
    response = client.get("/allBerryStats")
    assert response.status_code == 200
