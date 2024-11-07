import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import NavBar from './components/NavBar'
import Register from './components/Register'

function App() {
  const [isDark,setIsDark] = useState(false)
  const [isEng, setIsEng] = useState(true)

  function toggleDark(){
    setIsDark( old => !old)
  }

  function toggleLan(){
    setIsEng( old => !old)
  }
  return (
    <>
        <NavBar toggleLan={toggleLan} toggleDark={toggleDark} isDark={isDark} isEng={isEng}/>
        <Register isDark={isDark} isEng={isEng}/>
    </>

  )
}

export default App
