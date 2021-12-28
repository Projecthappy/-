public static void testRandom() {
    Random random = new Random();

    random.setSeed(10000L);

    for(int i = 0 ; i < 10 ; i ++) {
        System.out.println(random.nextInt(1000));
    }
    System.out.println("------------------");
    random = new Random();
    random.setSeed(10000L);
    for(int i = 0 ; i < 10 ; i ++) {
        System.out.println(random.nextInt(1000));
    }

}
