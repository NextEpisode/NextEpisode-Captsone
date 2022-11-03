import React, {useState} from 'react'
import {MediaCard} from "./MediaCard"
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
 
export const Search = () => {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);
    const [buttonClicked, setbuttonClicked] = useState(true);
    const [alignment, setAlignment] = React.useState('web');
    const handleFalse= () => setbuttonClicked((buttonClicked) => false);
    const handleTrue= () => setbuttonClicked((buttonClicked) => true);
    const handleChange = (event, newAlignment) => {
      setAlignment(newAlignment);
    };
 
 
    const onChange = e => {
        e.preventDefault();
 
        setQuery(e.target.value);
        // Fetch link not making use of env.local
        if (buttonClicked===true){
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
 
        }
 
        else {fetch(`https://api.themoviedb.org/3/search/tv?api_key=468018e64d6cfa119009ede09787dea0&language=en-US&page=1&include_adult=false&query=${e.target.value}`
        )
        .then((res) => res.json())
        .then((data) => {console.log(data);
            if(!data.errors) {
                setResults(data.results);
            } else {
                setResults([]);
            }
        });}
    };
 
    return (
        <div className="search-page">
           
            <div className="container">
            <ToggleButtonGroup
                color="primary"
                value={alignment}
                exclusive
                onChange={handleChange}
                aria-label="Platform">
                <ToggleButton onClick={handleTrue} value="web">Movies</ToggleButton>
                <ToggleButton onClick={handleFalse} value="android">TV Shows</ToggleButton>
                </ToggleButtonGroup>
 
                <div className="search-content">
                    <input type="text"
                    placeholder='Search'
                    value={query}
                    onChange={onChange}
                    />
                </div>
 
                {results.length > 0 && (
                    <ul className="results">
                        {results.map(media => (
                            <li key={media.id}>
                                <MediaCard media={media} type={buttonClicked}/>
                            </li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
      )
}
