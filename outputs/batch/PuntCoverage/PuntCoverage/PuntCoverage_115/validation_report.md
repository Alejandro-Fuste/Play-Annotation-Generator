# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_115`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_115/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 232: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_Tackle' for track '26' has invalid range: start=187, end=176. Clamping end to start.
> - Action 'Action_PreSnap' range [0-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-188] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-248] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-267] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-248] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-67] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-230] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-275] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-287] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-291] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-40] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-72] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-278] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-270] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-277] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-92] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-160] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-182] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-215] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-288] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_CatchPunt' range [171-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-234] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [238-299] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-37] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-220] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-221] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-297] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-83] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-125] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-92] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-245] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-227] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-220] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-205] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-230] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-231] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-256] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-294] for track '36' has 3 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.