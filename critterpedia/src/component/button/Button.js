import React from 'react';
import './Button.css';

class Button extends React.Component {

    render() {
        const { 
            height, width, 
            text, onClick 
        } = this.props;

        const halfHeight = Math.floor(height/2);
        const halfWidth  = Math.floor(width/2);

        // do not ask me how this works
        return (
            <svg width={width} height={height} viewBox={"0 0 " + width + " " + height} onClick={onClick}>
                <path fill="#ED2F5B" stroke="none" d={`
                    M 0,`+halfHeight+`
                    C 0,0 0,0 `+halfWidth+`,0
                    S `+width+`,0 `+width+`,`+halfHeight+`
                      `+width+`,`+height+` `+halfWidth+`,`+height+`
                      0,`+height+` 0,`+halfHeight
                }></path>
                <text x="50%" y="50%" fill="white" dominant-baseline="middle" text-anchor="middle">{text}</text>
            </svg>
        )
    }
}

export default Button;