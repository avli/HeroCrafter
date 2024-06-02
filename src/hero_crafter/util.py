from openai import OpenAI

_client = OpenAI()


def _make_assistant_request(name, gender, alignment, race, character_class):
    result = (f"Write a brief biography for a table top RPG character who is a {alignment} {gender} {race} "
              f"{character_class} who's name is {name}.")
    return result


def generate_biography(name, gender, alignment, race, character_class):
    completion = _client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a table top RPG player or dungeon master."},
            {"role": "user", "content": _make_assistant_request(name, gender, alignment, race, character_class)}
        ]
    )
    return completion.choices[0].message.content


def generate_portrait(name, gender, alignment, race, character_class):
    response = _client.images.generate(
      model="dall-e-3",
      prompt=_make_assistant_request(name, gender, alignment, race, character_class),
      size="1024x1024",
      quality="standard",
      n=1,
    )
    image_url = response.data[0].url
    return image_url
