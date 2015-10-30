/*************************************************************************
 *  Compilation:  javac StdRandom.java
 *  Execution:    java StdRandom
 *  Dependencies: StdOut.java
 *
 *  A library of static methods to generate pseudo-random numbers from
 *  different distributions (bernoulli, uniform, gaussian, discrete,
 *  and exponential). Also includes a method for shuffling an array.
 *
 *
 *  %  java StdRandom 5
 *  seed = 1316600602069
 *  59 16.81826  true 8.83954  0 
 *  32 91.32098  true 9.11026  0 
 *  35 10.11874  true 8.95396  3 
 *  92 32.88401  true 8.87089  0 
 *  72 92.55791  true 9.46241  0 
 *
 *  % java StdRandom 5
 *  seed = 1316600616575
 *  96 60.17070  true 8.72821  0 
 *  79 32.01607  true 8.58159  0 
 *  81 59.49065  true 9.10423  1 
 *  96 51.65818  true 9.02102  0 
 *  99 17.55771  true 8.99762  0 
 *
 *  % java StdRandom 5 1316600616575
 *  seed = 1316600616575
 *  96 60.17070  true 8.72821  0 
 *  79 32.01607  true 8.58159  0 
 *  81 59.49065  true 9.10423  1 
 *  96 51.65818  true 9.02102  0 
 *  99 17.55771  true 8.99762  0 
 *
 *
 *  Remark
 *  ------
 *    - Relies on randomness of nextDouble() method in java.util.Random
 *      to generate pseudorandom numbers in [0, 1).
 *
 *    - This library allows you to set and get the pseudorandom number seed.
 *
 *    - See http://www.honeylocust.com/RngPack/ for an industrial
 *      strength random number generator in Java.
 *
 *************************************************************************/		//COMMENT 
		//
import java.util.Random;		//IMPORT IDENTIFIER DOT IDENTIFIER DOT IDENTIFIER SEMICOLON 
		//
/**
 *  <i>Standard random</i>. This class provides methods for generating
 *  random number from various distributions.
 *  <p>
 *  For additional documentation, see <a href="http://introcs.cs.princeton.edu/22library">Section 2.2</a> of
 *  <i>Introduction to Programming in Java: An Interdisciplinary Approach</i> by Robert Sedgewick and Kevin Wayne.
 *
 *  @author Robert Sedgewick
 *  @author Kevin Wayne
 */		//COMMENT 
