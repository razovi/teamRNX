// A lot of crates that you might need are reexported from `superchain-client`
// Checkout the `[dev-dependencies]` section for deps that you might have to include manually
extern crate dotenv;
use tungstenite::http::header::AUTHORIZATION;
use dotenv::dotenv;
use superchain_client::config::Config;
use superchain_client::tungstenite::client::IntoClientRequest;
use superchain_client::{
    ethers::types::H160,
    futures::{self, StreamExt},
    tokio_tungstenite::connect_async,
    WsClient,
};
use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};


/// The list of pairs we want to receive event for
/// An empty list, or `None` means all pairs
/// The block height we want to receive prices from
const FROM_BLOCK: Option<u64> = Some(15_000_000);
/// the block height we want to receive prices to (inclusive)
/// `None` means continue streaming from head
const TO_BLOCK_INC: Option<u64> = None;
/// The websocket endpoint url
const URL: &str = "wss://beta.superchain.app/websocket";

#[tokio::main]
async fn main() {
let PAIRS_FILTER: [H160; 1] = ["0x004375dff511095cc5a197a54140a24efef3a416".parse().unwrap()];
    dotenv().ok();
    // First, we create a new client
    let mut req = URL.into_client_request().expect("invalid url");
    let config = Config::from_env();
    req.headers_mut().append(
        AUTHORIZATION,
        config
            .get_basic_authorization_value()
            .try_into()
            .expect("invalid auth value"),
    );

    let (websocket, _) = connect_async(req).await.unwrap();
    let client = WsClient::new(websocket).await;

    // Then we tell the WsClient that we want uniswap v2 prices
    let stream = client
        .get_prices(PAIRS_FILTER, FROM_BLOCK, TO_BLOCK_INC)
        .await
        .unwrap();
    futures::pin_mut!(stream);


    // And that's it! Now we can stream prices:
    while let Some(res) = stream.next().await {
        let price = res.unwrap();
        let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
        for lream in listener.incoming() {
            let lream = lream.unwrap();
            handle_connection(lream, &price);
            break;
        }
    }
}

fn handle_connection(mut stream: TcpStream, price: &superchain_client::Price) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();
    let boilerplate = "HTTP/1.1 200 OK\r\n\r\n";
    stream.write_all(format!("{}", boilerplate).as_bytes());
    stream.write_all(format!("{price:?}").as_bytes()).expect("unexpected error");
}
