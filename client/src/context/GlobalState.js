import React, { createContext, useReducer, useEffect } from "react";
import {AppReducer} from "./AppReducer"

// initial State
const initialState = {
    mylist: [],
};

// create context
export const GlobalContext = createContext(initialState);

// provider components
export const GlobalProvider = (props) => {
    const [state, dispatch] = useReducer(AppReducer, initialState); 

// actions

};


