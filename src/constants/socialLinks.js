import React from "react"
import {
  FaLinkedin,
  FaMedium,
  FaGithubSquare,
  FaTwitterSquare,
} from "react-icons/fa"

export default ({ styleClass }) => {
  const data = [
    {
      id: 1,
      icon: <FaLinkedin className="social-icon"></FaLinkedin>,
      url: "https://www.linkedin.com/in/miroslavpillar/",
    },
    {
      id: 2,
      icon: <FaMedium className="social-icon"></FaMedium>,
      url: "https://medium.com/@pillinho",
    },
    {
      id: 3,
      icon: <FaTwitterSquare className="social-icon"></FaTwitterSquare>,
      url: "https://twitter.com/pillinho_sk",
    },
    {
      id: 4,
      icon: <FaGithubSquare className="social-icon"></FaGithubSquare>,
      url: "https://github.com/Dromediansk",
    },
  ]
  const links = data.map(link => {
    return (
      <li key={link.id}>
        <a href={link.url} className="social-link">
          {link.icon}
        </a>
      </li>
    )
  })

  return (
    <ul className={`social-links ${styleClass ? styleClass : ""}`}>{links}</ul>
  )
}
