// Example of request to /pdfToImage endpoint using node (version >= 16)
const fs = require('node:fs/promises')
const http = require('node:http')
const path = require('node:path')


async function main(pdfFile) {
  const fullPdfPath = path.resolve(pdfFile)
  const pdfFolder = path.dirname(fullPdfPath)
  const fileName = path.basename(fullPdfPath).replace(/\.pdf$/ig, '')
  const pdfContentBase64 = await fs.readFile(pdfFile, 'base64')
  const imageFile = await fs.open(path.join(pdfFolder, `${fileName}.png`), 'w')
  const imageStream = await imageFile.createWriteStream()

  const options = {
    headers: {
      'Content-Type': 'text/plain',
      'Content-Length': Buffer.byteLength(pdfContentBase64),
    },
    method: 'POST',
  }

  const req = http.request('http://localhost:5000/pdfToImage', options, (res) => {
    res.on('data', (chunk) => {
      imageStream.write(chunk)
    })

    res.on('end', () => {
      imageStream.end()
    })
  })

  req.write(pdfContentBase64)
  req.end()
}

main(process.argv[2])
