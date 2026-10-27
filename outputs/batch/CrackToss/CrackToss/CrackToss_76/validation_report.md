# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_76`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 36 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 249 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 154: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
> - Action 'Action_PreSnap' range [0-7] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-230] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-247] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-242] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-190] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [140-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [237-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-204] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-71] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-87] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-101] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-107] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-173] for track '24' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-235] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-249] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-160] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-173] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-244] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '36' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.