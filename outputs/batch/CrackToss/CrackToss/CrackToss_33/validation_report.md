# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_33`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 67: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [49-68] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-87] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-98] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-112] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-33] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-42] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [49-79] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [91-100] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' for track '3' starts at frame 19, but the player has no visible bounding box on this frame.
> - Action 'Action_PullBlock' range [19-19] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [21-38] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [41-57] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [76-87] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-108] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-40] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-53] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-67] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-100] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [16-20] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-41] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-26] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-22] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-115] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-17] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-90] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-20] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-35] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-71] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-9] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-15] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [19-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-10] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-7] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-100] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-120] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-70] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-124] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-76] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-86] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-92] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-108] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-129] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '28' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.