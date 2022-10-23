import React from 'react'

export const TVCard = ({ tv }) => {
  return (
    <div className="tv-card">
        <div className="poster-wrapper">
            {tv.poster_path ? (
                <img 
                src={`https:image.tmdb.org/t/p/w200${tv.poster_path}`}
                alt={`${tv.title} Poster`}
                />
            ) : (
                <div className="filler-poster"></div>
            )}
        </div>
        <div className="info">
            <div className="header">
                <h3 className="name">{tv.title}</h3>
                <h4 className="first_air_date">
                    {tv.first_air_date ? tv.first_air_date.substring(0, 4) : '-'}
                    </h4>
            </div>
            <div className="controls">
                <button className="btn">
                    Add to My List
                </button>
            </div>
        </div>
    </div>
  );
}
