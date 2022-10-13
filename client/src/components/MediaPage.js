import React from 'react'
import { Link } from "react-router-dom";
import {Search} from "./Search"

export const MediaPage = (props) => {
  return (
    <div>
      <h1>
        Media Page
        <p> The media id is {props.media.overview} </p>
        </h1></div> 
  )
}
