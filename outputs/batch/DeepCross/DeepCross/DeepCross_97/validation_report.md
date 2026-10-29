# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_97`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 100: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 100: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 100: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_ThrowPass' for track '14' has invalid range: start=87, end=81. Clamping end to start.
> - Action 'Action_PreSnap' range [0-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [10-166] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [176-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [1-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [107-121] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [1-33] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-43] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-76] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-98] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [101-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-19] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-66] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-137] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-28] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-53] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-21] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [1-5] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-40] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-56] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-66] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-67] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-85] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-114] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-96] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-122] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-122] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-119] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-131] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '31' has 3 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.