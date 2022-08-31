import React from 'react'

export const MediaCard = ({ movie }) => {
  return (
    <div className="media-card">
        <div className="poster-wrapper">
            {movie.poster_path ? (
                <img 
                src={`https:image.tmdb.org/t/p/w200${movie.poster_path}`}
                alt={`${movie.title} Poster`}
                />
            ) : (
                <div className="filler-poster"></div>
            )}
        </div>
        <div className="info">
            <div className="header">
                <h3 className="title">{movie.title}</h3>
                <h4 className="release-date">
                    {movie.release_date ? movie.release_date.substring(0, 4) : '-'}
                    </h4>
            </div>
        </div>
    </div>
  );
}
