mapping = {
    "settings": {
        "index": {
            "max_result_window": 15000,
            "analysis": {
                "analyzer": {
                    "default": {
                        "type": "custom",
                        "tokenizer": "whitespace",
                        "filter": ["english_stemmer", "lowercase"]
                    },
                    "autocomplete": {
                        "type": "custom",
                        "tokenizer": "whitespace",
                        "filter": ["lowercase", "autocomplete_filter"]
                    },
                    "symbols": {
                        "type": "custom",
                        "tokenizer": "whitespace",
                        "filter": ["lowercase"]
                    }
                },
                "filter": {
                    "english_stemmer": {
                        "type": "stemmer",
                        "language": "english"
                    },
                    "autocomplete_filter": {
                        "type": "edge_ngram",
                        "min_gram": "1",
                        "max_gram": "20"
                    }
                }
            },
            "number_of_replicas": "0", #temporarily
            "number_of_shards": "5"
        }
    },
    "mappings": {
        "searchable_item": {
            "properties": {
                "name": {
                    "type": "text",
                    "fields": {
                        "symbol": {
                            "type": "text",
                            "analyzer": "symbols"
                        }
                    }
                },
                "gene_symbol": {
                    "type": "text",
                    "analyzer": "symbols"
                },
                "gene_synonyms": {
                    "type": "text",
                    "analyzer": "symbols"
                },
                "gene_type": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "gene_chromosomes": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "gene_chromosome_starts": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "gene_chromosome_ends": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "gene_chromosome_strand": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "description": {
                    "type": "text"
                },
                "external_ids": {
                    "type": "text",
                    "analyzer": "symbols"
                },
                "gene_biological_process": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        },
                        "symbol": {
                            "type": "text",
                            "analyzer": "symbols"
                        }

                    }
                },
                "gene_molecular_function": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        },
                        "symbol": {
                            "type": "text",
                            "analyzer": "symbols"
                        }

                    }
                },
                "gene_cellular_component": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        },
                        "symbol": {
                            "type": "text",
                            "analyzer": "symbols"
                        }

                    }
                },
                "species": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "href": {
                    "type": "text",
                    "analyzer": "symbols"
                },
                "category": {
                    "type": "keyword",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        },
                        "symbol": {
                            "type": "text",
                            "analyzer": "symbols"
                        }
                    }
                },
                "go_type": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "go_genes": {
                    "type": "text",
                    "analyzer": "symbols",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "go_species": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "disease_genes": {
                    "type": "text",
                    "analyzer": "symbols",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "disease_species": {
                    "type": "text",
                    "fields": {
                        "raw": {
                            "type": "keyword"
                        }
                    }
                },
                "disease_synonyms": {
                    "type": "text"
                },
                "id": {
                    "type": "text",
                    "analyzer": "symbols"
                },
                "name_key": {
                    "type": "text",
                    "analyzer": "symbols",
                    "fields": {
                        "autocomplete": {
                            "type": "text",
                            "analyzer": "autocomplete"
                        }
                    }
                },
                "homologs": {
                    "properties": {
                        "symbol": {
                            "type": "text",
                            "analyzer": "symbols"
                        },
                        "species": {
                            "type": "text"
                        },
                        "relationship_type": {
                            "type": "text"
                        },
                        "ancestral": {
                            "type": "text"
                        },
                        "panther_family": {
                            "type": "text",
                            "analyzer": "symbols"
                        },
                        "href": {
                            "type": "text"
                        }
                    }
                }
            }
        }
    }
}
