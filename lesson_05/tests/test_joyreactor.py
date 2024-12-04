import time
import requests

API_URL = 'https://api.joyreactor.com/graphql'
HEADERS = {'Content-Type': 'application/json'}


def search_posts(query_text):
    query = f"""
    query MyQuery {{
      search(query: "{query_text}") {{
        postPager {{
          posts {{
            id
            text
          }}
        }}
      }}
    }}
    """
    json_data = {
        'query': query,
    }
    response = requests.post(API_URL, headers=HEADERS, json=json_data)
    return response


class TestJoyReactorAPI:

    def test_search_query_success(self):
        response = search_posts("Аниме")
        assert response.status_code == 200, "Expected status code 200"

        data = response.json()
        assert "data" in data, "Response should contain 'data' key"
        assert "search" in data["data"], "Response should contain 'search' key"
        assert "postPager" in data["data"]["search"], "Response should contain 'postPager' key"
        assert "posts" in data["data"]["search"]["postPager"], "Response should contain 'posts' key"

        posts = data["data"]["search"]["postPager"]["posts"]
        assert isinstance(posts, list), "Posts should be a list"
        assert len(posts) > 0, "Should return at least one post"
        time.sleep(1)

    def test_search_empty_query(self):
        response = search_posts("")
        assert response.status_code == 200, "Expected status code 200"

        data = response.json()
        assert "data" in data, "Response should contain 'data' key"
        assert "search" in data["data"], "Response should contain 'search' key"
        assert "posts" in data["data"]["search"]["postPager"], "Response should contain 'posts' key"
        time.sleep(1)

    def test_search_non_existent_term(self):
        response = search_posts("nonexistentterm12345")
        assert response.status_code == 200, "Expected status code 200"

        data = response.json()
        assert "data" in data, "Response should contain 'data' key"
        assert "search" in data["data"], "Response should contain 'search' key"
        assert len(data["data"]["search"]["postPager"]["posts"]) == 0, "Should return no posts for non-existent term"
        time.sleep(1)

    def test_search_special_characters(self):
        response = search_posts("@#$%^&*()")
        assert response.status_code == 200, "Expected status code 200"

        data = response.json()
        assert "data" in data, "Response should contain 'data' key"
        assert "search" in data["data"], "Response should contain 'search' key"
        assert len(data["data"]["search"]["postPager"]["posts"]) == 0, "Should return no posts for special characters"
        time.sleep(1)

    def test_search_query_with_spaces(self):
        response = search_posts("Аниме 1080p")
        assert response.status_code == 200, "Expected status code 200"

        data = response.json()
        assert "data" in data, "Response should contain 'data' key"
        assert "search" in data["data"], "Response should contain 'search' key"
        assert len(data["data"]["search"]["postPager"]["posts"]) > 0, "Should return posts for query with spaces"
        time.sleep(1)

    def test_search_query_syntax_error(self):
        query = """
            query MyQuery {
              search(query: "тест") { }
            }
            """
        json_data = {
            'query': query,
        }
        response = requests.post(API_URL, headers=HEADERS, json=json_data)
        assert response.status_code == 200, "Expected status code 200"

        data = response.json()
        assert "errors" in data, "Response should contain 'errors' key"
        assert len(data["errors"]) > 0, "Should return errors for query syntax error"
        time.sleep(1)

    def test_empty_query(self):
        query = ''
        json_data = {
            'query': query,
        }
        response = requests.post(API_URL, headers=HEADERS, json=json_data)
        assert response.status_code == 200, "Expected status code 200"

        data = response.json()
        assert data == {"errors": [
            {"message": "GraphQL Request must include at least one of those two parameters: \"query\" or \"queryId\""}]
        }
