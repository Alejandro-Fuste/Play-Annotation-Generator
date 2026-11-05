# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_82`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 74 |
| Player Tracks | 74 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 351 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [16-160] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-41] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-56] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-219] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CatchPunt' range [222-224] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-250] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [16-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-97] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [109-117] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-193] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-256] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-285] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-309] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-322] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-429] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-245] for track '6' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [251-297] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-366] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-372] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-485] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-492] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-509] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-526] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [16-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-63] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [16-259] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-298] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-311] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [74-86] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-181] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-208] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-215] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-250] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-263] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-335] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-349] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-374] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [380-385] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-391] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-422] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [425-435] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-448] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-475] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-494] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-500] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [502-508] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-517] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 16, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [16-16] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-24] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-43] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-114] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-243] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [247-351] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-118] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-19] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-15] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-57] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-17] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-27] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-89] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-58] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-91] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-141] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-153] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [97-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-245] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-265] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-184] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-361] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-375] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-135] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-153] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-182] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-199] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-330] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [335-455] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-466] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [469-470] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-258] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-270] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-172] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-185] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-221] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-275] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-332] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-349] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-360] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-226] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-281] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [287-305] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-155] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-178] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-160] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-183] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-198] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-257] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-289] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-301] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-196] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-243] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-290] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-349] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-371] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [373-385] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-177] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-193] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-199] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-347] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [351-363] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-520] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-213] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-306] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [311-354] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-364] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-374] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-379] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-388] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-435] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-535] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-324] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-181] for track '37' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-197] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-279] for track '39' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [284-288] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-316] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-345] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-371] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [374-381] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [383-420] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-328] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-358] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [360-372] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-395] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-211] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-322] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-284] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-298] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-341] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [343-352] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-359] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-412] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-367] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-275] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-301] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-327] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-339] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-405] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [413-418] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-435] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-449] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-454] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-326] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-356] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-354] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-366] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-369] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-493] for track '48' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [496-499] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-404] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [472-483] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-508] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-416] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-569] for track '51' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [356-363] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-372] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-451] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-521] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-543] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-373] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-382] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-377] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-429] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-458] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [386-413] for track '57' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [416-423] for track '57' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [428-433] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-446] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-400] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-433] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [441-443] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-454] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-473] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-482] for track '58' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [490-491] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-504] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-408] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-417] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-478] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-491] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [499-500] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-510] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-518] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-529] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [537-558] for track '59' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [560-561] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-569] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-425] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [430-569] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-412] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-560] for track '61' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [439-440] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-456] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-526] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-486] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-569] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-528] for track '65' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [501-551] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-558] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-562] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-568] for track '73' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.
> - Player track '67' has undefined position. Will map to Position_Unknown.
> - Player track '67' has undefined team_side. Will map to Team_Unknown.
> - Player track '68' has undefined position. Will map to Position_Unknown.
> - Player track '68' has undefined team_side. Will map to Team_Unknown.
> - Player track '69' has undefined position. Will map to Position_Unknown.
> - Player track '69' has undefined team_side. Will map to Team_Unknown.
> - Player track '70' has undefined position. Will map to Position_Unknown.
> - Player track '70' has undefined team_side. Will map to Team_Unknown.
> - Player track '71' has undefined position. Will map to Position_Unknown.
> - Player track '71' has undefined team_side. Will map to Team_Unknown.
> - Player track '72' has undefined position. Will map to Position_Unknown.
> - Player track '72' has undefined team_side. Will map to Team_Unknown.
> - Player track '73' has undefined position. Will map to Position_Unknown.
> - Player track '73' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.