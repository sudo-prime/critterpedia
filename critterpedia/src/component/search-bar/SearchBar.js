import React from 'react';
import './SearchBar.css';

class SearchBar extends React.Component {

    render() {
        const { 
            height, width, 
            query, onChange 
        } = this.props;

        const halfHeight = Math.floor(height/2);
        const halfWidth  = Math.floor(width/2);

        return <svg width={width} height={height} viewBox={"0 0 " + width + " " + height}>
            <path fill="#E0E0E0" stroke="none" d={`
                M 0,`+halfHeight+`
                C 0,0 0,0 `+halfWidth+`,0
                S `+width+`,0 `+width+`,`+halfHeight+`
                `+width+`,`+height+` `+halfWidth+`,`+height+`
                0,`+height+` 0,`+halfHeight
            }></path>
            <foreignObject x="0px" y="0px" width={width} height={height}>
                <input 
                    type="text" 
                    id="searchbar" 
                    name="searchbar"
                    placeholder="Filter by name..."
                    value={query}
                    onChange={onChange}
                />
            </foreignObject>
        </svg>
        
        
        
        
        
        
    }
}

export default SearchBar;