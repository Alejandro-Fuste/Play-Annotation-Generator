# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_72`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_72/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 146: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_DownBlock' for track '4' has invalid range: start=144, end=16. Clamping end to start.
> - Segment 'Action_BallSnap' for track '13' has invalid range: start=139, end=64. Clamping end to start.
> - Segment 'Action_DownBlock' for track '13' has invalid range: start=144, end=64. Clamping end to start.
> - Action 'Action_None' range [139-199] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [147-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [175-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-197] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [199-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-243] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-201] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [165-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [144-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-214] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-217] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-238] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-222] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-276] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-299] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-14] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-24] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-31] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [144-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [152-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-176] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-114] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-187] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-202] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-272] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '35' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.