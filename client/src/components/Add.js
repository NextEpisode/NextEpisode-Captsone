import React, {useState} from 'react'
import {MediaCard} from "./MediaCard"
import { Link } from 'react-router-dom'

export const Add = () => {
    const [query, setQuery] = useState(""); 
    const [results, setResults] = useState([]);

    const onChange = e => {
        e.preventDefault();

        setQuery(e.target.value);
        // Fetch link not making use of env.local
        fetch(`https://api.themoviedb.org/3/search/movie?api_key=468018e64d6cfa119009ede09787dea0&language=en-US&page=1&include_adult=false&query=${e.target.value}`
        )
        .then((res) => res.json())
        .then((data) => {console.log(data);
            if(!data.errors) {
                setResults(data.results);
            } else {
                setResults([]);
            }
        });
    };


  return (
    <div className="add-page">
        <div className="container">
            <div className="add-content">
                <input type="text" 
                placeholder='Search for a movie'
                value={query}
                onChange={onChange}
                />
            </div>

            {results.length > 0 && ( 
                <ul className="results">
                    {results.map(movie => (
                        <li key={movie.id}>
                            <MediaCard movie={movie}/>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    </div>
  )
}
