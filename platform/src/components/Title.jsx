// src/Title.js

import React from "react";

import {
  faCommentDots,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

function Title() {
  return (
    <div>
      <h1>Chat Module <FontAwesomeIcon icon={faCommentDots} /></h1>
      {/* <faCommentDots /> */}
    </div>
  );
}

export default Title;
