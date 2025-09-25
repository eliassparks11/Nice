# Overview

This is a Telegram Bot called "Link-Bypasser-Bot" that specializes in bypassing advertisement links and generating direct download links. The bot accepts various types of shortened URLs, file hosting links, and ad-supported links, then processes them to provide clean, direct access URLs. It supports a wide range of platforms including Google Drive variations, file hosting services, URL shorteners, and streaming platforms.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Core Components

**Bot Framework**: Built using the Pyrogram library for Telegram bot functionality, requiring API credentials (TOKEN, HASH, ID) from Telegram's BotFather and my.telegram.org.

**Link Processing Engine**: The system uses two main modules:
- `bypasser.py`: Handles URL shorteners, ad-supported links, and Google Drive-based platforms
- `ddl.py`: Processes direct download links from file hosting services

**Service Categories**: The bot categorizes supported services into distinct groups:
- Google Drive variants (appdrive, driveapp, gdflix, etc.) 
- File hosting platforms (mediafire, uptobox, pixeldrain, etc.)
- URL shorteners (exe.io, bitly, tinyurl, etc.)
- Streaming services (streamtape, terabox, etc.)

**Authentication System**: Uses service-specific authentication tokens and cookies:
- GDTOT services require CRYPT, XSRF_TOKEN, and Laravel_Session
- Platform-specific CRYPT values for drivefire, kolop, hubdrive, katdrive
- Service tokens for uptobox and terabox cookie authentication

## Processing Logic

**URL Classification**: The system first determines the type of URL using pattern matching and service lists, then routes to appropriate processing functions.

**Scraping Strategy**: Uses multiple HTTP libraries (requests, cloudscraper) with different strategies:
- Standard requests for simple redirects
- CloudScraper for Cloudflare-protected sites  
- BeautifulSoup for HTML parsing and content extraction

**Error Handling**: Implements comprehensive exception handling with fallback mechanisms when primary processing methods fail.

## Command Interface

**CLI Mode**: Includes a standalone command-line interface (`app.py`) for testing and direct usage outside of Telegram.

**Bot Commands**: Supports basic Telegram bot commands:
- `/start`: Welcome message
- `/help`: Lists all supported services and platforms

# External Dependencies

**Telegram Integration**: Pyrogram and tgcrypto for secure Telegram API communication

**Web Scraping**: cloudscraper, requests, and BeautifulSoup for web content processing

**HTML/XML Parsing**: lxml and BeautifulSoup for content extraction from web pages

**Utility Libraries**: urllib3 for URL handling, python-dotenv for environment configuration

**Service-Specific**: lk21 library for specialized content processing

**Authentication**: Various service-specific APIs requiring tokens, cookies, and CRYPT values for accessing protected content