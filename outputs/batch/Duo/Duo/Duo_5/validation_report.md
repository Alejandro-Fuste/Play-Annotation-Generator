# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_5`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 12: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_BallCarry' range [155-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-197] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-209] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-191] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-209] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-125] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-209] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-155] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-209] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-155] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [115-181] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [180-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [115-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [125-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-156] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-185] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-161] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-209] for track '28' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.