public final class StdRandom {		//PUBLIC FINAL CLASS IDENTIFIER LCURPAREN 
		//
    private static Random random;    // pseudo-random number generator		//PRIVATE STATIC IDENTIFIER IDENTIFIER SEMICOLON COMMENT 
    private static long seed;        // pseudo-random number generator seed		//PRIVATE STATIC LONG IDENTIFIER SEMICOLON COMMENT 
		//
    // static initializer		//COMMENT 
    static {		//STATIC LCURPAREN 
        // this is how the seed was set in Java 1.4		//COMMENT 
        seed = System.currentTimeMillis();		//IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER LROUNPAREN RROUNPAREN SEMICOLON 
        random = new Random(seed);		//IDENTIFIER OPERATOR NEW IDENTIFIER LROUNPAREN IDENTIFIER RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    // don't instantiate		//COMMENT 
    private StdRandom() { }		//PRIVATE IDENTIFIER LROUNPAREN RROUNPAREN LCURPAREN RCURPAREN 
		//
    /**
     * Sets the seed of the psedurandom number generator.
     */		//COMMENT 
    public static void setSeed(long s) {		//PUBLIC STATIC VOID IDENTIFIER LROUNPAREN LONG IDENTIFIER RROUNPAREN LCURPAREN 
        seed   = s;		//IDENTIFIER OPERATOR IDENTIFIER SEMICOLON 
        random = new Random(seed);		//IDENTIFIER OPERATOR NEW IDENTIFIER LROUNPAREN IDENTIFIER RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns the seed of the psedurandom number generator.
     */		//COMMENT 
    public static long getSeed() {		//PUBLIC STATIC LONG IDENTIFIER LROUNPAREN RROUNPAREN LCURPAREN 
        return seed;		//RETURN IDENTIFIER SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Return real number uniformly in [0, 1).
     */		//COMMENT 
    public static double uniform() {		//PUBLIC STATIC DOUBLE IDENTIFIER LROUNPAREN RROUNPAREN LCURPAREN 
        return random.nextDouble();		//RETURN IDENTIFIER DOT IDENTIFIER LROUNPAREN RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns an integer uniformly between 0 (inclusive) and N (exclusive).
     * @throws IllegalArgumentException if <tt>N <= 0</tt>
     */		//COMMENT 
    public static int uniform(int N) {		//PUBLIC STATIC INT IDENTIFIER LROUNPAREN INT IDENTIFIER RROUNPAREN LCURPAREN 
        if (N <= 0) throw new IllegalArgumentException("Parameter N must be positive");		//IF LROUNPAREN IDENTIFIER OPERATOR INT_CONST RROUNPAREN THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        return random.nextInt(N);		//RETURN IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    ///////////////////////////////////////////////////////////////////////////		//COMMENT 
    //  STATIC METHODS BELOW RELY ON JAVA.UTIL.RANDOM ONLY INDIRECTLY VIA		//COMMENT 
    //  THE STATIC METHODS ABOVE.		//COMMENT 
    ///////////////////////////////////////////////////////////////////////////		//COMMENT 
		//
    /**
     * Returns a real number uniformly in [0, 1).
     * @deprecated clearer to use {@link #uniform()}
     */		//COMMENT 
    public static double random() {		//PUBLIC STATIC DOUBLE IDENTIFIER LROUNPAREN RROUNPAREN LCURPAREN 
        return uniform();		//RETURN IDENTIFIER LROUNPAREN RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns an integer uniformly in [a, b).
     * @throws IllegalArgumentException if <tt>b <= a</tt>
     * @throws IllegalArgumentException if <tt>b - a >= Integer.MAX_VALUE</tt>
     */		//COMMENT 
    public static int uniform(int a, int b) {		//PUBLIC STATIC INT IDENTIFIER LROUNPAREN INT IDENTIFIER COMMA INT IDENTIFIER RROUNPAREN LCURPAREN 
        if (b <= a) throw new IllegalArgumentException("Invalid range");		//IF LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        if ((long) b - a >= Integer.MAX_VALUE) throw new IllegalArgumentException("Invalid range");		//IF LROUNPAREN LROUNPAREN LONG RROUNPAREN IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER RROUNPAREN THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        return a + uniform(b - a);		//RETURN IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns a real number uniformly in [a, b).
     * @throws IllegalArgumentException unless <tt>a < b</tt>
     */		//COMMENT 
    public static double uniform(double a, double b) {		//PUBLIC STATIC DOUBLE IDENTIFIER LROUNPAREN DOUBLE IDENTIFIER COMMA DOUBLE IDENTIFIER RROUNPAREN LCURPAREN 
        if (!(a < b)) throw new IllegalArgumentException("Invalid range");		//IF LROUNPAREN OPERATOR LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN RROUNPAREN THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        return a + uniform() * (b-a);		//RETURN IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN RROUNPAREN OPERATOR LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns a boolean, which is true with probability p, and false otherwise.
     * @throws IllegalArgumentException unless <tt>p >= 0.0</tt> and <tt>p <= 1.0</tt>
     */		//COMMENT 
    public static boolean bernoulli(double p) {		//PUBLIC STATIC BOOLEAN IDENTIFIER LROUNPAREN DOUBLE IDENTIFIER RROUNPAREN LCURPAREN 
        if (!(p >= 0.0 && p <= 1.0))		//IF LROUNPAREN OPERATOR LROUNPAREN IDENTIFIER OPERATOR FLOAT_CONST OPERATOR IDENTIFIER OPERATOR FLOAT_CONST RROUNPAREN RROUNPAREN 
            throw new IllegalArgumentException("Probability must be between 0.0 and 1.0");		//THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        return uniform() < p;		//RETURN IDENTIFIER LROUNPAREN RROUNPAREN OPERATOR IDENTIFIER SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns a boolean, which is true with probability .5, and false otherwise.
     */		//COMMENT 
    public static boolean bernoulli() {		//PUBLIC STATIC BOOLEAN IDENTIFIER LROUNPAREN RROUNPAREN LCURPAREN 
        return bernoulli(0.5);		//RETURN IDENTIFIER LROUNPAREN FLOAT_CONST RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns a real number with a standard Gaussian distribution.
     */		//COMMENT 
    public static double gaussian() {		//PUBLIC STATIC DOUBLE IDENTIFIER LROUNPAREN RROUNPAREN LCURPAREN 
        // use the polar form of the Box-Muller transform		//COMMENT 
        double r, x, y;		//DOUBLE IDENTIFIER COMMA IDENTIFIER COMMA IDENTIFIER SEMICOLON 
        do {		//DO LCURPAREN 
            x = uniform(-1.0, 1.0);		//IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN OPERATOR FLOAT_CONST COMMA FLOAT_CONST RROUNPAREN SEMICOLON 
            y = uniform(-1.0, 1.0);		//IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN OPERATOR FLOAT_CONST COMMA FLOAT_CONST RROUNPAREN SEMICOLON 
            r = x*x + y*y;		//IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER SEMICOLON 
        } while (r >= 1 || r == 0);		//RCURPAREN WHILE LROUNPAREN IDENTIFIER OPERATOR INT_CONST OPERATOR OPERATOR IDENTIFIER OPERATOR INT_CONST RROUNPAREN SEMICOLON 
        return x * Math.sqrt(-2 * Math.log(r) / r);		//RETURN IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER LROUNPAREN OPERATOR INT_CONST OPERATOR IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER RROUNPAREN OPERATOR IDENTIFIER RROUNPAREN SEMICOLON 
		//
        // Remark:  y * Math.sqrt(-2 * Math.log(r) / r)		//COMMENT 
        // is an independent random gaussian		//COMMENT 
    }		//RCURPAREN 
		//
    /**
     * Returns a real number from a gaussian distribution with given mean and stddev
     */		//COMMENT 
    public static double gaussian(double mean, double stddev) {		//PUBLIC STATIC DOUBLE IDENTIFIER LROUNPAREN DOUBLE IDENTIFIER COMMA DOUBLE IDENTIFIER RROUNPAREN LCURPAREN 
        return mean + stddev * gaussian();		//RETURN IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns an integer with a geometric distribution with mean 1/p.
     * @throws IllegalArgumentException unless <tt>p >= 0.0</tt> and <tt>p <= 1.0</tt>
     */		//COMMENT 
    public static int geometric(double p) {		//PUBLIC STATIC INT IDENTIFIER LROUNPAREN DOUBLE IDENTIFIER RROUNPAREN LCURPAREN 
        if (!(p >= 0.0 && p <= 1.0))		//IF LROUNPAREN OPERATOR LROUNPAREN IDENTIFIER OPERATOR FLOAT_CONST OPERATOR IDENTIFIER OPERATOR FLOAT_CONST RROUNPAREN RROUNPAREN 
            throw new IllegalArgumentException("Probability must be between 0.0 and 1.0");		//THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        // using algorithm given by Knuth		//COMMENT 
        return (int) Math.ceil(Math.log(uniform()) / Math.log(1.0 - p));		//RETURN LROUNPAREN INT RROUNPAREN IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER LROUNPAREN RROUNPAREN RROUNPAREN OPERATOR IDENTIFIER DOT IDENTIFIER LROUNPAREN FLOAT_CONST OPERATOR IDENTIFIER RROUNPAREN RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Return an integer with a Poisson distribution with mean lambda.
     * @throws IllegalArgumentException unless <tt>lambda > 0.0</tt> and not infinite
     */		//COMMENT 
    public static int poisson(double lambda) {		//PUBLIC STATIC INT IDENTIFIER LROUNPAREN DOUBLE IDENTIFIER RROUNPAREN LCURPAREN 
        if (!(lambda > 0.0))		//IF LROUNPAREN OPERATOR LROUNPAREN IDENTIFIER OPERATOR FLOAT_CONST RROUNPAREN RROUNPAREN 
            throw new IllegalArgumentException("Parameter lambda must be positive");		//THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        if (Double.isInfinite(lambda))		//IF LROUNPAREN IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER RROUNPAREN RROUNPAREN 
            throw new IllegalArgumentException("Parameter lambda must not be infinite");		//THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        // using algorithm given by Knuth		//COMMENT 
        // see http://en.wikipedia.org/wiki/Poisson_distribution		//COMMENT 
        int k = 0;		//INT IDENTIFIER OPERATOR INT_CONST SEMICOLON 
        double p = 1.0;		//DOUBLE IDENTIFIER OPERATOR FLOAT_CONST SEMICOLON 
        double L = Math.exp(-lambda);		//DOUBLE IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER LROUNPAREN OPERATOR IDENTIFIER RROUNPAREN SEMICOLON 
        do {		//DO LCURPAREN 
            k++;		//IDENTIFIER OPERATOR OPERATOR SEMICOLON 
            p *= uniform();		//IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN RROUNPAREN SEMICOLON 
        } while (p >= L);		//RCURPAREN WHILE LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN SEMICOLON 
        return k-1;		//RETURN IDENTIFIER OPERATOR INT_CONST SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns a real number with a Pareto distribution with parameter alpha.
     * @throws IllegalArgumentException unless <tt>alpha > 0.0</tt>
     */		//COMMENT 
    public static double pareto(double alpha) {		//PUBLIC STATIC DOUBLE IDENTIFIER LROUNPAREN DOUBLE IDENTIFIER RROUNPAREN LCURPAREN 
        if (!(alpha > 0.0))		//IF LROUNPAREN OPERATOR LROUNPAREN IDENTIFIER OPERATOR FLOAT_CONST RROUNPAREN RROUNPAREN 
            throw new IllegalArgumentException("Shape parameter alpha must be positive");		//THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        return Math.pow(1 - uniform(), -1.0/alpha) - 1.0;		//RETURN IDENTIFIER DOT IDENTIFIER LROUNPAREN INT_CONST OPERATOR IDENTIFIER LROUNPAREN RROUNPAREN COMMA OPERATOR FLOAT_CONST OPERATOR IDENTIFIER RROUNPAREN OPERATOR FLOAT_CONST SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns a real number with a Cauchy distribution.
     */		//COMMENT 
    public static double cauchy() {		//PUBLIC STATIC DOUBLE IDENTIFIER LROUNPAREN RROUNPAREN LCURPAREN 
        return Math.tan(Math.PI * (uniform() - 0.5));		//RETURN IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER DOT IDENTIFIER OPERATOR LROUNPAREN IDENTIFIER LROUNPAREN RROUNPAREN OPERATOR FLOAT_CONST RROUNPAREN RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Returns a number from a discrete distribution: i with probability a[i].
     * throws IllegalArgumentException if sum of array entries is not (very nearly) equal to <tt>1.0</tt>
     * throws IllegalArgumentException unless <tt>a[i] >= 0.0</tt> for each index <tt>i</tt>
     */		//COMMENT 
    public static int discrete(double[] a) {		//PUBLIC STATIC INT IDENTIFIER LROUNPAREN DOUBLE LSQPAREN RSQPAREN IDENTIFIER RROUNPAREN LCURPAREN 
        double EPSILON = 1E-14;		//DOUBLE IDENTIFIER OPERATOR FLOAT_CONST SEMICOLON 
        double sum = 0.0;		//DOUBLE IDENTIFIER OPERATOR FLOAT_CONST SEMICOLON 
        for (int i = 0; i < a.length; i++) {		//FOR LROUNPAREN INT IDENTIFIER OPERATOR INT_CONST SEMICOLON IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER SEMICOLON IDENTIFIER OPERATOR OPERATOR RROUNPAREN LCURPAREN 
            if (!(a[i] >= 0.0)) throw new IllegalArgumentException("array entry " + i + " must be nonnegative: " + a[i]);		//IF LROUNPAREN OPERATOR LROUNPAREN IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR FLOAT_CONST RROUNPAREN RROUNPAREN THROW NEW IDENTIFIER LROUNPAREN STRING OPERATOR IDENTIFIER OPERATOR STRING OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN RROUNPAREN SEMICOLON 
            sum = sum + a[i];		//IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
        }		//RCURPAREN 
        if (sum > 1.0 + EPSILON || sum < 1.0 - EPSILON)		//IF LROUNPAREN IDENTIFIER OPERATOR FLOAT_CONST OPERATOR IDENTIFIER OPERATOR OPERATOR IDENTIFIER OPERATOR FLOAT_CONST OPERATOR IDENTIFIER RROUNPAREN 
            throw new IllegalArgumentException("sum of array entries does not approximately equal 1.0: " + sum);		//THROW NEW IDENTIFIER LROUNPAREN STRING OPERATOR IDENTIFIER RROUNPAREN SEMICOLON 
		//
        // the for loop may not return a value when both r is (nearly) 1.0 and when the		//COMMENT 
        // cumulative sum is less than 1.0 (as a result of floating-point roundoff error)		//COMMENT 
        while (true) {		//WHILE LROUNPAREN BOOLEAN_CONST RROUNPAREN LCURPAREN 
            double r = uniform();		//DOUBLE IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN RROUNPAREN SEMICOLON 
            sum = 0.0;		//IDENTIFIER OPERATOR FLOAT_CONST SEMICOLON 
            for (int i = 0; i < a.length; i++) {		//FOR LROUNPAREN INT IDENTIFIER OPERATOR INT_CONST SEMICOLON IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER SEMICOLON IDENTIFIER OPERATOR OPERATOR RROUNPAREN LCURPAREN 
                sum = sum + a[i];		//IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
                if (sum > r) return i;		//IF LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN RETURN IDENTIFIER SEMICOLON 
            }		//RCURPAREN 
        }		//RCURPAREN 
    }		//RCURPAREN 
		//
    /**
     * Returns a real number from an exponential distribution with rate lambda.
     * @throws IllegalArgumentException unless <tt>lambda > 0.0</tt>
     */		//COMMENT 
    public static double exp(double lambda) {		//PUBLIC STATIC DOUBLE IDENTIFIER LROUNPAREN DOUBLE IDENTIFIER RROUNPAREN LCURPAREN 
        if (!(lambda > 0.0))		//IF LROUNPAREN OPERATOR LROUNPAREN IDENTIFIER OPERATOR FLOAT_CONST RROUNPAREN RROUNPAREN 
            throw new IllegalArgumentException("Rate lambda must be positive");		//THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        return -Math.log(1 - uniform()) / lambda;		//RETURN OPERATOR IDENTIFIER DOT IDENTIFIER LROUNPAREN INT_CONST OPERATOR IDENTIFIER LROUNPAREN RROUNPAREN RROUNPAREN OPERATOR IDENTIFIER SEMICOLON 
    }		//RCURPAREN 
		//
    /**
     * Rearrange the elements of an array in random order.
     */		//COMMENT 
    public static void shuffle(Object[] a) {		//PUBLIC STATIC VOID IDENTIFIER LROUNPAREN IDENTIFIER LSQPAREN RSQPAREN IDENTIFIER RROUNPAREN LCURPAREN 
        int N = a.length;		//INT IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER SEMICOLON 
        for (int i = 0; i < N; i++) {		//FOR LROUNPAREN INT IDENTIFIER OPERATOR INT_CONST SEMICOLON IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR OPERATOR RROUNPAREN LCURPAREN 
            int r = i + uniform(N-i);     // between i and N-1		//INT IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN SEMICOLON COMMENT 
            Object temp = a[i];		//IDENTIFIER IDENTIFIER OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[i] = a[r];		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[r] = temp;		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER SEMICOLON 
        }		//RCURPAREN 
    }		//RCURPAREN 
		//
    /**
     * Rearrange the elements of a double array in random order.
     */		//COMMENT 
    public static void shuffle(double[] a) {		//PUBLIC STATIC VOID IDENTIFIER LROUNPAREN DOUBLE LSQPAREN RSQPAREN IDENTIFIER RROUNPAREN LCURPAREN 
        int N = a.length;		//INT IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER SEMICOLON 
        for (int i = 0; i < N; i++) {		//FOR LROUNPAREN INT IDENTIFIER OPERATOR INT_CONST SEMICOLON IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR OPERATOR RROUNPAREN LCURPAREN 
            int r = i + uniform(N-i);     // between i and N-1		//INT IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN SEMICOLON COMMENT 
            double temp = a[i];		//DOUBLE IDENTIFIER OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[i] = a[r];		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[r] = temp;		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER SEMICOLON 
        }		//RCURPAREN 
    }		//RCURPAREN 
		//
    /**
     * Rearrange the elements of an int array in random order.
     */		//COMMENT 
    public static void shuffle(int[] a) {		//PUBLIC STATIC VOID IDENTIFIER LROUNPAREN INT LSQPAREN RSQPAREN IDENTIFIER RROUNPAREN LCURPAREN 
        int N = a.length;		//INT IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER SEMICOLON 
        for (int i = 0; i < N; i++) {		//FOR LROUNPAREN INT IDENTIFIER OPERATOR INT_CONST SEMICOLON IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR OPERATOR RROUNPAREN LCURPAREN 
            int r = i + uniform(N-i);     // between i and N-1		//INT IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN SEMICOLON COMMENT 
            int temp = a[i];		//INT IDENTIFIER OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[i] = a[r];		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[r] = temp;		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER SEMICOLON 
        }		//RCURPAREN 
    }		//RCURPAREN 
		//
		//
    /**
     * Rearrange the elements of the subarray a[lo..hi] in random order.
     */		//COMMENT 
    public static void shuffle(Object[] a, int lo, int hi) {		//PUBLIC STATIC VOID IDENTIFIER LROUNPAREN IDENTIFIER LSQPAREN RSQPAREN IDENTIFIER COMMA INT IDENTIFIER COMMA INT IDENTIFIER RROUNPAREN LCURPAREN 
        if (lo < 0 || lo > hi || hi >= a.length) {		//IF LROUNPAREN IDENTIFIER OPERATOR INT_CONST OPERATOR OPERATOR IDENTIFIER OPERATOR IDENTIFIER OPERATOR OPERATOR IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER RROUNPAREN LCURPAREN 
            throw new IndexOutOfBoundsException("Illegal subarray range");		//THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        }		//RCURPAREN 
        for (int i = lo; i <= hi; i++) {		//FOR LROUNPAREN INT IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR OPERATOR RROUNPAREN LCURPAREN 
            int r = i + uniform(hi-i+1);     // between i and hi		//INT IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER OPERATOR INT_CONST RROUNPAREN SEMICOLON COMMENT 
            Object temp = a[i];		//IDENTIFIER IDENTIFIER OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[i] = a[r];		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[r] = temp;		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER SEMICOLON 
        }		//RCURPAREN 
    }		//RCURPAREN 
		//
    /**
     * Rearrange the elements of the subarray a[lo..hi] in random order.
     */		//COMMENT 
    public static void shuffle(double[] a, int lo, int hi) {		//PUBLIC STATIC VOID IDENTIFIER LROUNPAREN DOUBLE LSQPAREN RSQPAREN IDENTIFIER COMMA INT IDENTIFIER COMMA INT IDENTIFIER RROUNPAREN LCURPAREN 
        if (lo < 0 || lo > hi || hi >= a.length) {		//IF LROUNPAREN IDENTIFIER OPERATOR INT_CONST OPERATOR OPERATOR IDENTIFIER OPERATOR IDENTIFIER OPERATOR OPERATOR IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER RROUNPAREN LCURPAREN 
            throw new IndexOutOfBoundsException("Illegal subarray range");		//THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        }		//RCURPAREN 
        for (int i = lo; i <= hi; i++) {		//FOR LROUNPAREN INT IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR OPERATOR RROUNPAREN LCURPAREN 
            int r = i + uniform(hi-i+1);     // between i and hi		//INT IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER OPERATOR INT_CONST RROUNPAREN SEMICOLON COMMENT 
            double temp = a[i];		//DOUBLE IDENTIFIER OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[i] = a[r];		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[r] = temp;		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER SEMICOLON 
        }		//RCURPAREN 
    }		//RCURPAREN 
		//
    /**
     * Rearrange the elements of the subarray a[lo..hi] in random order.
     */		//COMMENT 
    public static void shuffle(int[] a, int lo, int hi) {		//PUBLIC STATIC VOID IDENTIFIER LROUNPAREN INT LSQPAREN RSQPAREN IDENTIFIER COMMA INT IDENTIFIER COMMA INT IDENTIFIER RROUNPAREN LCURPAREN 
        if (lo < 0 || lo > hi || hi >= a.length) {		//IF LROUNPAREN IDENTIFIER OPERATOR INT_CONST OPERATOR OPERATOR IDENTIFIER OPERATOR IDENTIFIER OPERATOR OPERATOR IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER RROUNPAREN LCURPAREN 
            throw new IndexOutOfBoundsException("Illegal subarray range");		//THROW NEW IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        }		//RCURPAREN 
        for (int i = lo; i <= hi; i++) {		//FOR LROUNPAREN INT IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR OPERATOR RROUNPAREN LCURPAREN 
            int r = i + uniform(hi-i+1);     // between i and hi		//INT IDENTIFIER OPERATOR IDENTIFIER OPERATOR IDENTIFIER LROUNPAREN IDENTIFIER OPERATOR IDENTIFIER OPERATOR INT_CONST RROUNPAREN SEMICOLON COMMENT 
            int temp = a[i];		//INT IDENTIFIER OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[i] = a[r];		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN SEMICOLON 
            a[r] = temp;		//IDENTIFIER LSQPAREN IDENTIFIER RSQPAREN OPERATOR IDENTIFIER SEMICOLON 
        }		//RCURPAREN 
    }		//RCURPAREN 
		//
    /**
     * Unit test.
     */		//COMMENT 
    public static void main(String[] args) {		//PUBLIC STATIC VOID IDENTIFIER LROUNPAREN IDENTIFIER LSQPAREN RSQPAREN IDENTIFIER RROUNPAREN LCURPAREN 
        int N = Integer.parseInt(args[0]);		//INT IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER LSQPAREN INT_CONST RSQPAREN RROUNPAREN SEMICOLON 
        if (args.length == 2) StdRandom.setSeed(Long.parseLong(args[1]));		//IF LROUNPAREN IDENTIFIER DOT IDENTIFIER OPERATOR INT_CONST RROUNPAREN IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER LSQPAREN INT_CONST RSQPAREN RROUNPAREN RROUNPAREN SEMICOLON 
        double[] t = { .5, .3, .1, .1 };		//DOUBLE LSQPAREN RSQPAREN IDENTIFIER OPERATOR LCURPAREN FLOAT_CONST COMMA FLOAT_CONST COMMA FLOAT_CONST COMMA FLOAT_CONST RCURPAREN SEMICOLON 
		//
        StdOut.println("seed = " + StdRandom.getSeed());		//IDENTIFIER DOT IDENTIFIER LROUNPAREN STRING OPERATOR IDENTIFIER DOT IDENTIFIER LROUNPAREN RROUNPAREN RROUNPAREN SEMICOLON 
        for (int i = 0; i < N; i++) {		//FOR LROUNPAREN INT IDENTIFIER OPERATOR INT_CONST SEMICOLON IDENTIFIER OPERATOR IDENTIFIER SEMICOLON IDENTIFIER OPERATOR OPERATOR RROUNPAREN LCURPAREN 
            StdOut.printf("%2d "  , uniform(100));		//IDENTIFIER DOT IDENTIFIER LROUNPAREN STRING COMMA IDENTIFIER LROUNPAREN INT_CONST RROUNPAREN RROUNPAREN SEMICOLON 
            StdOut.printf("%8.5f ", uniform(10.0, 99.0));		//IDENTIFIER DOT IDENTIFIER LROUNPAREN STRING COMMA IDENTIFIER LROUNPAREN FLOAT_CONST COMMA FLOAT_CONST RROUNPAREN RROUNPAREN SEMICOLON 
            StdOut.printf("%5b "  , bernoulli(.5));		//IDENTIFIER DOT IDENTIFIER LROUNPAREN STRING COMMA IDENTIFIER LROUNPAREN FLOAT_CONST RROUNPAREN RROUNPAREN SEMICOLON 
            StdOut.printf("%7.5f ", gaussian(9.0, .2));		//IDENTIFIER DOT IDENTIFIER LROUNPAREN STRING COMMA IDENTIFIER LROUNPAREN FLOAT_CONST COMMA FLOAT_CONST RROUNPAREN RROUNPAREN SEMICOLON 
            StdOut.printf("%2d "  , discrete(t));		//IDENTIFIER DOT IDENTIFIER LROUNPAREN STRING COMMA IDENTIFIER LROUNPAREN IDENTIFIER RROUNPAREN RROUNPAREN SEMICOLON 
            StdOut.println();		//IDENTIFIER DOT IDENTIFIER LROUNPAREN RROUNPAREN SEMICOLON 
        }		//RCURPAREN 
		//
        String[] a = "A B C D E F G".split(" ");		//IDENTIFIER LSQPAREN RSQPAREN IDENTIFIER OPERATOR STRING DOT IDENTIFIER LROUNPAREN STRING RROUNPAREN SEMICOLON 
        for (String s : a)		//FOR LROUNPAREN IDENTIFIER IDENTIFIER OPERATOR IDENTIFIER RROUNPAREN 
            StdOut.print(s + " ");		//IDENTIFIER DOT IDENTIFIER LROUNPAREN IDENTIFIER OPERATOR STRING RROUNPAREN SEMICOLON 
        StdOut.println();		//IDENTIFIER DOT IDENTIFIER LROUNPAREN RROUNPAREN SEMICOLON 
    }		//RCURPAREN 
		//
}		//RCURPAREN 
