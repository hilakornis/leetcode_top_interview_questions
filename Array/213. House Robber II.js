var robber = function(nums){
	if(nums.length == 1) return nums[0];
	return Math.max(aux(0, nums.length - 2, nums),aux(1, nums.length-1, nums));
}
function aux(startInx, endInx, nums){
	let prev1 = nums[0];
	let prev2 = 0;
	
	for(let i = startInx;i <= endInx; i++){
		let max = Math.max(prev1, prev2 + nums[i]);
		prev2 = prev1;
		prev1 = max;
	}
	
	return prev1;
}