

class MovieSchema:

    error_code_status_schema = {
        "type": "object",
        "required": ["status_code", "status_message"],
        "properties":
        {
            "status_code": {"type": "integer"},
            "status_message": {"type": "string"}
        }
    }

    movie_details_schema = {
        "type": "object",
        "properties":
        {
            "adult": {"type": "boolean"},
            "backdrop_path": {"type": "string"},
            "belongs_to_collection": {"anyOf": [{"type": "string"}, {}, {"type": "null"}]},
            "budget": {"type": "number"},
            "genres": {
                "type": "array",
                "properties":
                    {"id": {"type": "number"}, "name": {"type": "number"}}
            },
            "homepage": {"anyOf": [{"type": "string"}, {}]},
            "id": {"type": "number"},
            "imdb_id": {"type": "string"},
            "original_language": {"type": "string"},
            "original_title": {"type": "string"},
            "overview": {"type": "string"},
            "popularity": {"type": "number"},
            "poster_path": {"type": "string"},
            "production_companies": {
                "type": "array",
                "properties":
                    {
                        "id": {"type": "number"},
                        "logo_path": {"anyOf": [{"type": "string"}, {}, {"type": "null"}]},
                        "name": {"type": "string"},
                        "origin_country": {"type": "string"}
                    }
            },
            "production_countries": {
                "type": "array",
                "properties":
                    {
                        "iso_3166_1": {"type": "string"},
                        "name": {"type": "string"}
                    }
            },
            "release_date": {"type": "string"},
            "revenue": {"type": "number"},
            "runtime": {"type": "number"},
            "spoken_languages": {
                    "type": "array",
                    "properties":
                        {
                            "iso_639_1": {"type": "string"},
                            "name": {"type": "string"}
                        }
            },
            "status": {"type": "string"},
            "tagline": {"type": "string"},
            "title": {"type": "string"},
            "video": {"type": "boolean"},
            "vote_average": {"type": "number"},
            "vote_count": {"type": "number"}
        }


    }

    movie_external_ids_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "imdb_id": {"type": "string"},
            "facebook_id": {"type": "string"},
            "instagram_id": {"anyOf": [{"type": "string"}, {}]},
            "twitter_id": {"type": "string"}
        }
    }
