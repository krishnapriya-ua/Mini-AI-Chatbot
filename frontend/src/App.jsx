
import { Button } from "@mui/material"
import { useEffect, useRef, useState } from "react"
import axios from 'axios'
import './styles/home.css'

function App() {
  const [message,setMessage] = useState([])
  const [input,setInput] = useState('')
  const chatendref = useRef(null)

  useEffect(() => {
    chatendref?.current?.scrollIntoView({behavior:'smooth'})
  },[message])

  const handlesend = async() => {
    if(!input.trim()) return
    const response = await axios.post('http://localhost:8000/ask',{input})
    setMessage([...message,{sender:"user",text:input},{sender:"bot",text:response.data.answer}])
    setInput('')
  }
  return (
    <>
     <div className="wrapper">
      <div className="container box">

        <div className="header">
          <p>Mini-AI-Chatbot</p>
        </div>

        <div className="chat">
        {message.map((msg,index) => (
         
          <div key={index} className={`message ${msg.sender}`}>
            <p>{msg.text}</p>
          </div>
        ))}
        <div ref={chatendref} />
        </div>

        <div className="footer">
        <input type="text" value={input} onChange={(e) =>setInput(e.target.value)} onKeyDown={(e)=>e.key==='Enter' && handlesend()}  placeholder="Type here" className="typing"/>
        <Button variant="contained" className="send" onClick={handlesend}>send</Button>
        </div>
      </div>
     </div>
    </>
  )
}

export default App
