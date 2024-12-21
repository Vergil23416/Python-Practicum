def secret_replace(text, **replaces):
    new_s = ''
    for s in text:
        if s in replaces:
            new_s += replaces[s][0]
            replaces[s] = replaces[s][1:] + (replaces[s][0],)
        else:
            new_s += s
    return new_s
