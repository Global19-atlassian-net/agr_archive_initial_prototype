import React, { Component } from 'react';

import style from './style.css';

class ResultsList extends Component {
  renderRows() {
    return this.props.entries.map( (d, i) => {
      return (
        <div key={`sr${i}`} className={style.resultContainer}>
          <h3>
            <a href='#'>{d.symbol}</a>
          </h3>
          <dl>
            <dt>Source</dt>
            <dd>SGD</dd>
            <dt>Genomic Coordinates</dt>
            <dd>{`${d.genomicStartCoordinates}:${d.genomicStopCoordinates}`}</dd>
            <dt>Relative Coordinates</dt>
            <dd>{`chri${d.genomicStartCoordinates}:${d.genomicStopCoordinates}`}</dd>
          </dl>
        </div>
      );
    });
  }

  render() {
    return (
      <div>
        {this.renderRows()}
      </div>
    );
  }

}

export default ResultsList;