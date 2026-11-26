// Exhaustive/sampled test of conj:ham. Graph = cycle 0..n-1 plus chord subset.
// usage: ham n mode [arg1 arg2]   mode: all | few K | rand N seed
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
static int n; static int chordA[64],chordB[64],nch;
static int adj[16], D[16][16];
static uint16_t dp[1<<12];
static inline int pc(unsigned x){return __builtin_popcount(x);}
static void compD(void){
  for(int u=0;u<n;u++){
    int full=1<<n; memset(dp,0,sizeof(uint16_t)*full);
    int best[16]; for(int i=0;i<n;i++)best[i]=0;
    dp[1<<u]=1<<u;
    for(int m=1;m<full;m++){ unsigned ends=dp[m]; if(!ends)continue; int l=pc(m)-1;
      while(ends){int v=__builtin_ctz(ends); ends&=ends-1; if(l>best[v])best[v]=l;
        unsigned nx=adj[v]&~m; while(nx){int b=__builtin_ctz(nx); nx&=nx-1; dp[m|(1<<b)]|=1<<b;}}}
    for(int v=0;v<n;v++)D[u][v]=best[v];
  }
}
static inline int isddd(int S){
  int full=(1<<n)-1;
  for(int w=0;w<n;w++){ if(S>>w&1)continue; unsigned seen=0; int T=S;
    while(T){int x=__builtin_ctz(T);T&=T-1; unsigned b=1u<<D[w][x]; if(seen&b)return 0; seen|=b;} }
  return 1;
}
static long long viol_claim[16]; static long long hist[16]; static int maxS; static long long cnt;
static int doclaims; static long long nclaimsets;
static int has(int a,int b){return adj[a]>>b&1;}
static void claims(int S,int s){
  // C1: s>=3 => n>=3s
  if(s>=3 && n<3*s) viol_claim[0]++;
  // run structure on fixed cycle
  // count runs
  int runs=0; for(int i=0;i<n;i++) if((S>>i&1) && !(S>>((i+n-1)%n)&1)) runs++;
  if(runs>=2 && n-s<2*s) viol_claim[1]++; // multi-run claim: n-s>=2s
  if(runs==1){
    int t=n-s;
    for(int dir=1;dir>=-1;dir-=2) for(int r=0;r<n;r++){
      // x_k = pos(k-1), k=1..s; y_k = pos(s+k-1), k=1..t ; need S equal set
      int pos[16]; for(int k=0;k<n;k++) pos[k]=((r+dir*k)%n+n)%n;
      int M=0; for(int k=0;k<s;k++)M|=1<<pos[k]; if(M!=S)continue;
      nclaimsets++;
      #define X(k) pos[(k)-1]
      #define Y(k) pos[s+(k)-1]
      // T1 eq (1)
      for(int j=1;j<=s;j++){ if(D[Y(1)][X(j)]!=t+j-1||D[Y(t)][X(j)]!=n-j) viol_claim[2]++; }
      // T2 chords in S, y1-xj, yt-xj
      for(int j=1;j<=s;j++)for(int k=j+2;k<=s;k++) if(has(X(j),X(k))) viol_claim[3]++;
      for(int j=1;j<s;j++) if(has(Y(1),X(j))) viol_claim[4]++;
      for(int j=2;j<=s;j++) if(has(Y(t),X(j))) viol_claim[4]++;
      // T3 (2)
      for(int i=2;i<t;i++)for(int j=1;j<=s;j++) if(has(Y(i),X(j))){
        if(j>=2 && i-1<s) viol_claim[5]++;
        if(j<=s-1 && t-i<s) viol_claim[5]++; }
      // T4: structure holds? S induced path attached only by y1xs, ytx1
      int ok=1; for(int a=1;a<=s&&ok;a++){ for(int b=1;b<=s;b++) if(a!=b){ int e=has(X(a),X(b)); if(e!=(abs(a-b)==1)) ok=0; }
        for(int b=1;b<=t;b++) if(has(X(a),Y(b))){ if(!((a==s&&b==1)||(a==1&&b==t))) ok=0; } }
      if(ok){ // compute D_H from y1 and yt to all y: via D within H: brute DFS
        int nb=t; int hadj[16]; for(int a=1;a<=t;a++){hadj[a-1]=0; for(int b=1;b<=t;b++) if(a!=b&&has(Y(a),Y(b))) hadj[a-1]|=1<<(b-1);}
        // longest path in H from y1 / yt: dp
        for(int which=0;which<2;which++){
          int src=which?t-1:0; static uint16_t d2[1<<12]; memset(d2,0,sizeof(uint16_t)*(1<<t)); int bestH[16]={0};
          d2[1<<src]=1<<src;
          for(int m=1;m<(1<<t);m++){unsigned e=d2[m]; if(!e)continue; int l=pc(m)-1; while(e){int v=__builtin_ctz(e);e&=e-1; if(l>bestH[v])bestH[v]=l; unsigned nx=hadj[v]&~m; while(nx){int b=__builtin_ctz(nx);nx&=nx-1; d2[m|(1<<b)]|=1<<b;}}}
          for(int a=0;a<t;a++){ if(which==0)D[15][a]=0; }
          static int AA[16],BB[16]; for(int a=0;a<t;a++){ if(which==0)AA[a]=bestH[a]; else BB[a]=bestH[a]; }
          if(which==1){
            for(int a=0;a<t;a++){ int w=Y(a+1);
              for(int j=1;j<=s;j++){ int f=AA[a]+s+1-j, g=BB[a]+j; int mx=f>g?f:g; if(D[w][X(j)]!=mx) viol_claim[6]++; }
              // (4) when S is DDD (it is) -- w outside S
              if(abs(AA[a]-BB[a])<s-1) viol_claim[7]++;
              int mn=AA[a]<BB[a]?AA[a]:BB[a]; if(mn>t-s) viol_claim[8]++;
            }
          }
        }
      }
    }
  }
}
static void process(uint64_t chords){
  for(int i=0;i<n;i++)adj[i]=0;
  for(int i=0;i<n;i++){int j=(i+1)%n; adj[i]|=1<<j; adj[j]|=1<<i;}
  for(int c=0;c<nch;c++) if(chords>>c&1){adj[chordA[c]]|=1<<chordB[c]; adj[chordB[c]]|=1<<chordA[c];}
  compD(); cnt++;
  int best=1, bestS=1; int full=(1<<n)-1;
  for(int S=1;S<full;S++){ int s=pc(S); if(s<2)continue; if(!doclaims && s<=best)continue; if(isddd(S)){ if(s>best){best=s;bestS=S;} if(doclaims) claims(S,s);} }
  hist[best]++; if(best>maxS)maxS=best;
  int bound=n/3<2?2:n/3;
  if(best>bound){ printf("VIOLATION n=%d DDD=%d set=0x%x chords:",n,best,bestS); for(int c=0;c<nch;c++)if(chords>>c&1)printf(" %d-%d",chordA[c],chordB[c]); printf("\n"); fflush(stdout);}
}
static uint64_t rs;
static uint64_t rnd(void){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
int main(int argc,char**argv){
  n=atoi(argv[1]); char*mode=argv[2];
  nch=0; for(int i=0;i<n;i++)for(int j=i+2;j<n;j++){ if(i==0&&j==n-1)continue; chordA[nch]=i;chordB[nch]=j;nch++; }
  doclaims = n<=8 && strcmp(mode,"all")==0;
  if(!strcmp(mode,"all")){ for(uint64_t c=0;c<(1ULL<<nch);c++) process(c); }
  else if(!strcmp(mode,"part")){ uint64_t k=atoll(argv[3]),m=atoll(argv[4]); uint64_t tot=1ULL<<nch; for(uint64_t c=tot/m*k;c<tot/m*(k+1);c++) process(c); }
  else if(!strcmp(mode,"few")){ int K=atoi(argv[3]); // all with <=K chords
    for(uint64_t c=0;c<(1ULL<<nch);c++){ if(pc(c&0xffffffffu)>K)continue; process(c);} }
  else if(!strcmp(mode,"rand")){ long N=atol(argv[3]); rs=atoll(argv[4])*0x9E3779B97F4A7C15ULL+88172645463325252ULL; for(int i=0;i<10;i++)rnd();
    for(long i=0;i<N;i++){ int dens=1+rnd()%7; uint64_t c=0; for(int k=0;k<nch;k++) if((int)(rnd()%16)<dens*2) c|=1ULL<<k; process(c);} }
  printf("n=%d mode=%s graphs=%lld maxDDD=%d bound=%d hist:",n,mode,cnt,maxS,n/3<2?2:n/3);
  for(int k=1;k<=n;k++) if(hist[k]) printf(" %d:%lld",k,hist[k]); printf("\n");
  if(doclaims){ printf("claim-sets(single-run DDD, with orientation) = %lld\n",nclaimsets);
    const char*nm[]={"C1 s>=3=>n>=3s","C2 multi-run n-s>=2s","T1 eq(1)","T2a no chord inside S","T2b y1/yt attachments","T3 eq(2)","T4a formula(3)","T4b ineq(4)","T4c min(A,B)<=t-s"};
    for(int i=0;i<9;i++) printf("  violations %-26s %lld\n",nm[i],viol_claim[i]); }
  return 0; }
