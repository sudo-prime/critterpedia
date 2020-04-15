import React from 'react';
import './Slider.css';

class Slider extends React.Component {

    render() {
        const { 
            min, max,
            value,
            text, onChange
        } = this.props;

        return (
            <input type="range" min={min} max={max} value={value} onChange={onChange} step ='100' class="slider"></input>
        )
    }
}

export default Slider;