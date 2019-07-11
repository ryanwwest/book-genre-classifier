import csv
import nltk

stopwords = set(nltk.corpus.stopwords.words('english'))
most_common_english_words = [w for w in nltk.word_tokenize(open('most_common.txt', 'r').read()) if not w in stopwords]


def nltk_parser(parsed_books):
    number_parsed = 0

    # Create .csv file
    with open('data.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)

        header_row = ['word_count', 'words_per_sentence', 'average_length_of_word']
        for common_word in most_common_english_words:
            header_row.append(common_word)
        header_row.extend(['book_number', 'title', 'author', 'genre'])
        writer.writerow(header_row)

        for parsed_book, title, author, book_number in parsed_books:
            book = '\n'.join(parsed_book)

            # nltk Tokenization
            words_with_punctuation = nltk.word_tokenize(book)
            words = list(word.lower() for word in words_with_punctuation if word.isalpha())
            sentences = nltk.sent_tokenize(book)

            # Word Count
            total_word_count = len(words)

            # Average Words Per Sentence
            average_words_per_sentence = total_word_count / len(sentences)

            # Average Word Length
            total_char_count = 0
            for word in words:
                total_char_count += len(word)
            average_word_length = total_char_count / len(words)

            # Common Words
            words_without_stopwords = [w for w in words if not w in stopwords]
            frequency_distribution = nltk.FreqDist(words_without_stopwords)
            most_common_words_distribution = dict(frequency_distribution.most_common(1000))
            most_common_words_in_book = {}
            for word in most_common_english_words:
                word = word.lower()
                if word in most_common_words_distribution:
                    most_common_words_in_book[word] = round(
                        most_common_words_distribution[word] / float(total_word_count),
                        8)
                else:
                    most_common_words_in_book[word] = 0

            data_instance = [total_word_count, average_words_per_sentence, average_word_length]
            for word, word_freq_percent in sorted(most_common_words_in_book.iteritems()):
                data_instance.append(word_freq_percent)
            data_instance.extend([book_number, title, author])

            try:
                writer.writerow(data_instance)
            except:
                print(data_instance)

            number_parsed += 1

    return number_parsed
