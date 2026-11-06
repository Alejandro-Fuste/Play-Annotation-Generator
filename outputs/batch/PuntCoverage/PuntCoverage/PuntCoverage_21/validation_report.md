# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_21`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 149 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [16-326] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-188] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-239] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-262] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_Tackle' range [263-277] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [279-289] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-154] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [157-254] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-359] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-285] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-331] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-328] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [16-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-174] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [16-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-267] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-358] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-319] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [16-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-178] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-197] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-154] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-307] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-184] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-276] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-280] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-292] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-204] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-339] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-154] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-191] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [252-286] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [290-304] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [309-313] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [327-332] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [335-347] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-282] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-252] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-322] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-294] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-262] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-359] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-248] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-309] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-267] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-265] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-335] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-292] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '44' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.