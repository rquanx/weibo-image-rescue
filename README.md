
# Weibo Image Rescue Tool

## Introduction

The Weibo Image Rescue Tool is a command-line utility designed to help you rescue images from Weibo by updating and using CDN information.

## Features

- Update CDN information
- Force update CDN information and rescue image from a specific URL
- Rescue image from a specified URL

## Installation

First, clone the repository:

```bash
git clone https://github.com/rquanx/weibo-image-rescue.git
cd weibo-image-rescue
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Update CDN Information

To update CDN information, use the `-u` flag:

```bash
python main.py -u
```

### Force Update CDN Information and Rescue Image

To force update CDN information and rescue an image from a specific URL, use the `-f` flag followed by the image URL:

```bash
python main.py -f <image_url>
```

### Rescue Image from a Specified URL

To rescue an image from a specified URL without updating the CDN information, simply provide the image URL:

```bash
python main.py <image_url>
```

### Example

```bash
python main.py -f https://example.com/image.jpg
```

## Arguments

- `-u` : Update CDN information.
- `-f` : Force update CDN information and rescue image from URL. Provide the URL after the flag.
- `image_url` : The URL of the image to rescue.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more details on how to contribute.

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more details.

## Acknowledgements

Special thanks to all contributors and the open-source community for their invaluable support and contributions.
