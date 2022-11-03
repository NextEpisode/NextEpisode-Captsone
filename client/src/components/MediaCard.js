import React from 'react'
import { Link } from "react-router-dom";
 
export const MediaCard = ({ media, type }) => {
  return (
    <div className="media-card">
       
        <Link to={`/media-page/${media.id}?type=${type ? "movie" : "tv"}`}>
        <div className="poster-wrapper">
            {media.poster_path ? (
                <img
                src={`https:image.tmdb.org/t/p/w200${media.poster_path}`}
                alt={`${media.title} Poster`}
                />
            ) : (
                <div className="filler-poster"></div>
            )}
        </div>
        </Link>
 
        <div className="info">
            <div className="header">
                <h3 className="title">{media.title} {media.name}</h3>
                <h4 className="release-date">
                    {media.release_date ? media.release_date.substring(0, 4) : ''} {media.first_air_date ? media.first_air_date.substring(0, 4) : ''}
                    </h4>
            </div>
        </div>
    </div>
  );
}
