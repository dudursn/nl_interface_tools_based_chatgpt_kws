
def get_messages(opt):

    if (opt == "1"):
        print(opt)
        f = open("prompt_messages/mondial_prompt.txt", "r")
        system_message = f.read()
        return [
            {"role": "system", "content": system_message},
            {"role": "user", "content": "Cities of Thailand"},
            {"role": "assistant", "content": "search_keywords(City Thailand)"},
            {"role": "user", "content": "Total cities of Thailand"},
            {"role": "assistant", "content": "search_keywords(total City Thailand)"},
            {"role": "user", "content": "Country of Georgia"},
            {"role": "assistant", "content": "search_keywords(Country City Georgia)"},
            {"role": "user", "content": "Country and Cities of river Niger"},
            {"role": "assistant", "content": "search_keywords(Country City River Niger)"},
            {"role": "user", "content": "list the seas related to Barcelona "},
            {"role": "assistant", "content": "search_keywords(Sea City contains Barcelona)"},
            {"role": "user", "content": "List the economies of Cameroon"},
            {"role": "assistant", "content": "search_keywords(Economy Cameroon)"},
            {"role": "user", "content": "The Gross domestic product of Nigeria"},
            {"role": "assistant", "content": "search_keywords(Economy Gdp Nigeria)"},
            {"role": "user", "content": "Which is the language of canada?"},
            {"role": "assistant", "content": "search_keywords(Language Canada)"},
            {"role": "user", "content": "Airports with elevation greater than 1000"},
            {"role": "assistant", "content": "search_keywords(Airports elevation > 1000)"}
        ]
        
    system_message = "You are a helpful assistant that extract keywords from a block of text,\n" + \
        "search for it in a database and show the results."
    return [
        {"role": "system", "content": system_message}
    ]
        
