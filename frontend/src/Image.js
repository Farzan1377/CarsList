import React, { Component, useState } from 'react';
import PropTypes from 'prop-types';

function Image(props) {
    const [error, setError] = useState(false)
    const [source, setSource] = useState(props.src)
    const onError = () => {
        if (!error) {
            setSource(props.fallbackSource)
            setError(true)
          }
    }

    return (
      <img
        src={source}
        onError={onError}
        className={props.className}
      />
    );
  }

export default Image;