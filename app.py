from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def perform_search():
    query = request.form['query']
    all_results = perform_actual_search(query)

    # Pagination
    page = request.args.get('page', 1, type=int)
    results_per_page = 10
    start_index = (page - 1) * results_per_page
    end_index = start_index + results_per_page
    results = all_results[start_index:end_index]

    return render_template('results.html', query=query, results=results, page=page)


def perform_actual_search(query):
    # Dummy URLs for demonstration
    dummy_urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
        "https://example.com/page4",
        "https://example.com/page5",
        "https://example.com/page6",
        "https://example.com/page7",
        "https://example.com/page8",
        "https://example.com/page9",
        "https://example.com/page10",
        "https://example.com/page11",
        "https://example.com/page12",
        "https://example.com/page13",
    ]
    return dummy_urls


if __name__ == '__main__':
    app.run()
