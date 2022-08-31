import React from "react";
import { Link } from "react-router-dom";

export const Header = () => {
  return (
    <header>
      <div className="container">
        <div className="inner-content">
          <div className="brand">
            <Link to="/">Binge Watcher</Link>
          </div>

          <ul className="nav-links">
            <li>
              <Link to="/my-list">My List</Link>
            </li>
            <li>
              <Link to="/add" className="btn btn-main">
                Add Movie
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </header>
  );
};
