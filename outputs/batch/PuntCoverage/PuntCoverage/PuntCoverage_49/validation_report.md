# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_49`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 154 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 99: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 100: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 100: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SnapReceive' for track '13' has invalid range: start=36, end=30. Clamping end to start.
> - Action 'Action_None' range [58-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-80] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-329] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-36] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-53] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-30] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-35] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-291] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-40] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-288] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-62] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-129] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-329] for track '12' has 8 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-248] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-35] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [39-45] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-44] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-7] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-13] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-65] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-29] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-17] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-44] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-80] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-51] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-67] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-40] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-253] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' for track '26' starts at frame 254, but the player has no visible bounding box on this frame.
> - Action 'Action_Tackle' range [254-254] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [263-264] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [268-275] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [286-291] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-328] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-127] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-291] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-94] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-124] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-154] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-192] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-271] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-117] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-137] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-226] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-283] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-312] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-325] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-175] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-232] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-329] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-267] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-263] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-275] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-329] for track '50' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.