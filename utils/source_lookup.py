def build_source_lookup(source_trust):
    return {
        trust.source: trust
        for trust in source_trust
    }