#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;

        int arr[n];
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        int swaps=0;
        for(int i=0;i<n;i++)
        {
            for(int j=n-1;j>0;j--)
            {
                if(arr[i]&arr[j]==0)
                {
                    i++;
                }
                else if (arr[i]<arr[j])
                {
                    int temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                    swaps++;
                    i++;
                    j--;
                }
                else
                {
                    i++;
                }
            }
        }
        if(swaps==0)
        {
            cout<<"Yes"<<endl;
        }
        else
        {
            cout<<"No"<<endl;
        }
    }
}