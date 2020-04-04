import React from 'react';
import './App.css';
import Button from '../component/button/Button';
import SearchBar from '../component/search-bar/SearchBar'

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            query: "",
        };
    }

    handleQueryUpdated = (event) => {
        this.setState({query: event.target.value});
    }

    render() {
        return <div className="app">
            <div id="center-container">
                <SearchBar 
                    height={50}
                    width={300}
                    query={this.state.query}
                    onChange={this.handleQueryUpdated}
                /><br/>
                <Button
                    height={40}
                    width={100}
                    text="Click me!"
                    onClick={() => console.log("clicked")}
                /><br/>
                test text
            </div>
        </div>
    }
}

export default App;
