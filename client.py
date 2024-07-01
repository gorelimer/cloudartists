import soundcloud


class UserSearchClient(soundcloud.SoundCloud):
    def __init__(self, client_id) -> None:
        super().__init__(client_id=client_id)

    def search_by_place(self, place: str, **kw) -> list[soundcloud.User]:
        limit = kw.pop("limit", None)
        offset = kw.pop("offset", None)
        params = {
            "filter.place": place
        }

        result = self.search_users(
            '',
            limit=limit,
            offset=offset,
            **params,
            **kw
        )

        return list(result)
