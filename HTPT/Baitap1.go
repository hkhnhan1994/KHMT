// The Crawl function recursively crawls a given URL up to a certain depth, fetching the page content and printing the results.
func Crawl(url string, depth int, fetcher Fetcher, ret chan string) {
    // Close the ret channel once the function returns to signal that all results have been processed.
    defer close(ret)

    // If the depth is less than or equal to 0, return immediately to stop further crawling.
    if depth <= 0 {
        return
    }

    // Fetch the body content and URLs from the provided fetcher.
    body, urls, err := fetcher.Fetch(url)
    if err != nil {
        // If there was an error during fetching, send the error message through the ret channel.
        ret <- err.Error()
        return
    }

    // Send a message with the URL and its body content through the ret channel.
    ret <- fmt.Sprintf("found: %s %q", url, body)

    // Create an array of channels to collect the results from recursive calls to Crawl for each URL.
    result := make([]chan string, len(urls))
    for i, u := range urls {
        // Create a new channel for each URL to collect the results for that URL.
        result[i] = make(chan string)
        // Start a new goroutine to crawl the current URL with depth-1 and send the results to the corresponding channel.
        go Crawl(u, depth-1, fetcher, result[i])
    }

    // Loop through the result channels to collect and send the results received from the recursive calls.
    for i := range result {
        for s := range result[i] {
            // For each result received from the child Crawl calls, send it through the ret channel.
            ret <- s
        }
    }

    return
}

// The main function initiates the crawling process by starting a goroutine for the Crawl function
// and prints the results as they are received from the ret channel.
func main() {
    // Create a channel to collect the results from the Crawl function.
    result := make(chan string)
    // Start a goroutine to crawl the initial URL ("http://golang.org/") with a depth of 4.
    // The fetcher parameter is not shown here, but it is assumed to be an implementation of the Fetcher interface.
    go Crawl("http://golang.org/", 4, fetcher, result)

    // Loop through the results received from the Crawl function and print them.
    for s := range result {
        fmt.Println(s)
    }
}
