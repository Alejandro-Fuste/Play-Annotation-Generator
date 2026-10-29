# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_71`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 74: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 74: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 74: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 74: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-151] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-155] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-40] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-59] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-99] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-113] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-158] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [11-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [173-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [192-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [196-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-37] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-198] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-196] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [204-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-188] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-83] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-188] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-91] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-116] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-199] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '27' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.