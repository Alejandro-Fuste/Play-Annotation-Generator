# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_22`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [1-23] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-107] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-233] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-329] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [1-15] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-98] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-163] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-269] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-64] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-141] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-16] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-44] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-173] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [1-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-24] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-16] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-329] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-211] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_Tackle' range [251-258] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [264-265] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-104] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-166] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [96-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-300] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [302-307] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-329] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-267] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [269-302] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [316-317] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [319-324] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-168] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-228] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-280] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-301] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-325] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-296] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-329] for track '34' has 2 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.